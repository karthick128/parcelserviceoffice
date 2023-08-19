from inspect import findsource
from tkinter import *
from turtle import st
#from tkcalendar import Calendar
from LOGIN_BACKEND import INPUTS
from TRACKING_BACKEND import tracking
from tkinter import messagebox
from tkinter.ttk import Treeview
from tkinter import ttk
import tkinter as tk
from datetime import *
from write import store
import random


from write import store
import csv

def main():
    global a
    
    a=tracking()
    filename = "csv1.csv"
	
# writing to csv file
    with open(filename, 'r') as csv1: 
            items=csv.reader(csv1)
            for i in items:
                if i==[]:
                    continue
                else:
                    tracking_num=[]
                    for j in range(2,len(i)):
                        tracking_num.append(i[j])
                    a.pushSS([i[0],i[1]],tracking_num)
            a._iter_()
    
    

def submit():
        global track,details,z
        z=INPUTS()
        details = [e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get(),e11.get(),e12.get()]##str(cal.selection_get())]
        track = e10

        z.push_(details)
        z.push(track)
        
        print("HIIIIIIIIIIIIII")
        print(z.a1[:z.s1],z.b1[:z.s2])
def _tracking():
        global screen
        
        screen=LabelFrame(a,bd=2,relief="groove")
           
        screen.place(x=300,y=300,height=100,width=755)
        screen_label=Label(
            screen,
            text="Would you like to TRACK THE STATUS of your parcel ?",
            font="arial 16",
            bg="White",
            fg="black"
            ).grid(row=0,column=1)

        yes=Button(
            screen,
            text="YES",
            command = lambda : s2()
            ).grid(row=3,column=1)

        no=Button(
            screen,
            text="No",
            command= lambda : _back()).grid(row=3,column=3) 
      
        
def proceed():
    s=store()
    s.append_array()
    print(">>>>>>>")
    if e10==eeee1.get() and e9.get()==eeee4.get() :
        print("*")
        main()
        track_num=[e10]
        loc_pin=[e4.get(),e11.get()]
        #a.pushSS(loc_pin,track_num)

        p=a.getfront()
        status=0
    
        while a.getdest(p)[0]!=e9.get():
                p=a.getnext(p)
        p.t_s=True
        
        i=0
        while s.lst_p()[i][0]!=e9.get():
             i+=1
             
        if e10 not in s.lst_p()[i]:
                s.lst_p()[i].append(e10)
                p.t_n=s.lst_p()[i][2:len(s.lst_p()[i])]
                
                s=store(s.lst_p())
                s.append_array()
                status=1
        
        main()
        if status==1:
            for i in a.trackno(p):
                #print(i)
                pass
            messagebox.showinfo("STATUS OF THE PARCEL","PARCEL DELIVERED TO THE DESTINATION")
        else:
            print("Service not available")
            messagebox.showinfo("STATUS OF THE PARCEL","PARCEL IS YET TO BE  DELIVERED TO THE DESTINATION")
        print(a.getdest(p),a.trackno(p),a.track(p))
    else:
        no_track()
    
z=INPUTS()
def findS():
    
        global Ln
        main()
        
        p=a.getfront()
        i=0
            #print(a.getlen())
        while a.getdest(p)[1]!=eee1.get():
            i+=1
            p=p.next()
        Ln=[a.getdest(p)[0],a.trackno(p)]
        print(Ln)
        tv = ttk.Treeview(M,columns=(1,2,3), show='headings', height=8)
        tv.pack(pady=10)
       
       
        tv.heading(1, text="LOCATION NAME")
        tv.heading(2, text="TRACKING NUMBER")
        tv.heading(3, text="DELIVERY DATE")
       
        tv.insert(parent="",index=i,iid=i,values=(Ln[0],Ln[1][0]))
        style = ttk.Style()
        style.theme_use("default")
        style.map("Treeview")
        #print(details[11])
    

def FETCH_DETAILS():
    print("entereing")
    #z=INPUTS()
    global guindy
    i=0

    while e10!=z.b1[i]:
        i+=1
        messagebox.showinfo("INVALID ENTRY","NO SUCH PARCELS IN THE TRACKING NUMBER")
    print('........',z.a1[i])
    #r= Tk()
    #r.title("DETAILS OF THE PARCEL")
    tv = ttk.Treeview(n,columns=(1,2,3,4,5,6), show='headings', height=8)
    tv.pack(pady=10)
    guindy =z.a1[i]

            #print("guindy",Ln)
    tv.heading(1, text="SENDER NAME")
    tv.heading(2, text="PHONE")
    tv.heading(3, text="ADDRESS")
    tv.heading(4, text="DESTINATION")
    tv.heading(5, text="PINCODE")
    tv.heading(6, text="DELIVERY DATE")
    '''tv.heading(3, text="Date of depature")
            tv.heading(4,text="Tracking number")'''
    tv.insert(parent="",index=i,iid=i,values=(guindy[0],guindy[1],guindy[2],guindy[8],guindy[10],guindy[11]))
    style = ttk.Style()
    style.theme_use("default")
    style.map("Treeview")
    #print(details[11])

    
def no_track():
        messagebox.showinfo(" TRACKING NUMBER NOT FOUND!!" ,"PLEASE CHECK THE TRACKING NUMBER")



def admin_login(window):

    window.destroy()

    global n,TRACK_NUM,TRACKE
    n=Tk()


    n["bg"]="#a3f2f4"
    n.geometry("700x300")



    n.title("CUSTOMER DETAILS")

    n.geometry("1080x750")
    n.configure(bg = "#ffffff")
    canvas = Canvas(
        n,
        bg = "#ffffff",
        height = 750,
        width = 1080,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"C:\\Users\\preet\\OneDrive\\Desktop\\prj fin\\admin2pg\\bq.png")
    background = canvas.create_image(
        540.0, 375.0,
        image=background_img)

    entry0_img = PhotoImage(file = f"C:\\Users\\preet\\OneDrive\\Desktop\\prj fin\\admin2pg\\bqt1.png")
    entry0_bg = canvas.create_image(
        785.5, 279.5,
        image = entry0_img)

    TRACKE = Entry(
        bd = 0,
        bg = "#d9d9d9",
        highlightthickness = 0)

    TRACKE.place(
        x = 599.5, y = 258,
        width = 372.0,
        height = 41)

    img0 = PhotoImage(file = f"C:\\Users\\preet\\OneDrive\\Desktop\\prj fin\\admin2pg\\buqt1.png")
    sub = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command=lambda : FETCH_DETAILS(),
        relief = "flat")

    sub.place(
        x = 493, y = 365,
        width = 105,
        height = 34)

    n.resizable(False, False)
    n.mainloop()


    '''l0=Label(n,text="CUSTOMER DETAILS",font=("Comic Sans MS",15),bg="#a3f2f4",fg="white",width=25,height=2).grid(row=0,column=0)
    TRACK_NUM=Label(n,text="TRACKING NUMBER",font=("Arial"),bg="black",fg="white").grid(row=1,column=0)
    TRACKE=Entry(n)
    TRACKE.grid(row=1,column=1)
    sub=Button(n,text="SEARCH",bg="brown",fg="white",activebackground="blue",activeforeground="orange",command=lambda : FETCH_DETAILS() )
    sub.grid(row=1,column=2)'''
def _back():
    screen.destroy()
    
def call_two():
    h=store()
    if e1.get()=="":
        messagebox.showwarning("Invalid entry","Enter the name ")
    if len(e2.get()) !=10 or  e2.get()=="" or e2.get().isdigit()==False :
        messagebox.showwarning("Invalid mobile number","Enter valid phone number")
    if e3.get()=="":
        messagebox.showwarning("Invalid entry","Enter the address")
    c=0
    for i in h.lst:
        
        if e4.get() not in i[0] :
            c+=1
    if c==len(h.lst):
        messagebox.showwarning("regret ","sorry no services available to the location")
    if e4.get()=="":
        messagebox.showwarning("Invalid entry","Enter the location")
        
    if "@" not in e5.get() or e5.get()=="" :
        messagebox.showwarning("Invalid email id","Enter valid mail id")
    if e6.get()=="":
        messagebox.showwarning("Invalid entry","Enter the name ")
        
    if len(e7.get()) !=10 or  e7.get()=="" or e7.get().isdigit()==False :
        messagebox.showwarning("Invalid mobile number","Enter valid phone number")
    if e8.get()=="":
        messagebox.showwarning("Invalid entry","Enter the address")
    c1=0
    for i in h.lst:
        if e9.get() not in i[0]:
            c1+=1
    if c1==len(h.lst):

        messagebox.showwarning("regret ","sorry no services available to the location")
    if e9.get()=="":
        messagebox.showwarning("Invalid entry","Enter the location")
        
    c2=0   
    for i in h.lst:
        if int(e11.get()) != i[1]:
            c2+=1
    if c2==len(h.lst):

            messagebox.showwarning("regret ","sorry no services available to that pincode")
    if e11.get()=="":
        messagebox.showwarning("Invalid entry","Enter the pincode")
        
    c3=0
    for i in h.lst:
        if int(e12.get()) != i[1]:
            c3+=1
    if c3==len(h.lst):

        messagebox.showwarning("regret ","sorry no services available to the pincode")
    if e12.get()=="":
        messagebox.showwarning("Invalid entry","Enter the pincode")  
    
    
    else:
        messagebox.showinfo("your tracking number is ",e10)
        booking()
        submit()
        
def s1(p):
    global a,e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,z
    z=INPUTS()
    #global a,e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,z
    if p is not None:
        p.destroy()
    a1=Tk()
    a1.title("BOOKING PAGE")
    a1.geometry("1080x750")

    a1.configure(bg = "#ffffff")
    canvas = Canvas(
        a1,
        bg = "#ffffff",
        height = 750,
        width = 1080,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"C:\\Users\\preet\\OneDrive\\Desktop\\prj fin\\parcelpg\\bl.png")
    background = canvas.create_image(
        539.0, 375.0,
        image=background_img)

    entry0_img = PhotoImage(file = f"C:\\Users\\preet\\OneDrive\\Desktop\\prj fin\\parcelpg\\tl1.png")
    entry0_bg = canvas.create_image(
        659.5, 176.5,
        image = entry0_img)

    e1 = Entry(
        bd = 0,
        bg = "#e0c663",
        highlightthickness = 0)

    e1.place(
        x = 451.5, y = 161,
        width = 416.0,
        height = 29)

    entry1_img = PhotoImage(file = f"C:\\Users\\preet\\OneDrive\\Desktop\\prj fin\\parcelpg\\tl2.png")
    entry1_bg = canvas.create_image(
        659.5, 216.5,
        image = entry1_img)

    e2 = Entry(
        bd = 0,
        bg = "#e0c663",
        highlightthickness = 0)

    e2.place(
        x = 451.5, y = 201,
        width = 416.0,
        height = 29)

    entry2_img = PhotoImage(file = f"C:\\Users\\preet\\OneDrive\\Desktop\\prj fin\\parcelpg\\tl3.png")
    entry2_bg = canvas.create_image(
        659.5, 256.5,
        image = entry2_img)

    e3 = Entry(
        bd = 0,
        bg = "#e0c663",
        highlightthickness = 0)

    e3.place(
        x = 451.5, y = 241,
        width = 416.0,
        height = 29)

    entry3_img = PhotoImage(file = f"C:\\Users\\preet\\OneDrive\\Desktop\\prj fin\\parcelpg\\tl4.png")
    entry3_bg = canvas.create_image(
        659.5, 298.5,
        image = entry3_img)

    e4 = Entry(
        bd = 0,
        bg = "#e0c663",
        highlightthickness = 0)

    e4.place(
        x = 451.5, y = 283,
        width = 416.0,
        height = 29)

    entry4_img = PhotoImage(file = f"C:\\Users\\preet\\OneDrive\\Desktop\\prj fin\\parcelpg\\tl5.png")
    entry4_bg = canvas.create_image(
        659.5, 340.5,
        image = entry4_img)

    e5 = Entry(
        bd = 0,
        bg = "#e0c663",
        highlightthickness = 0)

    e5.place(
        x = 451.5, y = 325,
        width = 416.0,
        height = 29)

    entry5_img = PhotoImage(file = f"C:\\Users\\preet\\OneDrive\\Desktop\\prj fin\\parcelpg\\tl6.png")
    entry5_bg = canvas.create_image(
        659.5, 379.5,
        image = entry5_img)

    e6 = Entry(
        bd = 0,
        bg = "#e0c663",
        highlightthickness = 0)

    e6.place(
        x = 451.5, y = 364,
        width = 416.0,
        height = 29)

    entry6_img = PhotoImage(file = f"C:\\Users\\preet\\OneDrive\\Desktop\\prj fin\\parcelpg\\tl7.png")
    entry6_bg = canvas.create_image(
        659.5, 415.5,
        image = entry6_img)

    e7 = Entry(
        bd = 0,
        bg = "#e0c663",
        highlightthickness = 0)

    e7.place(
        x = 451.5, y = 400,
        width = 416.0,
        height = 29)

    entry7_img = PhotoImage(file = f"C:\\Users\\preet\\OneDrive\\Desktop\\prj fin\\parcelpg\\tl8.png")
    entry7_bg = canvas.create_image(
        659.5, 458.5,
        image = entry7_img)

    e8 = Entry(
        bd = 0,
        bg = "#e0c663",
        highlightthickness = 0)

    e8.place(
        x = 451.5, y = 443,
        width = 416.0,
        height = 29)

    entry8_img = PhotoImage(file = f"C:\\Users\\preet\\OneDrive\\Desktop\\prj fin\\parcelpg\\tl9.png")
    entry8_bg = canvas.create_image(
        659.5, 501.5,
        image = entry8_img)

    e9 = Entry(
        bd = 0,
        bg = "#e0c663",
        highlightthickness = 0)

    e9.place(
        x = 451.5, y = 486,
        width = 416.0,
        height = 29)

    entry9_img = PhotoImage(file = f"C:\\Users\\preet\\OneDrive\\Desktop\\prj fin\\parcelpg\\tl10.png")
    entry9_bg = canvas.create_image(
        659.5, 541.5,
        image = entry9_img)

    e10 = random.randint(20220000,20230000)

    entry10_img = PhotoImage(file = f"C:\\Users\\preet\\OneDrive\\Desktop\\prj fin\\parcelpg\\tl11.png")
    entry10_bg = canvas.create_image(
        659.5, 584.5,
        image = entry10_img)

    e11= Entry(
        bd = 0,
        bg = "#e0c663",
        highlightthickness = 0)

    e11.place(
        x = 451.5, y = 526,
        width = 416.0,
        height = 29)
    entry11_img = PhotoImage(file = f"C:\\Users\\preet\\OneDrive\\Desktop\\prj fin\\parcelpg\\tl12.png")
    entry11_bg = canvas.create_image(
        659.5, 627.5,
        image = entry11_img)

    e12= Entry(
        bd = 0,
        bg = "#e0c663",
        highlightthickness = 0)

    e12.place(
        x = 451.5, y = 569,
        width = 416.0,
        height = 29)
    e13 = Entry(
        bd = 0,
        bg = "#e0c663",
        highlightthickness = 0)

    e13.place(
        x = 451.5, y = 612,
        width = 416.0,
        height = 29)

    img0 = PhotoImage(file = f"C:\\Users\\preet\\OneDrive\\Desktop\\prj fin\\parcelpg\\bul1.png")
    sub = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command=lambda : call_two(),
        relief = "flat")

    sub.place(
        x = 436, y = 649,
        width = 163,
        height = 31)

    img1 = PhotoImage(file = f"C:\\Users\\preet\\OneDrive\\Desktop\\prj fin\\parcelpg\\bul2.png")
    subj = Button(
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command=lambda : backs(a1),
        relief = "flat")

    subj.place(
        x = 254, y = 647,
        width = 163,
        height = 33)

    a1.resizable(False, False)
    a1.mainloop()   






    """l1=Label(a1,text="NAME OF THE SENDER").grid(row=0,column=0)
    l2=Label(a1,text="PHONE NUM").grid(row=1,column=0)
    l3=Label(a1,text="ADDRESS").grid(row=2,column=0)
    l4=Label(a1,text="SOURCE").grid(row=3,column=0)
    l5=Label(a1,text="EMAIL").grid(row=4,column=0)
    l6=Label(a1,text="NAME OF THE RECIEVER").grid(row=5,column=0)
    l7=Label(a1,text="PHONE NUM").grid(row=6,column=0)
    l8=Label(a1,text="ADDRESS").grid(row=7,column=0)
    l9=Label(a1,text="DESTINATION").grid(row=8,column=0)
    #l10=Label(a1,text="TRACKING NUMBER").grid(row=9,column=0)
    l11=Label(a1,text="PINCODE OF THE SOURCE").grid(row=9,column=0)
    l12=Label(a1,text="PINCODE OF THE DESTINATION").grid(row=10,column=0)
    l13=Label(a1,text="EXPECTED DELIVERY DATE").grid(row=11,column=0)

    e1=Entry(a1)
    e2=Entry(a1)
    e3=Entry(a1)
    e4=Entry(a1)
    e5=Entry(a1)
    e6=Entry(a1)
    e7=Entry(a1)
    e8=Entry(a1)
    e9=Entry(a1)
    e10=random.randint(20220000,20230000)
    e11=Entry(a1)
    e12=Entry(a1)
    e13=Entry(a1)
    e1.grid(row=0,column=1)
    e2.grid(row=1,column=1)
    e3.grid(row=2,column=1)
    e4.grid(row=3,column=1)
    e5.grid(row=4,column=1)
    e6.grid(row=5,column=1)
    e7.grid(row=6,column=1)
    e8.grid(row=7,column=1)
    e9.grid(row=8,column=1)
    #e10.grid(row=9,column=1)
    e11.grid(row=9,column=1)
    e12.grid(row=10,column=1)
    e13.grid(row=11,column=1)
    global cal
    ##cal=Calendar(a1)
    cal.grid(row=18,column=1)
    sub=Button(a1,text="Submit",command=lambda : call_two() )
    sub.grid(row=20,column=5)
    subj=Button(a1,text="back",command=lambda : backs(a1) )
    subj.grid(row=20,column=7)"""
def backsS(ind):
    frontpage(ind)
    #ind.destroy()


    
def back(a):
    frontpage(a)

def s2():
    global eeee1,e2,e3,eeee4
    #main()
    
    a=Tk()
    a.title("TRACKING STATUS")
    a.geometry()
    a.geometry("1080x750")
    a.configure(bg = "#ffffff")
    canvas = Canvas(
        a,
        bg = "#ffffff",
        height = 750,
        width = 1080,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    

    '''l1=Label(a,text="ENTER THE TRACKING NUMBER").grid(row=12,column=0)
   
    l4=Label(a,text="ENTER THE LOCATION NAME OF THE DESTINATION ").grid(row=24,column=0)
    ee1=Entry(a)
    
    ee4=Entry(a)
    ee1.grid(row=12,column=1)
    
    ee4.grid(row=24,column=1)
    sub=Button(a,text="PROCEED",command=lambda : proceed() )
    sub.grid(row=50,column=5)'''


def s3(arrs):
    
    
    global eee1,M
    M=Tk()
    M.title("DATEWISE LIST OF DELIVERIES")
    M.geometry("1080x1000")
    global e1,e2,e3
    M["bg"]="#a3f2f4"
    #a2.geometry("1080x1000")
    l0=Label(M,text="DATEWISE LIST OF DELIVERIES",font=("Comic Sans MS",15),bg="#a3f2f4",fg="white",width=30,height=2).grid(row=0,column=0,pady=10,padx=25)
    l1=Label(M,text="ENTER THE PINCODE",font=("Arial"),bg="black",fg="white").grid(row=1,column=0)
    eee1=Entry(M)
    eee1.grid(row=1,column=1) 
    sub=Button(M,text="SEARCH",font=("Arial"),bg="brown",fg="white",activebackground="blue",activeforeground="orange",command=lambda :findS() )
    sub.grid(row=2,column=2)
    
    
    
    #arrs.destroy()

def proceed1():
    c=0
    filename="csv1.csv"
    with open(filename, 'r') as csv1: 
            items=csv.reader(csv1)
            for i in items:
                #print("hii",i)
                if i==[]:
                    continue
                elif eeee4.get() in i:
                    c+=1
                    filename="csv1.csv"
                    with open(filename, 'r') as csv1: 
                        items=csv.reader(csv1)
                        for i in items:
                            #print("hii",i)
                            if i==[]:
                                continue
                            elif i[0]==eeee4.get():
                                if eeee1.get() in i:
                                    messagebox.showinfo("STATUS OF THE PARCEL","PARCEL DELIVERED TO THE DESTINATION")
                                else:
                                    messagebox.showinfo("STATUS OF THE PARCEL","NO SUCH PARCELS ")
    #w.destroy()
    if c==0:
        messagebox.showinfo("Destination","Destination Invalid")
    #w.destroy()

def status_tracking(windss):
    windss.destroy()
    global eeee1,eeee4

    
    h=Tk()
    h.title("TRACKING STATUS")
    h.geometry("1080x750")
    background_img = PhotoImage(file = f"C:\\Users\\preet\\OneDrive\\Desktop\\prj fin\\trackingpg\\ba.png")
    canvas = Canvas(
    h,
    bg = "#ffffff",
    height = 750,
    width = 1080,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
    canvas.place(x = 0, y = 0)
    background = canvas.create_image(
        540.0, 375.0,
        image=background_img)

    entry0_img = PhotoImage(file = f"C:\\Users\\preet\\OneDrive\\Desktop\\prj fin\\trackingpg\\bat1.png")
    entry0_bg = canvas.create_image(
        785.5, 279.5,
        image = entry0_img)

    eeee1 = Entry(
        bd = 0,
        bg = "#d9d9d9",
        highlightthickness = 0)

    eeee1.place(
        x = 599.5, y = 258,
        width = 372.0,
        height = 41)

    entry1_img = PhotoImage(file = f"C:\\Users\\preet\\OneDrive\\Desktop\\prj fin\\trackingpg\\bat2.png")
    entry1_bg = canvas.create_image(
        785.5, 332.5,
        image = entry1_img)

    eeee4 = Entry(
        bd = 0,
        bg = "#d9d9d9",
        highlightthickness = 0)

    eeee4.place(
        x = 599.5, y = 311,
        width = 372.0,
        height = 41)

    img0 = PhotoImage(file = f"C:\\Users\\preet\\OneDrive\\Desktop\\prj fin\\trackingpg\\bab1.png")
    sub = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command=lambda : proceed(),
        relief = "flat")

    sub.place(
        x = 493, y = 365,
        width = 105,
        height = 34)

    img1 = PhotoImage(file = f"C:\\Users\\preet\\OneDrive\\Desktop\\prj fin\\trackingpg\\bab2.png")
    sub1= Button(
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command=lambda : backs(h),relief = "flat")

    sub1.place(
        x = 631, y = 365,
        width = 105,
        height = 34)

    a.resizable(False, False)
    a.mainloop()

    
    '''bbo=Label(h,text="TRAKING STATUS",font=("Comic Sans MS",20),bg="#a3f2f4",fg="white",width=20,height=2).grid(row=0,column=0,pady=10,padx=25)
    l1=Label(h,text="ENTER THE TRACKING NUMBER",font=("Arial"),bg="black",fg="white").grid(row=1,column=0)
   
    l4=Label(h,text="ENTER THE LOCATION NAME OF THE DESTINATION ",font=("Arial"),bg="black",fg="white").grid(row=2,column=0)
    eeee1=Entry(h)
    
    eeee4=Entry(h)
    eeee1.grid(row=1,column=1)

   
    
    eeee4.grid(row=2,column=1)
    sub=Button(h,text="PROCEED",font=("Arial"),bg="brown",fg="white",activebackground="blue",activeforeground="orange",command=lambda : proceed1() )
    sub.grid(row=3,column=2)
    sub=Button(h,text="BACK",font=("Arial"),bg="brown",fg="white",activebackground="blue",activeforeground="orange",command=lambda : backs(h) )
    sub.grid(row=3,column=3)
    windss.destroy()'''
    
def backs(wii):
    s7(wii)
    #wii.destroy()
def booking():
    s=store()
    s.append_array()

    i=0
    status=0
    
    while s.lst_p()[i][0]!=e9.get():
        i+=1
             
    if e10 not in s.lst_p()[i]:
            s.lst_p()[i].append(e10)
            #p.t_n=s.lst_p()[i][2:len(s.lst_p()[i])]
                
            s=store(s.lst_p())
            s.append_array()
            status=1

    main()
    
    p=a.getfront()
    while a.getdest(p)[0]!=e9.get():
        p=a.getnext(p)
    p.t_s=True

    messagebox.showinfo("BOOKING SUCCESFULL","ORDER PLACED ")

def s7(winds):
    winds.destroy()
    g = Tk()

    g.geometry("1080x750")
    g.configure(bg = "#ffffff")
    canvas = Canvas(
        g,
        bg = "#ffffff",
        height = 750,
        width = 1080,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"C:\\Users\\preet\\OneDrive\\Desktop\\prj fin\\cust2pg\\bk1.png")
    background = canvas.create_image(
        540.0, 375.0,
        image=background_img)

    img0 = PhotoImage(file = f"C:\\Users\\preet\\OneDrive\\Desktop\\prj fin\\cust2pg\\buk1.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command=lambda:backsS(g),
        relief = "flat")

    b0.place(
        x = 128, y = 602,
        width = 269,
        height = 74)

    img1 = PhotoImage(file = f"C:\\Users\\preet\\OneDrive\\Desktop\\prj fin\\cust2pg\\buk2.png")
    b1 = Button(
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command=lambda:s3(g),
        relief = "flat")

    b1.place(
        x = 125, y = 502,
        width = 439,
        height = 75)

    img2 = PhotoImage(file = f"C:\\Users\\preet\\OneDrive\\Desktop\\prj fin\\cust2pg\\buk3.png")
    b2 = Button(
        image = img2,
        borderwidth = 0,
        highlightthickness = 0,
        command=lambda:s1(g),
        relief = "flat")

    b2.place(
        x = 123, y = 401,
        width = 441,
        height = 76)

    img3 = PhotoImage(file = f"C:\\Users\\preet\\OneDrive\\Desktop\\prj fin\\cust2pg\\buk4.png")
    b3 = Button(
        image = img3,
        borderwidth = 0,
        highlightthickness = 0,
        command=lambda:status_tracking(g),
        relief = "flat")

    b3.place(
        x = 118, y = 302,
        width = 436,
        height = 73)

    g.resizable(False, False)
    g.mainloop()

   
    """g=Tk()
    g.title("CUSTOMER LOGIN MANAGEMENT SYSTEM")
    g.geometry("1080x1000")
    g["bg"]="#a3f2f4"
    bbo=Label(g,text="CHOOSE A SERVICE",font=("Comic Sans Ms",20),bg="#a3f2f4",fg="white",width=20,height=2).grid(row=0,column=0,pady=10,padx=25)
    bb1=Button(g,text="STATUS TRACKING ",command=lambda:status_tracking(g),width=20,height=3,activebackground="blue",activeforeground="orange",bg="blue",fg="white").grid(row=1,column=0,pady=10)
    bb5=Button(g,text="PARCEL BOOKING ",command=lambda:s1(g),width=20,height=3,activebackground="blue",activeforeground="orange",bg="blue",fg="white").grid(row=2,column=0,pady=10)
    bb3=Button(g,text="UPDATES ",command=lambda:s3(g),width=20,height=3,activebackground="blue",activeforeground="orange",bg="blue",fg="white").grid(row=3,column=0,pady=10)
    bb4=Button(g,text="BACK ",command=lambda:backsS(g),width=20,height=3,activebackground="blue",activeforeground="orange",bg="blue",fg="white").grid(row=4,column=0,pady=10)
    winds.destroy()"""


def treeview():
    a2 = Tk()
    

    
def admin_password(window1):
    def proceeding(windowS):
        if user.get()=="HK" and password1.get()=="123":
            
            admin_login(windowS)
        else:
            messagebox.askretrycancel("Invalid Login","Invalid username or password")
        windowS.destroy()
    window1.destroy()
    j = Tk()

    j.geometry("1080x750")
    j.configure(bg = "#ffffff")
    j.title("ADMIN DETAILS  MANAGEMENT SYSTEM")
    canvas = Canvas(
        j,
        bg = "#ffffff",
        height = 750,
        width = 1080,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"C:\\Users\\preet\\OneDrive\\Desktop\\prj fin\\bx1.png")
    background = canvas.create_image(
        540.0, 375.0,
        image=background_img)

    entry0_img = PhotoImage(file = f"C:\\Users\\preet\\OneDrive\\Desktop\\prj fin\\tx1.png")
    entry0_bg = canvas.create_image(
        811.5, 466.0,
        image = entry0_img)

    user = Entry(
        bd = 0,
        bg = "#d9c298",
        highlightthickness = 0)

    user.place(
        x = 661.0, y = 441,
        width = 301.0,
        height = 48)

    entry1_img = PhotoImage(file = f"C:\\Users\\preet\\OneDrive\\Desktop\\prj fin\\tx2.png")
    entry1_bg = canvas.create_image(
        811.5, 553.0,
        image = entry1_img)

    password1= Entry(
        bd = 0,
        bg = "#d9c298",
        highlightthickness = 0)

    password1.place(
        x = 661.0, y = 528,
        width = 301.0,
        height = 48)

    img0 = PhotoImage(file = f"C:\\Users\\preet\\OneDrive\\Desktop\\prj fin\\bux1.png")
    bb1= Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,command=lambda:proceeding(j),
        relief = "flat")

    bb1.place(
        x = 688, y = 607,
        width = 169,
        height = 65)

    j.resizable(False,False)
    j.mainloop()   
    '''j=Tk()
    j.title("ADMIN DETAILS  MANAGEMENT SYSTEM")
    j.geometry("1080x1000")

    j["bg"]="#a3f2f4"
    l0=Label(j,text="ADMIN LOGIN",font=("Comic Sans MS",20),bg="#a3f2f4",fg="white",width=20,height=2).grid(row=0,column=0,pady=10)

    l1=Label(j,text="USERNAME",font=("Arial"),width=20,height=3,activebackground="blue",activeforeground="orange",bg="black",fg="white").grid(row=1,column=0,pady=10)
    l4=Label(j,text="PASSWORD ",font=("Arial"),width=20,height=3,activebackground="blue",activeforeground="orange",bg="black",fg="white").grid(row=2,column=0,pady=10)
    user=Entry(j)
    password=Entry(j)
    user.grid(row=1,column=1)
    password.grid(row=2,column=1)
    sub=Button(j,text="PROCEED",width=7,height=2,activebackground="blue",activeforeground="orange",bg="blue",fg="white",command=lambda:proceeding(j),)
    sub.grid(row=3,column=1)
    '''
class password_cls:
    def __init__(self):
        self.s=0
        self.pass_dic={}
        self.push()
    def push(self):
        self.pass_dic["kaviya"]='hkservice'
        self.s+=1
        print(self.pass_dic)
    def find(self):
        print("<<<<<<<<<", self.username_login.get(), self.password_login.get())
        #print(self.pass_dic.keys())
        if self.username_login.get() in self.pass_dic.keys():
            
            if self.pass_dic[self.username_login.get()]== self.password_login.get():
                messagebox.showinfo("login","login successful")
                s7(h)
            elif self.pass_dic[ self.username_login.get()] !=  self.password_login.get():
                messagebox.showinfo("login","invalid password")
        else:
            messagebox.showinfo("login  failed","please check username or password")

    def password(self,winds):
        global user,password,h
        winds.destroy()
        
        h=Tk()
        h.title("CUSTOMER LOGIN MANAGEMENT SYSTEM")
        h.geometry("1080x750")
        h.configure(bg = "#ffffff")
        canvas = Canvas(h,bg = "#ffffff",height = 750,width = 1080,bd = 0,highlightthickness = 0,relief = "ridge")
        canvas.place(x = 0, y = 0)

        background_img = PhotoImage(file = f"C:\\Users\\preet\\OneDrive\\Desktop\\prj fin\\b1.png")
        canvas.create_image(
        540.0, 375.0,
        image=background_img)
        
        entry0_img = PhotoImage(file = f"C:\\Users\\preet\\OneDrive\\Desktop\\prj fin\\t1.png")
        canvas.create_image(811.5, 466.0,image = entry0_img)
        user=Entry(bd = 0,bg = "#d9c298",highlightthickness = 0)
        user.place(x = 661.0, y = 441,width = 301.0,height = 48)
        entry1_img = PhotoImage(file = f"C:\\Users\\preet\\OneDrive\\Desktop\\prj fin\\t2.png")
        canvas.create_image(
            811.5, 553.0,
            image = entry1_img)

        password= Entry(
            bd = 0,
            bg = "#d9c298",
            highlightthickness = 0)

        password.place(
            x = 661.0, y = 528,
            width = 301.0,
            height = 48)


        img0 = PhotoImage(file = f"C:\\Users\\preet\\OneDrive\\Desktop\\prj fin\\bu1.png")

    
        
        sub=Button(image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        relief = "flat",command=lambda :self.find() )
        sub.place(
        x = 688, y = 607,
        width = 224,
        height = 65)

        
        
        self.username_login = user
        self.password_login=password
        h.resize(False,False)
        h.mainloop()


    #winds.destroy()'''
def frontpage(p=None):

    def log():
        s1(b)
    if p is not None:
        p.destroy()
    b=Tk()
    b.title("COURIER MANAGEMENT SYSTEM")
    b.geometry("1080x750")
    b.configure(bg = "#ffffff")
    canvas = Canvas(b,bg = "#ffffff",height = 750,width = 1080,bd = 0,highlightthickness = 0,relief = "ridge")
    canvas.place(x = 0, y = 0)
    background_img = PhotoImage(file = f"frontpg\\background.png")
    canvas.create_image(540.0, 500.0,image=background_img)
    
    def pincodes():
        s2()

    

        p.destroy()
    pasw=password_cls()
    img0 = PhotoImage(file = f"C:\\Users\\preet\\OneDrive\\Desktop\\prj fin\\img0.png")
    b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:pasw.password(b),
    relief = "flat")

    b0.place(
    x = 635, y = 314,
    width = 375,
    height = 375)

    img1 = PhotoImage(file = f"C:\\Users\\preet\\OneDrive\\Desktop\\prj fin\\img1.png")
    b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:admin_password(b),
    relief = "flat")

    b1.place(
    x = 82, y = 314,
    width = 375,
    height = 375)
    b.mainloop()

frontpage(p=None)
mainloop()
