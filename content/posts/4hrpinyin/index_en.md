---
date: 2025-04-30
draft: false
title: Human-computer interaction, 4-hour quick-access Pinyin Mini games
lang: en
---


** The reason for the thought is that my son is in the first grade, and he is a little confused about the same pronunciation. b and d, p and q, front and back nasal sounds, flat and raised tongue sounds, and what's even more maddening is that the second and fourth sounds are still unclear. So I thought, could I write a simple Web version of the exercise application in Python and practice it every day? **

So, I first asked Deepseek: Does Python have a library that can parse Chinese characters into pinyin? The answer was:

---
date: 2025-04-30
draft: false
title: Human-computer interaction, 4-hour quick-access Pinyin Mini games
lang: en
---

###2. Other optional libraries
#### 1. **xpinyin**
- ** Features **: Lightweight library, suitable for simple scenarios, supports acronyms and basic polyphones.
- ** Example **:
  ```python
  from xpinyin import Pinyin
  p = Pinyin()
  print(p. get_pinyin("China", " ") #Output: zhong guo
  ```

#### 2. **jieba has embedded pinyin function **
- ** Applicable scenarios **: If the 'jieba' word segmentation has been used, you can combine its pinyin module to simplify the process.
- ** Example **:
  ```python
  import jieba.pinyin
  print(list(jieba.pinyin.cut("China"))) #Output: "'zhong ', 'guo']
  ```

---
date: 2025-04-30
draft: false
title: Human-computer interaction, 4-hour quick-access Pinyin Mini games
lang: en
---

###4. Performance and Expansion
- ** Performance optimization **: pypinyin optimizes memory usage for long text, and the actual conversion time of 100,000 characters is about 0.5 seconds (reference source: CSDN technical document).
- ** Community support **: GitHub is continuously updated, with detailed documentation, and you can quickly provide feedback through Issues if you encounter problems.

---
date: 2025-04-30
draft: false
title: Human-computer interaction, 4-hour quick-access Pinyin Mini games
lang: en
---

** Is it clear? Then I sorted out my needs. For example, where do I want my son to practice? It definitely cannot be on my computer. He has an iPad. But I definitely don't have the ability to use python to develop an iPad application for him. (I did ask Deepseek this question, and its answer directly persuaded me to quit. **

So my second question is:
```
I want to use python's pypinyin library to make a web version of Pinyin practice Mini programs and use it with safari on my iPad. Requirements:
1) Hosted on a cloud Ubuntu dual-core 4G memory virtual machine 
2) Personal use, regardless of load
3) Pre-upload a txt file (uploaded by non-players) under the game directory, with a 2-character, 3-character, or 4-character word on each line. Call during game time. 4) Generate several initials and several finals (including tones), allowing players to choose to pair them. Successful pairing results in one point: 5) Confusion options are required, such as flat tongue, raised tongue, front nasal and back nasal, the same as finals, but different tones.
6) For home games, don't design too complex. The current generation design architecture does not need to output code.
```

You can see its reply and my follow-up communication here: [https://zhida.zhihu.com/search/3660727441320885667? utm_psn=1900496915898044702]()

I learned something more from this, so my third question followed:

```
#I want to use python's pypinyin library to make a web version of Pinyin practice Mini programs and use it with safari on my iPad. Requirements:
 ** Hosted on an Ubuntu dual-core 4G memory virtual machine in the cloud **
 ** Personal use, regardless of load **
 ** Pre-upload a txt file (uploaded by non-players) in the game directory, with a 2-character, 3-character, or 4-character word on each line. Call during game time. **
 ** Generate several initials and several finals (including tones), allowing players to choose to pair them. Successful pairing and score one point **
 ** Need confusing options, such as flat tongue, raised tongue, front nasal and back nasal, same as finals, but different tones. **
 ** Home games, no concurrency requirements, only use Nginx +Flask.** 
 ##Architecture: /pinyin_game
          丨 ── app.py (main program)
          ├── /static
          │   ├── game.css
          │   └── game.js
          ├── /templates
          │   └── index.html
          ├── /game_data
          │   └── words.txt
          └── requirements.txt

Now requirements: 1) As a python programmer, if you have any doubts about the requirements, you can ask me, and I will answer.
2) When you have collected all requirements, output the complete app.py code
```

From this point on, I started asking Deepseek to output code. Our communication session can be found here [https://zhida.zhihu.com/search/3660886151844133199? utm_psn=1900497277719643426]()

After that, there were some cumbersome debugging steps, so I wouldn't post the number of words. I even spent more than 50% of my time learning from Deepseek how to configure Nginx + Waitress to suit my Mini games.

Summary:
1. Don't expect a conversation to allow Deepseek to fulfill your needs. Don't even expect Deepseek to implement requirements in a context. Limited by the length of the morning and afternoon and the hallucinations it can create as the context increases, I would suggest restarting the conversation after collecting the answers to your current question.
2. Deepseek allows you to get answers faster, but how to use the answers depends on our own thinking. We lack relevant knowledge, but we have the ability to use this knowledge.
3. Don't expand your needs. Home applications have no requirements for concurrency, so when I found out that it recommended me to deploy using Nginx + gunicorn, and I found that gunicorn took up a lot of my memory, I decisively asked if it had a more lightweight solution and finally chose waitress.

Finally, hide a secret item: If you think that Deepseek's official website keeps crashing, I recommend you download the Cherry Studio + silicon-based mobile API. Register and receive 20 million tokens: [https://cloud.siliconflow.cn/i/iLENLilu]()


