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
覆盖其源论文中的 **1349 个 Figure 与 475 个 Table**，Figure 图表类型分布：

| 类型 | 中文名 | 数量 | | 类型 | 中文名 | 数量 |
|---|---|---|---|---|---|---|
| mixed | 多面板混合图 | 381 | | map | 地图 | 37 |
| line | 折线图 | 138 | | box | 箱线图 | 34 |
| heatmap | 热力图 | 51 | | bar | 柱状图 | 24 |
| scatter | 散点图 | 45 | | horizontal-bar | 横向条形图 | 14 |
| grouped-bar | 分组柱状图 | 38 | | histogram | 直方图 | 12 |
| stacked-bar | 堆叠柱状图 | 60 | | radar | 雷达图 | 10 |

另有 `other`（桑基图/小提琴图/瀑布图/甘特图等词表外形态，见各条目 note）
118 个、`image`（照片/影像/截图）227 个、`diagram`（架构/流程示意图）149 个。
pie 6 个、area 5 个。

Table 的数据形态分布：benchmark-scores 124、statistics 120、comparison 83、
other 69、examples 41、hyperparameters 25、ablation 13。

> 统计口径：paper 类（A1–A89）的 groundtruth.json 汇总。B–F 类的数据源本身
> 覆盖更多形态（地理边界/层级/网络/OHLC 等，见各文件夹 `chart_forms`），
> 尚未逐文件盘点。

数据源本身来自公开渠道（Our World in Data、Rdatasets、TidyTuesday、
vega/plotly/seaborn/fivethirtyeight、arXiv、Europe PMC、各国官方机构公开报告），
仅供内部测评使用。
