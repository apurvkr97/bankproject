from tkinter import *
import aback

def get_selected_row(event):
    global selected_tuple
    index=list1.curselection()[0]
    #list1.curselection()return which row is selected like (2,),(7,0) so {this [0]} index is used so as to  get values like 1,2,7,6
    #print(index)
    selected_tuple=list1.get(index)#gets detais of everything abt row 2nd , 5th
    #print(selected_tuple) #prints details of row selected like (1506 , 'name ', 4445 , 'city',)
    e1.delete(0,END)
    e1.insert(END,selected_tuple[0])
    e2.delete(0,END)
    e2.insert(END,selected_tuple[1])
    e3.delete(0,END)
    e3.insert(END,selected_tuple[2])
    e4.delete(0,END)
    e4.insert(END,selected_tuple[3])


def retrieve_view():
    list1.delete(0,END)
    #vv=aback.view()
    #list1.insert(END,vv) this 2 lines inserts like  in tuple in the list1(sabkuch ek line mein)
    for i in aback.view():
        list1.insert(END,i)

def add_acc():
    if accno.get()=="" or name_val.get()=="" or city.get()=="" or bal.get()=="":
        msg="ENTRIES cannot be NULL"
        list1.delete(0,END)
        list1.insert(END,msg)
    #print(type(accno.get()))
    else:
        xyz=aback.checkaccount(int(accno.get()))
        #print(xyz)
        if type(xyz)==int:
            list1.delete(0,END)
            aback.insert_value(accno.get(),name_val.get(),bal.get(),city.get())
            t=(accno.get(),name_val.get(),bal.get(),city.get())
            list1.insert(END,t)
        else:
            list1.delete(0,END)
            list1.insert(END,xyz)


def delete_acc():
    if accno.get()=="":
        msg="account no. cannot be NULL for deletion"
        list1.delete(0,END)
        list1.insert(END,msg)
    else:
        xyz=aback.checkaccount(int(accno.get()))
        #print(xyz)
        if type(xyz)==int:
            msg="NO account no :"+accno.get() +"exists in database"
            clear_all()
            list1.insert(END,msg)
        else:
            aback.delete_account(int(accno.get()))
            msg="Sucessfully deleted account no :"+accno.get()
            clear_all()
            list1.insert(END,msg)


def clear_all():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e6.delete(0,END)
    list1.delete(0,END)

def search_acc():
    list1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    result=aback.search_account(accno.get())
    #print(result)
    if (type(result)==str):
        list1.insert(END,result)
    else:
        for i in result:
            list1.insert(END,i)
            e2.insert(END,i[1])
            e3.insert(END,i[2])
            e4.insert(END,i[3])

def deposit():
    if amt.get()=="" or accno.get()=="":
        msg="Account Number or AMONUT cannot be vacant"
        list1.delete(0,END)
        list1.insert(END,msg)
    else:
        netbal=aback.deposit_money(accno.get(),amt.get())
        e5.delete(0,END)
        e6.delete(0,END)
        e6.insert(END,netbal)
        search_acc()

def withdrawal():
    if amt.get()=="" or accno.get()=="":
        msg="Account Number or AMONUT cannot be vacant"
        list1.delete(0,END)
        list1.insert(END,msg)
    else:
        msg=aback.with_money(accno.get(),amt.get())
        e5.delete(0,END)
        e6.delete(0,END)
        if type(msg)==float:
            e6.insert(END,msg)
            e3.delete(0,END)
            e3.insert(END,msg)
            search_acc()#this last step updates the list
        else:
            list1.delete(0, END)
            list1.insert(END,msg)


def transfer_amt():
    if destination_acc.get()=="" or accno.get()==""or amt.get()=="":
        msg="Source Account no./Destination Account no./ Amount cannot be vacant"
        list1.delete(0,END)
        list1.insert(END,msg)
    else:
        result1=aback.search_account(accno.get())
        result2=aback.search_account(destination_acc.get())
        if type(result1)==str or type(result2)==str:
                list1.delete(0,END)
                list1.insert(END,"Invalid source or Destination account")
        else:
            #----WITHDRAW MONEY PART--------
            msg=aback.with_money(accno.get(),amt.get())
            e6.delete(0,END)
            #print(msg)
            if type(msg)==float:
                e6.insert(END,msg)
                e3.delete(0,END)
                e3.insert(END,msg)
                #------NOW DEPOSIT MONEY PART-------
                newbal=aback.deposit_money(destination_acc.get(),amt.get())
                e5.delete(0,END)
                #===ADDING ALL IN LIST===
                #retrieve_view()
                list1.delete(0,END)
                person1=aback.search_account(accno.get())
                person2=aback.search_account(destination_acc.get())
                list1.insert(END,person1)
                list1.insert(END,person2)
            else:
                list1.delete(0, END)
                list1.insert(END,"NOT enough balance in source account")








win = Tk()
win.title('BANK MANAGEMENT SYSTEM ')

l1=Label(win,text="Account no :",width=20,height=6)
l1.grid(row=0,column=0)
accno=StringVar()
e1=Entry(win,width=20,textvariable=accno)
e1.grid(row=0,column=1)
b1=Button(win,text="Search account",width=15,command=search_acc)
b1.grid(row=0,column=2)
b6=Button(win,text="Clear",width=15,command=clear_all)
b6.grid(row=0,column=3)
b2=Button(win,text="Add account to database",width=20,command=add_acc)
b2.grid(row=0,column=4)
b7=Button(win,text="Delete account from database",width=25,command=delete_acc)
b7.grid(row=0,column=5)



l2=Label(win,text="Name",width=20)
l2.grid(row=1,column=0)
name_val=StringVar()
e2=Entry(win,width=20,textvariable=name_val)
e2.grid(row=1,column=1)
l3=Label(win,text="Balance",width=39)
l3.grid(row=1,column=4)

bal=StringVar()
e3=Entry(win,width=20,textvariable=bal)
e3.grid(row=1,column=5)

l4=Label(win,text="City",width=20,height = 8)
l4.grid(row=1,column=2)

city=StringVar()
e4=Entry(win,width=20,textvariable=city)
e4.grid(row=1,column=3)

list1=Listbox(win,width=100)
list1.grid(row=2,column=1,columnspan=4)
sb1=Scrollbar(win)
sb1.grid(row=2,column=5)
list1.bind("<<ListboxSelect>>",get_selected_row)


b5=Button(win,text="Retrieve all account",width=20,command=retrieve_view)
b5.grid(row=2,column=0)
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

l5=Label(win,text="AMOUNT",width=20,height=10)
l5.grid(row=3,column=0)
amt=StringVar()
e5=Entry(win,width=20,textvariable=amt)
e5.grid(row=3,column=1)
b8=Button(win,text="TRANSFER to account",width=20,command=transfer_amt)
b8.grid(row=3,column=3)
l7=Label(win, width=20, text="Destination account no:")
l7.grid(row=3,column=4)
destination_acc=StringVar()
e7=Entry(win,width=20,textvariable=destination_acc)
e7.grid(row=3,column=5)

b3=Button(win,text="DEPOSIT AMONUT",width=20,command=deposit)
b3.grid(row=4,column=1)
b4=Button(win,text="WITHDRAW AMOUNT",width=20,command=withdrawal)
b4.grid(row=4,column=4)



l6=Label(win,text="NET BALANCE",width=20,height=7)
l6.grid(row=5,column=2)
net_bal=StringVar()
e6=Entry(win,width=20,textvariable=net_bal)
e6.grid(row=5,column=3)

win.mainloop()
