import requests
import re
from bs4 import BeautifulSoup
import json
# Making a GET request
# r = requests.get('https://www.sports-reference.com/cbb/conferences/big-ten/2020-schedule.html')
#
# # Parsing the HTML
# soup = BeautifulSoup(r.content, 'html.parser')
# text = soup.get_text()
#
# list1 = []
# for line in text.split("\n"):
#     if len(re.findall("[0-9]+$", line)) > 0:
#         if len(re.findall("\w+,\s\w+\s", line)):
#             if len(line.split(", ")) == 3:
#                 list1.append(line.split(", ")[2])
# list2 = []
# for i in list1:
#     word = re.findall("[a-z\s]+", i.lower())
#     print(word)
#     num = re.findall("[0-9]+", i)
#     dict1 = {}
#     dict1["year"] = num[0]
#     dict1["team1"] = word[0]
#     dict1["team1 score"] = num[1]
#     dict1["team2"] = word[1]
#     dict1["team2 score"] = num[2]
#     list2.append(dict1)
# print(list2)




r = requests.get('https://www.espn.com/mens-college-basketball/standings/_/group/7')

 # Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')
text = soup.prettify()
print(text)


# page = soup.find('p')
# print(page)
