# 稀缺图表形态补充：E7–E22

新增 16 条 special-form query，总量 132 → 148；dataset 父目录 18 → 34。数据均从公开免登录的 Rdatasets 下载，CSV 保持上游原始字节，来源链接、文档链接、实测行数和 SHA-256 记录在各 query.json 的 files 中。

本文件及 query.json 中的 chart_forms 仅供维护者和评分器使用。标签列出本批重点考察的合理候选，不穷举所有可行图形，也不要求模型必须使用某一种。现有任务标签未改写，因此覆盖变化表示新增任务的候选覆盖，不表示模型实际产出。

## 新增任务

| ID | 数据 | 行数 | CSV 列数（含索引） | 重点候选 |
|---|---|---:|---:|---|
| E7 | [skye-lava](../dataset/e7-skye-lava/query.json) | 23 | 4 | ternary |
| E8 | [iron-measurements](../dataset/e8-iron-measurements/query.json) | 53 | 3 | bland-altman, dumbbell |
| E9 | [laboratory-assays](../dataset/e9-laboratory-assays/query.json) | 252 | 5 | bland-altman, error-bar |
| E10 | [respiratory-followups](../dataset/e10-respiratory-followups/query.json) | 444 | 9 | alluvial, parallel-sets |
| E11 | [british-election-survey](../dataset/e11-british-election-survey/query.json) | 1525 | 11 | parallel-sets, mosaic, diverging-bar |
| E12 | [us-sector-employment](../dataset/e12-us-sector-employment/query.json) | 143412 | 5 | horizon-chart, bump-chart |
| E13 | [melbourne-pedestrians](../dataset/e13-melbourne-pedestrians/query.json) | 1976 | 3 | calendar-heatmap |
| E14 | [penguin-measurements](../dataset/e14-penguin-measurements/query.json) | 344 | 9 | raincloud, beeswarm, correlogram |
| E15 | [cattle-growth](../dataset/e15-cattle-growth/query.json) | 660 | 5 | raincloud, beeswarm, slope |
| E16 | [state-election-history](../dataset/e16-state-election-history/query.json) | 1097 | 5 | bump-chart, slope |
| E17 | [painting-elements](../dataset/e17-painting-elements/query.json) | 403 | 72 | upset |
| E18 | [forensic-glass](../dataset/e18-forensic-glass/query.json) | 214 | 11 | parallel-coordinates, clustergram, correlogram |
| E19 | [canada-migration](../dataset/e19-canada-migration/query.json) | 90 | 9 | od-matrix-heatmap, chord |
| E20 | [hawk-measurements](../dataset/e20-hawk-measurements/query.json) | 908 | 20 | upset |
| E21 | [new-york-airport-weather](../dataset/e21-new-york-airport-weather/query.json) | 26115 | 16 | rose, radial-bar |
| E22 | [clemson-daily-temperatures](../dataset/e22-clemson-daily-temperatures/query.json) | 33148 | 4 | calendar-heatmap, horizon-chart |

其中 E12、E21、E22 为万行级数据，E17 为 72 列宽表。E7（23 行）、E8（53 行）、E19（90 行）是保留完整原始记录的经典小数据，例外原因已写入 files.note。没有通过复制样本扩大数据量。

## 覆盖变化

统计单位为带有该标签的 query 数，一条 query 对一个标签计一次；不统计 PDF 面板数量。

| 标签 | 新增前 | 新增后 |
|---|---:|---:|
| alluvial | 3 | 4 |
| beeswarm | 3 | 5 |
| bland-altman | 1 | 3 |
| bump-chart | 1 | 3 |
| calendar-heatmap | 2 | 4 |
| chord | 10 | 11 |
| clustergram | 1 | 2 |
| correlogram | 1 | 3 |
| diverging-bar | 1 | 2 |
| dumbbell | 5 | 6 |
| error-bar | 1 | 2 |
| horizon-chart | 1 | 3 |
| mosaic | 4 | 5 |
| od-matrix-heatmap | 1 | 2 |
| parallel-coordinates | 7 | 8 |
| parallel-sets | 1 | 3 |
| radial-bar | 1 | 2 |
| raincloud | 1 | 3 |
| rose | 4 | 5 |
| slope | 5 | 7 |
| ternary | 1 | 2 |
| upset | 3 | 5 |

## 验证与边界

已校验全部 148 个 query 的 JSON、本地附件存在性、ID 唯一和连续；新增 CSV 的行列数、SHA-256、文件大小、小数据例外及 query 文本均已核验。新增 CSV 与仓库已有 CSV 无字节级重复；这不等同于完成语义或同源去重。

本批不修改原有划分脚本或标签体系。仍有以下标签少于 3 条，尚不能声称支持所有标签在训练、测试、验证集同时覆盖；其中也包含 dashboard、interactive 等需要后续整理口径的标签。

3d-prism: 1, circos: 2, clustergram: 2, dashboard: 2, diagram: 2, diverging-bar: 2, dual-axis-line: 2, error-bar: 2, flowchart: 1, geo-scatter: 1, hammock: 1, icon-chart: 1, image: 1, infographic: 1, interactive: 2, line-overlay: 1, nested-grid-map: 1, nomogram: 1, od-matrix-heatmap: 2, oncoplot: 2, point-density-map: 1, radial-bar: 2, scatter-3d: 1, spinogram: 1, spiral-chart: 1, ternary: 2, timeline: 1, tree: 1。

实验室数据的 Bat 嵌套于实验室和样本，不可把不同实验室的同号批次或重复行当作天然一一配对；一致性分析应有合理的样本对应定义。就业数据包含总量与细分序列；字段不能直接视为互斥行业求和。缺失值与异常值均保留，由分析任务自行判断。
