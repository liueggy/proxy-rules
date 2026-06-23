# 外部开源规则源

本仓库优先维护个人规则；通用大规则建议通过外部远程规则源引用，避免重复维护。

## 已选主规则源

### blackmatrix7/ios_rule_script

- GitHub: https://github.com/blackmatrix7/ios_rule_script
- Stars: 26k+
- 覆盖客户端：Quantumult X、Loon、Clash/Stash、Surge、Shadowrocket 等
- 特点：分类非常细，适合作为外部规则源
- License: 仓库未声明标准 SPDX License，使用时建议保留来源，不要大规模复制再发布为原创

本仓库当前采用：

- QX：直接引用 `rule/QuantumultX/<Name>/<Name>.list`
- Loon：直接引用 `rule/Loon/<Name>/<Name>.list`
- Stash：通过 `rule-providers` 引用 `rule/Clash/<Name>/<Name>.yaml`

## 已接入分类

| 分类 | 用途 | 策略建议 |
|---|---|---|
| OpenAI | ChatGPT / OpenAI API | AI |
| Claude | Claude / Anthropic | AI |
| Gemini | Google Gemini | AI |
| GitHub | GitHub 相关服务 | Proxy |
| Telegram | Telegram | Proxy |
| YouTube | YouTube | Streaming |
| Netflix | Netflix | Streaming |
| Disney | Disney+ | Streaming |
| Spotify | Spotify | Streaming |
| Apple | Apple 服务 | Apple / DIRECT |
| Advertising | 广告拦截 | REJECT |
| AdvertisingLite | 轻量广告拦截 | REJECT |
| China | 国内服务 | DIRECT |
| Global | 常见国际服务 | Proxy |

## 注意

1. 外部规则会随上游变化，若上游路径调整，远程导入可能失效。
2. 广告拦截规则不要过度叠加，容易导致 App 白屏或登录异常。
3. AI / Streaming 策略组需要你在客户端配置中存在，否则导入规则可能报策略不存在。
4. Stash 使用外部 provider 时，建议通过 `stash/external-providers.yaml` 作为 Override 导入。
