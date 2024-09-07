# html_utils.py

import requests
from bs4 import BeautifulSoup

class HtmlUtils:

    @staticmethod
    def parse_html_get_ip_address(html: str) -> str:
        """从 HTML 中解析 IP 地址"""
        soup = BeautifulSoup(html, 'html.parser')
        ip_address_element = soup.find(id="divString0")
        if ip_address_element:
            return ip_address_element.get_text().strip()
        return None

    @staticmethod
    def get_url_html(url: str) -> str:
        """获取指定 URL 的 HTML 内容"""
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.text
            else:
                print(f"Error: Unable to fetch the URL. Status code: {response.status_code}")
                return ""
        except requests.RequestException as e:
            print(f"Error fetching the URL: {e}")
            return ""
