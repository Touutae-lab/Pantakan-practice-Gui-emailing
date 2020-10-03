from tkinter import *
from tkinter.ttk import *
from sending import email_input
gui = Tk()
gui.title('Sending Email Program')
gui.geometry('300x150')

def new_gui():
    while email_input(mail.get(),pss.get()):
        login_status = True

#def popupmsg():
#    popup = Tk()
#    popup.wm_title("!")
#    label = Label(popup, text='Password is Incorrect!', font= ('Calibri', 18))
#    label.pack()
#    B1 = Button(popup, text="Okay", command=popup.destroy)
#    B1.pack()
#    popup.mainloop()

def login_status():
   A = mail.get()
   B = pss.get()
   if email_input(A, B):
       gui.quit()
gui_frame = Frame(gui)
gui2_frame = Frame(gui)
gui3_frame = Frame(gui)

usr_label = Label(gui_frame, text="Login", font = ('Calibri', 18), foreground='black')


login_label = Button(gui3_frame, text='Confirm', command= login_status)
login_label.pack(side = BOTTOM)


La1 = Label(gui2_frame, text="E-Mail").grid(row=0,padx=10,pady=10)
La2 = Label(gui2_frame, text="Password").grid(row=1,padx=10,pady=10)

mail = Entry(gui2_frame)
pss  = Entry(gui2_frame)

mail.grid(row=0, column=1, padx= 10, pady=10)
pss.grid(row=1, column=1, padx=10,pady=10)


login_label.pack()
usr_label.pack()
gui_frame.pack()
gui2_frame.pack()
gui3_frame.pack()


    

gui.mainloop()



