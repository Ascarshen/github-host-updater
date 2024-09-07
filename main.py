# main.py

from get_ip_address_worker import GetIpAddressWorker
from github_url import GithubUrl
from concurrent.futures import ThreadPoolExecutor, as_completed

def process_url(url):
    worker = GetIpAddressWorker()
    result = worker.action(url)
    return result

if __name__ == "__main__":
    # 打开文件用于写入
    with open("output.txt", "w") as f:
        f.write("# GitHub URLs and Their IP Addresses\n")
        f.write(f"# Updated on {__import__('datetime').datetime.now()}\n\n")

        # 使用 ThreadPoolExecutor 创建线程池
        with ThreadPoolExecutor(max_workers=100) as executor:
            futures = [executor.submit(process_url, url) for url in GithubUrl.GITHUB_URL]

            # 使用 as_completed 逐个处理完成的任务
            for future in as_completed(futures):
                try:
                    result = future.result()  # 获取任务的返回结果
                    f.write(result)  # 将结果写入文件
                except Exception as e:
                    f.write(f"Error processing URL: {e}\n")
