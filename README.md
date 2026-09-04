# chart-querys

图表组件 skill 的 Agent 测评 query 集。**每条 query 一个自包含文件夹**：

```
A1-llama3-technical-report/
├── query.json                      # id / category / query / files / chart_forms
└── llama3-technical-report.pdf     # 该条 query 引用的数据源
```

- `query`：用户口吻的指令文本，引用同目录下的数据文件名，拷出即可独立执行
- `files[]`：每项含 `file`（本地文件名）与 `source`（原始语料路径，溯源用）
- `chart_forms`：该条预期考察的图表形态（评分维度参考）

类别（id 前缀）：A=论文解读、B=中文产业报告、C=英文产业报告、
D=数据集可视化、E=特殊图表形态（地图/层级/网络/热力图/蜡烛图）、F=跨源综合。

数据源本身来自公开渠道（Our World in Data、Rdatasets、TidyTuesday、
vega/plotly/seaborn/fivethirtyeight、arXiv、各国官方机构公开报告），
仅供内部测评使用。
