import requests
import re
from pprint import pprint as print

class Sinoptik:
    '''
    Receives html of sinoptik.ua weather forecast service page and looking for
    a raw data.
    Input parameters and formatting:
    city - cyrilic name of the city
    ten_days - False for 7 days and True for 10 days
    date - date in format yyyy-mm-dd
    '''
    def __init__(self,
                 city: str='київ',
                 ten_days: bool=False,
                 date: tuple=(None, None, None)):

        self.address = f'https://ua.sinoptik.ua/погода-{city.lower()}/\
{date if date[0] else "10-днів" if ten_days else ""}'

    @property
    def forecast(self) -> list:
        r = requests.get(self.address).text
        exp = r"""<p class="date \w*">(\d*)<\/p>\s*<p class="month">(\w*)<\/p> <div class="weatherIco d\d\d\d" title="([\w,\s]*)"><img class="weatherImg"\ssrc.{,100}temperature">\s<div class="min">\w+\.\s<span>([-+]?[\d]*)&deg;<\/span><\/div>\s<div class="max">\w+\..<span>([-+]?[\d]*)&deg;<\/span><\/div>"""
        matches = re.findall(exp, r, re.MULTILINE)
        return matches


weather = Sinoptik()
print(weather.forecast)
