# chart-querys

图表组件 skill 的 Agent 测评 query 集，用开放式分析任务考察数据理解、图表选型和报告表达。

## 当前有什么

当前共 **148 条 query、92 个 chart_forms 标签**，按 6 个类别存放在 4 个父目录中。

| 类别 | ID 范围 | 数量 | 目录 | 内容 |
|---|---|---:|---|---|
| paper | A1–A89 | 89 | `paper/` | 论文解读，均附图表评分基准 |
| report-zh | B1–B10 | 10 | `report/` | 中文报告分析 |
| report-en | C1–C10 | 10 | `report/` | 英文报告分析 |
| dataset | D1–D12 | 12 | `dataset/` | 原始数据分析 |
| special-form | E1–E22 | 22 | `dataset/` | 地理、层级、网络、成分、迁移、配对测量等数据 |
| cross-source | F1–F5 | 5 | `cross-source/` | 多来源综合分析 |

最近新增 **E7–E22 共 16 条原始数据任务**：熔岩成分、炉渣测量、实验室分析、呼吸状态随访、英国选举调查、美国行业就业、墨尔本行人、企鹅体型、牛体重、美国各州选举、绘画元素、玻璃成分、加拿大迁移、鹰类观测、纽约机场天气和 Clemson 温度。

本批包含 143,412 行就业记录、26,115 行天气记录、33,148 行温度记录，以及 72 列绘画元素宽表（含索引列）；3 个经典小数据集的行数例外已记录在 `files.note`。
详见 [新增任务及覆盖变化](docs/coverage-additions-2026-09.md)。

## 文件结构与使用

图表组件 skill 的 Agent 测评 query 集。**每条 query 一个自包含文件夹**，
按类别归入 4 个父目录（report-zh / report-en 同入 `report/`，
dataset / special-form 同入 `dataset/`）：

```
paper/a1-llama3-technical-report/
├── query.json                      # id / category / query / files / chart_forms
├── llama3-technical-report.pdf     # 该条 query 引用的数据源
└── groundtruth.json                # 评分基准（paper 类）
```

- `query`：用户口吻的开放式指令，不指定图表类型，引用同目录下的数据文件名，
  拷出即可独立执行
- `files[]`：每项含 `file`（本地文件名）与 `source`（原始语料路径，溯源用）
- `chart_forms`：该条预期考察的图表形态（评分维度参考，不喂给被测模型）
- `groundtruth.json`：paper 类 query 附带的论文图表盘点（Figure/Table 清单、
  类型、数量），格式与构造规则见 `AGENTS.md`

## 全部任务的图表标签覆盖

下表由当前所有 `query.json` 的 `chart_forms` 汇总，**一条 query 对同一标签计一次**。一条任务可有多个标签，数量不可相加作为任务总数。
这是评分参考中的候选覆盖，不是模型实际产出的图表数，也不是论文 Figure 或子面板数。

92 个标签中混有图形、泛称、交付形式和功能标签，不能直接视为 92 种严格定义的图表。
当前保留原标签，不合并 `geo`／`map` 等近义项。`funnel` 在论文中也可能指发表偏倚漏斗图；`waterfall` 在肿瘤研究中也可能指按患者排列的变化幅度图，评分时须结合来源语境。

### 覆盖较多：10 条及以上

| 标签 | 中文名 | Query 数 |
|---|---|---:|
| `line` | 折线图 | 82 |
| `bar` | 柱状图 | 72 |
| `scatter` | 散点图 | 59 |
| `heatmap` | 热力图 | 54 |
| `boxplot` | 箱线图 | 43 |
| `stacked-bar` | 堆叠柱状图 | 32 |
| `grouped-bar` | 分组柱状图 | 27 |
| `network` | 网络图 | 26 |
| `violin` | 小提琴图 | 25 |
| `histogram` | 直方图 | 21 |
| `horizontal-bar` | 横向条形图 | 20 |
| `bubble` | 气泡图 | 18 |
| `pie` | 饼图 | 18 |
| `forest-plot` | 森林图 | 17 |
| `radar` | 雷达图 | 16 |
| `sankey` | 桑基图 | 13 |
| `dot-plot` | 点图 | 12 |
| `chord` | 弦图 | 11 |
| `survival-curve` | 生存曲线 | 11 |
| `ridgeline` | 山脊图 | 10 |

### 中等覆盖：4–9 条

| 标签 | 中文名 | Query 数 |
|---|---|---:|
| `area` | 面积图 | 9 |
| `lollipop` | 棒棒糖图 | 9 |
| `venn` | 韦恩图 | 9 |
| `parallel-coordinates` | 平行坐标图 | 8 |
| `slope` | 坡度图（斜率图） | 7 |
| `treemap` | 矩形树图 | 7 |
| `choropleth` | 分级设色地图 | 6 |
| `dumbbell` | 哑铃图 | 6 |
| `flow-map` | 流向地图 | 6 |
| `geo` | 地理可视化（泛称） | 6 |
| `icicle` | 冰柱图 | 6 |
| `sunburst` | 旭日图 | 6 |
| `beeswarm` | 蜂群图 | 5 |
| `candlestick` | 蜡烛图／K线图 | 5 |
| `density` | 密度图 | 5 |
| `funnel` | 漏斗图（含领域歧义） | 5 |
| `gantt` | 甘特图 | 5 |
| `hexbin` | 六边形分箱图 | 5 |
| `map` | 地图（泛称） | 5 |
| `mosaic` | 马赛克图 | 5 |
| `rose` | 玫瑰图 | 5 |
| `surface-3d` | 三维曲面图 | 5 |
| `upset` | UpSet集合交集图 | 5 |
| `waterfall` | 瀑布图（含领域歧义） | 5 |
| `wordcloud` | 词云图 | 5 |
| `alluvial` | 冲积图／类别流转图 | 4 |
| `calendar-heatmap` | 日历热力图 | 4 |
| `contour` | 等值线图 | 4 |
| `distribution` | 分布展示（泛称） | 4 |
| `scatter-matrix` | 散点矩阵图 | 4 |
| `stacked-area` | 堆叠面积图 | 4 |
| `streamgraph` | 流图／河流图 | 4 |

### 少量覆盖：3 条

| 标签 | 中文名 | Query 数 |
|---|---|---:|
| `bland-altman` | Bland–Altman一致性图 | 3 |
| `bump-chart` | 排名变化图 | 3 |
| `comparison-bar` | 对比条形图 | 3 |
| `correlogram` | 相关矩阵图 | 3 |
| `dendrogram` | 树状聚类图 | 3 |
| `donut` | 环形图 | 3 |
| `horizon-chart` | 地平线图 | 3 |
| `parallel-sets` | 平行集合图 | 3 |
| `raincloud` | 雨云图 | 3 |
| `ranking` | 排名展示（泛称） | 3 |
| `volcano` | 火山图 | 3 |
| `waffle` | 华夫图／方格占比图 | 3 |

### 优先补充：1–2 条

| 标签 | 中文名 | Query 数 |
|---|---|---:|
| `circos` | Circos圆形关系图 | 2 |
| `clustergram` | 聚类热力图 | 2 |
| `dashboard` | 仪表盘（交付形式） | 2 |
| `diagram` | 示意图（泛称） | 2 |
| `diverging-bar` | 发散条形图 | 2 |
| `dual-axis-line` | 双轴折线图 | 2 |
| `error-bar` | 误差棒图 | 2 |
| `interactive` | 交互式展示（功能标签） | 2 |
| `od-matrix-heatmap` | 起讫点矩阵热力图 | 2 |
| `oncoplot` | 癌症突变谱图 | 2 |
| `radial-bar` | 径向条形图 | 2 |
| `ternary` | 三元图／三角坐标图 | 2 |
| `3d-prism` | 三维棱柱图 | 1 |
| `flowchart` | 流程图 | 1 |
| `geo-scatter` | 地理散点图 | 1 |
| `hammock` | 吊床图 | 1 |
| `icon-chart` | 图标统计图／象形图 | 1 |
| `image` | 图片（照片／影像／截图） | 1 |
| `infographic` | 信息图（综合表达） | 1 |
| `line-overlay` | 折线叠加（组合方式） | 1 |
| `nested-grid-map` | 嵌套网格地图 | 1 |
| `nomogram` | 列线图 | 1 |
| `point-density-map` | 点密度地图 | 1 |
| `scatter-3d` | 三维散点图 | 1 |
| `spinogram` | 分箱比例图 | 1 |
| `spiral-chart` | 螺旋图 | 1 |
| `timeline` | 时间轴图 | 1 |
| `tree` | 树形图 | 1 |

目前 **28 个标签不足 3 条**（16 个仅 1 条、12 个仅 2 条）。其中部分需先整理标签口径；不能只靠补数据解决所有分类问题。

## 论文评分基准中的图表数量

89 条 paper 类 query 均附带 groundtruth，
覆盖其源论文中的 **1349 个 Figure 与 475 个 Table**。

Figure 类型分布（受控词表 17 类，按 Figure 条目计；`other` 在下文单列）：

| 类型 | 中文名 | 数量 | | 类型 | 中文名 | 数量 |
|---|---|---|---|---|---|---|
| mixed | 多面板混合图 | 381 | | map | 地图 | 37 |
| image | 照片/影像/截图 | 227 | | box | 箱线图 | 34 |
| diagram | 架构/流程示意图 | 149 | | bar | 柱状图 | 24 |
| line | 折线图 | 138 | | horizontal-bar | 横向条形图 | 14 |
| stacked-bar | 堆叠柱状图 | 60 | | histogram | 直方图 | 12 |
| heatmap | 热力图 | 51 | | radar | 雷达图 | 10 |
| scatter | 散点图 | 45 | | pie | 饼图 | 6 |
| grouped-bar | 分组柱状图 | 38 | | area | 面积图 | 5 |

`other`（词表外形态）共 118 个，按各条目 note 拆分：

| 类型 | 数量 | | 类型 | 数量 |
|---|---|---|---|---|
| sankey 桑基图 | 12 | | hammock 吊床图 | 5 |
| parallel-coordinates 平行坐标图 | 11 | | dumbbell 哑铃图 | 4 |
| violin 小提琴图 | 8 | | gantt 甘特图 | 4 |
| surface-3d 3D 曲面图 | 7 | | bubble / funnel / sunburst / treemap | 各 2 |
| candlestick K线图 | 6 | | infographic / streamgraph / alluvial | 各 2 |
| forest-plot 森林图 | 6 | | hexbin / spiral / beeswarm / icicle / slope / raincloud / rose / strip-dot | 各 1 |
| network 共现网络图 | 6 | | 文本框/小表格等非图表内容 | 16 |
| contour 等值线图 | 6 | | wordcloud 词云 | 5 |

`mixed`（381 个）为生物医学论文典型的多面板复合图，单图常含 6–10 个面板，
面板级构成写在各条目 `note` 中（出现最多的面板类型为 heatmap、scatter、bar、
violin、survival-curve、network 等）。

Table 的数据形态分布：benchmark-scores 124、statistics 120、comparison 83、
other 69、examples 41、hyperparameters 25、ablation 13。

> 统计口径：paper 类（A1–A89）的 groundtruth.json 汇总。B–F 类的数据源本身
> 覆盖更多形态（地理边界/层级/网络/OHLC 等，见各文件夹 `chart_forms`），
> 尚未逐文件盘点。

## 训练 / 测试 / 验证集划分

使用 Python 3 标准库，无需安装依赖：

```bash
python3 scripts/split_dataset.py --output splits --seed 42
```

按 query 数量以 6:2:2 划分，使用最大余数法取整（148 条为 89/30/29）。
三个集合的 query 互不重复，每条恰好分配一次；固定数据与 seed 可复现。
根据 `chart_forms` 多标签进行交换优化，默认必须让每个集合覆盖所有标签，
否则非零退出、不写输出。类型少于 3 条时列出补充需求；搜索未成功不代表数学上无解，
可调整 `--seed` 或增加 `--attempts`（默认 30）。

当前数据存在只出现 1–2 次的标签，无法满足严格全覆盖。需要先查看尽力覆盖结果时运行：

```bash
python3 scripts/split_dataset.py --best-effort --output splits --seed 42
```

输出 `train.json`、`test.json`、`validation.json` 三份清单（仅含 id 和相对数据根目录的
query_file），以及供评分器使用的 `coverage_report.json`（覆盖数、缺失类型、补充需求）。
不复制原始数据。运行器根据清单读取 query 和本地附件，不能将原始 query.json 中的
`chart_forms` 或 groundtruth、覆盖报告喂给被测模型。
`--root` 可指定其他同结构数据根目录，默认使用脚本所在仓库。
输出目录内的同名文件会被覆盖。划分单位是 query，复用相同来源文件的不同 query
仍可能分到不同集合；本脚本不保证来源级隔离。

## 数据来源与溯源

现有数据来自公开渠道：Our World in Data、Rdatasets、TidyTuesday、vega／plotly／seaborn／fivethirtyeight、arXiv、Europe PMC 及各国官方机构公开报告，仅供内部测评使用。

E7–E22 均从 [Rdatasets](https://vincentarelbundock.github.io/Rdatasets/) 公开归档下载，CSV 保留上游原始字节，仅更改本地文件名。归档中的原始来源包括美国劳工统计局、墨尔本开放数据平台、NOAA、Iowa Environmental Mesonet、Palmer Station 生态研究和经典研究数据。
每条新增任务的 `files` 记录下载地址 `source`、说明页 `documentation`、实测行数 `rows` 和校验值 `sha256`；这不表示已逐一回到最初机构核对原始记录。

新增和修改规则见 [AGENTS.md](AGENTS.md)。`query` 只能描述数据与分析目标，不指定图形、布局或交互；`chart_forms`、groundtruth 和覆盖报告仅供维护者及评分器使用，不得喂给被测模型。
