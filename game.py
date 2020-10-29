import tkinter as tk
from threading import Thread
import tkinter.messagebox
import random
import time
import datetime
import sys
class square(tk.Label):
    freeze=(2,2)
    def __init__(self,master,text='',width=30,height=15,bg='red',x=0,y=0):
        super().__init__(master=master,text=text,width=width,height=height,bg=bg)
        self.text=text
        #self.width=width
        #self.height=height
        #self.bg=bg
        self.x=x
        self.y=y
        #self.active=False
        self.bind('<Button-1>', self.mouve)
    
    def mouve(self,*args):
        # print(args)
        # print(self.x,self.y,self.freeze)
        if (abs(self.x-square.freeze[0])+abs(self.y-square.freeze[1]))==1:
            # print('yes')
            # print(self.x,self.y,square.freeze)
            self.x,self.y,square.freeze=square.freeze[0],square.freeze[1],(self.x,self.y)
            #self.destroy()
            self.grid(row=self.x,column=self.y)
            if self.master.master.check_game():
                self.master.master.end=time.strftime('%c')
                f=open('score.txt','a')
                f.write(self.master.master.start+'\t'+self.master.master.end+'\n')
                if self.master.master.level<=2:
                	self.master.master.start_new_game(self.master.master.level+1)
                else:
                	tkinter.messagebox.showinfo(message='Congratutation! you Won the game')
                	main.destroy()
                	sys.exit()


            
class My_game(tk.Tk,Thread):
    def __init__(self):
        super().__init__()
        self.title("Square Game")
        #main.geometry("450x450")
        self.configure(background="light green")
        self.fr=tk.Frame(master=self,width=450,height=450,bg='white')

    def start_new_game(self,level=1):
        square.freeze=(level+1,level+1)
        self.level=level
        self.start=time.strftime('%c')
        self.fr.destroy()
        self.fr=tk.Frame(main,width=450,height=450,bg='white')
        num=list(range(1,(level+2)**2))
        rand_num=[]
        for i in range((level+2)**(2)-1):
            ch=random.choice(num)
            num.remove(ch)
            rand_num.append(ch)
        self.numbers=[square(self.fr,text=str(rand_num[i]),width=round((40-(5*(level+1)))/(level+2)),height=round(((40-(5*(level+1)))/(level+2))/2),bg='red',x=i//(level+2),y=i%(level+2)) for i in range(((level+2)**2)-1)]
        for i,j in enumerate(self.numbers):
            j.grid(row=i//(level+2),column=i%(level+2),padx=5,pady=5)
        self.fr.pack()

    def check_game(self):
        for j in self.numbers:
            print(str((j.x*3+j.y)+1),j.text)
            if str((j.x*3+j.y)+1)!=j.text:
                return False
        return True

main=My_game()
main.start_new_game(1)
main.mainloop()