# chart-querys 数据集构造规则

本仓库是图表组件 skill 的 Agent 测评 query 集。每条 query 一个自包含文件夹，
按 `category` 归入 4 个父目录（paper / report / dataset / cross-source；
report-zh 与 report-en 同入 `report/`，dataset 与 special-form 同入 `dataset/`）：

```
paper/a1-llama3-technical-report/
├── query.json                      # id / category / query / files / chart_forms
├── llama3-technical-report.pdf     # 该条 query 引用的数据源
└── groundtruth.json                # 评分基准（paper 类必需，其余类别按需）
```

## query 撰写规则（核心）

### 1. 开放性：只描述分析目标，不规定产出形式

query 文本只允许包含两类信息：

- **数据是什么**：文件名、规模、字段、时间范围（如"3.3 万首歌的音频特征"）
- **要什么交付物**：分析什么主题、回答什么问题，交付物表述为
  "图文报告 / 可视化报告 / 分析页面 / 仪表盘"这类**中性词**

**禁止**在 query 中指定任何具体图表类型（柱状图、折线图、饼图、散点图、
热力图、雷达图、蜡烛图、treemap、choropleth 等），也禁止规定布局、配色、
交互方式。图表选型是被测能力，写进 query 就等于送分。

### 2. 无隐形提示

- **不预设结论**：不写"证明 X""揭示 X 的增长"这类带倾向的表述，
  用"分析 X 与 Y 的关系""X 有什么规律"代替。
- **不用图表名当领域词**：如"生存曲线""K 线图"也是提示，
  改写为"患者生存情况""股价行情"。
- **不暗示数据形态的处理方式**：不写"按国家分组""转置宽表"
  "降采样"这类处理指令，让模型自己判断。
- **数据描述保持中立**：只陈述事实（行数、字段含义），
  不评价数据"适合"怎么展示。

### 3. 文件引用

query 文本中只写**同目录下的本地文件名**，不写任何绝对/项目相对路径，
保证文件夹拷到任何环境都能独立执行。

## query.json 字段

| 字段 | 说明 |
|---|---|
| `id` | 类别字母 + 序号（A1、B3、D12…），各类别内连续编号 |
| `category` | paper / report-zh / report-en / dataset / special-form / cross-source |
| `query` | 用户口吻指令，遵守上述开放性规则 |
| `files` | `[{file, source}]`：本地文件名 + 原始语料路径（仅溯源用） |
| `chart_forms` | **评分参考元数据**，列出该数据适合考察的图表形态；只给评分器看，**禁止喂给被测模型** |

## groundtruth.json（paper 类必需）

对论文逐页盘点其中的图（Figure）与表（Table），作为评分基准。统一格式：

```json
{
  "id": "A1",
  "source_file": "llama3-technical-report.pdf",
  "paper_title": "The Llama 3 Herd of Models",
  "stats": { "figures_total": 34, "tables_total": 25 },
  "figures": [
    { "label": "Figure 1", "chart_type": "line", "count": 2, "caption": "..." }
  ],
  "tables": [
    { "label": "Table 5", "data_form": "benchmark-scores", "rows": 12, "cols": 6, "caption": "..." }
  ]
}
```

- `figures[].chart_type` 受控词表：`line / bar / grouped-bar / stacked-bar /
  horizontal-bar / area / scatter / pie / histogram / heatmap / box / radar /
  map / diagram / image / mixed / other`。架构图、流程图归 `diagram`，
  照片/截图归 `image`，两者不算数据图表。
- 一个文件夹含**多篇论文**时（如对比类 query）：`source_file`/`paper_title`
  填主论文，另加 `extra_sources: [{file, title}]`；figures/tables 每个条目
  加 `source` 字段填所属文件名，数组按论文分组、组内编号升序。
- `figures[].count`：该 Figure 内同类型子图/面板数量（如"fig1 折线图 × 2"
  记为 `count: 2`）；单图为 1。一个 Figure 混合多种类型时
  `chart_type: "mixed"`，细节写进 `note`。
- `tables[].data_form` 受控词表：`benchmark-scores / hyperparameters /
  statistics / comparison / ablation / examples / other`；
  `rows`/`cols` 为约数。
- 盘点以 PDF 实际渲染为准（用 `.cache/venv` 的 pymupdf 渲染页面逐张看），
  不能只靠 caption 文字猜类型。

## 数据源规则

- 只收**公开免登录**来源：arXiv、Our World in Data、Rdatasets、TidyTuesday、
  vega/plotly/seaborn/fivethirtyeight、各国官方机构公开报告。
  遇反爬/登录墙直接换源，不纠缠。
- 数据量门槛：CSV 一般 >100 行（特殊经典小数据集需在 files 备注说明）；
  PDF >500KB。要覆盖万行级大表、宽表、多文件组合等对组件有压力的形态。
- 形态覆盖：时间序列、分类对比、分布、地理、层级、网络、OHLC 等，
  每新增数据优先补未覆盖的形态。
- 单个文件不超过 100MB（GitHub 硬限制），超了不入库。

## 新增/修改 query 流程

1. 按 `<父目录>/<类别字母小写><序号>-<数据文件名>/`（如 `paper/a11-xxx`）建文件夹，
   父目录与 category 的映射：paper→`paper/`、report-zh/report-en→`report/`、
   dataset/special-form→`dataset/`、cross-source→`cross-source/`。
   放入 query.json 和数据文件；paper 类还需 groundtruth.json。
2. 校验：query 文本扫一遍禁用词（图表类型名、结论性表述、处理指令）；
   JSON 合法性、files 本地文件存在性。
3. commit + push 本仓库后，到主仓库 dsh-design-harness 更新 submodule
   gitlink 并 commit。
4. 主仓库 `.cache/chart-data-corpus/QUERIES.md` 是人读索引，
   由 `query/*/*/query.json` 生成，改动后重新生成同步。
