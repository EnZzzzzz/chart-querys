#!/usr/bin/env python3
"""按 query 划分 60%/20%/20%，以 chart_forms 为多标签覆盖目标。"""

import argparse
from collections import Counter
import json
from pathlib import Path
import random
import sys


NAMES = ("train", "test", "validation")


def capacities(n):
    # 最大余数法；相同余数按 train/test/validation 的顺序分配。
    weights = (6, 2, 2)
    sizes = [n * w // 10 for w in weights]
    for i in sorted(range(3), key=lambda i: -(n * weights[i] % 10))[:n - sum(sizes)]:
        sizes[i] += 1
    return sizes


def read_records(root):
    records = []
    ids = set()
    for parent in ("paper", "report", "dataset", "cross-source"):
        for path in sorted((root / parent).glob("*/query.json")):
            data = json.loads(path.read_text(encoding="utf-8"))
            identifier = data["id"]
            if identifier in ids:
                raise ValueError(f"重复 id: {identifier}")
            ids.add(identifier)
            labels = data["chart_forms"]
            if not isinstance(labels, list) or not labels or not all(
                isinstance(label, str) and label for label in labels
            ):
                raise ValueError(f"无效 chart_forms: {path}")
            for entry in data["files"]:
                name = entry["file"]
                if Path(name).name != name or not (path.parent / name).is_file():
                    raise ValueError(f"本地数据文件无效或不存在: {path.parent / name}")
            records.append({"id": identifier, "query_file": path.relative_to(root).as_posix(),
                            "labels": set(labels)})
    if not records:
        raise ValueError("未找到 query.json")
    return records


def partition(records, seed, attempts):
    """固定容量随机重启、交换优化；只在实测满足覆盖后声称成功。"""
    rng = random.Random(seed)
    sizes = capacities(len(records))
    labels = [record["labels"] for record in records]
    totals = Counter(label for row in labels for label in row)
    best = None
    best_score = -1
    upper_bound = sum(min(3, count) for count in totals.values())
    for _ in range(attempts):
        order = list(range(len(records)))
        rng.shuffle(order)
        groups = []
        offset = 0
        for size in sizes:
            groups.append(order[offset:offset + size])
            offset += size
        counts = [Counter(label for i in group for label in labels[i]) for group in groups]
        score = sum(len(count) for count in counts)
        if score > best_score:
            best_score = score
            best = [group[:] for group in groups]
        if score == upper_bound:
            return best
        for _ in range(max(1000, len(records) * 100)):
            a, b = rng.sample(range(3), 2)
            if not groups[a] or not groups[b]:
                continue
            ia, ib = rng.randrange(len(groups[a])), rng.randrange(len(groups[b]))
            x, y = groups[a][ia], groups[b][ib]
            removed, added = labels[x] - labels[y], labels[y] - labels[x]
            delta = sum((counts[b][v] == 0) - (counts[a][v] == 1) for v in removed)
            delta += sum((counts[a][v] == 0) - (counts[b][v] == 1) for v in added)
            if delta < 0:
                continue
            for v in sorted(removed):
                counts[a][v] -= 1
                counts[b][v] += 1
            for v in sorted(added):
                counts[b][v] -= 1
                counts[a][v] += 1
            groups[a][ia], groups[b][ib] = y, x
            score += delta
            if score > best_score:
                best_score = score
                best = [group[:] for group in groups]
            if score == upper_bound:
                return best
    return best


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path, default=Path("splits"))
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--attempts", type=int, default=30)
    parser.add_argument("--best-effort", action="store_true", help="允许缺失覆盖，并在报告中逐项列出")
    args = parser.parse_args()
    if args.attempts < 1:
        parser.error("--attempts 必须大于 0")
    records = read_records(args.root.resolve())
    totals = Counter(label for record in records for label in record["labels"])
    rare = {label: {"available": count, "additional_needed": 3 - count}
            for label, count in sorted(totals.items()) if count < 3}
    if rare and not args.best_effort:
        print("无法在三个互不重复的集合中覆盖所有类型。以下类型至少需要补齐到 3 条独立 query：", file=sys.stderr)
        print(json.dumps(rare, ensure_ascii=False, indent=2), file=sys.stderr)
        print("未生成划分。允许缺失覆盖时可使用 --best-effort。", file=sys.stderr)
        return 2
    groups = partition(records, args.seed, args.attempts)
    report = {"seed": args.seed, "ratios": [0.6, 0.2, 0.2], "total": len(records),
              "label_field": "chart_forms", "rare_types": rare, "splits": {}}
    manifests = {}
    for name, group in zip(NAMES, groups):
        counts = Counter(label for i in group for label in records[i]["labels"])
        report["splits"][name] = {"size": len(group), "chart_forms": dict(sorted(counts.items())),
                                  "missing_types": sorted(totals.keys() - counts.keys())}
        manifests[name] = [{k: records[i][k] for k in ("id", "query_file")} for i in sorted(group)]
    report["full_coverage"] = all(not s["missing_types"] for s in report["splits"].values())
    if not report["full_coverage"] and not args.best_effort:
        print("搜索预算内未找到全覆盖划分；可增大 --attempts 或更换 --seed。未生成文件。", file=sys.stderr)
        return 2
    args.output.mkdir(parents=True, exist_ok=True)
    for name, payload in {**manifests, "coverage_report": report}.items():
        (args.output / f"{name}.json").write_text(
            json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for name, stats in report["splits"].items():
        print(f"{name}: {stats['size']} 条，覆盖 {len(stats['chart_forms'])}/{len(totals)} 种类型")
    print(f"完整覆盖: {report['full_coverage']}；输出: {args.output.resolve()}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (ValueError, OSError, KeyError, TypeError) as exc:
        print(f"错误: {exc}", file=sys.stderr)
        sys.exit(2)
