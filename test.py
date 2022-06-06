from tkinter import*
from attr import attr
import requests
import urllib3
from bs4 import BeautifulSoup
import re
import webbrowser

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

def callback(url):
    webbrowser.open_new_tab(url)
 
root = Tk()
root.title("조선대학교")
root.geometry("540x280")
 
 
lbl = Label(root, text = "조선대학교 공지사항")
lbl.pack()
for i in range(0, len(Uni)):
    lb2 = Label(root, text=Uni[i][0])
    link=Label(root,text=LINK,font=('Helveticabold', 8), fg="blue",cursor="hand2",pady=10)
    lb2.pack()
    link.pack()
    link.bind("<Button-1>",lambda e: callback(LINK)) 

root.mainloop()
