---
date: 2025-08-10 17:10:10+08:00
draft: false
lang: en
title: Want to collect QwenCode's wool? wait
---


Hello everyone, I am Old V, a very unprofessional AI geek.

##Preface

When I was testing Claude + Kimi2 VS Gemini CLI, I didn't dare to test Qwen Code because I saw it online that it would "backstab" and unknowingly bill you a hundred yuan. This time I heard that it provides a free quota of 2000 requests per day to users in the mainland of China, which once again aroused my interest in collecting wool. At least, money will not be deducted for no reason.

##Installation and Certification

Let's just do it, and our execution power is still strong! Refer to [QwenCode GitHub Page](https://github.com/QwenLM/qwen-code), the installation steps are clearly written, which is not much different from Claude Code and Gemini CLI. It is worth mentioning that QwenCode provides two authentication methods:

1. **OAuth authentication **: It will jump to a page and ask you to enter your account password. On a system without a GUI (such as Linux), it will give you a string of URLs that you can copy into the browser of other devices to complete the authentication.
2. ** Customize OpenAI compatible configuration **: You can manually set baseURL, Key and model.

Of course, in order to collect wool, we must be thorough! I directly use OAuth certification under Ubuntu. However, the problem comes:

- It tells me to copy the URL, but don't flash your screen. I left the mouse button to hold down all links and right click to select Copy, but I couldn't do any of these actions.
- The screen keeps flashing, and the QR code is not displayed completely. I can't even scroll the mouse to display the QR code completely!
- I didn't take a screenshot to show you what state it was at that time. I suggest you try it yourself. I hope I'm not the only one who encountered this problem.

Finally, based on superhuman memory (actually, I took a photo), I typed the URL word for word in the browser to complete the login. If the performance in the subsequent tests is good, this small flaw will not obscure the shortcomings.

##Test Experience

As usual, I threw the design documents I had thrown to Claude Code and Gemini CLI to QwenCode and let it output the code. Result:

- ** Speed **: The output is very fast. After completing it, I checked it against the design document to see if the file was misplaced in the directory. He is a very careful child.
- **Token consumption **: Only 48K token is used, which saves a lot compared to Claude Code.

However, despite being careful and saving, my job is not satisfactory:

1. Running code reported pandas and numpy errors.
2. It analyzed a bunch and recommended reinstalling pandas and numpy. After installation, the error was still reported.
3. It then asked me to install a specified version of the library, saying it was to eliminate compatibility issues. But weren't you the one who gave requirements.txt?
4. I still reported an error, but I still need to download the binary file and compile it again? Stop playing!

If you have read my previous articles about Claude Code and Gemini CLI, Gemini CLI once disagreed and asked me to delete the virtual environment. QwenCode is really worthy of being code from fork. It has the same temper and violently corrects mistakes if there is a disagreement.

##File sorting task

At this point, there is no need to continue troubleshooting. I asked it to do some simple file sorting tasks: write the current directory structure and all code to the Markdown file. Result:

- Like Gemini CLI, it is fast, accurate, and does not do much.
- Token consumption is still low, 48K, and a total of less than 1M.

##Summary and Suggestions

If I had to choose between Claude Code and Gemini CLI to write code, I would definitely choose Claude Code. Even if I only used Kimi2's model, the effect would be good. The Gemini CLI uses the Gemini 2.5 Pro, but its performance is average. Today's QwenCode inherits the shortcomings of Gemini CLI.

However, I couldn't bear to delete the 2000 free requests a day. It's okay to keep it for some simple chores, but there are always some small tasks that can be used.

- ** Want to write code in QwenCode? ** It is recommended to wait a little longer, stability needs to be improved.
- ** Want to play? ** Highly recommend trying it for free! After all, my evaluation is subjective and there are few cases. Your actual experience is the most important.

##About me

I am Lao V, a very unprofessional creator in the AI field. Want to learn more about AI technology trends? Welcome to follow my blog **[AI Bu Know](https://blog.vftl.top/)** or **[alternate link](https://blog.vftl.site/)** to get the latest AI information and superficial analysis!
