import re

def remove_html_tags(content):
    return re.sub(r"<[^>]*>", "", content)