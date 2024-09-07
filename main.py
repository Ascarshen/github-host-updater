# main.py

from get_ip_address_worker import GetIpAddressWorker
from github_url import GithubUrl
from concurrent.futures import ThreadPoolExecutor, as_completed

def process_url(url):
    worker = GetIpAddressWorker()
    result = worker.action(url)
    return result

if __name__ == "__main__":

    with open("output.txt", "w") as f:
        f.write("# GitHub URLs and Their IP Addresses\n")
        f.write(f"Updated on {__import__('datetime').datetime.now()}\n\n")

        f.write("```bash\n")

        with ThreadPoolExecutor(max_workers=10) as executor:
            futures = [executor.submit(process_url, url) for url in GithubUrl.GITHUB_URL]

            for future in as_completed(futures):
                try:
                    result = future.result() 
                    if result:
                        url, ip = result.split(" ")[-1], result.split(" ")[0]
                        f.write(f"{ip} {url}\n")  
                except Exception as e:
                    f.write(f"# Error processing URL: {e}\n")

        f.write("```\n")
