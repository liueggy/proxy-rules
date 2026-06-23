# Proxy Rules

个人代理规则仓库，按 Quantumult X、Stash、Loon 分类维护。

> 仓库公开后，可直接使用 GitHub Raw URL 作为远程规则 / 远程资源链接。

## 目录结构

```text
.
├── quantumult-x/   # Quantumult X 规则、重写、任务
├── stash/          # Stash / Clash / Mihomo 规则集与覆写
├── loon/           # Loon 规则、插件
└── docs/           # 使用说明
```

## 快速导入链接

将仓库推送到 GitHub 后，以下链接中的 `liueggy/proxy-rules` 即可使用：

### Quantumult X

- 分流规则：  
  `https://raw.githubusercontent.com/liueggy/proxy-rules/main/quantumult-x/rules.list`
- 重写规则：  
  `https://raw.githubusercontent.com/liueggy/proxy-rules/main/quantumult-x/rewrite.conf`
- 任务脚本配置：  
  `https://raw.githubusercontent.com/liueggy/proxy-rules/main/quantumult-x/task.conf`

### Stash / Clash / Mihomo

- 规则集：  
  `https://raw.githubusercontent.com/liueggy/proxy-rules/main/stash/rules.yaml`
- 覆写配置：  
  `https://raw.githubusercontent.com/liueggy/proxy-rules/main/stash/override.yaml`

### Loon

- 分流规则：  
  `https://raw.githubusercontent.com/liueggy/proxy-rules/main/loon/rules.list`
- 插件：  
  `https://raw.githubusercontent.com/liueggy/proxy-rules/main/loon/plugin.plugin`

## 命名约定

- `Proxy`：默认代理策略组
- `DIRECT`：直连
- `REJECT`：拒绝 / 广告拦截
- `AI`：AI 服务策略组，可按需要在客户端中创建
- `Apple`：Apple 服务策略组，可按需要在客户端中创建

## 注意

1. 这里先放基础模板，后续可以继续按用途拆分：AI、流媒体、广告、Apple、Telegram、GitHub 等。
2. 远程规则文件建议保持纯规则格式，不要混入客户端不支持的注释或段落。
3. 如果某个软件导入失败，优先检查策略组名称是否存在，比如 `Proxy`、`AI`、`Apple`。
