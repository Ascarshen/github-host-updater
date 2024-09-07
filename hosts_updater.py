import requests

# GitHub Hosts 文件的 URL
hosts_url = "https://raw.githubusercontent.com/maxiaof/github-hosts/master/hosts"

# 下载并返回最新的 hosts 文件内容
def fetch_latest_hosts(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("下载成功，以下是最新的 hosts 内容：")
            print(response.text)
        else:
            print(f"下载失败，状态码：{response.status_code}")
    except Exception as e:
        print(f"下载过程中发生错误: {e}")

if __name__ == "__main__":
    fetch_latest_hosts(hosts_url)
