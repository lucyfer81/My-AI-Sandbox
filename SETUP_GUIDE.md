# 双语博客设置指南

## 1. 腾讯云API配置

### 获取API密钥
1. 访问：https://console.cloud.tencent.com/cam/capi
2. 创建新的API密钥
3. 在GitHub仓库设置中添加Secrets：
   - `TENCENT_SECRET_ID`: 你的SecretId
   - `TENCENT_SECRET_KEY`: 你的SecretKey

### 本地测试
```bash
export TENCENT_SECRET_ID=你的SecretId
export TENCENT_SECRET_KEY=你的SecretKey
.venv/bin/python3 scripts/translate.py
```

## 2. 工作流程

### 新文章发布流程
1. 创建中文文章：`hugo new posts/文章名/index.md`
2. 编辑内容，提交到git
3. GitHub Action自动触发翻译
4. 自动生成对应的index_en.md文件

### 目录结构
```
content/posts/
├── 文章1/
│   ├── index.md      # 中文原版
│   └── index_en.md   # 自动翻译的英文版
├── 文章2/
│   ├── index.md
│   └── index_en.md
└── ...
```

## 3. 术语表更新

编辑`translation-glossary.json`文件，添加专业术语的对应翻译。

## 4. 手动翻译

如需手动调整翻译结果，直接编辑生成的index_en.md文件即可。