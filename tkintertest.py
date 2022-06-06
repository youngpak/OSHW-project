import tkinter as tk
from tkinter import *
from turtle import color
import webbrowser
from click import command
from matplotlib import lines
from attr import attr
import requests
import urllib3
from bs4 import BeautifulSoup
import re

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="조선대학교 공지사항 간편 조회\n", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=3)
        tk.Label(self, text="6월 학사 일정\n").pack()
        frame = tk.Frame(self)
        frame.pack()
        scrollbar = Scrollbar(frame)
        scrollbar.pack(side="right",fill="y")

        listbox = Listbox(frame,selectmode='extended', height=10,yscrollcommand=scrollbar.set)
        f=open("sche.txt",'r',encoding='utf-8')
        lines=f.readlines()
        for line in lines:
            listbox.insert(END,str(line))
        listbox.pack(side="left")

        f.close()
        tk.Label(self, text="\n\n방문을 원하는 공지사항을 선택해주세요!\n",font=('Helvetica', 10, "bold")).pack()
        tk.Button(self, text="조선대학교 공지사항",
                  command=lambda: master.switch_frame(PageOne)).pack(pady=8)
        tk.Button(self, text="IT융합대학 전자공학부 공지사항",
                  command=lambda: master.switch_frame(PageTwo)).pack(pady=8)
        tk.Button(self, text="sw중심대학사업단 공지사항",
                  command=lambda: master.switch_frame(PageFive)).pack(pady=8)
        tk.Button(self, text="e-class 바로가기",
                  command=lambda: master.switch_frame(PageThree)).pack(pady=8)
        tk.Button(self, text="조선대학교 사이트 바로가기",
                  command=lambda: master.switch_frame(PageFour)).pack(pady=8)
                  

class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg='blue')
        tk.Label(self, text="조선대학교 공지사항", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="뒤로 가기", command=lambda: master.switch_frame(StartPage)).pack()
    
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
        root.geometry("660x660")
        
        
        lbl = Label(root, text = "조선대학교 공지사항")
        lbl.pack()
        for i in range(0, len(Uni)):
            lb2 = Label(root, text=Uni[i][0])
            link=Label(root,text=LINK,font=('Helveticabold', 8), fg="blue",cursor="hand2",pady=10)
            lb2.pack()
            link.pack()
            link.bind("<Button-1>",lambda e: callback(LINK)) 

        root.mainloop()

class PageTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg='red')
        tk.Label(self, text="IT융합대학 공지사항", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        urllib3.disable_warnings()

        College_Dataset = [
                        ["조선대학교", "https://www3.chosun.ac.kr"]
        ]

        College_Notice_Dataset = [
                        ["IT융합대학 전자공학부", "https://www4.chosun.ac.kr/eic/5604/subview.do?enc=Zm5jdDF8QEB8JTJGYmJzJTJGZWljJTJGMzI0JTJGYXJ0Y2xMaXN0LmRvJTNG"]
        ]

        College_Name = College_Dataset[0][0]
        URL = College_Notice_Dataset[0][1]
        LIST_idx = College_Dataset[0][1]

        webpage_response = requests.get(URL, verify=False)
        html = webpage_response.text

        if webpage_response.status_code == 200:
            soup = BeautifulSoup(html, "html.parser")
            datalist = soup.find_all("td", attrs = {"class":"td-subject"})

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
        root.geometry("660x660")
        
        
        lbl = Label(root, text = "IT융합대학 전자공학부 공지사항")
        lbl.pack()
        for i in range(0, len(Uni)):
            lb2 = Label(root, text=Uni[i][0])
            link=Label(root,text=LINK,font=('Helveticabold', 8), fg="blue",cursor="hand2",pady=10)
            lb2.pack()
            link.pack()
            link.bind("<Button-1>",lambda e: callback(LINK)) 

        root.mainloop()


class PageThree(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self,master)
        tk.Frame.configure(self,bg='blue')
        tk.Label(self,text="e-class 바로가기",command=webbrowser.open_new(r"https://clc.chosun.ac.kr/ilos/main/main_form.acl"), font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
       


class PageFour(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self,master)
        tk.Frame.configure(self,bg='Blue')
        tk.Label(self,text="조선대학교 사이트 바로가기",command=webbrowser.open_new(r"https://www3.chosun.ac.kr/chosun/index...do?main=Y"), font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        
class PageFive(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self,master)
        urllib3.disable_warnings()

        College_Dataset = [
                        ["조선대학교", "https://www3.chosun.ac.kr"]
        ]

        College_Notice_Dataset = [
                        ["sw중심대학", "https://sw.chosun.ac.kr/home/kor/board.do?menuPos=62"]
        ]

        College_Name = College_Dataset[0][0]
        URL = College_Notice_Dataset[0][1]
        LIST_idx = College_Dataset[0][1]

        webpage_response = requests.get(URL, verify=False)
        html = webpage_response.text

        if webpage_response.status_code == 200:
            soup = BeautifulSoup(html, "html.parser")
            datalist = soup.find_all("div", attrs = {"class":"table_line"})

        else :
            print(webpage_response.status_code)


        SP = list()

        for ITEM in range(0, len(datalist)):
            temp = list()
            name = datalist[ITEM].find("a")
            TEXT = re.sub("\t|\n", "", name.text)
            address = datalist[ITEM].find("a")["onclick"]
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
        root.geometry("660x660")
        
        
        lbl = Label(root, text = "sw중심대학사업단 공지사항")
        lbl.pack()
        for i in range(0, len(Uni)):
            lb2 = Label(root, text=Uni[i][0])
            link=Label(root,text=LINK,font=('Helveticabold', 8), fg="blue",cursor="hand2",pady=10)
            lb2.pack()
            link.pack()
            link.bind("<Button-1>",lambda e: callback(LINK)) 

        root.mainloop()

        

if __name__ == "__main__":
    app = SampleApp()
    app.title("조선대학교 공지사항")
    app.geometry("700x1000")   
    app.mainloop()

