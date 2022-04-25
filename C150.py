from tkinter import *
import random
root= Tk()
root.title()
root.geometry("600x400")
input_box=Entry(root)
input_box.place(relx=0.5,rely=0.2,anchor=CENTER)
label_Friends=Label(root)
label_random=Label(root)
label_lucky_friend=Label(root)
list_1=[]
def addFriend():
    friend_name=input_box.get()
    list_1.append(friend_name)
    label_Friends["text"]="Your Friend List: "+str(list_1)
def luckyFriend():
    length=len(list_1)
    random_number=random.randint(0,length-1)
    label_random["text"]="Random Number Is "+str(random_number)
    Lucky_friend_name=list_1[random_number]
    label_lucky_friend["text"]="Your Lucky Friend Is "+str(Lucky_friend_name)
button=Button(root,text="Add Friend In The List",command=addFriend)
button.place(relx=0.5,rely=0.3,anchor=CENTER)
button_2=Button(root,text="Who Is My Lucky Friend",command=luckyFriend)
button_2.place(relx=0.5,rely=0.5,anchor=CENTER)
label_Friends.place(relx=0.5,rely=0.4,anchor=CENTER)
label_random.place(relx=0.5,rely=0.6,anchor=CENTER)
label_lucky_friend.place(relx=0.5,rely=0.7,anchor=CENTER)
root.mainloop()