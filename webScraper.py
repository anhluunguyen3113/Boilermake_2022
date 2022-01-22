import requests
import re
from bs4 import BeautifulSoup

# Making a GET request
r = requests.get('https://www.sports-reference.com/cbb/conferences/big-ten/2020-schedule.html')

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

text = soup.get_text()
#print(text)
#p = re.pattern("\a*,\s")


for line in text.split("\n"):
    if len(re.findall("[0-9]+$", line)) > 0:
        if len(re.findall("\w+,\s\w+\s", line)):
            print(line)










#print(soup.prettify())


# for para in soup.find_all("p"):
#     print(para.get_text())



# use the child attribute to get
# the name of the child tag