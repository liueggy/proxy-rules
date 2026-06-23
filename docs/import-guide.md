# 远程导入说明

## Quantumult X

示例配置：

```ini
[filter_remote]
https://raw.githubusercontent.com/liueggy/proxy-rules/main/quantumult-x/rules.list, tag=Eggy Rules, force-policy=Proxy, update-interval=86400, opt-parser=false, enabled=true

[rewrite_remote]
https://raw.githubusercontent.com/liueggy/proxy-rules/main/quantumult-x/rewrite.conf, tag=Eggy Rewrite, update-interval=86400, opt-parser=false, enabled=true

[task_remote]
https://raw.githubusercontent.com/liueggy/proxy-rules/main/quantumult-x/task.conf, tag=Eggy Task, update-interval=86400, opt-parser=false, enabled=true
```

## Stash

Stash 推荐导入 Override：

```yaml
https://raw.githubusercontent.com/liueggy/proxy-rules/main/stash/override.yaml
```

如果你在主配置中手动引用规则集：

```yaml
rule-providers:
  eggy-custom:
    type: http
    behavior: classical
    url: https://raw.githubusercontent.com/liueggy/proxy-rules/main/stash/rules.yaml
    path: ./ruleset/eggy-custom.yaml
    interval: 86400

rules:
  - RULE-SET,eggy-custom,Proxy
  - GEOIP,CN,DIRECT
  - MATCH,Proxy
```

## Loon

### Remote Rule

```ini
[Remote Rule]
https://raw.githubusercontent.com/liueggy/proxy-rules/main/loon/rules.list, policy=Proxy, tag=Eggy Rules, enabled=true
```

### Plugin

```ini
https://raw.githubusercontent.com/liueggy/proxy-rules/main/loon/plugin.plugin
```

## 常见问题

### 1. 导入后提示策略组不存在

请在客户端里创建这些策略组，或把规则里的策略名改成你已有的：

- `Proxy`
- `AI`
- `Apple`
- `DIRECT`
- `REJECT`

### 2. Raw 链接打不开

可以尝试将 `raw.githubusercontent.com` 换成镜像域名，或确保当前网络能访问 GitHub Raw。
