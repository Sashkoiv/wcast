import requests
from xml.dom.minidom import parseString

html_string = requests.get("""https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BA%D0%B8%D1%97%D0%B2/10-%D0%B4%D0%BD%D1%96%D0%B2""").text
# html_string = """
# <!DOCTYPE html>
# <html><head><title>title</title></head><body><p>test</p></body></html>
# """

# extract the text value of the document's <p> tag:
doc = parseString(html_string)
paragraph = doc.getElementsByTagName("p")[0]
content = paragraph.firstChild.data

print(content)