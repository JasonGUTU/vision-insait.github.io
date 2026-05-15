# Vision Group 网站（Jekyll）

本仓库是 **Vision Group** 组站：用 **Jekyll** 管理页面与内容，视觉与脚本来自 **Block 1.3.2** 已编译的 `dist`（通过 `assets` 符号链接接入）。

---

## 技术栈与资源

| 部分 | 说明 |
|------|------|
| 站点生成 | [Jekyll 4](https://jekyllrb.com/) |
| 样式 / 组件 | Block 主题：`../block-1.3.2/dist/assets`（CSS、JS、字体、favicon 等） |
| 静态资源入口 | 项目根目录的 `assets` → **符号链接** 指向同级目录下的 **`../block-1.3.2/dist/assets`**（Block 1.3.2 已构建的 `dist`） |

若你的 Block 工程路径不同，请自行调整 `assets` 链接目标；布局中统一使用 `/assets/...`。

---

## 目录结构（你在改什么）

```
├── _config.yml          # 站点名、collections、permalink 等
├── Gemfile / Rakefile   # 依赖与带 UTF-8 的构建任务
├── assets -> ../block-1.3.2/dist/assets   # 符号链接（勿删目标目录）
├── _includes/           # head、导航、页脚、脚本片段
├── _layouts/            # 页面骨架（default、person、topic、publication 等）
├── _people/             # 成员：每人一个 Markdown + YAML 元数据
├── _research_topics/    # 研究方向：每个 topic 一页
├── _publications/       # 论文：作者用 person_id 关联成员
├── _projects/           # Demos / 项目：可选 contributors
├── _jobs/               # 招聘条目（列表在 job/index）
├── _posts/              # 博客文章
├── index.md             # 首页
├── people/              # People 总览 + Faculty / Students / Postdocs
├── research/            # Research 总览（列出所有 topic）
├── publications/        # 论文列表
├── demos/               # 项目列表
├── job/                 # 招聘列表
└── blog/                # 博客列表
```

---

## 数据模型（怎么互相关联）

### 成员 `_people/*.md`

建议字段：

- **`person_id`**（必填）：全站唯一 ID，论文里的 `authors`、项目里的 `contributors` 都引用它。
- **`title`**：页面标题（可与姓名一致）。
- **`name_display`**：展示用姓名（可选，缺省可用 `title`）。
- **`role`**：`faculty` | `phd` | `postdoc` | `visitor`（legacy `student` 与 `phd` 同在 People 页的 PhD 区块展示）。People 单页为 **`/people/`**，按角色分段列出。
- **`start_date`**（必填，建议 `YYYY-MM-DD` 字符串）：在 **Faculty / Postdocs / PhD / Visitors** 各区块内按 **升序** 排序——**越早加入越靠上，越新越靠下**。
- **`order`**（可选，整数，默认 `0`）：占位字段，便于以后扩展或外部脚本使用；**当前模板仅按 `start_date` 排序**，同一天多人时请把日期错开（例如 `2025-09-01` / `2025-09-02`）。
- **`topics`**：字符串数组，每项必须是某个 `_research_topics` 里定义的 **`topic_id`**。
- 其它：`title_en`、`homepage`、`photo`（图片 URL，相对站点根，如 `/assets/...`）等按需加。

### 研究方向 `_research_topics/*.md`

- **`topic_id`**（必填）：与成员 `topics` 里写的字符串完全一致。
- **`title`**、`order`（导航/列表排序）、`summary` 等。

### 论文 `_publications/*.md`

- **`author_line_full`**（推荐）：论文的**完整作者列表**（纯文本），用于标题下方与列表页展示，不加链接。
- **`authors`**：仅列出**本机构成员**的 `person_id`，用于详情页底部带链接的作者区块。
- **`author_line`**（可选）：旧字段；若未设置 `author_line_full` 则回退显示。
- **`topics`**（可选）：同上，用于论文页展示 topic 链接。
- **`year`**、`venue`、`paper_url` 等。

### 项目 `_projects/*.md`

- **`contributors`**（可选）：`person_id` 数组，在项目页展示成员链接。
- **`external_url`**（可选）：站外项目主页。设置后，Topic / Demos 列表上的封面、标题与按钮会直接打开该链接（新标签页）；访问本站 `/demos/.../` 路径也会自动跳转。与 **`demo_url`** 不同：`demo_url` 仅在站内项目页保留第二个 “Live demo” 按钮。
- **`demo_url`**（可选）：站内项目页上的外部演示链接（未设置 `external_url` 时生效）。

### 关联效果（Liquid 已实现）

1. 打开**成员页**：自动列出所有 `authors` 含该 `person_id` 的论文。  
2. 打开**某个 Research Topic**：自动列出所有 `topics` 含该 `topic_id` 的成员。  
3. 打开**某篇论文**：根据 `authors` 解析并列出站内成员。

---

## 本地安装与构建

```bash
bundle install
rake build          # 推荐：已设置 UTF-8，避免资产路径编码问题
# 或
rake serve          # 本地预览（含 livereload）
```

依赖会安装到项目内的 **`vendor/bundle/`**（由已提交的 `.bundle/config` 指定）。若出现 `Could not find ... in locally installed gems`，在项目根目录再执行一次 **`bundle install`** 即可。

若不用 Rake，请手动带 UTF-8（`template/dist/assets` 下存在含非 ASCII 文件名的图片时，否则 Jekyll 可能在清理/拷贝静态文件时报错）：

```bash
LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8 bundle exec jekyll build
LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8 bundle exec jekyll serve
```

生成结果在 **`_site/`**。

---

## 常用 URL（`permalink: pretty` 时）

| 页面 | 路径 |
|------|------|
| 首页 | `/` |
| People 总览 | `/people/` |
| People（按 Faculty → Postdocs → PhD → Visitors 分段） | `/people/` |
| 单个成员 | `/people/<文件名>/`（如 `luc-van-gool.md` → `/people/luc-van-gool/`） |
| Research 总览 | `/research/` |
| 单个 Topic | `/research/topics/<文件名>/` |
| 论文列表 / 单篇 | `/publications/`、`/publications/<slug>/` |
| Demos | `/demos/`、`/demos/<slug>/` |
| 招聘列表 / 单条 | `/job/`、`/job/<slug>/` |
| 博客列表 / 文章 | `/blog/`、`/blog/...`（由文章日期与文件名决定） |

---

## 导航与配置

主导航在 **`_includes/navbar.html`**（内页）；首页使用 **`_includes/navbar-landing.html`**（透明导航，对齐 `landing-it-company`）。站点标题、首页文案与 **`site.landing`** 在 **`_config.yml`**。多栏页脚为 **`site.footer`**，首页赞助商为 **`site.sponsors`**。新增 collection 或修改 `permalink` 后需重新执行 `jekyll build`。

## 页面与 Block 1.3.2 模板对应关系

| 本站 | Block 参考 | 实现位置 |
|------|----------------|----------|
| 首页 | `landing-it-company.html`（视频 Hero + card-grid 研究方向） | `_layouts/home.html` + `index.md` |
| Research 列表 | `service-v1.html` + 每主题下紧凑论文列表 | `_layouts/research-list.html` + `research/index.md` |
| People（单页分段） | `blocks/team.html` **Team #3 / #2**（Faculty 大图行；Postdoc / PhD / Visitor 圆形头像卡片） | `_layouts/people.html` + `people/index.md` |
| Research Topic 子页 | 单栏：成员列表 + 紧凑论文列表 | `_layouts/topic.html`；可选 `hero_image` |
| Publications 列表 / 单篇 | 扁平紧凑列表 / `blog-single` 风格正文 | `_layouts/publications-list.html`、`_layouts/publication.html` |
| Demos 列表 | `blog.html` 三栏大图卡片 | `_layouts/demos-grid.html` + `demos/index.md` |
| Blog / Job 列表 | 与 Publications 列表相同的紧凑行样式 | `_layouts/blog-list.html`、`_layouts/job-list.html` |
| 单个 Project | `portfolio-single.html` | `_layouts/project.html`；封面等见 `_projects/*.md` 的 `cover_image` 等字段 |

---

## 克隆仓库后注意

1. **`assets` 符号链接**：默认指向同级目录 **`../block-1.3.2/dist/assets`**。请把本仓库与 Block 工程放在同一父目录下，或自行修改 `assets` 链接目标。Windows 若不支持 symlink，可复制整个 `dist/assets` 到本站根目录的 `assets/`。  
2. **示例内容**：`_people`、`_publications` 等为演示数据，上线前替换为真实元数据即可，字段名保持不变则关联逻辑无需改代码。

如有 GitHub Pages 部署需求，可再配 `baseurl`（子路径站点）与 CI 里的 `LC_ALL`；需要时可单独加一页说明部署步骤。
