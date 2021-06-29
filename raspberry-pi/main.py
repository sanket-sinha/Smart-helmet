import tkinter as Tk
import cv2
from tkinter import ttk
from tkinter.ttk import Frame
from PIL import Image,ImageTk
import detect_vehical
import receive
import accgyro
import sendrequest
import smssend
import time
import gps

DeviceID = 'Device_01' #do not change

########################################################################
class OtherFrame(Tk.Toplevel):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self, original):
        """Constructor"""
        self.original_frame = original
        Tk.Toplevel.__init__(self)
        self.geometry("800x480")
        self.title("Rear Camera")
        self.frame = Frame(self)
        self.frame.place(x=20, y=20)
        self.lmain1 = Tk.Label(self.frame)
        self.lmain1.grid(row=0, column=0)
        btn = Tk.Button(self, text="Close",font="Times 20 bold", command=self.onClose)
        btn.place(x=350, y=350)
        #self.cap = cv2.VideoCapture('test1.mp4')
        #self.show_frame()
        """
        cv2image = cv2.imread('qr.jpg', 1)
        img = Image.fromarray(cv2image).resize((1200, 600))
        imgtk = ImageTk.PhotoImage(image = img)
        self.lmain1.imgtk = imgtk
        self.lmain1.configure(image=imgtk)
        print("a")
        """
 
        
 
    #----------------------------------------------------------------------
    def onClose(self):
        """"""
        self.destroy()
        self.original_frame.show()
    
    
    #----------------------------------------------------------------------
    def show_frame(self):
        ret, Frame = self.cap.read()
        #cv2image = detect_vehical.detect_vehical(Frame)
        cv2image = cv2.cvtColor(Frame, cv2.COLOR_BGR2RGBA)
        #show(cv2image)
        #lmain.after(10, show_frame)
        img = Image.fromarray(cv2image).resize((320, 240))
        imgtk = ImageTk.PhotoImage(image = img)
        self.lmain1.imgtk = imgtk
        self.lmain1.configure(image=imgtk)
        self.lmain1.after(10, self.show_frame)
        #print("s")
 
########################################################################
class MyApp(object):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        self.root = parent
        self.root.title("Main frame")
        self.frame = Frame(parent)
        self.frame.place(x=20, y=40)
        self.text=Tk.Label(self.frame, text="Smart Helmet with Quick Ambulance Support Project\n",
                           justify=Tk.CENTER,
                           font="Times 20 bold",
                           padx=30)
        self.text.pack(side="top")
        self.lmain = Tk.Label(self.frame,justify=Tk.CENTER)
        self.lmain.pack()
        cv2image = cv2.imread('Device-01.png', 1)
        img = Image.fromarray(cv2image).resize((200, 200))
        imgtk = ImageTk.PhotoImage(image = img)
        self.lmain.imgtk = imgtk
        self.lmain.configure(image=imgtk)
        closeButton = Tk.Button(self.frame, text = "CLOSE", width = 20, height= 1)
        closeButton.configure(command= lambda: parent.destroy())              
        closeButton.pack()

        videoButton = Tk.Button(self.frame, text = "Rear camera", width = 20, height= 1)
        videoButton.configure(command=self.openFrame)      
        videoButton.pack()
        
        resetButton = Tk.Button(self.frame, text = "Cancel Request", width = 20, height= 1)
        resetButton.configure(command=self.status=False)      
        resetButton.pack()
        self.G=accgyro.calibrate()
        self.Gx=self.G['x']
        self.Gy=self.G['y']
        self.Gz=self.G['z']
        a=15
        self.Px=self.Gx+a
        self.Py=self.Gy+a
        self.Pz=self.Gz+a
        self.Nx=self.Gx-a
        self.Ny=self.Gy-a
        self.Nz=self.Gz-a

        helpnumber = sendrequest.helpnumber(DeviceID)
        self.number = "91"+str(helpnumber)
        ishelmetwear = receive.status()
        
        if not ishelmetwear:
            print('wear helmet')
        self.checkstatus()
            #block egnition first time code is not not ready
        #self.cap = cv2.VideoCapture(0)
        #self.show_frame()
 
        #btn = Tk.Button(parent, text="Open Frame", command=self.openFrame)
        #btn.place(x=300,y=430)
       

        #videoButton = Tk.Button(parent, text = "Video", width = 20, height= 1)
        #videoButton.configure(command=video)   
        #videoButton.place(x=100,y=430) 

 
    #----------------------------------------------------------------------
    def hide(self):
        """"""
        self.root.withdraw()
 
    #----------------------------------------------------------------------
    def openFrame(self):
        """"""
        self.hide()
        subFrame = OtherFrame(self)
 
    #----------------------------------------------------------------------
    def show(self):
        """"""
        self.root.update()
        self.root.deiconify()
        
    
    #----------------------------------------------------------------------
    def checkstatus(self):
        """"""
        
        status=accgyro.status(self.Px,self.Py,self.Pz,self.Nx,self.Ny,self.Nz)
        if status:
            print('accident')
            lat = float(gps.getlat())
            lon = float(gps.getlon())
            time.sleep(2)
            sendrequest.sendrequest(lat, lon, DeviceID)
            location = "I got an accident help me. My location is: http://maps.google.com/?q=" +str(lat)+","+str(lon)
            print(location)
            resp = smssend.sendSMS(self.number, location)
            print(resp)
            print('message send')
            root.destroy()
        #time.sleep(0.5)
        self.lmain.after(10,self.checkstatus)
        
    """
    #----------------------------------------------------------------------
    def show_frame(self):
        ret, Frame = self.cap.read()
        cv2image = detect_vehical.detect_vehical(Frame)
        cv2image = cv2.cvtColor(cv2image, cv2.COLOR_BGR2RGBA)
        #show(cv2image)
        #lmain.after(10, show_frame)
        img = Image.fromarray(cv2image).resize((1200, 600))
        imgtk = ImageTk.PhotoImage(image = img)
        self.lmain.imgtk = imgtk
        self.lmain.configure(image=imgtk)
        self.lmain.after(10, self.show_frame)
        print("s")
        """
 
#----------------------------------------------------------------------
if __name__ == "__main__":
    root = Tk.Tk()
    root.geometry("800x480")
    app = MyApp(root)
    root.mainloop()
    print("exit")
