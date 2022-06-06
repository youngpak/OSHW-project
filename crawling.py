import requests
import urllib3
from bs4 import BeautifulSoup
import re

urllib3.disable_warnings()

College_Dataset = [
                   ["조선대학교", "https://www3.chosun.ac.kr"]
]

College_Notice_Dataset = [
                   ["조선대학교", "https://www3.chosun.ac.kr/chosun/217/subview.do"]
]

College_Name = College_Dataset[0][0]
URL = College_Notice_Dataset[0][1]
LIST_idx = College_Dataset[0][1]

webpage_response = requests.get(URL, verify=False)
html = webpage_response.text

if webpage_response.status_code == 200:
    soup = BeautifulSoup(html, "html.parser")
    datalist = soup.find_all("td", attrs = {"class":"subject align-l"})

else :
    print(webpage_response.status_code)


SP = list()

for ITEM in range(0, len(datalist)):
    temp = list()
    name = datalist[ITEM].find("a")
    TEXT = re.sub("\t|\n", "", name.text)
    address = datalist[ITEM].find("a")["href"]
    LINK = str(LIST_idx) + address

    temp.append(TEXT)
    temp.append(LINK)
    SP.append(temp)

Uni = list()

for X in SP:
    if X not in Uni:
        Uni.append(X)

print(College_Name)

for i in range(0, len(Uni)):
    print(Uni[i][0])
    print(Uni[i][1])

def func1():
    import tkinter as tk

    root1 = tk.Tk()

    def kill1():
        root1.destroy()
        from py2 import func2
        func2()

    button1 = tk.Button(root1, bg = 'green', text = 'hit to kill py1 and start py2', command = kill1)
    button1.pack()
    tk.Label()

    root1.mainloop()

if __name__ == '__main__':
    func1()