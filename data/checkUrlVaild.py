import yaml
import requests
from urllib.parse import urlparse
import time
import os

def check_url(url):
    """检查单个 URL 的访问性，返回状态码和错误信息，使用通用 User-Agent"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    try:
        response = requests.head(url, timeout=10, allow_redirects=True, headers=headers)
        return response.status_code, None
    except requests.exceptions.RequestException as e:
        return None, str(e)

def is_valid_url(url):
    """检查 URL 是否格式正确"""
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

def process_yaml(yaml_content):
    """处理 YAML 内容并实时检查所有 URL（支持多文档）"""
    try:
        # 解析所有 YAML 文档
        documents = list(yaml.safe_load_all(yaml_content))
        inaccessible_count = 0
        
        # 遍历每个文档
        for data in documents:
            if not isinstance(data, list):
                continue
                
            for taxonomy in data:
                taxonomy_name = taxonomy.get('taxonomy', '未知分类')
                links = taxonomy.get('links', [])
                list_items = taxonomy.get('list', [])
                
                # 检查顶层 links
                for link in links:
                    url = link.get('url')
                    title = link.get('title', '无标题')
                    # 如果 title 中包含“墙”，跳过检查
                    if '墙' in title:
                        continue
                    if url and is_valid_url(url):
                        status, error = check_url(url)
                        # 只有当 status 为 None（即连接失败）时，才认为不可访问
                        if status is None:
                            inaccessible_count += 1
                            print(f"\n不可访问 URL #{inaccessible_count}:")
                            print("-" * 50)
                            print(f"分类: {taxonomy_name}")
                            print(f"标题: {title}")
                            print(f"URL: {url}")
                            print(f"错误信息: {error}")
                            print("-" * 50)
                
                # 检查 list 中的 links
                for item in list_items:
                    term = item.get('term', '未知项')
                    sub_links = item.get('links', [])
                    for link in sub_links:
                        url = link.get('url')
                        title = link.get('title', '无标题')
                        # 如果 title 中包含“墙”，跳过检查
                        if '墙' in title:
                            continue
                        if url and is_valid_url(url):
                            status, error = check_url(url)
                            # 只有当 status 为 None（即连接失败）时，才认为不可访问
                            if status is None:
                                inaccessible_count += 1
                                print(f"\n不可访问 URL #{inaccessible_count}:")
                                print("-" * 50)
                                print(f"分类: {taxonomy_name} > {term}")
                                print(f"标题: {title}")
                                print(f"URL: {url}")
                                print(f"错误信息: {error}")
                                print("-" * 50)
        
        return inaccessible_count
    
    except yaml.YAMLError as e:
        print(f"YAML 解析错误: {e}")
        return 0

def main():
    # 指定 YAML 文件路径
    yaml_file_path = "webstack.yml"  # 请替换为你的 YAML 文件路径
    
    # 检查文件是否存在
    if not os.path.exists(yaml_file_path):
        print(f"错误: 文件 {yaml_file_path} 不存在！")
        return
    
    # 读取 YAML 文件内容
    try:
        with open(yaml_file_path, 'r', encoding='utf-8') as file:
            yaml_content = file.read()
    except Exception as e:
        print(f"读取文件错误: {e}")
        return
    
    print("开始检查 URL 访问性...")
    print(f"当前时间: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    
    inaccessible_count = process_yaml(yaml_content)
    
    if inaccessible_count == 0:
        print("\n所有 URL 均可正常访问！")
    else:
        print(f"\n检查完毕，共发现 {inaccessible_count} 个不可访问的 URL")
    
    print(f"检查完成时间: {time.strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    main()