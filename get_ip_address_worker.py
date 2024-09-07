# get_ip_address_worker.py

from html_utils import HtmlUtils


class GetIpAddressWorker:

    def action(self, url: str) -> str:
        """获取指定 URL 的 IP 地址"""
        full_url = f"https://tools.tutorialspoint.com/ip_lookup_ajax.php?host={url}"
        html_resource = HtmlUtils.get_url_html(full_url)
        format_str = f"IP address of {url} is "
        ip_address = HtmlUtils.parse_html_get_ip_address(html_resource)
        
        if ip_address:
            return f"{ip_address.replace(format_str, '')} {url}\n"
        else:
            return f"Failed to get IP address for {url}\n"

    def default_value(self) -> str:
        """默认返回值"""
        return None


