#!/usr/bin/env python3
"""
翻译验证脚本
用于验证翻译结果的质量和完整性
"""

import os
import sys
from pathlib import Path
import yaml
import toml

def validate_translation(english_file):
    """验证翻译后的英文文件"""
    issues = []
    
    try:
        with open(english_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 检查文件结构
        if not content.startswith('---'):
            issues.append("文件格式错误：缺少YAML front matter分隔符")
        
        # 解析front matter
        parts = content.split('---', 2)
        if len(parts) < 3:
            issues.append("文件结构错误：无法解析front matter")
            return issues
        
        front_matter_str = parts[1]
        body = parts[2]
        
        try:
            front_matter = yaml.safe_load(front_matter_str)
        except:
            try:
                front_matter = toml.loads(front_matter_str)
            except Exception as e:
                issues.append(f"front matter解析错误: {e}")
                return issues
        
        # 检查必要字段
        required_fields = ['title', 'date']
        for field in required_fields:
            if field not in front_matter:
                issues.append(f"缺少必要字段: {field}")
        
        # 检查语言标识
        if front_matter.get('lang') != 'en':
            issues.append("缺少或错误的语言标识")
        
        # 检查内容长度
        if len(body.strip()) < 100:
            issues.append("翻译内容过短，可能翻译不完整")
        
        # 检查是否包含未翻译的中文
        chinese_chars = sum(1 for char in body if '\u4e00' <= char <= '\u9fff')
        if chinese_chars > len(body) * 0.1:  # 超过10%的中文字符
            issues.append("翻译中仍包含大量中文字符")
        
    except Exception as e:
        issues.append(f"文件读取错误: {e}")
    
    return issues

def validate_all_translations():
    """验证所有英文翻译文件"""
    en_posts_dir = Path('content/en/posts')
    
    if not en_posts_dir.exists():
        print("英文文章目录不存在")
        return
    
    all_valid = True
    
    for english_file in en_posts_dir.glob('**/index.md'):
        print(f"验证: {english_file}")
        issues = validate_translation(english_file)
        
        if issues:
            print(f"  ❌ 发现问题:")
            for issue in issues:
                print(f"    - {issue}")
            all_valid = False
        else:
            print(f"  ✅ 验证通过")
    
    if all_valid:
        print("\n🎉 所有翻译文件验证通过！")
        return True
    else:
        print("\n⚠️  发现翻译问题，请检查并修复")
        return False

if __name__ == "__main__":
    validate_all_translations()