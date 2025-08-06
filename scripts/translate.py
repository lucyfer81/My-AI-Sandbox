#!/usr/bin/env python3
"""
使用腾讯云官方SDK的翻译实现
基于 credential_validation.py 的验证成功代码
"""

import os
import json
import toml
import yaml
from pathlib import Path
import subprocess

# 腾讯云官方SDK
from tencentcloud.common import credential
from tencentcloud.tmt.v20180321 import tmt_client, models

# 腾讯云API配置
TENCENT_SECRET_ID = os.getenv('TENCENT_SECRET_ID', 'YOUR_SECRET_ID')
TENCENT_SECRET_KEY = os.getenv('TENCENT_SECRET_KEY', 'YOUR_SECRET_KEY')
TENCENT_REGION = "ap-guangzhou"  # 必须使用广州地域

# 加载术语表
try:
    with open('translation-glossary.json', 'r', encoding='utf-8') as f:
        glossary = json.load(f)['术语表']
except (FileNotFoundError, KeyError):
    glossary = {}

def translate_with_tencent(text, source_lang="zh", target_lang="en"):
    """使用腾讯云官方SDK翻译文本"""
    if not TENCENT_SECRET_ID or not TENCENT_SECRET_KEY:
        print("错误: 未设置TENCENT_SECRET_ID和TENCENT_SECRET_KEY环境变量")
        return f"[Translation failed - no API credentials] {text}"
    
    if not text.strip():
        return text
    
    try:
        # 创建腾讯云凭证
        cred = credential.Credential(TENCENT_SECRET_ID, TENCENT_SECRET_KEY)
        
        # 创建TMT客户端（必须使用ap-guangzhou地域）
        client = tmt_client.TmtClient(cred, TENCENT_REGION)
        
        # 构造翻译请求
        req = models.TextTranslateRequest()
        req.SourceText = text
        req.Source = source_lang
        req.Target = target_lang
        req.ProjectId = 0  # 免费项目固定填0
        
        # 发送翻译请求
        resp = client.TextTranslate(req)
        
        # 获取翻译结果
        translated_text = resp.TargetText
        
        # 应用术语表
        return apply_glossary(translated_text)
        
    except Exception as e:
        print(f"翻译错误: {e}")
        if "AuthFailure" in str(e):
            print("  → 权限错误：检查子账号是否授权 TMT_QcsRole 策略")
        elif "InvalidParameterValue" in str(e):
            print("  → 参数错误：检查地域是否为 ap-guangzhou")
        return f"[Translation failed] {text}"

def apply_glossary(text):
    """应用术语表进行后处理"""
    for zh_term, en_term in glossary.items():
        text = text.replace(zh_term, en_term)
    return text

def process_markdown_file(chinese_file):
    """处理单个markdown文件"""
    try:
        with open(chinese_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 分离front matter和正文 (支持+++和---)
        if content.startswith('---') or content.startswith('+++'):
            delimiter = '---' if content.startswith('---') else '+++'
            parts = content.split(delimiter, 2)
            if len(parts) >= 3:
                front_matter_str = parts[1]
                body = parts[2]
                
                try:
                    # 尝试解析为TOML格式
                    try:
                        front_matter = toml.loads(front_matter_str)
                    except:
                        # 如果TOML解析失败，尝试YAML
                        import yaml
                        front_matter = yaml.safe_load(front_matter_str)
                    
                    # 翻译标题和描述
                    front_matter['title'] = translate_with_tencent(str(front_matter.get('title', '')))
                    if 'description' in front_matter:
                        front_matter['description'] = translate_with_tencent(str(front_matter['description']))
                    
                    # 翻译标签
                    if 'tags' in front_matter:
                        front_matter['tags'] = [translate_with_tencent(str(tag)) for tag in front_matter['tags']]
                    
                    # 翻译分类
                    if 'categories' in front_matter:
                        front_matter['categories'] = [translate_with_tencent(str(cat)) for cat in front_matter['categories']]
                    
                    # 翻译正文
                    translated_body = translate_with_tencent(body)
                    
                    # 生成新的front matter，保持为YAML格式
                    import yaml
                    new_front_matter = yaml.dump(front_matter, allow_unicode=True, default_flow_style=False)
                    
                    # 组合新文件内容（使用标准---分隔符）
                    new_content = f"---\n{new_front_matter}---\n{translated_body}"
                    
                    # 生成英文文件路径
                    english_file = chinese_file.replace('index.md', 'index_en.md')
                    
                    # 检查是否已存在英文版本
                    if Path(english_file).exists():
                        print(f"英文版本已存在: {english_file}")
                        return False
                    
                    with open(english_file, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    
                    print(f"已生成英文版本: {english_file}")
                    return True
                    
                except Exception as e:
                    print(f"处理文件 {chinese_file} 时出错: {e}")
                    return False
        
        return False
    except Exception as e:
        print(f"读取文件 {chinese_file} 时出错: {e}")
        return False

def batch_translate():
    """批量翻译现有文章"""
    print("开始批量翻译现有文章...")
    
    # 检查腾讯云API凭证
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
    batch_translate()