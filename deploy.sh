#!/bin/bash

# Hugo 双语博客部署脚本
# 适用于反向代理和Cloudflare Pages

echo "🚀 开始部署双语博客..."

# 清理旧的构建文件
rm -rf public/
rm -rf .hugo_build.lock

# 设置环境变量
export HUGO_ENV="production"

# 构建静态站点（用于Cloudflare Pages）
echo "📦 构建静态站点..."
hugo --gc --minify

echo "✅ 静态站点构建完成"

# 本地测试（反向代理模式）
echo "🌐 启动反向代理模式..."
echo "命令: hugo server --appendPort=false --bind=0.0.0.0 --baseURL=http://blog_test.vftl.site"
echo "访问: http://blog_test.vftl.site"

# 显示构建结果
echo "📁 构建文件列表:"
ls -la public/

# 显示语言文件统计
echo "🌏 语言内容统计:"
echo "中文文章: $(find content/posts -name "index.md" | wc -l)"
echo "英文文章: $(find content/posts -name "index_en.md" | wc -l)"

echo "🎉 部署脚本执行完成"