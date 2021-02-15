import pickle
from tkinter import *
from PIL import ImageTk, Image
from datetime import date
import pandas as pd



#                               D E F S





root = Tk()

root.title('')

path='/Users/jcc/CODING/PYTHON/transactions.xlsx'

my_img = ImageTk.PhotoImage(Image.open('/Users/jcc/CODING/PYTHON/pablito.png'))
my_chk_img = ImageTk.PhotoImage(Image.open('/Users/jcc/CODING/PYTHON/pablito_check.jpg'))







def delete():

    top_cl.destroy()
    df3 = pd.read_excel(path)
    df3.drop(df3.index, inplace=True)
    df3.to_excel(path, index=False)
    reset = 0
    pickle.dump(reset,open('/Users/jcc/CODING/PYTHON/bank_account.p','wb'))
    
    




# Checks input and adds to count
def finish_deposit():

    
    deposit = amount_added.get()
    

    if (deposit.isdigit()):
        Label (top_dp, text='~ ' + deposit + ' dollars have been deposited into the account.',fg='#2d5aa3', font='none 13 italic').place(x=20,y=220)

        today = date.today()
        # Updates pickle file for bank_account balance
        deposit = int(deposit)
        account_balance= pickle.load( open('/Users/jcc/CODING/PYTHON/bank_account.p','rb'))
        new_balance = account_balance + deposit
        pickle.dump(new_balance, open('/Users/jcc/CODING/PYTHON/bank_account.p','wb'))

        # Creats a DataFrame and appends values to it.
        df1= pd.read_excel(path)
        SeriesA = df1['Deposit']
        SeriesB = df1['Date']
        A = pd.Series(deposit)
        B = pd.Series(today)
        SeriesA = SeriesA.append(A)
        SeriesB = SeriesB.append(B)
        df2 = pd.DataFrame({"Deposit":SeriesA, "Date":SeriesB})
        df2.to_excel(path, index=False)
        amount_added.delete(0, END)
        
        
        
    
    # if user inputs something that doesn't have a numeric value
    else:
        Label (top_dp, text='~ Invalid entry. Please enter a number.', font='none 13 italic').place(x=20,y=220)
        return


    









# Deposit window and entry widget
def deposit_window():

    global top_dp
    global amount_added
    global my_img

    top_dp = Toplevel()
    top_dp.title('')
    my_label = Label(top_dp, image=my_img).pack()
    deposit_Mm = Button(top_dp, text='Main Menu', command=top_dp.destroy).pack()
    Label (top_dp, text="Enter amount to be deposited: ",font='none 14 ').place(x=20,y=110)

    v = StringVar()
    amount_added = Entry(top_dp, width='20', textvariable= v)
    amount_added.place(x=25,y=140)
    Button (top_dp, text='Deposit',command=finish_deposit).place(x=25,y=180)









# Check window and balance display
def check_window():


    check_df= pd.read_excel(path)


    last_transactions= []
    last_transactions.append(check_df.tail(3))
    

    global top_ch

    top_ch = Toplevel()
    top_ch.title('')

    my_label = Label(top_ch, image=my_chk_img).pack()
    btn2= Button(top_ch, text='Main Menu', command=top_ch.destroy).pack()
    balance_check = str(pickle.load(open('/Users/jcc/CODING/PYTHON/bank_account.p','rb')))

    Label (top_ch, text='Account Summary', bg='white',font='Arial 15').place(x=10,y=105)
    Label (top_ch, text="Checking - 019 ",bg='#a7a5a6',fg='white',font='Arial 15 bold').place(x=10,y=137)
    Label (top_ch, text= 'Current Balance:' ,bg='white',fg='black',font='Arial 13 italic').place(x=230,y=320)

    Label (top_ch, text= '$ ' + balance_check,bg='white',fg='black',font='Arial 13 ').place(x=340,y=320)

    if check_df.size > 0:

        for i in last_transactions:
            Label (top_ch, text= i, bg='#a7a5a6', fg='white', font='Arial 20 bold').place(x=120,y=180)


        Label (top_ch, text="   $",bg='#a7a5a6',fg='white',font='Arial 16 bold').place(x=125,y=202)
        Label (top_ch, text="   $",bg='#a7a5a6',fg='white',font='Arial 16 bold').place(x=125,y=227)
        Label (top_ch, text="   $",bg='#a7a5a6',fg='white',font='Arial 16 bold').place(x=125,y=252)


    else:
        pass

# Clear window and clear option
def clear():
    
    global top_cl

    top_cl = Toplevel()
    top_cl.title('')
    top_cl.geometry('400x100')
    Label (top_cl, text="Are you sure you want to reset the account: [019] ?").place(x=30,y=20)
    Button (top_cl, text="yes", command=delete).place(x=160,y=50)
    Button (top_cl, text="no", command=top_cl.destroy).place(x=220,y=50)







#                               M A F S





# Main menu window
main_label = Label(root, image=my_img).pack()
intro_label = Label(root, text='Welcome back Isabella. What would you like to do?',fg='black', font='Arial 14').place(x=40,y=100)
deposit_btn = Button(root, text='Deposit', command=deposit_window,height=1, width=25).place(x=80,y=150)
check_btn = Button(root, text='Check', command=check_window, height=1, width=25).place(x=80, y=180)
clear_btn = Button(root,fg='red', text='Clear', command=clear, height=1, width=5).place(x=350, y=379)



mainloop()


