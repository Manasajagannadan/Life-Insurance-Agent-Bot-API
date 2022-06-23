from NaiveBayes import Pool
import os
import pyttsx3
import random
import time
import speech_recognition as sr
from tkinter import *
from texttospeech import speech11

root = Tk()
root.title("LIFE INSURANCE AGENT")
root.geometry("1600x800")

Classes = ["H", "B"]
out = "output"
base = "data/"
p=Pool()
for i in Classes:
    print(i)
    p.learn(base + i, i)

base = "test/"
print("\nEnter For which insurance are you looking for ?\n")
sample = input("Please type here : ")

l1 = Label(root, text = sample, font = ("arial", 15, "bold"))
l1.pack()

r=0.1
rr=r
rrr=r 
rrrr=r

img = PhotoImage(file = "API_Images/human.png")
img1 = PhotoImage(file = "API_Images/computer.png")
root.configure(background = "black")

background_image = PhotoImage(file="API_Images/giff.gif")
background = Label(root, image = background_image, bd=0)
background.pack()

text_file = open("test\output\output_displayed.txt", "w")
text_file.write(sample)
text_file.close()

text_file1 = open("test\output\output_displayed.html", "w")
text_file1.write(sample)
text_file1.close()

try:
    for i in range(0, 5, 1):
        with open("test\output\output_displayed.txt", "a") as text_file:
            text_file.write("\n")
            dir = os.listdir(base + out)
            for file in dir:
                result = p.Probability(base + out + "/" + file)
                if file=="output_displayed.txt":
                    #print(out + ": " + file + ": " + str(result))
                    req = str(result[0])
                    #print(req[2])
                    count_n = 0
                    for i in range(0,4,1):
                        l = "data/"
                        c = "Chatbot.txt"
                        sen = str(result[0])
                        k2 = sen[2]
                        k1 = k2 + c
                        tt = k1
                        l1["text"] = k1
                        fp = open(l + k2 + "/" + k1)
                        lines = fp.read().split("\n")
                        
                        l2 = Label(root, text = lines[i], font = ("arial", 15, "bold"))
                        l2.place(relx = 0.5, rely = rr, anchor = CENTER)
                        rr += 0.2

                        imglabel  = Label(root, image = img1)
                        imglabel.place(relx = 0.1, rely = rrr, anchor = CENTER)
                        rrr += 0.2

                        engine = pyttsx3.init()
                        k=''
                        k=lines[i]
                        engine.say(k)
                        engine.setProperty('rate', 45)
                        engine.setProperty('volume', 5)
                        engine.runAndWait()

                        in1 = input("\nEnter your respnse : y/n : ")

                        l3 = Label(root, text = in1, font = ("arial", 15, "bold"))
                        l3.place(relx = 0.7, rely = r, anchor = CENTER)
                        r += 0.2

                        imglabel1 = Label(root, image = img)
                        imglabel1.place(relx = 0.8, rely = rrrr, anchor = CENTER)
                        rrrr += 0.2

                        if in1=='n':
                            count_n += 1
            l3 = Label(root, text = "It is an Insurance Policy Name ", font = ("arial", 15, "bold"))
            l3.place(relx = 0.5, rely = 0.8, anchor = CENTER)
            
            if count_n<=1:
                print(sen[2])
                if(sen[2]=='H'):
                    dis = "You are eligible for Home Insurance policy\n"
                    dis1 = "Shortly our representative will be touch with you\n"
                    dis2 = "Thank you for choosing EXL company service. See you!."
                    dis3 = dis + dis1 + dis2
                    l3["text"] = dis3
                    speech11(dis3)
                
                if(sen[2]=='B'):
                    dis = "You are eligible for BIKE Insurance policy\n"
                    dis1 = "Shortly our representative will be touch with you\n"
                    dis2 = "Thank you for choosing EXL company service. See you!."
                    dis3 = dis + dis1 + dis2
                    l3['text'] = dis3
                    speech11(dis3)
                root.mainloop()
                time.sleep(1)
                exit()
            else:
                l ="data/"
                c = "Chatbot.txt" 
                sen = str(result[1])
                k2 = sen[2]
                k1 = k2 + c
                print(k1)
                l1["text"] = tt + " " + k1
                count_n1 = 0

                for i in range(0,4,1):
                    fp=open(l + k2 + "/" + k1)
                    lines=fp.read().split("\n")
                    newQ=" "
                    #rkv = lines[i]

                    l2 = Label(root, text = lines[i], font = ("arial", 15, "bold"))
                    l2.place(relx = 0.5, rely = rr, anchor = CENTER)
                    rr += 0.2

                    imglabel  = Label(root, image = img1)
                    imglabel.place(relx = 0.1, rely = rrr, anchor = CENTER)
                    rrr += 0.2

                    engine = pyttsx3.init()
                    k=''
                    k=lines[i]
                    engine.say(k)
                    engine.setProperty('rate', 45)
                    engine.setProperty('volume', 5)
                    engine.runAndWait()

                    new = lines[i]
                    in1 = input("Enter your respnse : y/n :")

                    l3 = Label(root, text = in1, font = ("arial", 15, "bold"))
                    l3.place(relx = 0.7, rely = r, anchor = CENTER)
                    r += 0.2

                    imglabel1 = Label(root, image = img)
                    imglabel1.place(relx = 0.8, rely = rrrr, anchor = CENTER)
                    rrrr += 0.2

                    if in1 == 'y':
                        for i in range(10, len(new), 1):
                            newQ = newQ+new[i]
                        print(newQ)
                        text_file = open("test\output\output_displayed.txt", "a")
                        text_file.write(newQ)
                        break
                    count_n1 += 1
                if count_n1!=0:
                    new1=input("\nPlease Enter one of the insurance name : ")
                    text_file=open("test\output\output_displayed.txt", "a")
                    text_file.write(new1)
except:
	pass           