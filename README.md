# AI Accelerator：会前、会上、会后联动版

面向联想各部门领导的业务价值讨论资料。正文沿用 MD 第 0–7 章，三种材料按同一章节联动。

## 三种使用方式

**会前发送 `index.html`。** 默认打开 10 页简版，帮助参会者了解合作目标、六层架构、七个案例、能力底座、工具分工、Ontology 和联合推进方向。不是主持人执行手册。

**会上使用 `presentation.html`。** 默认打开 40 页详版，展开 Demo、内容与讨论。第二页已改为面向部门领导的四类管理议题，不再展示主持人的休息与时间控制安排。

**会后发送 `docs/meeting.md`。** 保存完整业务论证、案例、治理边界、合作计划与未确认事项。当前资料不是已发生会议的纪要；实际决定需在会议结束后由相关人员确认再补入。

两个 HTML 都独立包含简版和详版，顶部按钮可切换，左侧“查看同章详版 / 返回同章简版”保持当前 MD 章节。点击“会后 MD”即可下载内嵌的完整 Markdown。只分享其中一个 HTML 也可以切换两个版本，不依赖另一个 HTML 文件。

## 左侧目录

MD0–MD7 的八个章节条目在桌面、窄窗口和手机上默认显示。顶部“收起目录 / 展开目录”由用户手动控制，不再因窄屏自动消失。当前章节与版本页码会高亮。

手机端为保持演示排版会缩放画布；正式会议展示建议使用桌面或横屏。

## 公网部署

这是纯静态站点，不需要后端、数据库、API 密钥、Manus 登录或 npm。

1. 解压后将 `ai-accelerator-linked` 目录的内容上传到静态网站托管服务。
2. `index.html` 为默认入口，即会前简版；会上打开同目录 `presentation.html`。
3. GitHub Pages 或普通静态 Web 服务器都可部署。所有路径采用相对路径，可以放在项目子目录。
4. 当前未接入视频，只部署两个 HTML 即可浏览。若希望 Markdown 也有直接文件链接，请同时部署 `docs/`。
5. 视频接入后还需要部署 `media/` 或其对应公开视频资源。

例如部署目录结构：

```text
index.html
presentation.html
docs/meeting.md
media/...
```

当前任务只生成文件，没有发布到任何公网账户。发布前请审阅内部项目名称、历史数据、成本与待决策事项的可公开范围。

## 源码与重建

```text
index.html              默认简版的独立成品
presentation.html       默认详版的独立成品
template.html           导航、阅读阶段切换和响应式封装
build.py                标准库构建脚本
deck.json               40页详版章节与顺序
summary-deck.json       10页简版章节与对应详版页码
slides/                 40页完整HTML源码
summary-slides/         10页完整HTML源码
videos.json             七个视频的配置
docs/meeting.md         会后完整阅读资料
media/README.md         视频接入说明
```

编辑对应页面或 Markdown 后运行：

```bash
python3 build.py
```

然后重新上传生成的 `index.html` 和 `presentation.html`。构建只封装已有页面，不改写各页正文。

本地预览：

```bash
python3 -m http.server 8000
```

浏览器打开 `http://localhost:8000/`。无视频时，也可直接双击成品 HTML 离线打开。

## 章节链接与会议操作

入口支持 `#chapter-2` 或 `#md-2` 跳到案例章节。具体页面可用 `#summary-p-4` 或 `#detail-p-14`，页面锚点也能指定版本。`?view=summary` 或 `?view=detail` 可指定初始阅读阶段。

上一页/下一页按钮与方向键、PageUp/PageDown、Home/End 可导航。F 可在浏览器允许时请求全屏。连续纵向滚动仍可使用。

七个 Demo 视频尚未提供；所有指标和待确认事项均不构成实际结果、选定 Owner 或会议决议。

## 本轮意见修订

三份材料同步突出 Why：MD0 一级目录改为“Why · 为什么现在”，以“AI 是 ISS Biz Team 的必走之路”为起点，从“散、浅、贵”的探索阶段特征，转向可持续、可衡量、更平衡的业务能力。阶段痛点是讨论和验证框架，不是未经核实的量化诊断或已实现收益。

封面、三方协同与完整 MD 同步更新 ISS Biz Team 的六项优势，以及 COO AI Team 的六项优势；Item 强调以用户为中心（user-centric），将业务需求桥接为可落地应用。保留 10 页简版、40 页详版、MD0–MD7 章节、七个案例和视频接入配置，不更改原有联动方式。
