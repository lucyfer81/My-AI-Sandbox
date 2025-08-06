---
date: 2025-07-30
draft: false
title: Imperfect combination of Claude Code and Silicon Flow
lang: en
---



---
date: 2025-07-30
draft: false
title: Imperfect combination of Claude Code and Silicon Flow
lang: en
---

> ** Note: Currently, only the following non-thinking models are supported (more models will be supported later)**
>
> - `Pro/moonshotai/Kimi-K2-Instruct`
> - `moonshotai/Kimi-K2-Instruct`
> - `Pro/deepseek-ai/DeepSeek-V3`
> - `deepseek-ai/DeepSeek-V3`
> - `moonshotai/Kimi-Dev-72B`
> - `baidu/ERNIE-4.5-300B-A47B`

---
date: 2025-07-30
draft: false
title: Imperfect combination of Claude Code and Silicon Flow
lang: en
---

### 1. `Pro/moonshotai/Kimi-K2-Instruct`

Everything starts well until it outputs to this point:

```text
  First initialize the infrastructure of the Node.js project:
  null<|tool_call_begin|>functions.Bash:1<|tool_call_argument_begin|>"{command: npm init -y, description: initialize Node.js project package.json}"<|tool_call_end|><|tool_calls_section_end|><|tool_calls_section_end|>
```

I understand that there was a mistake in calling the tool?

---
date: 2025-07-30
draft: false
title: Imperfect combination of Claude Code and Silicon Flow
lang: en
---

### 3. `deepseek-ai/DeepSeek-V3`

A perfect output of what it is going to do. But when I asked it to follow its plan, I repeated what I had just said, but I refused to do it.

---
date: 2025-07-30
draft: false
title: Imperfect combination of Claude Code and Silicon Flow
lang: en
---

Judging from the above test results, it seems that the model of the Kimi platform is really usable. If I used Silicon Flow, I would choose `deepseek-ai/Deepseek-V3`. Compared with its brother who didn't do anything but claimed to have done everything, it was cheaper.

