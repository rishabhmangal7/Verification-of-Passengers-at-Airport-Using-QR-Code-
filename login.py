from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import pymysql
import cv2
import numpy as np
from pyzbar.pyzbar import decode

from PIL import ImageTk, Image


def forgot_password():
    def reset():
        securityquescombo.current(0)
        newpassEntry.delete(0, END)
        answerforgotEntry.delete(0, END)
        mailentry.delete(0, END)
        passentry.delete(0, END)

    def reset_password():
        if securityquescombo.get() == 'Select' or answerforgotEntry.get() == '' or newpassEntry.get() == '':
            showerror('Error', 'All Fields Are Required', parent=root2)
        else:
            try:
                con = pymysql.connect(host='localhost', user='root', password='5540', database='loginpage')
                cur = con.cursor()
                cur.execute('select * from login where email=%s and question=%s and answer=%s',
                            (mailentry.get(), securityquescombo.get(), answerforgotEntry.get()))
                row = cur.fetchone()
                if row is None:
                    showerror('Error', 'Security Question or Answer is Incorrect\n\n\tPlease Try Again ', parent=root2)

                else:
                    cur.execute('update login set password=%s where email=%s', (newpassEntry.get(), mailentry.get()))
                    con.commit()
                    con.close()
                    showinfo('Success', 'Password is reset, please login with new password', parent=root2)
                    reset()
                    root2.destroy()


            except Exception as e:
                showerror('Error', f"Error due to: {e}", parent=root)

    if mailentry.get() == '':
        showerror('Error', 'Please enter the email address to reset your password', parent=root)
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='5540', database='loginpage')
            cur = con.cursor()
            cur.execute('select * from login where email=%s', mailentry.get())
            row = cur.fetchone()
            if row is None:
                showerror('Error', 'Please enter the valid email address', parent=root)

            else:
                con.close()
                root2 = Toplevel()
                root2.title('forgot Password')
                root2.geometry('470x560+400+60')
                root2.config(bg='white')
                root2.focus_force()
                root2.grab_set()
                forgotLabel = Label(root2, text='forgot', font=('times new roman', 22, 'bold'), fg='black', bg='white')
                forgotLabel.place(x=128, y=10)
                forgotpassLabel = Label(root2, text='Password', font=('times new roman', 22, 'bold'), fg='green',
                                        bg='white')
                forgotpassLabel.place(x=225, y=10)

                passwordimage = PhotoImage(file='resource/Images/password.png')
                forgotimageLabel = Label(root2, image=passwordimage, bg='white')
                forgotimageLabel.place(x=170, y=70)

                securityquesLabel = Label(root2, text='Security Questions', font=('times new roman', 19, 'bold'),
                                          fg='black',
                                          bg='white')
                securityquesLabel.place(x=60, y=220)
                securityquescombo = ttk.Combobox(root2, font=('times new roman', 19), state='readonly', justify=CENTER,
                                                 width=28)
                securityquescombo['values'] = (
                    'Select', 'Your First Pet Name?', 'Your Birth Place Name?', 'Your Best Friend Name?',
                    'Your Favourite Teacher?', 'Your Favourite Hobby?')
                securityquescombo.place(x=60, y=260)
                securityquescombo.current(0)

                answerforgotLabel = Label(root2, text='Answer', font=('times new roman', 19, 'bold'), fg='black',
                                          bg='white')
                answerforgotLabel.place(x=60, y=310)
                answerforgotEntry = Entry(root2, font=('times new roman', 19,), fg='black', width=30,
                                          bg='white')
                answerforgotEntry.place(x=60, y=350)

                newpassLabel = Label(root2, text='New Password', font=('times new roman', 19, 'bold'), fg='black',
                                     bg='white')
                newpassLabel.place(x=60, y=400)
                newpassEntry = Entry(root2, font=('times new roman', 19,), fg='black', width=30,
                                     bg='white')
                newpassEntry.place(x=60, y=440)

                changepassbutton = Button(root2, text='Change Password', font=('arial', 17, 'bold'), bg='green',
                                          fg='white', cursor='hand2', activebackground='green',
                                          activeforeground='white',
                                          command=reset_password)
                changepassbutton.place(x=130, y=500)

                root2.mainloop()

        except Exception as e:
            showerror('Error', f"Error due to: {e}", parent=root)


def register_window():
    root.destroy()
    import register

def chat_window():
    root.destroy()
    import chatbot

def Option_window():
    root.destroy()
    import Option

def face_window():
    root.destroy()
    import main_video

def scan_window():
    root.destroy()
    import ScanQR

def signin():
    if mailentry.get() == '' or passentry.get() == '':
        showerror('Error', 'All Fields Are Required')

    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='5540', database='loginpage')
            cur = con.cursor()
            cur.execute('select * from login where email=%s and password=%s', (mailentry.get(), passentry.get()))
            row = cur.fetchone()
            if row is None:
                showerror('error', 'Invalid Email or Password')
            else:
                root
                root.geometry('1920x1080+0+10')
                root.title('Option Window')

                bg = PhotoImage(file='resource/Images/loginbg.png')
                bgLabel = Label(root, image=bg)
                bgLabel.place(x=0, y=0)

                ScanImage = PhotoImage(file='resource/Images/Scan.png')
                scanButton = Button(root, image=ScanImage, bd=0, cursor='hand2', bg='gold', activebackground='gold',
                                    activeforeground='gold', command=scan_window)
                scanButton.place(x=200, y=180)

                FaceImage = PhotoImage(file='resource/Images/face.png')
                faceButton = Button(root, image=FaceImage, bd=0, cursor='hand2', bg='gold', activebackground='gold',
                                    activeforeground='gold', command=face_window)
                faceButton.place(x=850, y=220)

                root.mainloop()

            con.close()
        except Exception as e:
            showerror('Error', f"Error due to: {e}", parent=root)


root = Tk()
root.geometry('1920x1080+0+10')
root.title('Login Page')
bglogin = ImageTk.PhotoImage(Image.open("resource/Images/he.png"))
bgloginLabel = Label(root, image=bglogin)
bgloginLabel.place(x=0, y=0)

frame = Frame(root, width=660, height=320)
frame.place(x=500, y=200)

userimage = PhotoImage(file='resource/Images/user.png')
userimageLabel = Label(frame, image=userimage)
userimageLabel.place(x=10, y=50)
mailLabel = Label(frame, text='Email', font=('arial', 22, 'bold'), fg='black')
mailLabel.place(x=220, y=32)
mailentry = Entry(frame, font=('arial', 22,), fg='black')
mailentry.place(x=220, y=70)

passLabel = Label(frame, text='Password', font=('arial', 22, 'bold'), fg='black')
passLabel.place(x=220, y=120)
passentry = Entry(frame, font=('arial', 22,), fg='black')
passentry.place(x=220, y=160)
regbutton = Button(frame, text='Register New Account?', font=('arial', 12,), bd=0, fg='gray20',
                   cursor='hand2', command=register_window,
                   activebackground='white', activeforeground='gray20')
regbutton.place(x=220, y=200)

forgotbutton = Button(frame, text='Forgot Password?', font=('arial', 12,), bd=0, fg='red',
                      cursor='hand2', command=forgot_password,
                      activebackground='white', activeforeground='gray20')
forgotbutton.place(x=410, y=200)

loginbutton2 = Button(frame, text='Login', font=('arial', 18, 'bold'), fg='white', bg='gray20', cursor='hand2',
                      activebackground='gray20', activeforeground='white', command=signin)
loginbutton2.place(x=450, y=240)

HelpButton = Button(frame, text='Need Help?', font=('arial', 12,), bd=0, fg='gray20',
                   cursor='hand2', command=chat_window,
                   activebackground='white', activeforeground='gray20')
HelpButton.place(x=250, y=250)

root.mainloop()
