from NaiveBayes import Pool
import os
import pyttsx3
import random
import time
import speech_recognition as sr

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

text_file = open("test\output\output_displayed.txt", "w")
text_file.write(sample)
text_file.close()
#--------------------------------------------------------------------------------------------------

#out = "output"
#dir = os.listdir(base_1 + out)
#print(dir)

for i in range(0, 5, 1):
    with open("test\output\output_displayed.txt", "a") as text_file:
        text_file.write("\n")
        dir = os.listdir(base + out)
        for file in dir:
            result = p.Probability(base + out + "/" + file)
            if file=="output_displayed.txt":
                print(out + ": " + file + ": " + str(result))
                req = str(result[0])
                print(req[2])
                count_n = 0
                for i in range(0,5,1):
                    l = "data/"
                    c = "Chatbot.txt"
                    sen = str(result[0])
                    k2 = sen[2]
                    k1 = k2 + c
                    print(k1)
                    fp = open(l + k2 + "/" + k1)
                    lines = fp.read().split("\n")
                    print(lines[i])
                    #-------------------------------------------------------
                    #--------------------------------------------------------
                   # engine = pyttsx3.init()
                    #k=''
                    #k=lines[i]
                    #engine.say(k)
                    #engine.setProperty('rate', 45)
                    #engine.setProperty('volume', 5)
                    #engine.runAndWait()
                    #----------------------------------------------------------
                    #----------------------------------------------------------
                    in1 = input("\nEnter your respnse : y/n : ")
                    if in1=='n':
                        count_n+=1
                if count_n<=1:
                    print(sen[2])
                    m2 = sen[2]
                    exit()
                else:
                    l ="data/"
                    c = "Chatbot.txt" 
                    sen = str(result[1])
                    k2 = sen[2]
                    k1 = k2 + c
                    print(k1)
                    count_n1 = 0
                    #fp = open(l + k2 + "/" + k1)
                    #lines = fp.read().split("/n")
                    #print(lines[i])
                    for i in range(0,3,1):
                        fp=open(l + k2 + "/" + k1)
                        lines=fp.read().split("\n")
                        newQ=" "
                        print(lines[i])
                        #------------------------------------
                        #---------------------------------------
                     #   engine = pyttsx3.init()
                     #   k=''
                        #k=input('enter the text u want to speak out')
                     #   k=lines[i]
                     #   engine.say(k)
                     #   engine.setProperty('rate',45)
                     #   engine.setProperty('volume', 5)
                     #   engine.runAndWait()
                        #------------------------------------------
                        #------------------------------------------
                        new=lines[i]
                        in1 = input("\nEnter your respnse : y/n :")
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
                    #------------------------------------------------------------------------
                        text_file=open("test\output\output_displayed.txt", "a")
                        text_file.write(new1)



