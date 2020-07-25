from tkinter import*
import random
import time
import datetime
import sqlite3
import tkinter.messagebox
import tempfile
import os

dash=Tk()
width=int((dash.winfo_screenwidth())*0.952)
height=int((dash.winfo_screenheight())*7/8)
dash.geometry ("%dx%d+0+0"%(width,height))
dash.maxsize(width,height)
dash.configure(bg='Green')
dash.title('Restaurant Managment System')
left=Frame(dash,bg='Green')
left.pack(side=LEFT)

#left photos
photod1=PhotoImage(file='d1.png')
photo_labeld1=Label(left,image=photod1)
photo_labeld1.pack(side=TOP,fill=BOTH)
photod2=PhotoImage(file='d2.png')
photo_labeld2=Label(left,image=photod2)
photo_labeld2.pack(side=TOP,fill=BOTH)
photod3=PhotoImage(file='d3.png')
photo_labeld3=Label(left,image=photod3)
photo_labeld3.pack(side=TOP,fill=BOTH)
photod4=PhotoImage(file='d4.png')
photo_labeld4=Label(left,image=photod4)
photo_labeld4.pack(side=TOP,fill=BOTH)
photod5=PhotoImage(file='d5.png')
photo_labeld5=Label(left,image=photod5)
photo_labeld5.pack(side=TOP,fill=BOTH)
photod6=PhotoImage(file='d6.png')
photo_labeld6=Label(left,image=photod6,bg='Green')
photo_labeld6.pack(side=TOP,fill=BOTH)
#
right=Frame(dash,bg='Green')
right.pack(side=RIGHT)
photod7=PhotoImage(file='d7.png')
photo_labeld7=Label(right,image=photod7)
photo_labeld7.pack(side=TOP,fill=BOTH)
photop1=PhotoImage(file='p1.png')
photo_labelp1=Label(right,image=photop1)
photo_labelp1.pack(side=TOP,fill=BOTH)
photop2=PhotoImage(file='p2.png')
photo_labelp2=Label(right,image=photop2)
photo_labelp2.pack(side=TOP,fill=BOTH)
photop3=PhotoImage(file='p3.png')
photo_labelp3=Label(right,image=photop3)
photo_labelp3.pack(side=TOP,fill=BOTH)
photop4=PhotoImage(file='p4.png')
photo_labelp4=Label(right,image=photop4)
photo_labelp4.pack(side=TOP,fill=BOTH)


btn=Frame(dash,bg='Green')
btn.pack(side=BOTTOM)
th=Label(btn,text='LOST time is never FOUND again!!!!!',font=('arial 12 bold'),fg='white',bg='Green')
th.pack(side=BOTTOM)
Up_photo=Frame(dash,bg='Green')
Up_photo.pack(side=TOP)
Up_photol=Frame(Up_photo,bg='Green')
Up_photol.pack(side=LEFT,fill=BOTH)
Up_photoR=Frame(Up_photol,bg='Green')
Up_photoR.pack(side=RIGHT,fill=BOTH)

#
photop=PhotoImage(file='principal.png')
photo_labelp=Label(Up_photol,image=photop)
photo_labelp.pack(side=TOP)
schoole=Label(Up_photol,text='Principal(S.K Mallick)',font=('arial 10 bold'),padx=40)
schoole.pack(side=TOP)

photos=PhotoImage(file='sar.png')
photo_labels=Label(Up_photo,image=photos)
photo_labels.pack(side=TOP,fill=BOTH)
school=Label(Up_photo,text='HOD,Computer\n(Saikat Kumar Roy)',font=('arial 10 bold'),padx=40,pady=15)
school.pack(side=TOP)
photosar=PhotoImage(file='school.png')
photo_labelsar=Label(Up_photoR,image=photosar)
photo_labelsar.pack(side=TOP)
schools=Label(Up_photoR,text='\tSNSVM\t\t',font=('arial 10 bold'),padx=45,pady=10)
schools.pack(side=TOP)

wlc=Frame(dash,bg='Green')
wlc.pack(side=TOP)


def skip():
    dash.destroy()
lab_w=Label(wlc,text='Welcome To SNSVM Restaurant',font=('arial 40 bold'),bg='Green',
            justify=CENTER,fg='white')
lab_w.pack(side=TOP)
lab_s=Label(wlc,text='2019-2020',font=('arial 20 bold'),bg='Green',
            justify=CENTER,fg='white')
lab_s.pack(side=TOP)
lab_v=Label(wlc,text='...version 3.Os...',font=('arial 15 bold'),bg='Green',
            justify=CENTER,fg='white')
lab_v.pack(side=TOP)
U_photo=Frame(dash,bg='Green')
U_photo.pack(side=BOTTOM)

ujjwal=Label(U_photo,text='Ujjwal',font=('arial 10 bold'),padx=55)
ujjwal.pack(side=BOTTOM,anchor='nw')
photom=PhotoImage(file='ujjwal.png')
photo_labelm=Label(U_photo,image=photom)
photo_labelm.pack(side=LEFT,anchor='se')

ria=Label(U_photo,text='Ria',font=('arial 10 bold'),padx=100)
ria.pack(side=BOTTOM,anchor='nw')
photor=PhotoImage(file='ria.png')
photo_labelr=Label(U_photo,image=photor)
photo_labelr.pack(side=LEFT,anchor='se')


amit=Label(U_photo,text='Amit',font=('arial 10 bold'),padx=45)
amit.pack(side=BOTTOM,anchor='nw')
photoa=PhotoImage(file='amit.png')
photo_labela=Label(U_photo,image=photoa)
photo_labela.pack(side=LEFT,anchor='se')

skipe=Button(right,text='Skip>>',font=('arial 16 bold'),bg='Green',command=skip,fg='white')
skipe.pack(side=BOTTOM,anchor='se')

dash.mainloop()


#import search
root=Tk()
width=int((root.winfo_screenwidth())*0.952)
height=int((root.winfo_screenheight())*5/6)
root.geometry ("%dx%d+0+0"%(width,height))
root.maxsize(width,height)
#root.minsize(1000,600)
root.title ("Restaurant Management System")
root.configure (background = 'hot pink')

#heading
Tops = Frame (root, bg= 'Cadet Blue',bd=10, pady=5, relief=RIDGE)
Tops.pack (side=TOP,fill=BOTH)
lblTitle = Label (Tops, font=('arial',30,'bold'), text= "Restaurant Management Systems",
                  bd=21, bg= 'maroon', fg= 'Cornsilk', justify= CENTER)
lblTitle.pack(side=TOP,fill=BOTH)
#my own
#------------------------------------------------------------------

MenuFrame= Frame (root, bg='Misty Rose2', bd=10, relief=RIDGE)
MenuFrame.pack (side=LEFT,fill=BOTH)
#name
fm=Frame(MenuFrame,bg='Misty Rose',bd=10,relief=RIDGE)
fm.pack(side=LEFT,anchor='nw',fill=BOTH)
fm3=Frame(fm,bg='Misty Rose2')
fm3.pack(side=TOP,fill=BOTH)
fm2=Frame(fm,bg='Misty Rose2')
fm2.pack(side=TOP,anchor='nw',fill=BOTH)
fm1=Frame(fm2,bg='Misty Rose2')
fm1.pack(side=RIGHT,anchor='ne',fill=BOTH)
#
fm_btn=Frame(fm,bg='Misty Rose',bd=5,relief=RIDGE)
fm_btn.pack(side=BOTTOM)
fm102=Frame(fm_btn,bg='Misty Rose')
fm102.pack(side=RIGHT,anchor='se')

lblitle=Label(fm3, font=('arial',15,'bold'), text= "Customer Details",
              bd=8, bg= 'maroon', fg= 'Cornsilk', justify= CENTER)
lblitle.pack(side=TOP,fill=BOTH)
#RIGHT FRAME
ReceiptCal_F= Frame (root, bg= 'Misty Rose2', bd=10,relief=RIDGE)
ReceiptCal_F.pack (side=LEFT,fill=BOTH)
#P
pho_F= Frame (ReceiptCal_F, bg= 'Misty Rose2', bd=4, relief=RIDGE)
pho_F.pack (side=TOP,fill=BOTH)

#@button frame
Buttons_F= Frame (ReceiptCal_F, bg= 'Misty Rose2', bd=3, relief=RIDGE)
Buttons_F.pack (side=BOTTOM,fill=BOTH)
#recipt frame
Receipt_F= Frame (ReceiptCal_F, bg= 'Misty Rose2', bd=4, relief=RIDGE)
Receipt_F.pack (side=LEFT,anchor='nw',fill=BOTH)

#---------------------------
Cost_F= Frame (MenuFrame, bg= 'Misty Rose2', bd=4)
Cost_F.pack (side=BOTTOM,fill=BOTH)
Drinks_F= Frame (MenuFrame, bg= 'Misty Rose2', bd=10,relief=RIDGE)
Drinks_F.pack (side=LEFT,anchor='nw',fill=X)
Drinks_F1= Frame (Drinks_F, bg= 'Misty Rose2')
Drinks_F1.pack (side=RIGHT,anchor='nw',fill=X)
#photo frame
p1=Frame(Cost_F,bd=10,relief=RIDGE)
p1.pack(side=TOP,anchor='nw',fill=BOTH)
#----------
Cake_F= Frame (MenuFrame, bg= 'Misty Rose2', bd=10, relief=RIDGE)
Cake_F.pack (side=LEFT,anchor='nw',fill=X)
Cake_F1= Frame (Cake_F, bg= 'Misty Rose2')
Cake_F1.pack (side=RIGHT,anchor='nw',fill=X)
#

#
var1= IntVar()
var2= IntVar()
var3= IntVar()
var4= IntVar()
var5= IntVar()
var6= IntVar()
var7= IntVar()
var8= IntVar()
var9= IntVar()
var10= IntVar()
var11= IntVar()
var12= IntVar()
var13= IntVar()
var14= IntVar()
var15= IntVar()
var16= IntVar()
#==================
DateofOrder = StringVar()
PaidTax = StringVar()

TotalCost = StringVar()


text_Input = StringVar()
operator = ""
#input of drinks
E_Sprit =StringVar()
E_CocaCola =StringVar()
E_ThumsUp =StringVar()
E_GreenTea =StringVar()
E_Coffee =StringVar()
E_Lasi =StringVar()
E_Tea =StringVar()
E_IceCream =StringVar()
#cakes input
E_Samosa = StringVar()
E_Idli = StringVar()
E_Dosa = StringVar()
E_Jalebi = StringVar()
E_Rasgulla = StringVar()
E_ChowMein = StringVar()
E_Litti = StringVar()
E_Pizza = StringVar()

#deleting drinks
E_Sprit.set('0')
E_CocaCola.set('0')
E_ThumsUp.set('0')
E_GreenTea.set('0')
E_Coffee.set('0')
E_Lasi.set('0')
E_Tea.set('0')
E_IceCream.set('0')

nam=StringVar()
#pn=StringVar()
pn=StringVar()
addr=StringVar()
ra=StringVar()


#deleting cakes
E_Samosa.set("0")
E_Idli.set("0")
E_Dosa.set("0")
E_Jalebi.set("0")
E_Rasgulla.set('0')
E_ChowMein.set("0")
E_Litti.set("0")
E_Pizza.set("0")
nam.set("")
pn.set("")
addr.set("")

DateofOrder.set (time.strftime ("%d/%m/%Y"))
ra.set(random.randint(100000,9999999))
def iExit ():
    iExit = tkinter.messagebox.askyesno ("Exit Restaurant System", "Confirm if you want to exit")
    if iExit > 0:
        root.destroy()

    return

def searche():
    e=str(nam.get().lower())
    if(nam.get()!=''):
        rd=Tk()
        #rd.geometry('550x550')
        rd.title("Customer Details")
        rd.configure(bg='maroon')
        nam1=Label(rd,text='Name',font=('arial 15 bold'),bg='maroon',fg='white')
        nam1.grid(row=0,column=0,sticky=W)
        ou5=Text(rd,width=20,height=1,font=('none 16 bold'),bg='maroon',fg='white')
        ou5.grid(row=0,column=1)
        ou5.insert(END,e)
        nam2=Label(rd,text='Slip No:',font=('arial 15 bold'),bg='maroon',fg='white')
        nam2.grid(row=1,column=0,sticky=W)
        nam3=Label(rd,text='Phone No:',font=('arial 15 bold'),bg='maroon',fg='white')
        nam3.grid(row=2,column=0,sticky=W)
        nam4=Label(rd,text='Address:',font=('arial 15 bold'),bg='maroon',fg='white')
        nam4.grid(row=3,column=0,sticky=W)
        nam5=Label(rd,text='Total Cost:',font=('arial 15 bold'),bg='maroon',fg='white')
        nam5.grid(row=4,column=0,sticky=W)
        nam6=Label(rd,text='Date of Order:',font=('arial 15 bold'),bg='maroon',fg='white')
        nam6.grid(row=5,column=0,sticky=W)
        def clk():
            crr=sqlite3.connect('Data.db')
            c=crr.cursor()
            c.execute('select* from data')
            l=c.fetchall()
            d={}
            for row in l:
                d[row[0]]=row[1],row[2],row[3],row[4],row[5]
            try:
                b=d[e]
                slip=b[0]
                number=b[1]
                adress=b[2]
                cost=b[3]
                date=b[4]
                ou.insert(0.0,slip)
                ou1.insert(0.0,number)
                ou2.insert(0.0,adress)
                ou3.insert(0.0,cost)
                ou4.insert(0.0,date)
            except:
                tkinter.messagebox.showinfo("program",'No such Name found')
                rd.destroy()
        ou=Text(rd,width=20,height=1,font=('none 16 bold'),bg='maroon',fg='white')
        ou.grid(row=1,column=1)
        ou1=Text(rd,width=20,height=1,font=('none 16 bold'),bg='maroon',fg='white')
        ou1.grid(row=2,column=1)
        ou2=Text(rd,width=20,height=1,font=('none 16 bold'),bg='maroon',fg='white')
        ou2.grid(row=3,column=1)
        ou3=Text(rd,width=20,height=1,font=('none 16 bold'),bg='maroon',fg='white')
        ou3.grid(row=4,column=1)
        ou4=Text(rd,width=20,height=1,font=('none 16 bold'),bg='maroon',fg='white')
        ou4.grid(row=5,column=1)

        clk()
        rd.mainloop()
    else:
        tkinter.messagebox.showinfo("program",'Please Enter the Name')
    
def recipt():
    a=nam.get().lower()
    b=pn.get()
    c=addr.get()
    d=TotalCost.get()
    x=ra.get()
    y=DateofOrder.get()
    
    q="insert into data values"+'('+'"'+a+'"'+','+'"'+x+'"'+','+'"'+b+'"'+','+'"'+c+'"'+','+'"'+d+'"'+','+'"'+y+'"'+')'
    crr=sqlite3.connect('Data.db')
    c=crr.cursor()
    #c.execute("create table Recipt(Name TEXT,SlipNO TEXT,PhoneNo TEXT,Adress TEXT,TotalCost TEXT,DateofOrder TEXT)")
    c.execute(q)
    
    crr.commit()
    c.close()
    #---------------------
    root1=Tk()
    fra=Frame(root1)
    fra.pack(side=TOP)
    root1.title('Receipt')
    def code():
        q=txtReceipt.get('1.0','end-1c')
        filename=tempfile.mktemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename)
    

    txtReceipt=Text (fra,width = 50, height = 100, bg = "white", bd = 4, font = ('arial', 8, 'bold'))
    txtReceipt.grid (row = 0, column = 0)
    root1.maxsize(700,700)
    Item1 = float ( E_Sprit.get ())
    Item2 = float ( E_CocaCola.get ())
    Item3 = float ( E_ThumsUp.get ())
    Item4 = float ( E_GreenTea.get ())
    Item5 = float ( E_Coffee.get ())
    Item6 = float ( E_Lasi.get ())
    Item7 = float ( E_Tea.get ())
    Item8 = float ( E_IceCream.get ())

    Item9 = float ( E_Samosa.get ())
    Item10 = float ( E_Idli.get ())
    Item11 = float ( E_Dosa.get ())
    Item12 = float ( E_Jalebi.get ())
    Item13 = float ( E_Rasgulla.get ())
    Item14 = float ( E_ChowMein.get ())
    Item15 = float ( E_Litti.get ())
    Item16 = float ( E_Pizza.get ())
    txtReceipt.insert(END,"Slip No:\t\t\t"+ra.get()+'\n')               
    if(nam.get()!=''):
        if(nam.get().isalpha()==True):
            txtReceipt.insert(END,'Name:\t\t\t'+nam.get()+'\n')
        else:
            tkinter.messagebox.showinfo("program",'Please Enter the Correct Name')
    if(pn.get()!=''):
        if(pn.get().isnumeric()==True):
            txtReceipt.insert(END,'Phone No:\t\t'+pn.get()+'\n')
        else:
            tkinter.messagebox.showinfo("program",'Please Enter the Correct Phone No')
    if(addr.get()!=''):
        txtReceipt.insert(END,'Address:\t\t\t'+addr.get()+'\n')
    txtReceipt.insert(END,'Date of order:\t\t'+DateofOrder.get()+'\n')
    txtReceipt.insert(END,'-------------------------------------------------------'+'\n')
    if(var1.get()==1):
        txtReceipt.insert(END,'Price of Sprite:\t\t'+'Rs.'+str(Item1*10)+'\n')
    if(var2.get()==1):
        txtReceipt.insert(END,'Price of Coca Cola:\t\t'+'Rs.'+str(Item2*10)+'\n')
    if(var3.get()==1):
        txtReceipt.insert(END,'Price of Thums Up:\t\t'+'Rs.'+str(Item3*10)+'\n')
    if(var4.get()==1):
        txtReceipt.insert(END,'Price of Green Tea:\t\t'+'Rs.'+str(Item4*15)+'\n')
    if(var5.get()==1):
        txtReceipt.insert(END,'Price of Coffee:\t\t'+'Rs.'+str(Item5*10)+'\n')
    if(var6.get()==1):
        txtReceipt.insert(END,'Price of Lassi:\t\t'+'Rs.'+str(Item6*15)+'\n')
    if(var7.get()==1):
        txtReceipt.insert(END,'Price of Tea:\t\t'+'Rs.'+str(Item7*10)+'\n')
    if(var8.get()==1):
        txtReceipt.insert(END,'Price of Ice Cream:\t\t'+'Rs.'+str(Item8*10)+'\n')
    if(var9.get()==1):
        txtReceipt.insert(END,'Price of Somasa:\t\t'+'Rs.'+str(Item9*5)+'\n')
    if(var10.get()==1):
        txtReceipt.insert(END,'Price of Idli:\t\t'+'Rs.'+str(Item10*5)+'\n')
    if(var11.get()==1):
        txtReceipt.insert(END,'Price of Dosa:\t\t'+'Rs.'+str(Item11*20)+'\n')
    if(var12.get()==1):
        txtReceipt.insert(END,'Price of Jalebi:\t\t'+'Rs.'+str(Item12*15)+'\n')
    if(var13.get()==1):
        txtReceipt.insert(END,'Price of Rasgulla:\t\t'+'Rs.'+str(Item13*5)+'\n')
    if(var14.get()==1):
        txtReceipt.insert(END,'Price of Chow Mein:\t\t'+'Rs.'+str(Item14*15)+'\n')
    if(var15.get()==1):
        txtReceipt.insert(END,'Price of Litti:\t\t'+'Rs.'+str(Item15*10)+'\n')
    if(var16.get()==1):
        txtReceipt.insert(END,'Price of Pizza:\t\t'+'Rs.'+str(Item16*10)+'\n')
    txtReceipt.insert(END,'-'*55+'\n')
    txtReceipt.insert(END,'Paid Tax:\t\t\t'+PaidTax.get()+'\n')
    if(TotalCost.get()!=''):
        txtReceipt.insert(END,'Total Cost:\t\t'+TotalCost.get()+'\n')
    txtReceipt.insert(END,"      "+'\n')
    if(TotalCost.get()==''):
        tkinter.messagebox.showinfo("program",'Please Calculate the total cost')
        root1.destroy
    if(ra.get()==''):
        tkinter.messagebox.showinfo("program",'Please Enter Slip No')
        txtReceipt.delete("1.0",END)
    if(nam.get()==''):
        tkinter.messagebox.showinfo("program",'Please Enter the Name')
        txtReceipt.delete("1.0",END)
    if(len(pn.get())<=9):
        tkinter.messagebox.showinfo("program",'Please Enter Correct Phone No')
        txtReceipt.delete("1.0",END)
    if(len(pn.get())>=11):
        tkinter.messagebox.showinfo("program",'Please Enter Correct Phone No')
        txtReceipt.delete("1.0",END)
    if(addr.get()==''):
        tkinter.messagebox.showinfo("program",'Please Enter the Address')
        txtReceipt.delete("1.0",END)
    code()
    root1.destroy()
    root1.mainloop()

    
def Reset ():
    PaidTax.set("")
    TotalCost.set("")
    txtReceipt.configure(state=NORMAL)
    txtReceipt.delete("1.0",END)
    txtReceipt.configure(state=DISABLED)

    E_Sprit.set("0")
    E_CocaCola.set("0")
    E_ThumsUp.set("0")
    E_GreenTea.set("0")
    E_Coffee.set("0")
    E_Lasi.set("0")
    E_Tea.set("0")
    E_IceCream.set("0")                    
    

    E_Samosa.set("0")
    E_Idli.set("0")
    E_Dosa.set("0")
    E_Jalebi.set("0")
    E_Rasgulla.set("0")
    E_ChowMein.set("0")
    E_Litti.set("0")
    E_Pizza.set("0")


    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    

    txtSprit.configure (state = DISABLED)
    txtCocaCola.configure (state = DISABLED) 
    txtThumsUp.configure (state = DISABLED)
    txtGreenTea.configure (state = DISABLED)
    txtCoffee.configure (state = DISABLED)
    txtLasi.configure (state = DISABLED)
    txtTea.configure (state = DISABLED)
    txtIceCream.configure (state = DISABLED)

    txtSamosa.configure(state = DISABLED)
    txtIdli.configure (state = DISABLED)
    txtDosa.configure (state = DISABLED)
    txtJalebi.configure(state = DISABLED)
    txtRasgulla.configure (state = DISABLED)
    txtChowMein.configure (state = DISABLED)
    txtLitti.configure (state = DISABLED)
    txtPizza.configure (state = DISABLED)

#=========================
    nam.set('')
    pn.set('')
    addr.set('')
    ra.set(random.randint(100000,9999999))
    
    
  
def CostofItem ():
    try:
        Item1 = float ( E_Sprit.get ())
    except:
        tkinter.messagebox.showinfo("program",'Please Enter the Correct amount in sprite')
    try:
        Item2 = float ( E_CocaCola.get ())
    except:
        tkinter.messagebox.showinfo("program",'Please Enter the Correct amount in CocaCola')
    try:
        Item3 = float ( E_ThumsUp.get ())
    except:
        tkinter.messagebox.showinfo("program",'Please Enter the Correct amount in ThumsUp')
    try:
        Item4 = float ( E_GreenTea.get ())
    except:
        tkinter.messagebox.showinfo("program",'Please Enter the Correct amount in Green Tea')
    try:
        Item5 = float ( E_Coffee.get ())
    except:
        tkinter.messagebox.showinfo("program",'Please Enter the Correct amount in Coffee')
    try:
        Item6 = float ( E_Lasi.get ())
    except:
        tkinter.messagebox.showinfo("program",'Please Enter the Correct amount in Lassi')
    try:
        Item7 = float ( E_Tea.get ())
    except:
        tkinter.messagebox.showinfo("program",'Please Enter the Correct amount in Tea')
    try:
        Item8 = float ( E_IceCream.get ())
    except:
        tkinter.messagebox.showinfo("program",'Please Enter the Correct amount in Ice Cream')
    try:
        Item9 = float ( E_Samosa.get ())
    except:
        tkinter.messagebox.showinfo("program",'Please Enter the Correct amount in Samosa')
    try:
        Item10 = float ( E_Idli.get ())
    except:
        tkinter.messagebox.showinfo("program",'Please Enter the Correct amount in Idli')
    try:
        Item11 = float ( E_Dosa.get ())
    except:
        tkinter.messagebox.showinfo("program",'Please Enter the Correct amount in Dosa')
    try:
        Item12 = float ( E_Jalebi.get ())
    except:
        tkinter.messagebox.showinfo("program",'Please Enter the Correct amount in Jalebi')
    try:
        Item13 = float ( E_Rasgulla.get ())
    except:
        tkinter.messagebox.showinfo("program",'Please Enter the Correct amount in Rasgulla')
    try:
        Item14 = float ( E_ChowMein.get ())
    except:
        tkinter.messagebox.showinfo("program",'Please Enter the Correct amount in ChowMein')
    try:
        Item15 = float ( E_Litti.get ())
    except:
        tkinter.messagebox.showinfo("program",'Please Enter the Correct amount in Litti')
    try:
        Item16 = float ( E_Pizza.get ())
    except:
        tkinter.messagebox.showinfo("program",'Please Enter the Correct amount in Pizza')
    try:

        PriceofDrinks = (Item1 * 10) + (Item2 * 10) + (Item3 * 10) \
                        + (Item4 * 15) + (Item5 * 10) + (Item6 * 15)\
                        + (Item7 * 10) + (Item8 * 10)

        PriceofCakes = (Item9 *5) + (Item10 * 5) + (Item11 * 20) \
                        + (Item12 * 15) + (Item13 *5) + (Item14 * 15)\
                        + (Item15 * 10) + (Item16 *100)

        TT = (float(PriceofDrinks)+ float(PriceofCakes))
        Tax=(5/100)*TT
        h='Rs.'+str(Tax)
        PaidTax.set(h)
        TC = "Rs."+str("%.2f" %( Tax + TT ))
        TotalCost.set(TC)
        enters()
    except:
        return None
def enters():
    txtReceipt.configure(state=NORMAL)
    Item1 = float ( E_Sprit.get ())
    Item2 = float ( E_CocaCola.get ())
    Item3 = float ( E_ThumsUp.get ())
    Item4 = float ( E_GreenTea.get ())
    Item5 = float ( E_Coffee.get ())
    Item6 = float ( E_Lasi.get ())
    Item7 = float ( E_Tea.get ())
    Item8 = float ( E_IceCream.get ())

    Item9 = float ( E_Samosa.get ())
    Item10 = float ( E_Idli.get ())
    Item11 = float ( E_Dosa.get ())
    Item12 = float ( E_Jalebi.get ())
    Item13 = float ( E_Rasgulla.get ())
    Item14 = float ( E_ChowMein.get ())
    Item15 = float ( E_Litti.get ())
    Item16 = float ( E_Pizza.get ())
    txtReceipt.insert(END,"Slip No:\t\t\t"+ra.get()+'\n')       
    if(nam.get()!=''):
        if(nam.get().isalpha()==True):
            txtReceipt.insert(END,'Name:\t\t\t'+nam.get()+'\n')
            
        else:
            tkinter.messagebox.showinfo("program",'Please Enter the Correct Name')
            txtReceipt.delete("1.0",END)
     
    if(pn.get()!=''):
        if(pn.get().isnumeric()==True):
            txtReceipt.insert(END,'Phone No:\t\t\t'+pn.get()+'\n')
        else:
            tkinter.messagebox.showinfo("program",'Please Enter the Correct Phone No')
            txtReceipt.delete("1.0",END)
        
    if(addr.get()!=''):
        txtReceipt.insert(END,'Address:\t\t\t'+addr.get()+'\n')
    txtReceipt.insert(END,'Date of order:\t\t\t'+DateofOrder.get()+'\n')
    txtReceipt.insert(END,'-'*55+'\n')
    if(var1.get()==1):
        txtReceipt.insert(END,'Price of Sprite:\t\t\t'+'Rs.'+str(Item1*10)+'\n')
    if(var2.get()==1):
        txtReceipt.insert(END,'Price of Coca Cola:\t\t\t'+'Rs.'+str(Item2*10)+'\n')
    if(var3.get()==1):
        txtReceipt.insert(END,'Price of Thums Up:\t\t\t'+'Rs.'+str(Item3*10)+'\n')
    if(var4.get()==1):
        txtReceipt.insert(END,'Price of Green Tea:\t\t\t'+'Rs.'+str(Item4*15)+'\n')
    if(var5.get()==1):
        txtReceipt.insert(END,'Price of Coffee:\t\t\t'+'Rs.'+str(Item5*10)+'\n')
    if(var6.get()==1):
        txtReceipt.insert(END,'Price of Lassi:\t\t\t'+'Rs.'+str(Item6*15)+'\n')
    if(var7.get()==1):
        txtReceipt.insert(END,'Price of Tea:\t\t\t'+'Rs.'+str(Item7*10)+'\n')
    if(var8.get()==1):
        txtReceipt.insert(END,'Price of Ice Cream:\t\t\t'+'Rs.'+str(Item8*10)+'\n')
    if(var9.get()==1):
        txtReceipt.insert(END,'Price of Somasa:\t\t\t'+'Rs.'+str(Item9*5)+'\n')
    if(var10.get()==1):
        txtReceipt.insert(END,'Price of Idli:\t\t\t'+'Rs.'+str(Item10*5)+'\n')
    if(var11.get()==1):
        txtReceipt.insert(END,'Price of Dosa:\t\t\t'+'Rs.'+str(Item11*20)+'\n')
    if(var12.get()==1):
        txtReceipt.insert(END,'Price of Jalebi:\t\t\t'+'Rs.'+str(Item12*15)+'\n')
    if(var13.get()==1):
        txtReceipt.insert(END,'Price of Rasgulla:\t\t\t'+'Rs.'+str(Item13*5)+'\n')
    if(var14.get()==1):
        txtReceipt.insert(END,'Price of Chow Mein:\t\t\t'+'Rs.'+str(Item14*15)+'\n')
    if(var15.get()==1):
        txtReceipt.insert(END,'Price of Litti:\t\t\t'+'Rs.'+str(Item15*10)+'\n')
    if(var16.get()==1):
        txtReceipt.insert(END,'Price of Pizza:\t\t\t'+'Rs.'+str(Item16*100)+'\n')
    txtReceipt.insert(END,'-'*55+'\n')
    txtReceipt.insert(END,'Paid Tax:\t\t\t'+PaidTax.get()+'\n')
    txtReceipt.insert(END,'Total Cost:\t\t\t'+TotalCost.get()+'\n')
    txtReceipt.insert(END,"      "+'\n')
    if(ra.get()==''):
        tkinter.messagebox.showinfo("program",'Please Enter Slip No')
        txtReceipt.delete("1.0",END)
    if(nam.get()==''):
        tkinter.messagebox.showinfo("program",'Please Enter the Name')
        txtReceipt.delete("1.0",END)
    if(len(pn.get())<=9):
        tkinter.messagebox.showinfo("program",'Please Enter Correct Phone No')
        txtReceipt.delete("1.0",END)
    if(len(pn.get())>=11):
        tkinter.messagebox.showinfo("program",'Please Enter Correct Phone No')
        txtReceipt.delete("1.0",END)
    if(addr.get()==''):
        tkinter.messagebox.showinfo("program",'Please Enter the Address')
        txtReceipt.delete("1.0",END)
    txtReceipt.configure(state=DISABLED)
    scrollbar.config(command=txtReceipt.yview)
    txtReceipt.config(yscrollcommand=scrollbar.set)
def Sprite ( ):
    if (var1.get() == 1):
        txtSprit.configure(state = NORMAL)
        txtSprit.focus ( )
        txtSprit.delete("0",END)
        E_Sprit.set(" ")
    elif (var1.get() == 0):
        txtSprit.configure(state = DISABLED)
        E_Sprit.set("0")
def Coca_Cola( ):
    if (var2.get() == 1):
        txtCocaCola.configure(state = NORMAL)
        txtCocaCola.focus ( )
        txtCocaCola.delete("0",END)
        E_CocaCola.set(" ")
    elif (var2.get() == 0):
        txtCocaCola.configure(state = DISABLED)
        E_CocaCola.set("0")
def Thums_Up( ):
    if (var3.get() == 1):
        txtThumsUp.configure(state = NORMAL)
        txtThumsUp.focus ( )
        txtThumsUp.delete("0",END)
        E_ThumsUp.set(" ")
    elif (var3.get() == 0):
        txtThumsUp.configure(state = DISABLED)
        E_ThumsUp.set("0")
def GreenTea( ):
    if (var4.get() == 1):
        txtGreenTea.configure(state = NORMAL)
        txtGreenTea.focus ( )
        txtGreenTea.delete("0",END)
        E_GreenTea.set(" ")
    elif (var4.get() == 0):
        txtGreenTea.configure(state = DISABLED)
        E_GreenTea.set("0")
def Coffee( ):
    if (var5.get() == 1):
        txtCoffee.configure(state = NORMAL)
        txtCoffee.focus ( )
        txtCoffee.delete("0",END)
        E_Coffee.set(" ")
    elif (var5.get() == 0):
        txtCoffee.configure(state = DISABLED)
        E_Coffee.set("0")
def Lasi( ):
    if (var6.get() == 1):
        txtLasi.configure(state = NORMAL)
        txtLasi.focus ( )
        txtLasi.delete("0",END)
        E_Lasi.set(" ")
    elif (var6.get() == 0):
        txtLasi.configure(state = DISABLED)
        E_Lasi.set("0")
def Tea( ):
    if (var7.get() == 1):
        txtTea.configure(state = NORMAL)
        txtTea.focus ( )
        txtTea.delete("0",END)
        E_Tea.set(" ")
    elif (var7.get() == 0):
        txtTea.configure(state = DISABLED)
        E_Tea.set("0")
def IceCream():
    if (var8.get() == 1):
        txtIceCream.configure(state = NORMAL)
        txtIceCream.focus ( )
        txtIceCream.delete("0",END)
        E_IceCream.set(" ")
    elif (var8.get() == 0):
        txtIceCream.configure(state = DISABLED)
        E_IceCream.set("0")
#food
def Samosa():
    if (var9.get() == 1):
        txtSamosa.configure(state = NORMAL)
        txtSamosa.focus ( )
        txtSamosa.delete("0",END)
        E_Samosa.set(" ")
    elif (var8.get() == 0):
        txtSamosa.configure(state = DISABLED)
        E_Samosa.set("0")
def Idli():
    if (var10.get() == 1):
        txtIdli.configure(state = NORMAL)
        txtIdli.focus ( )
        txtIdli.delete("0",END)
        E_Idli.set(" ")
    elif (var10.get() == 0):
        txtIdli.configure(state = DISABLED)
        E_Idli.set("0")
def Dosa():
    if (var11.get() == 1):
        txtDosa.configure(state = NORMAL)
        txtDosa.focus ( )
        txtDosa.delete("0",END)
        E_Dosa.set(" ")
    elif (var11.get() == 0):
        txtDosa.configure(state = DISABLED)
        E_Dosa.set("0")
def Jalebi():
    if (var12.get() == 1):
        txtJalebi.configure(state = NORMAL)
        txtJalebi.focus ( )
        txtJalebi.delete("0",END)
        E_Jalebi.set(" ")
    elif (var12.get() == 0):
        txtJalebi.configure(state = DISABLED)
        E_Jalebi.set("0")
def Rasgulla():
    if (var13.get() == 1):
        txtRasgulla.configure(state = NORMAL)
        txtRasgulla.focus ( )
        txtRasgulla.delete("0",END)
        E_Rasgulla.set(" ")
    elif (var13.get() == 0):
        txtRasgulla.configure(state = DISABLED)
        E_Rasgulla.set("0")
def ChowMein():
    if (var14.get() == 1):
        txtChowMein.configure(state = NORMAL)
        txtChowMein.focus ( )
        txtChowMein.delete("0",END)
        E_ChowMein.set(" ")
    elif (var14.get() == 0):
        txtChowMein.configure(state = DISABLED)
        E_ChowMein.set("0")
def Litti():
    if (var15.get() == 1):
        txtLitti.configure(state = NORMAL)
        txtLitti.focus ( )
        txtLitti.delete("0",END)
        E_Litti.set(" ")
    elif (var15.get() == 0):
        txtLitti.configure(state = DISABLED)
        E_Litti.set("0")
def Pizza():
    if (var16.get() == 1):
        txtPizza.configure(state = NORMAL)
        txtPizza.focus ( )
        txtPizza.delete("0",END)
        E_Pizza.set(" ")
    elif (var16.get() == 0):
        txtPizza.configure(state = DISABLED)
        E_Pizza.set("0")


lam0=Label(fm2,text='Slip No:\t\t\t',font=('arial 14 bold'),bg='Misty Rose2').pack(side=TOP,anchor='nw',fill=BOTH)
txtlam4=Entry(fm1,textvariable=ra,font=('arial 14 bold'),bd=3,width=8,state=DISABLED)
txtlam4.pack(side=TOP,anchor='ne',fill=BOTH)


lab=Label(fm2,text='Name:\t\t\t',font=('arial',14,'bold'),bg='Misty Rose2').pack(side=TOP,anchor='nw',fill=BOTH)
lab1=Label(fm2,text='Phone No:\t\t',font=('arial',14,'bold'),bg='Misty Rose2').pack(side=TOP,anchor='nw',fill=BOTH)
lab2=Label(fm2,text='Address:\t\t\t',font=('arial',14,'bold'),bg='Misty Rose2',pady=5).pack(side=TOP,anchor='nw',fill=BOTH)
txtName=Entry(fm1,font=('arial',14,'bold'),textvariable=nam,bd=3,width=13)
#txtName.grid(row=1,column=1)
txtName.pack(side=TOP,anchor='ne',fill=BOTH)
txtpno=Entry(fm1,font=('arial',14,'bold'),textvariable=pn,bd=3,width=13)
txtpno.pack(side=TOP,anchor='ne',fill=BOTH)
txtaddr=Entry(fm1,font=('arial',14,'bold'),textvariable=addr,bd=3,width=13)
txtaddr.pack(side=TOP,anchor='ne',fill=BOTH)

#txtlam4.grid(row=0,column=1)
date=Label(fm2,text='Date:\t\t\t',font=('arial 14 bold'),bg='Misty Rose2')
date.pack(side=TOP,anchor='nw',fill=X)
txtdate=Entry(fm1,textvariable=DateofOrder,font=('arial 14 bold'),justify=LEFT,state=DISABLED,
              width=10)
txtdate.pack(side=RIGHT,anchor='ne',fill=X)


#============================== Drinks Name==============================

Sprit= Checkbutton (Drinks_F, text="Sprite\t", variable= var1, onvalue= 1, offvalue= 0,
                    font=('arial', 14, 'bold'),
                    bg= 'Misty Rose2',command=Sprite).pack(side=TOP,anchor='nw',fill=BOTH)

CocaCola = Checkbutton (Drinks_F, text="Coca Cola", variable= var2, onvalue= 1,
                        offvalue= 0, font=('arial', 14, 'bold'),
                        bg= 'Misty Rose2',command=Coca_Cola).pack(side=TOP,anchor='nw',fill=BOTH)

ThumsUp= Checkbutton (Drinks_F, text="Thums Up", variable= var3, onvalue= 1,
                      offvalue= 0, font=('arial', 14, 'bold'),
                      bg= 'Misty Rose2',command=Thums_Up).pack(side=TOP,anchor='nw',fill=BOTH)

GreenTea= Checkbutton (Drinks_F, text="Green Tea", variable= var4, onvalue= 1,
                       offvalue= 0, font=('arial', 14, 'bold'),
                       bg= 'Misty Rose2',command=GreenTea).pack(side=TOP,anchor='nw',fill=BOTH)

Coffee= Checkbutton (Drinks_F, text="Coffee\t", variable= var5, onvalue= 1,
                     offvalue= 0, font=('arial', 14, 'bold'),
                     bg= 'Misty Rose2',command=Coffee).pack(side=TOP,anchor='nw',fill=BOTH)

Lasi= Checkbutton (Drinks_F, text="Lassi\t", variable= var6, onvalue= 1,
                   offvalue= 0, font=('arial', 14, 'bold'),
                   bg= 'Misty Rose2',command=Lasi).pack(side=TOP,anchor='nw',fill=BOTH)

Tea= Checkbutton (Drinks_F, text="Tea\t", variable= var7, onvalue= 1, offvalue= 0,
                  font=('arial', 14, 'bold'),bg= 'Misty Rose2',command=Tea
                  ).pack(side=TOP,anchor='nw',fill=BOTH)

IceCream= Checkbutton (Drinks_F, text="Ice Cream", variable= var8, onvalue= 1,
                       offvalue= 0, font=('arial', 14, 'bold'),
                       bg= 'Misty Rose2',command=IceCream).pack(side=TOP,anchor='nw',fill=BOTH)
#==========================================================================

#========================== Entry Box for Drinks ==========================

txtSprit = Entry (Drinks_F1, font = ('arial', 16, 'bold'), bd=4, width=6, justify = LEFT,
                  state = DISABLED, textvariable = E_Sprit)
txtSprit.pack(side=TOP,anchor='nw',fill=BOTH)

txtCocaCola = Entry (Drinks_F1, font = ('arial', 16, 'bold'), bd=4, width=6, justify = LEFT,
                     state = DISABLED, textvariable =E_CocaCola)
txtCocaCola.pack(side=TOP,anchor='nw',fill=BOTH)

txtThumsUp = Entry (Drinks_F1, font = ('arial', 16, 'bold'), bd=4, width=6, justify = LEFT,
                       state = DISABLED, textvariable = E_ThumsUp)
txtThumsUp.pack(side=TOP,anchor='nw',fill=BOTH)

txtGreenTea = Entry (Drinks_F1, font = ('arial', 16, 'bold'), bd=4, width=6, justify = LEFT,
                        state = DISABLED, textvariable = E_GreenTea)
txtGreenTea.pack(side=TOP,anchor='nw',fill=BOTH)

txtCoffee = Entry (Drinks_F1, font = ('arial', 16, 'bold'), bd=4, width=6, justify = LEFT,
                       state = DISABLED, textvariable = E_Coffee)
txtCoffee.pack(side=TOP,anchor='nw',fill=BOTH)

txtLasi = Entry (Drinks_F1, font = ('arial', 16, 'bold'), bd=4, width=6, justify = LEFT,
                           state = DISABLED, textvariable = E_Lasi)
txtLasi.pack(side=TOP,anchor='nw',fill=BOTH)

txtTea = Entry (Drinks_F1, font = ('arial', 16, 'bold'), bd=4, width=6, justify = LEFT,
                            state = DISABLED, textvariable = E_Tea )
txtTea.pack(side=TOP,anchor='nw',fill=BOTH)

txtIceCream = Entry (Drinks_F1, font = ('arial', 16, 'bold'), bd=4, width=6, justify = LEFT,
                            state = DISABLED, textvariable = E_IceCream)
txtIceCream.pack(side=TOP,anchor='nw',fill=BOTH)
#frame
p2=Frame(p1,bd=10,relief=RIDGE)
p2.pack(side=LEFT,anchor='nw',fill=BOTH)
#photo-----------
photo5=PhotoImage(file='ice.png')
photo_label5=Label(p1,image=photo5)
photo_label5.pack(side=BOTTOM,fill=BOTH)
photo6=PhotoImage(file='d.png')
photo_label6=Label(p2,image=photo6)
photo_label6.pack(side=BOTTOM,fill=BOTH)

#=============================== Cakes =================================

Samosa= Checkbutton (Cake_F, text="Samosa\t", variable= var9, onvalue= 1, offvalue= 0, font=('arial', 14, 'bold'),
                                    bg= 'Misty Rose2',command=Samosa).pack(side=TOP,anchor='nw',fill=BOTH)

Idli= Checkbutton (Cake_F, text="Idli\t", variable= var10, onvalue= 1, offvalue= 0, font=('arial', 14, 'bold'),
                                    bg= 'Misty Rose2',command=Idli).pack(side=TOP,anchor='nw',fill=BOTH)

Dosa= Checkbutton (Cake_F, text="Dosa\t", variable= var11, onvalue= 1, offvalue= 0, font=('arial', 14, 'bold'),
                                    bg= 'Misty Rose2',command=Dosa).pack(side=TOP,anchor='nw',fill=BOTH)

Jalebi= Checkbutton (Cake_F, text="Jalebi\t", variable= var12, onvalue= 1, offvalue= 0, font=('arial', 14, 'bold'),
                                    bg= 'Misty Rose2',command=Jalebi).pack(side=TOP,anchor='nw',fill=BOTH)

Rasgulla= Checkbutton (Cake_F, text="Rasgulla\t", variable= var13, onvalue= 1, offvalue= 0, font=('arial',14, 'bold'),
                                    bg= 'Misty Rose2',command=Rasgulla).pack(side=TOP,anchor='nw',fill=BOTH)

ChowMein= Checkbutton (Cake_F, text="Chow Mein", variable= var14, onvalue= 1, offvalue= 0, font=('arial',14, 'bold'),
                                    bg= 'Misty Rose2',command=ChowMein).pack(side=TOP,anchor='nw',fill=BOTH)

Litti= Checkbutton (Cake_F, text="Litti\t", variable= var15, onvalue= 1, offvalue= 0, font=('arial', 14, 'bold'),
                                    bg= 'Misty Rose2',command=Litti).pack(side=TOP,anchor='nw',fill=BOTH)

Pizza= Checkbutton (Cake_F, text="Pizza\t", variable= var16, onvalue= 1, offvalue= 0, font=('arial', 14, 'bold'),
                                    bg= 'Misty Rose2',command=Pizza).pack(side=TOP,anchor='nw',fill=BOTH)

#===========================Enter Box for Cakes===============================

txtSamosa = Entry (Cake_F1, font = ('arial', 16, 'bold'), bd=4, width=6, justify = LEFT,
                       state = DISABLED, textvariable = E_Samosa)
txtSamosa.pack(side=TOP,anchor='nw',fill=BOTH)

txtIdli = Entry (Cake_F1, font = ('arial', 16, 'bold'), bd=4, width=6, justify = LEFT,
                          state = DISABLED, textvariable = E_Idli)
txtIdli.pack(side=TOP,anchor='nw',fill=BOTH)

txtDosa = Entry (Cake_F1, font = ('arial', 16, 'bold'), bd=4, width=6, justify = LEFT,
                             state = DISABLED, textvariable = E_Dosa)
txtDosa.pack(side=TOP,anchor='nw',fill=BOTH)

txtJalebi = Entry (Cake_F1, font = ('arial', 16, 'bold'), bd=4, width=6, justify = LEFT,
                              state = DISABLED, textvariable = E_Jalebi)
txtJalebi.pack(side=TOP,anchor='nw',fill=BOTH)

txtRasgulla = Entry (Cake_F1, font = ('arial', 16, 'bold'), bd=4, width=6, justify = LEFT,
                                 state = DISABLED, textvariable = E_Rasgulla)
txtRasgulla.pack(side=TOP,anchor='nw',fill=BOTH)

txtChowMein = Entry (Cake_F1, font = ('arial', 16, 'bold'), bd=4, width=6, justify = LEFT,
                                   state = DISABLED, textvariable = E_ChowMein)
txtChowMein.pack(side=TOP,anchor='nw',fill=BOTH)

txtLitti = Entry (Cake_F1, font = ('arial', 16, 'bold'), bd=4, width=6, justify = LEFT,
                                        state = DISABLED, textvariable = E_Litti)
txtLitti.pack(side=TOP,anchor='nw',fill=BOTH)

txtPizza = Entry (Cake_F1, font = ('arial', 16, 'bold'), bd=4, width=6, justify = LEFT,
                                      state = DISABLED, textvariable = E_Pizza)
txtPizza.pack(side=TOP,anchor='nw',fill=BOTH)

#=============================Total Cost================================



#===========================Payment Information===========================

lblPaidTax = Label (Cost_F, font = ('arial',14,'bold'), text = "Paid Tax", bd = 7, bg = 'Misty Rose2', fg = 'black')
lblPaidTax.pack(side=LEFT,anchor='nw',fill=BOTH)
txtPaidTax = Entry (Cost_F, font = ('arial', 14, 'bold'), textvariable =PaidTax, bd = 7, bg = "white",
                    width =8, justify = RIGHT,state=DISABLED)
txtPaidTax.pack(side=LEFT,anchor='nw',fill=BOTH)


lblTotalCost = Label (Cost_F, font = ('arial',14,'bold'), text = "Total Cost", bd = 7, bg = 'Misty Rose2', fg = 'black')
lblTotalCost.pack(side=LEFT,anchor='ne',fill=BOTH)
txtTotalCost = Entry (Cost_F, font = ('arial', 14, 'bold'),textvariable=TotalCost, bd =7,bg="white",width=8
                         , justify = RIGHT,state=DISABLED)
txtTotalCost.pack(side=RIGHT,anchor='ne',fill=BOTH)

#==============================Receipt==================================
scrollbar=Scrollbar(Receipt_F)
scrollbar.pack(side=RIGHT,fill=Y)
txtReceipt = Text (Receipt_F, width = 35, height = 15, bg = "white", bd = 4, font = ('arial', 12, 'bold'),state=DISABLED)
txtReceipt.pack(side=TOP,anchor='ne',fill=BOTH)

#---------------------------------


#==============================Buttons===================================
photo4=PhotoImage(file='2.png')
photo_label4=Label(pho_F,image=photo4)
photo_label4.pack(side=RIGHT,fill=BOTH)

btnTotal = Button (Buttons_F, padx = 10, pady = 1, bd = 7, fg = "black", font = ('arial', 12, 'bold'), width=4, text = "Total",
                   bg = 'Green',command=CostofItem).pack(side=LEFT,anchor='sw',fill=BOTH)

btnReceipt = Button (Buttons_F, padx = 10, pady = 1, bd = 7, fg = "black", font = ('arial', 12, 'bold'), width=5, text = "Receipt",
                   bg = 'Blue',command=recipt).pack(side=LEFT,anchor='sw',fill=BOTH)

btnReset = Button (Buttons_F, padx = 10, pady = 1, bd = 7, fg = "black", font = ('arial', 12, 'bold'), width=4, text = "Reset",
                   bg = 'Yellow',command=Reset).pack(side=LEFT,anchor='sw',fill=BOTH)

btnExit = Button (Buttons_F, padx = 10, pady = 1, bd = 7, fg = "black", font = ('arial', 12, 'bold'), width=4, text = "Exit",
                   bg = 'Red',command=iExit).pack(side=LEFT,anchor='sw',fill=BOTH)
btnsearch=Button(fm_btn,bd=7,font=('arial 16 bold'),width=6,
                 bg='Yellow',text="Search Customer \nDetails",command=searche).pack(anchor='sw',fill=BOTH)
photo1=PhotoImage(file='1.png')
photo_label=Label(fm_btn,image=photo1)
photo_label.pack(side=BOTTOM,fill=BOTH)

photo2=PhotoImage(file='samosa.png')
photo_label2=Label(fm102,image=photo2)
photo_label2.pack(side=BOTTOM,fill=BOTH)
photo3=PhotoImage(file='galabi.png')
photo_label3=Label(fm102,image=photo3)
photo_label3.pack(side=BOTTOM,fill=BOTH)
photo7=PhotoImage(file='r.png')
photo_label7=Label(fm102,image=photo7)
photo_label7.pack(side=BOTTOM,fill=BOTH)


root.mainloop()


