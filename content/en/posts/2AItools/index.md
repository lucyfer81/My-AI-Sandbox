---
date: 2025-07-27
draft: false
title: 'Two major AI artifacts: Claude+Kimi vs. Gemini CLI, who is more fragrant?'
lang: en
---


Recently, I swiped a question on Zhihu: Which one should I choose from Claude Code or Gemini CLI? Haha, as a "mature" adult, I don't make multiple choice questions! Only children choose sides, I want them all! So, I installed both artifacts on my Ubuntu virtual machine and experienced them myself. Let me talk to you about my feelings. It is purely subjective, down-to-earth, non-technical, and the kind that ordinary people can understand.

---
date: 2025-07-27
draft: false
title: 'Two major AI artifacts: Claude+Kimi vs. Gemini CLI, who is more fragrant?'
lang: en
---

##Task 1: Let AI write code

For the first task, I threw a super detailed code requirement to these two AIs, asking them to generate code in their respective directories and place it according to the directory structure I specified. How was the result? The code quality of the two is similar, there is no big difference in functionality, and both run well.

** Cost comparison **:

- Claude+Kimi: Used 2.8 million tokens, equivalent to 9.8 dollars (the price is clearly marked on the screen, and Claude will tell you affectionately how much he spent when he quits, which is very humane). However, I used the Kimi package and actually spent 1.8 RMB. The exchange rate was touching and it felt quite worth it.
- Gemini CLI: I only used 32K token, and the cost was so low that I suspected that it was secretly fishing.

** Summary **: Claude+Kimi works well, but the token burns me so much that I can't afford it. Gemini CLI saves money to the point of flying, and the price/performance ratio is directly increased.

---
date: 2025-07-27
draft: false
title: 'Two major AI artifacts: Claude+Kimi vs. Gemini CLI, who is more fragrant?'
lang: en
---

##Task 3: Troubleshooting mistakes and exposing real skills

This part was an unexpected episode. I tried to run the code for the first module, but it turned over-it wasn't that the code was wrong, it was that the X API Key level I used was not enough (who told me to spend the subscription fee of $200/month). At this time, a judgment was made on the performance of the two.

- **Claude+Kimi**: This guy is like a detective. He proactively discovered that my API permissions were not enough, helped me analyze the problem, rejected an unreliable alternative I proposed (because it was inconsistent with the original intention), and finally used Reddit's API to bypass the problem perfectly. I only inserted two or three sentences throughout the process, and I relied on it to handle the rest myself, which saved me so much trouble.
- **Gemini CLI**: emmm, a bit of a drag. At first, it was brainless and agreed with my bad idea of changing to another X API, and it felt a bit "dog licking". Then when implementing the new solution, the code was written muddle-headed. I guess it may be that the Python library it relies on doesn't support the new version of X's API, but it never thought of using 'requests' to directly call the interface, and its IQ was a bit lost.

** Summary **: Claude+Kimi is a dimensional-reduction blow when it comes to error debugging. Gemini CLI is like a novice programmer with a good attitude but limited capabilities.

---

##Final thoughts

Claude+Kimi (non-full-blood version) has already amazed me. I feel like an all-round housekeeper with a good brain and considerate. I look forward to trying the full-blood version one day! But its token consumption is really scary. Ordinary people have to check the thickness of their wallet first when using it. Gemini CLI is like a down-to-earth tool person. Its document processing capabilities are really good (what the Internet says is right), and it is still free now, and its price/performance ratio is directly exploding. What else do you need a bicycle?

In general, Claude+Kimi is suitable for players who pursue the ultimate experience and have a good budget;Gemini CLI is the choice for civilians who save money and worry. Both are good, how to choose specifically? It depends on your wallet and needs! As for me, I will hold the free Gemini CLI fragrance for now. Claude+Kimi will wait until I win the lottery and come back to enjoy you!
