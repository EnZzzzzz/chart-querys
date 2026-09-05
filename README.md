# chart-querys

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

类别（id 前缀）：paper/A=论文解读、report/B=中文产业报告、report/C=英文产业报告、
dataset/D=数据集可视化、dataset/E=特殊数据形态（地理/层级/网络等）、
cross-source/F=跨源综合。

## 图表类型覆盖

目前共 **132 条 query**（paper 89 / report 20 / dataset 18 / cross-source 5）。
89 条 paper 类 query 均附带 groundtruth，
覆盖其源论文中的 **1349 个 Figure 与 475 个 Table**。

Figure 类型分布（受控词表 17 类，按 Figure 条目计）：

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

数据源本身来自公开渠道（Our World in Data、Rdatasets、TidyTuesday、
vega/plotly/seaborn/fivethirtyeight、arXiv、Europe PMC、各国官方机构公开报告），
仅供内部测评使用。
