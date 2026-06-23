# 外部开源规则源

本文件由 `source/rules.yaml` 自动生成。通用大规则建议通过外部远程规则源引用，避免重复维护。

## 已接入来源

### blackmatrix7/ios_rule_script

- GitHub: https://github.com/blackmatrix7/ios_rule_script
- Branch: `master`

## 已接入分类

| 来源 | 分类 | 策略 |
|---|---|---|
| blackmatrix7 | AdvertisingLite | `REJECT` |
| blackmatrix7 | OpenAI | `AI` |
| blackmatrix7 | Claude | `AI` |
| blackmatrix7 | Gemini | `AI` |
| blackmatrix7 | GitHub | `Proxy` |
| blackmatrix7 | Telegram | `Proxy` |
| blackmatrix7 | YouTube | `Streaming` |
| blackmatrix7 | Netflix | `Streaming` |
| blackmatrix7 | Disney | `Streaming` |
| blackmatrix7 | Spotify | `Streaming` |
| blackmatrix7 | Apple | `Apple` |

## 注意

1. 外部规则会随上游变化，若上游路径调整，远程导入可能失效。
2. 广告拦截规则不要过度叠加，容易导致 App 白屏或登录异常。
3. AI / Streaming 策略组需要你在客户端配置中存在，否则导入规则可能报策略不存在。
