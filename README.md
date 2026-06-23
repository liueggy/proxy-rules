<div align="center">

# Proxy Rules

Personal rule center for Quantumult X, Stash, Clash, Mihomo and Loon.

[![Build](https://img.shields.io/github/actions/workflow/status/liueggy/proxy-rules/build-rules.yml?branch=main&style=for-the-badge&label=Build)](https://github.com/liueggy/proxy-rules/actions)
[![Last Commit](https://img.shields.io/github/last-commit/liueggy/proxy-rules?style=for-the-badge&label=Last%20Commit)](https://github.com/liueggy/proxy-rules/commits/main)
[![Repo Size](https://img.shields.io/github/repo-size/liueggy/proxy-rules?style=for-the-badge&label=Repo%20Size)](https://github.com/liueggy/proxy-rules)

</div>

---

## Overview

<table>
<tr>
<td width="33%" valign="top">

<b>Clients</b><br><br>

<a href="#quantumult-x"><img src="https://img.shields.io/badge/Quantumult%20X-111827?style=flat-square" /></a>
<a href="#stash--clash--mihomo"><img src="https://img.shields.io/badge/Stash-111827?style=flat-square" /></a>
<a href="#loon"><img src="https://img.shields.io/badge/Loon-111827?style=flat-square" /></a>

</td>
<td width="33%" valign="top">

<b>Pipeline</b><br><br>

<a href="source/rules.yaml"><img src="https://img.shields.io/badge/source-rules.yaml-2563eb?style=flat-square" /></a>
<a href="scripts/build.py"><img src="https://img.shields.io/badge/build-generator-2563eb?style=flat-square" /></a>
<a href="scripts/check.py"><img src="https://img.shields.io/badge/check-validator-2563eb?style=flat-square" /></a>

</td>
<td width="33%" valign="top">

<b>External</b><br><br>

<a href="https://github.com/blackmatrix7/ios_rule_script"><img src="https://img.shields.io/badge/blackmatrix7-ios__rule__script-0f766e?style=flat-square" /></a>
<a href="docs/external-sources.md"><img src="https://img.shields.io/badge/docs-external__sources-0f766e?style=flat-square" /></a>

</td>
</tr>
</table>

---

## Quick Import

### Quantumult X

[![Main Rules](https://img.shields.io/badge/Main%20Rules-rules.list-111827?style=flat-square)](quantumult-x/rules.list)

```text
https://raw.githubusercontent.com/liueggy/proxy-rules/main/quantumult-x/rules.list
```

[![External Rules](https://img.shields.io/badge/External%20Rules-filter__remote-111827?style=flat-square)](quantumult-x/external-filter-remote.conf)

```text
https://raw.githubusercontent.com/liueggy/proxy-rules/main/quantumult-x/external-filter-remote.conf
```

[![Policy Snippet](https://img.shields.io/badge/Policy%20Snippet-policy.conf-111827?style=flat-square)](quantumult-x/policy-snippet.conf)

```text
https://raw.githubusercontent.com/liueggy/proxy-rules/main/quantumult-x/policy-snippet.conf
```

<details>
<summary>More</summary>

Rewrite:

```text
https://raw.githubusercontent.com/liueggy/proxy-rules/main/quantumult-x/rewrite.conf
```

Task:

```text
https://raw.githubusercontent.com/liueggy/proxy-rules/main/quantumult-x/task.conf
```

</details>

### Stash / Clash / Mihomo

[![Override](https://img.shields.io/badge/Override-override.yaml-111827?style=flat-square)](stash/override.yaml)

```text
https://raw.githubusercontent.com/liueggy/proxy-rules/main/stash/override.yaml
```

[![External Override](https://img.shields.io/badge/External%20Override-providers.yaml-111827?style=flat-square)](stash/external-providers.yaml)

```text
https://raw.githubusercontent.com/liueggy/proxy-rules/main/stash/external-providers.yaml
```

[![Ruleset](https://img.shields.io/badge/Ruleset-rules.yaml-111827?style=flat-square)](stash/rules.yaml)

```text
https://raw.githubusercontent.com/liueggy/proxy-rules/main/stash/rules.yaml
```

### Loon

[![Main Rules](https://img.shields.io/badge/Main%20Rules-rules.list-111827?style=flat-square)](loon/rules.list)

```text
https://raw.githubusercontent.com/liueggy/proxy-rules/main/loon/rules.list
```

[![External Rules](https://img.shields.io/badge/External%20Rules-remote__rules-111827?style=flat-square)](loon/external-remote-rules.conf)

```text
https://raw.githubusercontent.com/liueggy/proxy-rules/main/loon/external-remote-rules.conf
```

[![Plugin](https://img.shields.io/badge/Plugin-plugin.plugin-111827?style=flat-square)](loon/plugin.plugin)

```text
https://raw.githubusercontent.com/liueggy/proxy-rules/main/loon/plugin.plugin
```

[![Policy Snippet](https://img.shields.io/badge/Policy%20Snippet-policy.conf-111827?style=flat-square)](loon/policy-snippet.conf)

```text
https://raw.githubusercontent.com/liueggy/proxy-rules/main/loon/policy-snippet.conf
```

---

## Categories

<table>
<tr>
<td width="50%" valign="top">

<b>AI</b><br><br>

<a href="quantumult-x/rules/ai.list"><img src="https://img.shields.io/badge/QX-ai.list-2563eb?style=flat-square" /></a>
<a href="stash/rules/ai.yaml"><img src="https://img.shields.io/badge/Stash-ai.yaml-2563eb?style=flat-square" /></a>
<a href="loon/rules/ai.list"><img src="https://img.shields.io/badge/Loon-ai.list-2563eb?style=flat-square" /></a>

</td>
<td width="50%" valign="top">

<b>Direct Servers</b><br><br>

<a href="quantumult-x/rules/direct-servers.list"><img src="https://img.shields.io/badge/QX-direct.list-0f766e?style=flat-square" /></a>
<a href="stash/rules/direct-servers.yaml"><img src="https://img.shields.io/badge/Stash-direct.yaml-0f766e?style=flat-square" /></a>
<a href="loon/rules/direct-servers.list"><img src="https://img.shields.io/badge/Loon-direct.list-0f766e?style=flat-square" /></a>

</td>
</tr>
</table>

<details>
<summary>Copy category links</summary>

AI for Quantumult X:

```text
https://raw.githubusercontent.com/liueggy/proxy-rules/main/quantumult-x/rules/ai.list
```

AI for Stash:

```text
https://raw.githubusercontent.com/liueggy/proxy-rules/main/stash/rules/ai.yaml
```

AI for Loon:

```text
https://raw.githubusercontent.com/liueggy/proxy-rules/main/loon/rules/ai.list
```

Direct servers for Quantumult X:

```text
https://raw.githubusercontent.com/liueggy/proxy-rules/main/quantumult-x/rules/direct-servers.list
```

Direct servers for Stash:

```text
https://raw.githubusercontent.com/liueggy/proxy-rules/main/stash/rules/direct-servers.yaml
```

Direct servers for Loon:

```text
https://raw.githubusercontent.com/liueggy/proxy-rules/main/loon/rules/direct-servers.list
```

</details>

---

## Policies

<table>
<tr><td><code>DIRECT</code></td><td>China, LAN, own servers</td></tr>
<tr><td><code>Proxy</code></td><td>Default proxy</td></tr>
<tr><td><code>AI</code></td><td>OpenAI, Claude, Gemini</td></tr>
<tr><td><code>Streaming</code></td><td>YouTube, Netflix, Disney, Spotify</td></tr>
<tr><td><code>Apple</code></td><td>Apple, iCloud, CDN</td></tr>
<tr><td><code>REJECT</code></td><td>Ads, trackers</td></tr>
</table>

---

## Direct Servers

<table>
<tr><th>Name</th><th>IP</th><th>Policy</th></tr>
<tr><td>ocean</td><td><code>167.71.221.110</code></td><td><code>DIRECT</code></td></tr>
<tr><td>Hermes</td><td><code>168.144.136.246</code></td><td><code>DIRECT</code></td></tr>
<tr><td>toy</td><td><code>167.71.214.73</code></td><td><code>DIRECT</code></td></tr>
</table>

---

## Build

```bash
python3 scripts/build.py
python3 scripts/check.py
```

```bash
python3 scripts/check.py --urls
```

---

## Layout

```text
.
├── source/rules.yaml
├── scripts/build.py
├── scripts/check.py
├── quantumult-x/
├── stash/
├── loon/
├── docs/
└── .github/workflows/
```

---

<div align="center">

[![GitHub](https://img.shields.io/badge/GitHub-liueggy%2Fproxy--rules-111827?style=for-the-badge)](https://github.com/liueggy/proxy-rules)

</div>
