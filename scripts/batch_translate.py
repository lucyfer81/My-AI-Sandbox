#!/usr/bin/env python3
"""
批量翻译现有文章的脚本
"""

import os
from pathlib import Path
import subprocess
import sys

# 将当前目录添加到路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from translate import process_markdown_file

def batch_translate_existing():
    """批量翻译现有文章"""
    print("开始批量翻译现有文章...")
    
    # 检查腾讯云API凭证
    from translate import TENCENT_SECRET_ID, TENCENT_SECRET_KEY
    if not TENCENT_SECRET_ID or not TENCENT_SECRET_KEY:
        print("错误: 未设置TENCENT_SECRET_ID和TENCENT_SECRET_KEY环境变量")
        print("获取方式: https://console.cloud.tencent.com/cam/capi")
        return
    
    posts_dir = Path('content/posts')
    
    if not posts_dir.exists():
        print("错误: content/posts目录不存在")
        return
    
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
    
    # 询问确认
    response = input("是否开始翻译？(y/N): ")
    if response.lower() != 'y':
        print("取消翻译")
        return
    
    translated_count = 0
    for chinese_file in chinese_files:
        print(f"\n处理: {chinese_file}")
        try:
            if process_markdown_file(chinese_file):
                translated_count += 1
                print(f"✓ 已翻译: {chinese_file}")
            else:
                print(f"✗ 跳过: {chinese_file}")
        except Exception as e:
            print(f"✗ 错误: {e}")
    
    print(f"\n批量翻译完成，共处理 {translated_count} 篇文章")

if __name__ == "__main__":
    batch_translate_existing()