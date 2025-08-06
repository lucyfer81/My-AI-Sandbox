---
title: 'Claude Code 和 Silicon Flow 的奇妙相遇'
date: 2025-07-30
draft: false
lang: zh
---

上周调试通了Clude Code 和 Kimi，于是我开始惦记我在Silicon Flow还有几十块钱别浪费了呀，于是开始研究他们俩能不能一起过。

当中还研究过是不是能够用Claude Code Router，可谁曾想Silicon Flow 自己就已经支持 Anthropic API了呢。省了我很多事情。

老规矩，安装配置参照Silicon Flow的官方文档：https://docs.siliconflow.cn/cn/usercases/use-siliconcloud-in-ClaudeCode

> **注：目前仅支持下列非思考模型（更多模型稍后支持）**
>
> - `Pro/moonshotai/Kimi-K2-Instruct`
> - `moonshotai/Kimi-K2-Instruct`
> - `Pro/deepseek-ai/DeepSeek-V3`
> - `deepseek-ai/DeepSeek-V3`
> - `moonshotai/Kimi-Dev-72B`
> - `deepseek-ai/DeepSeek-Coder-V2-Instruct`
> - `deepseek-ai/DeepSeek-R1`
> - `deepseek-ai/DeepSeek-R1-Distill-Qwen-32B`
> - `deepseek-ai/DeepSeek-R1-Distill-Llama-70B`

## 我的配置过程

### 1. 安装 Claude Code

```bash
npm install -g @anthropic-ai/claude-code
```

### 2. 配置 Silicon Flow

在 `~/.claude.json` 中添加：

```json
{
  "mcpServers": {
    "anthropic": {
      "command": "npx",
      "args": ["-y", "@anthropic-ai/claude-mcp-server"],
      "env": {
        "ANTHROPIC_API_KEY": "你的硅基流动API Key",
        "ANTHROPIC_BASE_URL": "https://api.siliconflow.cn/v1"
      }
    }
  }
}
```

### 3. 使用体验

配置完成后，Claude Code 就可以直接使用 Silicon Flow 的模型了。我测试了一下，效果还不错：

- **响应速度**：比直接访问 Anthropic 官网快不少，毕竟是国内节点
- **价格**：硅基流动的价格还算合理，特别是有活动的时候
- **稳定性**：目前为止没遇到什么问题

## 小技巧

如果你不想全局安装 Claude Code，也可以在项目目录下安装：

```bash
npm install @anthropic-ai/claude-code
npx claude
```

## 总结

总的来说，Silicon Flow + Claude Code 的组合还是挺香的。特别是对于我这种经常需要写代码的人来说，省去了很多麻烦。

唯一的遗憾是目前还不支持 Claude 的思考模型，希望后面能加上吧。