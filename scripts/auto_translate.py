#!/usr/bin/env python3
"""
自动翻译现有文章的无交互版本
"""

import os
import sys
from pathlib import Path

# 设置环境变量
os.environ['TENCENT_SECRET_ID'] = 'YOUR_SECRET_ID'
os.environ['TENCENT_SECRET_KEY'] = 'YOUR_SECRET_KEY'

# 将当前目录添加到路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from translate import process_markdown_file, check_tencent_credentials

def auto_translate():
    """自动翻译现有文章"""
    print("开始自动翻译现有文章...")
    
    # 检查腾讯云API凭证
    if not check_tencent_credentials():
        print("错误: 腾讯云API凭证未配置")
        return
    
    posts_dir = Path('content/posts')
    
    # 获取所有中文文章
    chinese_files = []
    for index_file in posts_dir.glob('**/index.md'):
        english_file = index_file.parent / 'index_en.md'
        if not english_file.exists():
            chinese_files.append(str(index_file))
    
    if not chinese_files:
        print("没有找到需要翻译的中文文章")
        return
    
    print(f"找到 {len(chinese_files)} 篇需要翻译的文章")
    
    translated_count = 0
    for chinese_file in chinese_files[:2]:  # 先翻译前2篇测试
        print(f"\n处理: {chinese_file}")
        try:
            if process_markdown_file(chinese_file):
                translated_count += 1
                print(f"✓ 已翻译: {chinese_file}")
            else:
                print(f"✗ 跳过: {chinese_file}")
        except Exception as e:
            print(f"✗ 错误: {e}")
    
    print(f"\n自动翻译完成，共处理 {translated_count} 篇文章")

if __name__ == "__main__":
    auto_translate()