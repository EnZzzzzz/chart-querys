import unittest

from split_dataset import capacities, partition


class SplitTests(unittest.TestCase):
    def test_rounding(self):
        self.assertEqual(capacities(132), [79, 27, 26])
        for n in range(100):
            self.assertEqual(sum(capacities(n)), n)

    def test_coverage_disjoint_and_reproducible(self):
        records = [{"labels": {"common", f"rare-{i % 5}"}} for i in range(30)]
        groups = partition(records, 42, 10)
        self.assertEqual(groups, partition(records, 42, 10))
        self.assertEqual([len(g) for g in groups], [18, 6, 6])
        self.assertEqual(sorted(i for g in groups for i in g), list(range(30)))
        expected = set.union(*(r["labels"] for r in records))
        for group in groups:
            self.assertEqual(set.union(*(records[i]["labels"] for i in group)), expected)

    def test_single_sample(self):
        self.assertEqual(partition([{"labels": {"unique"}}], 42, 1), [[0], [], []])


if __name__ == "__main__":
    unittest.main()
