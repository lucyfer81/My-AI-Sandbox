+++
title = '智谱，其实挺靠谱'
date = 2025-08-20T13:52:34+08:00
draft = false
+++
**大家好，我是老V。一个非常不专业的AI不极客。**

智谱的GLM4.5模型发布也有一段时间了，而我也将它配置在Claude Code里面用了一段时间了。之所以没有及时发个评测文章，也是因为我在用它做一个应用。确实挺香的。现在应用框架做完，有时间来写点东西，回顾一下这几天使用GLM4.5的感受了。


老规矩，安装的步骤不罗嗦，配置步骤看官方文档。https://docs.z.ai/scenario-example/develop-tools/claude  或者：https://docs.bigmodel.cn/cn/guide/develop/claude  简单来说就是和Kimi一模一样。

这里要说一个有意思的事情了。我一开始搜索智谱，其实被引导到了https://z.ai/ 稀里糊涂用google账号登录，创建了个key，放进Claude Code使用。因为它号称免费，我也没想太多。过了一段时间以后，我无意间点了网页上的Billing，它显示我用了一块多美刀。我有点糊涂，这到底是免费还是不免费啊。你说免费吧，干嘛显示我用了多少钱？你说不免费吧，它也没收我钱。不管它，羊毛继续薅，纵欲在我欠它2块多美刀的时候它不给我用了。想想还挺惋惜。

后来我搜索了才知道，z.ai应该是给外国人用的。咱们自己用https://open.bigmodel.cn。好吧，开源大模型呗。研究了文档得知，GLM-4.5 和 GLM-4.5-Air 都可以用在Claude Code里。默认使用GLM-4.5。

配置好了开干。这次我正好有现成想做的设计，直接扔给它。三下五除二完成。当然不可能一次性百分之百正确，后面也需要排错。但是好在Claude Code + GLM4.5的排错和 Claude Code+ Kimi2一样挺靠谱。但是token的使用确实惊人。改一个bug烧掉1M的token是常事儿。因为心疼钱，所以当中我还穿插了用QWEN Code 和Gemini CLI来排错。实事求是，这俩确实不如Claude Code + GLM4.5 或Claude Code+ Kimi2。 这更应征了我的想法，Gemini CLI的脚本不如Claude Code。可能Claude Code天生就是为了代码准备的。

但是有一个雷需要提醒，虽然GLM-4.5-Air 可以配置在Claude Code里，但是效果大大不如GLM-4.5。

好了，大家如果有兴趣，自己也可以去试试。新注册用户还有免费送token：Join BigModel.cn via my link for 20M tokens! Explore AGI apps with me. Link: https://www.bigmodel.cn/invite?icode=3UCbs3vJ5bJrKdeKL%2BzG%2BEjPr3uHog9F4g5tjuOUqno%3D



## 后记
我不是专业的AI测评，而上面的感受也非常主观。但无论如何，智谱挺靠谱。可以作为Kimi2的另一个选择。

**我是老V，一个非常不专业的AI领域创作者。想了解更多AI科技动态？欢迎关注我的博客 “AI布知道”，获取最新AI资讯与浅薄解析！ 博客链接：https://blog.vftl.top 或 https://blog.vftl.site**
