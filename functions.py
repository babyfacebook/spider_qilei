import urllib
import re
def get_image_from_url(url):
    content = urllib.urlopen(url).read()
    pattern = re.compile(r'((http|\./)[^ ]*?\.(jpg|jpeg|png|gif))')
    li = re.findall(pattern, content)
    return li

def get_url_from_url(url):
    content = urllib.urlopen(url).read()
    pattern = re.compile(r'((?<=(href="))[^ ]*?(?=(")))(?<!(.css))')
    li = re.findall(pattern, content)
    return li
