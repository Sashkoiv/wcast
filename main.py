import requests
from html.parser import HTMLParser

html_string = requests.get('https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BA%D0%B8%D1%97%D0%B2/10-%D0%B4%D0%BD%D1%96%D0%B2').text


class Parser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.in_p = []

    def handle_starttag(self, tag, attrs):
        if (tag == 'p'):
            self.in_p.append(tag)

    def handle_endtag(self, tag):
        if (tag == 'p'):
            self.in_p.pop()

    def handle_data(self, data):
        if self.in_p:
            print("<p> data :", data)

parser = Parser()
parser.feed(html_string)