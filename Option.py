from tkinter import *

def face_window():
    root.destroy()
    import main_video

def scan_window():
    root.destroy()
    import ScanQR

root = Tk()
root.geometry('1920x1080+0+10')
root.title('Registration Form')

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
