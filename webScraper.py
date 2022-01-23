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




r = requests.get('https://www.sports-reference.com/cbb/conferences/big-ten/2022.html')

 # Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')
text = soup.get_text()
#print(text)

list1 = []
for line in text.split("\n"):
    if len(re.findall("[0-9]+$", line)) > 0:
        if len(re.findall("[0-9]\w", line)):
            if len(re.findall("\/", line)) > 0:
                break;
            else:
                if len(re.findall("[0-9][a-z]", line.lower())) > 0:
                    dict1 = {}
                    num = re.findall("[0-9]+", line)
                    word = re.findall("[a-z\s]+", line.lower())
                    dict1["ranking"] = num[0]
                    print(word[0])
                    dict1["name"] = word[0]
                    # print(line)
                    # print(num)
                    wl = num[2][3:]
                    if len(wl) == 2:
                        dict1["win"] = wl[0]
                        dict1["loss"] = wl[1]
                        # print("win " + wl[0])
                        # print("loss " + wl[1])
                    elif wl[0] == '1':
                        dict1["win"] = wl[0:2]
                        dict1["loss"] = wl[2]
                        # print("win " + wl[0:2])
                        # print("loss " + wl[2])
                    else:
                        dict1["win"] = wl[0]
                        dict1["loss"] = wl[1:]
                        # print("win " + wl[0])
                        # print("loss " + wl[1:])
                    list1.append(dict1)
print(list1)






