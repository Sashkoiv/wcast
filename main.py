import requests
import re
from pprint import pprint as print

r = requests.get('https://ua.sinoptik.ua/погода-київ/10-днів').text

exp = r"""<p class="date \w*">(\d*)<\/p>\s*<p class="month">(\w*)<\/p> <div class="weatherIco d\d\d\d" title="([\w,\s]*)"><img class="weatherImg"\ssrc.{,100}temperature">\s<div class="min">\w+\.\s<span>([-+]?[\d]*)&deg;<\/span><\/div>\s<div class="max">\w+\..<span>([-+]?[\d]*)&deg;<\/span><\/div>"""

matches = re.findall(exp, r, re.MULTILINE)

print(matches)
