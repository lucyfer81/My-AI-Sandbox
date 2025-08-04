+++
title = 'Claude Code与 Silicon Flow的不完美结合'
date = 2025-07-30
draft = false
+++


---

上周调试通了Clude Code 和 Kimi，于是我开始惦记我在Silicon Flow还有几十块钱别浪费了呀，于是开始研究他们俩能不能一起过。

当中还研究过是不是能够用Claude Code Router，可谁曾想Silicon Flow 自己就已经支持 Anthropic API了呢。省了我很多事情。

老规矩，安装配置参照Silicon Flow的官方文档：https://docs.siliconflow.cn/cn/usercases/use-siliconcloud-in-ClaudeCode

---

> **注：目前仅支持下列非思考模型（更多模型稍后支持）**
>
> - `Pro/moonshotai/Kimi-K2-Instruct`
> - `moonshotai/Kimi-K2-Instruct`
> - `Pro/deepseek-ai/DeepSeek-V3`
> - `deepseek-ai/DeepSeek-V3`
> - `moonshotai/Kimi-Dev-72B`
> - `baidu/ERNIE-4.5-300B-A47B`

---

但是非常不幸，并非如此。

我轮流测试了这几个模型，都是同样的提示词：

> 请阅读本目录下的gdel_lightapp.md，我想按照它的建议用nodejs开发这个轻应用。请指导我如何进行。请用中文输出你的所有建议和指导

结果如下：

---

### 1. `Pro/moonshotai/Kimi-K2-Instruct`

开始一切都很好，直到它输出到这一步：

```text
  首先初始化Node.js项目的基础结构：
  null<|tool_call_begin|>functions.Bash:1<|tool_call_argument_begin|>"{command: npm init -y, description: 初始化Node.js项目package.json}"<|tool_call_end|><|tool_calls_section_end|><|tool_calls_section_end|>
```

我理解就是调用工具出错呗？

---

### 2. `moonshotai/Kimi-K2-Instruct`、`moonshotai/Kimi-Dev-72B`、`baidu/ERNIE-4.5-300B-A47B`

直接调用模型就出错。

---

### 3. `deepseek-ai/DeepSeek-V3`

非常完美的输出了它要做什么。但是当我让它按照自己的计划做的时候，重复了一遍自己刚才说的，但是打死也不做。

---

### 4. `Pro/deepseek-ai/DeepSeek-V3`

非常完美的输出了它要做什么。当我让它按照自己的计划做的时候，它声称自己做了，但是实际上什么也没做。

---

就上面的测试结果看起来，真正能用的还是Kimi平台的模型。如果用Silicon Flow的话，我会选择`deepseek-ai/DeepSeek-V3`。对比它那个什么都没做，却声称都做了的兄弟，好歹它便宜一点。

