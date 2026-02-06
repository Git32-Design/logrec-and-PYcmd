import requests
from datetime import datetime

def get_pypi_package_info(package_name):
    """获取 PyPI 包的详细信息"""
    url = f"https://pypi.org/pypi/{package_name}/json"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        info = data['info']
        releases = data['releases']
        
        # 提取关键信息
        package_info = {
            '包名': info['name'],
            '当前版本': info['version'],
            '作者': info['author'],
            '作者邮箱': info['author_email'],
            '描述': info['summary'],
            '详细描述': info['description'][:200] + '...' if len(info['description']) > 200 else info['description'],
            '主页': info['home_page'],
            '项目地址': info.get('project_urls', {}),
            '许可证': info['license'],
            'Python版本要求': info['requires_python'],
            '关键词': info['keywords'],
            '分类器': info['classifiers'][:5],  # 只显示前5个
            '依赖': info.get('requires_dist', []),
            '发布时间': info.get('release_url', 'N/A'),
            '总版本数': len(releases),
        }
        
        # 最新版本的下载信息
        latest_version = info['version']
        if latest_version in releases:
            latest_files = releases[latest_version]
            package_info['最新版本文件'] = [
                {
                    '文件名': f['filename'],
                    '大小': f'{f["size"] / 1024:.2f} KB',
                    '类型': f['packagetype'],
                    '上传时间': f['upload_time']
                }
                for f in latest_files
            ]
        
        return package_info
        
    except requests.exceptions.RequestException as e:
        return {'错误': f'请求失败: {e}'}

def compare_versions(package_name, local_version):
    """比较本地版本和 PyPI 版本"""
    url = f"https://pypi.org/pypi/{package_name}/json"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        pypi_version = data['info']['version']
        
        print("\n" + "=" * 60)
        print("[Version Comparison]")
        print("=" * 60)
        print(f"Local Version : {local_version}")
        print(f"PyPI Version  : {pypi_version}")
        
        if local_version == pypi_version:
            print("[OK] Versions match!")
        elif local_version > pypi_version:
            print(f"[NEW] Local version is newer, consider publishing to PyPI")
            print(f"\nPublish steps:")
            print(f"  1. python -m build")
            print(f"  2. twine check dist/*")
            print(f"  3. twine upload dist/*")
        else:
            print(f"[WARNING] PyPI version is newer, consider updating local")
            
    except Exception as e:
        print(f"Version comparison failed: {e}")

# 使用示例
if __name__ == "__main__":
    package_name = "LogrecAndPYcmd"
    local_version = "5.8.8"  # 你的本地版本
    
    info = get_pypi_package_info(package_name)
    
    # 美化输出
    print("=" * 60)
    print(f"[Package Info] {package_name}")
    print("=" * 60)
    
    for key, value in info.items():
        if key == '最新版本文件':
            print(f"\n{key}:")
            for file in value:
                print(f"  - {file['文件名']}")
                print(f"    Size: {file['大小']}, Type: {file['类型']}")
                print(f"    Upload time: {file['上传时间']}")
        elif key == '项目地址':
            print(f"\n{key}:")
            for url_name, url in value.items():
                print(f"  - {url_name}: {url}")
        elif isinstance(value, list):
            print(f"\n{key}:")
            for item in value[:5]:  # 限制显示数量
                print(f"  - {item}")
        else:
            print(f"{key}: {value}")
    
    # 版本对比
    compare_versions(package_name, local_version)
