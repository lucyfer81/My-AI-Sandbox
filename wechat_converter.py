#!/usr/bin/env python3
"""
微信公众号文章转换器
将Hugo博客文章转换为微信公众号富文本格式
"""

import os
import re
import argparse
import markdown
from pathlib import Path
from datetime import datetime
import base64
import mimetypes


class WeChatConverter:
    def __init__(self, posts_dir="content/posts", output_dir="wechat_articles"):
        self.posts_dir = Path(posts_dir)
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        
        # 初始化markdown转换器
        self.md = markdown.Markdown(extensions=[
            'fenced_code',
            'tables',
            'nl2br',
            'sane_lists'
        ])
    
    def parse_frontmatter(self, content):
        """解析Hugo frontmatter"""
        lines = content.split('\n')
        
        # 找到frontmatter的起始和结束位置
        start_idx = -1
        end_idx = -1
        
        for i, line in enumerate(lines):
            if line.strip() == '+++':
                if start_idx == -1:
                    start_idx = i
                else:
                    end_idx = i
                    break
        
        if start_idx == -1 or end_idx == -1:
            return {}, content
        
        # 解析frontmatter内容
        frontmatter_lines = lines[start_idx+1:end_idx]
        frontmatter = {}
        
        for line in frontmatter_lines:
            if '=' in line:
                key, value = line.split('=', 1)
                key = key.strip()
                value = value.strip().strip("'\"")
                frontmatter[key] = value
        
        # 获取正文内容
        main_content = '\n'.join(lines[end_idx+1:])
        
        return frontmatter, main_content
    
    def convert_markdown_to_wechat(self, content, post_dir):
        """将markdown转换为微信公众号富文本格式"""
        
        # 处理图片引用
        def replace_image(match):
            alt_text = match.group(1)
            image_path = match.group(2)
            
            # 构建完整图片路径
            full_image_path = post_dir / image_path
            
            if full_image_path.exists():
                # 读取图片并转换为base64
                with open(full_image_path, 'rb') as img_file:
                    img_data = img_file.read()
                    img_base64 = base64.b64encode(img_data).decode('utf-8')
                    
                # 获取图片类型
                mime_type, _ = mimetypes.guess_type(str(full_image_path))
                if not mime_type:
                    mime_type = 'image/jpeg'
                
                # 微信公众号图片格式
                return f'<img src="data:{mime_type};base64,{img_base64}" alt="{alt_text}" style="max-width: 100%; height: auto; display: block; margin: 10px 0;">'
            else:
                # 如果图片不存在，返回占位符
                return f'<div style="color: #999; text-align: center; padding: 20px; background: #f5f5f5; margin: 10px 0;">[图片: {image_path}]</div>'
        
        # 替换markdown图片语法
        content = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', replace_image, content)
        
        # 转换markdown为HTML
        html_content = self.md.convert(content)
        
        # 微信公众号样式优化
        styled_content = self.apply_wechat_styles(html_content)
        
        return styled_content
    
    def apply_wechat_styles(self, html_content):
        """应用微信公众号样式"""
        
        # 为不同标签添加样式
        style_rules = {
            'h1': 'font-size: 20px; font-weight: bold; margin: 20px 0 15px 0; color: #333; line-height: 1.4;',
            'h2': 'font-size: 18px; font-weight: bold; margin: 18px 0 12px 0; color: #333; line-height: 1.4;',
            'h3': 'font-size: 16px; font-weight: bold; margin: 16px 0 10px 0; color: #333; line-height: 1.4;',
            'p': 'font-size: 16px; line-height: 1.8; margin: 15px 0; color: #333; text-align: justify;',
            'blockquote': 'border-left: 4px solid #e6e6e6; padding-left: 15px; margin: 15px 0; color: #666; font-style: italic;',
            'code': 'background-color: #f5f5f5; padding: 2px 4px; border-radius: 3px; font-family: monospace; font-size: 14px;',
            'pre': 'background-color: #f5f5f5; padding: 15px; border-radius: 5px; overflow-x: auto; margin: 15px 0;',
            'ul': 'margin: 15px 0; padding-left: 20px;',
            'ol': 'margin: 15px 0; padding-left: 20px;',
            'li': 'margin: 8px 0; font-size: 16px; line-height: 1.6;',
            'table': 'width: 100%; border-collapse: collapse; margin: 15px 0;',
            'th': 'background-color: #f5f5f5; padding: 12px; text-align: left; font-weight: bold; border: 1px solid #ddd;',
            'td': 'padding: 12px; border: 1px solid #ddd; font-size: 14px; line-height: 1.5;',
            'strong': 'font-weight: bold;',
            'em': 'font-style: italic;'
        }
        
        # 应用样式到HTML内容
        for tag, style in style_rules.items():
            # 使用正则表达式为标签添加样式
            pattern = f'<{tag}([^>]*)>'
            replacement = f'<{tag} style="{style}"\\1>'
            html_content = re.sub(pattern, replacement, html_content)
        
        # 包装在主容器中
        wrapped_content = f'''
<div style="max-width: 600px; margin: 0 auto; padding: 20px; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', sans-serif;">
{html_content}
</div>
'''
        
        return wrapped_content
    
    def generate_wechat_html(self, frontmatter, content, post_name):
        """生成完整的微信公众号HTML"""
        
        title = frontmatter.get('title', '无标题')
        date = frontmatter.get('date', '')
        
        # 格式化日期
        if date:
            try:
                date_obj = datetime.fromisoformat(date.replace('T', ' ').replace('Z', '+00:00'))
                formatted_date = date_obj.strftime('%Y年%m月%d日')
            except:
                formatted_date = date
        else:
            formatted_date = ''
        
        # 生成完整HTML
        html_template = f'''<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{
            margin: 0;
            padding: 0;
            background-color: #fff;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', sans-serif;
        }}
        .article-header {{
            text-align: center;
            padding: 30px 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            margin-bottom: 30px;
        }}
        .article-title {{
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 10px;
            line-height: 1.3;
        }}
        .article-date {{
            font-size: 14px;
            opacity: 0.9;
        }}
        .article-content {{
            max-width: 600px;
            margin: 0 auto;
            padding: 0 20px 40px;
        }}
        img {{
            max-width: 100%;
            height: auto;
            display: block;
            margin: 15px 0;
            border-radius: 5px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }}
        @media (max-width: 768px) {{
            .article-title {{
                font-size: 20px;
            }}
            .article-content {{
                padding: 0 15px 30px;
            }}
        }}
    </style>
</head>
<body>
    <div class="article-header">
        <div class="article-title">{title}</div>
        <div class="article-date">{formatted_date}</div>
    </div>
    <div class="article-content">
        {content}
    </div>
</body>
</html>'''
        
        return html_template
    
    def convert_post(self, post_path):
        """转换单个博客文章"""
        post_path = Path(post_path)
        
        if not post_path.exists():
            print(f"文章不存在: {post_path}")
            return False
        
        # 读取文章内容
        with open(post_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 解析frontmatter和正文
        frontmatter, main_content = self.parse_frontmatter(content)
        
        # 获取文章所在目录（用于图片路径解析）
        post_dir = post_path.parent
        
        # 转换markdown为微信公众号格式
        wechat_content = self.convert_markdown_to_wechat(main_content, post_dir)
        
        # 生成完整HTML
        html_content = self.generate_wechat_html(frontmatter, wechat_content, post_path.stem)
        
        # 保存输出文件（使用目录名作为文件名）
        dir_name = post_path.parent.name
        output_filename = f"{dir_name}_wechat.html"
        output_path = self.output_dir / output_filename
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"转换完成: {post_path.name} -> {output_path}")
        return True
    
    def convert_all_posts(self):
        """转换所有博客文章"""
        if not self.posts_dir.exists():
            print(f"文章目录不存在: {self.posts_dir}")
            return
        
        # 获取已转换的文件列表
        converted_files = set()
        if self.output_dir.exists():
            for file in self.output_dir.glob("*_wechat.html"):
                # 从文件名中提取目录名（去掉_wechat.html后缀）
                dir_name = file.stem.replace("_wechat", "")
                converted_files.add(dir_name)
        
        converted_count = 0
        skipped_count = 0
        
        # 遍历所有文章目录
        for post_dir in self.posts_dir.iterdir():
            if post_dir.is_dir():
                index_file = post_dir / "index.md"
                if index_file.exists():
                    dir_name = post_dir.name
                    
                    # 检查是否已经转换过
                    if dir_name in converted_files:
                        print(f"跳过已转换的文章: {dir_name}")
                        skipped_count += 1
                        continue
                    
                    # 转换文章
                    if self.convert_post(index_file):
                        converted_count += 1
        
        print(f"\n转换完成！")
        print(f"新转换文章: {converted_count} 篇")
        print(f"跳过已转换文章: {skipped_count} 篇")
        print(f"输出目录: {self.output_dir}")
    
    def convert_recent_posts(self, count=5):
        """转换最近的文章"""
        if not self.posts_dir.exists():
            print(f"文章目录不存在: {self.posts_dir}")
            return
        
        posts = []
        
        # 收集所有文章
        for post_dir in self.posts_dir.iterdir():
            if post_dir.is_dir():
                index_file = post_dir / "index.md"
                if index_file.exists():
                    posts.append(index_file)
        
        # 按修改时间排序，取最新的count篇
        posts.sort(key=lambda x: x.stat().st_mtime, reverse=True)
        
        for post in posts[:count]:
            self.convert_post(post)
        
        print(f"\n最近{count}篇文章转换完成！输出目录: {self.output_dir}")


def main():
    parser = argparse.ArgumentParser(description='将Hugo博客文章转换为微信公众号富文本格式')
    parser.add_argument('--posts-dir', default='content/posts', help='博客文章目录路径')
    parser.add_argument('--output-dir', default='wechat_articles', help='输出目录路径')
    parser.add_argument('--post', help='转换指定文章路径')
    parser.add_argument('--recent', type=int, help='转换最近N篇文章')
    parser.add_argument('--all', action='store_true', help='转换所有文章')
    
    args = parser.parse_args()
    
    converter = WeChatConverter(args.posts_dir, args.output_dir)
    
    if args.post:
        converter.convert_post(args.post)
    elif args.recent:
        converter.convert_recent_posts(args.recent)
    elif args.all:
        converter.convert_all_posts()
    else:
        print("请指定要转换的文章:")
        print("  --post PATH    转换指定文章")
        print("  --recent N     转换最近N篇文章")
        print("  --all          转换所有文章")
        print("示例:")
        print("  python wechat_converter.py --recent 3")
        print("  python wechat_converter.py --post content/posts/100_minirps/index.md")
        print("  python wechat_converter.py --all")


if __name__ == "__main__":
    main()