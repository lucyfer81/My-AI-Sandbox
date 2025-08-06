# 新发布文章操作指南

## 快速开始

### 1. 创建新文章

```bash
# 方法一：使用Hugo命令（推荐）
hugo new posts/文章标题/index.md

# 方法二：手动创建目录和文件
mkdir -p content/posts/$(date +%Y%m%d)_文章标题
touch content/posts/$(date +%Y%m%d)_文章标题/index.md
```

### 2. 文章模板

在 `content/posts/文章标题/index.md` 中使用以下模板：

```markdown
+++
title = "文章标题"
date = $(date +%Y-%m-%d)  # 自动生成
draft = false
# 可选字段
description = "文章描述"
tags = ["标签1", "标签2"]
categories = ["分类"]
+++

## 正文内容

这里是你的文章内容...

### 图片使用

#### 本地图片
1. 将图片放在与index.md同目录下
2. 在markdown中使用相对路径引用：

```markdown
![图片描述](图片文件名.png)
```

#### 示例：
![AI截图](screenshot.png)

#### 注意事项：
- 图片文件名使用英文或数字，避免中文
- 支持格式：png, jpg, jpeg, gif, webp
- 建议图片宽度不超过1200px，文件大小不超过2MB

## 完整示例

### 目录结构
```
content/posts/
└── $(date +%Y%m%d)_我的AI项目/
    ├── index.md           # 中文原文
    ├── architecture.png   # 架构图
    ├── demo.gif          # 演示动画
    └── results.jpg       # 结果截图
```

### 文章内容示例
```markdown
+++
title = "我用AI做了一个智能待办清单"
date = 2024-01-15
draft = false
description = "分享如何使用Claude Code和腾讯云开发一个AI驱动的待办清单应用"
tags = ["AI", "开发", "应用"]
categories = ["技术分享"]
+++

## 项目背景

在快节奏的工作环境中...

### 技术架构

![系统架构](architecture.png)

### 核心功能演示

![功能演示](demo.gif)

## 实现过程...
```

## 发布后自动翻译流程

1. **推送中文文章到GitHub**后，GitHub Actions自动：
   - 检测到新的中文文章
   - 调用腾讯云翻译API
   - 生成英文版本到 `content/en/posts/相同路径/index.md`
   - 自动提交并推送翻译结果

2. **翻译后的英文文章会自动**：
   - 保持相同目录结构
   - 翻译标题、描述、标签
   - 添加 `lang: en` 标识
   - 保留所有图片引用（路径不变）

## 图片处理注意事项

### 1. 图片路径规则
- **中文文章**: `content/posts/文章标题/图片.png`
- **英文文章**: `content/en/posts/文章标题/图片.png`（自动引用相同图片）

### 2. 图片优化建议
```bash
# 压缩图片（可选）
# 使用在线工具如 TinyPNG 或本地工具

# 重命名建议
原始文件名：截图 2024-01-15 上午10.30.45.png
优化后：feature-overview-2024-01-15.png
```

### 3. 多设备适配
在markdown中设置图片尺寸：
```markdown
![描述](image.png){: width="600px"}
```

## 实用命令汇总

### 创建带图片的文章
```bash
# 1. 创建目录
POST_NAME="$(date +%Y%m%d)_ai_assistant"
mkdir -p content/posts/$POST_NAME

# 2. 创建文章文件
cat > content/posts/$POST_NAME/index.md << 'EOF'
+++
title = "我的AI助手开发记"
date = $(date +%Y-%m-%d)
draft = false
tags = ["AI", "开发"]
+++

## 项目介绍

这是一个关于...

![界面截图](ui-screenshot.png)
EOF

# 3. 添加图片
# 将图片复制到对应目录
cp your-screenshot.png content/posts/$POST_NAME/ui-screenshot.png
```

### 本地预览
```bash
# 启动本地服务器
hugo server -D

# 访问 http://localhost:1313 查看效果
```

### 发布到GitHub
```bash
git add content/posts/
git commit -m "Add new post: 文章标题"
git push origin master
```

## 故障排除

### 图片不显示
- 检查文件路径是否正确
- 确认图片已提交到Git仓库
- 检查文件扩展名是否正确

### 翻译失败
- 检查GitHub Secrets是否配置正确
- 确认腾讯云API额度充足
- 查看GitHub Actions日志获取详细信息

### 格式问题
- 使用 `hugo server` 本地预览检查格式
- 确保YAML front matter格式正确
- 检查图片文件是否损坏

## 最佳实践

1. **文件命名**：使用英文和数字，避免特殊字符
2. **图片管理**：所有图片放在文章目录内，便于管理
3. **版本控制**：及时提交图片和文章到Git
4. **备份**：重要图片保留原始文件
5. **测试**：发布前本地预览检查格式和图片

## 快捷脚本

### 一键创建新文章（保存为 `new-post.sh`）
```bash
#!/bin/bash
POST_TITLE="$1"
if [ -z "$POST_TITLE" ]; then
    echo "用法: ./new-post.sh 文章标题"
    exit 1
fi

POST_DIR="content/posts/$(date +%Y%m%d)_${POST_TITLE// /-}"
mkdir -p "$POST_DIR"

cat > "$POST_DIR/index.md" << EOF
+++
title = "$POST_TITLE"
date = $(date +%Y-%m-%d)
draft = false
tags = ["待分类"]
+++

## 引言

在这里开始你的文章...

## 总结

EOF

echo "已创建文章: $POST_DIR/index.md"
echo "将图片放入: $POST_DIR/"
```

使用方法：
```bash
chmod +x new-post.sh
./new-post.sh "我的AI项目分享"
```