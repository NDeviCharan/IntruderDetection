from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import ast
import cv2
import numpy as np
import datetime
from imutils.video import VideoStream
from imutils.video import FPS
import argparse
import imutils
import time
import cv2

protopath =  "MobileNetSSD_deploy.prototxt.txt"
modelpath =  "MobileNetSSD_deploy.caffemodel"

w=Tk()
w.geometry('925x500')
w.title('Login')
w.configure(bg='#ff4f5a')
w.minsize(925,500)



def signin():
    signin_win=Frame(w,width=925,height=500,bg='white')
    signin_win.place(x=0,y=0)
    f1=Frame(signin_win,width=350,height=350,bg='white')
    f1.place(x=480,y=100)
    
    global img1
    img1 = ImageTk.PhotoImage(Image.open("signin.png"))
    Label(signin_win,image=img1,border=0,bg='white').place(x=50,y=50)

    l2=Label(signin_win,text="Sign in",fg='#ff4f5a',bg='white')
    l2.config(font=('Microsoft YaHei UI Light',23, 'bold'))
    l2.place(x=600,y=60)

    def on_enter(e):
        e1.delete(0,'end')    
    def on_leave(e):
        if e1.get()=='':   
            e1.insert(0,'Username')

    
    e1 =Entry(f1,width=25,fg='black',border=0,bg='white')
    e1.config(font=('Microsoft YaHei UI Light',11, ))
    e1.bind("<FocusIn>", on_enter)
    e1.bind("<FocusOut>", on_leave)
    e1.insert(0,'Username')
    e1.place(x=30,y=60)

    Frame(f1,width=295,height=2,bg='black').place(x=25,y=87)

    #------------------------------------------------------

    def on_enter(e):
        e2.delete(0,'end')    
    def on_leave(e):
        if e2.get()=='':   
            e2.insert(0,'Password')

    
    e2 =Entry(f1,width=21,fg='black',border=0,bg='white')
    e2.config(font=('Microsoft YaHei UI Light',11, ))
    e2.bind("<FocusIn>", on_enter)
    e2.bind("<FocusOut>", on_leave)
    e2.insert(0,'Password')
    e2.place(x=30,y=130)

    Frame(f1,width=295,height=2,bg='black').place(x=25,y=157)

    #-mech------------------------------------------------
    def signin_cmd():
        
        file=open('datasheet.txt','r')
        d=file.read()
        r=ast.literal_eval(d)
        file.close()
        

        key=e1.get()
        value=e2.get()
        
        if key in r.keys() and value==r[key]:           
            messagebox.showinfo("","     successfully logged in    ")
            w.destroy()
            pd = CropImg("Intrusion Area")
            pd.run()  

        
        else:
            messagebox.showwarning('try again', 'invalid username or password')


    #------------------------------------------------------
    Button(f1,width=39,pady=7,text='Sign in',bg='#ff4f5a',fg='white',border=0,command=signin_cmd).place(x=35,y=204)
    l1=Label(f1,text="Don't have an account?",fg="black",bg='white')
    l1.config(font=('Microsoft YaHei UI Light',9, ))
    l1.place(x=75,y=250)

    b2=Button(f1,width=6,text='Sign up',border=0,bg='white',fg='#ff4f5a',command=signup)
    b2.place(x=215,y=250)




def signup():
    signup_win=Frame(w,width=925,height=500,bg='white')
    signup_win.place(x=0,y=0)
    f1=Frame(signup_win,width=350,height=350,bg='white')
    f1.place(x=480,y=70)

    
    global img2
    img2 = ImageTk.PhotoImage(Image.open("signup.png"))
    Label(signup_win,image=img2,border=0,bg='white').place(x=30,y=90)

    l2=Label(signup_win,text="Sign up",fg='#ff4f5a',bg='white')
    l2.config(font=('Microsoft YaHei UI Light',23, 'bold'))
    l2.place(x=600,y=60)

    def on_enter(e):
        e1.delete(0,'end')    
    def on_leave(e):
        if e1.get()=='':   
            e1.insert(0,'Username')

    
    e1 =Entry(f1,width=25,fg='black',border=0,bg='white')
    e1.config(font=('Microsoft YaHei UI Light',11, ))
    e1.bind("<FocusIn>", on_enter)
    e1.bind("<FocusOut>", on_leave)
    e1.insert(0,'Username')
    e1.place(x=30,y=60)

    Frame(f1,width=295,height=2,bg='black').place(x=25,y=87)

    #------------------------------------------------------

    def on_enter(e):
        e2.delete(0,'end')    
    def on_leave(e):
        if e2.get()=='':   
            e2.insert(0,'Password')

    
    e2 =Entry(f1,width=21,fg='black',border=0,bg='white')
    e2.config(font=('Microsoft YaHei UI Light',11, ))
    e2.bind("<FocusIn>", on_enter)
    e2.bind("<FocusOut>", on_leave)
    e2.insert(0,'Password')
    e2.place(x=30,y=130)

    Frame(f1,width=295,height=2,bg='black').place(x=25,y=157)

    def on_enter(e):
        e3.delete(0,'end')    
    def on_leave(e):
        if e3.get()=='':   
            e3.insert(0,'Confirm Password')

    
    e3 =Entry(f1,width=21,fg='black',border=0,bg='white')
    e3.config(font=('Microsoft YaHei UI Light',11, ))
    e3.bind("<FocusIn>", on_enter)
    e3.bind("<FocusOut>", on_leave)
    e3.insert(0,'Confirm Password')
    e3.place(x=30,y=130+70)

    Frame(f1,width=295,height=2,bg='black').place(x=25,y=157+70)    

    
    #Mechenism------------------------------------------------
    
    def signup_cmd():
        key=e1.get()
        value=e2.get()
        value2=e3.get()
        
        if value==value2:
            file=open('datasheet.txt','r+')
            d=file.read()
            r=ast.literal_eval(d)
            print(r)
            

            dict2={key:value}
            print(dict2)
            r.update(dict2)
            print(r)
            file.truncate(0)
            file.close()
            print(r)
            file=open('datasheet.txt','w')
            w=file.write(str(r))
             
            messagebox.showinfo("","     successfully signed up     ")
            
        else:
            messagebox.showwarning('try again', 'password should match ')


    #-------------------------------------------------------
    Button(f1,width=39,pady=7,text='Sign up',bg='#ff4f5a',fg='white',border=0,command=signup_cmd).place(x=35,y=204+60)
    l1=Label(f1,text="Already have an account?",fg="black",bg='white')
    l1.config(font=('Microsoft YaHei UI Light',9, ))
    l1.place(x=70,y=250+63)

    b2=Button(f1,width=6,text='Sign in',border=0,bg='white',fg='#ff4f5a',command=signin)
    b2.place(x=210,y=250+63)
    
def detect(image,frame1):
    ap = argparse.ArgumentParser()
    ap.add_argument("-p", "--prototxt", required=False,
        help="path to Caffe 'deploy' prototxt file")
    ap.add_argument("-m", "--model", required=False,
        help="path to Caffe pre-trained model")
    ap.add_argument("-c", "--confidence", type=float, default=0.2,
        help="minimum probability to filter weak detections")
    args = vars(ap.parse_args())
    

    # initialize the list of class labels MobileNet SSD was trained to
    # detect, then generate a set of bounding box colors for each class
    CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
	"bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
	"dog", "horse", "motorbike", "person", "pottedplant", "sheep",
	"sofa", "train", "tvmonitor"]
    COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))
    
    # load our serialized model from disk
    net = cv2.dnn.readNetFromCaffe(prototxt = protopath, caffeModel = modelpath)

    success=True
    frame = image
    (h, w) = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)),
        0.007843, (300, 300), 127.5)

    # pass the blob through the network and obtain the detections and predictions
    net.setInput(blob)
    detections = net.forward()
		# loop over the detections
    for i in np.arange(0, detections.shape[2]):
		# extract the confidence (i.e., probability) associated with the prediction
        confidence = detections[0, 0, i, 2];
        if confidence > args["confidence"]:
            idx=int(detections[0, 0, i, 1]);
            if(idx==15):
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX,startY, endX, endY) = box.astype("int")
                label="{}:{:.2f}%".format(CLASSES[idx],confidence * 100)
                cv2.rectangle(frame, (startX, startY), (endX, endY),COLORS[idx], 2)
                y=startY - 15 if startY - 15 > 15 else startY + 15
                cv2.putText(frame, label, (startX, y),cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 2)
			
    cv2.imshow(frame1,frame)



class CropImg(object):
    def __init__(self, window_name):
        self.window_name = window_name # Name for our window
        self.points = [] # List of points defining our polygon
        self.done = False

    def on_mouse(self, event, x, y, buttons, user_param):
        # Mouse callback that gets called for every mouse event (i.e. moving, clicking, etc.)
        if self.done==True:
            return
        if event == cv2.EVENT_RBUTTONDOWN:
            # right click means adding a point at current position to the list of points
            self.points.append([x, y]);


    def run(self):
        # Let's create our working window and set a mouse callback to handle events
        vs=cv2.VideoCapture(0)#start the webcam
        fps_start_time = datetime.datetime.now()
        fps = 0
        total_frames = 0
        cv2.namedWindow(self.window_name)
        success,image = vs.read()
        cv2.imshow(self.window_name,image)
        cv2.waitKey(1)
        cv2.setMouseCallback(self.window_name, self.on_mouse)
        cropped_image=None

        while(not self.done):
            success,image = vs.read()
            current_time = datetime.datetime.now().strftime("%A, %I:%M:%S %p %d %B %Y")
            cv2.putText(image, current_time, (110, 20), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 1)
            
            
            if (len(self.points) > 0):
                for i in range(len(self.points)):
                    cv2.circle(image,(self.points[i]),5,(0,255,130),2);
            cv2.imshow(self.window_name, image)
            if cv2.waitKey(50) == 13:
                self.done = True
            
            total_frames=total_frames+1;
            fps_end_time = datetime.datetime.now()
            time_diff = fps_end_time - fps_start_time
            if time_diff.seconds == 0:
                fps = 0.0
            else:
                fps = (total_frames / time_diff.seconds)
            fps_text = "FPS: {:.2f}".format(fps)
            cv2.putText(image, fps_text, (5, 30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 1)
            
        while True:
            total_frames = total_frames + 1
            fps_end_time = datetime.datetime.now()
            time_diff = fps_end_time - fps_start_time
            if time_diff.seconds == 0:
                fps = 0.0
            else:
                fps = (total_frames / time_diff.seconds)
            fps_text = "FPS: {:.2f}".format(fps)
            success,image=vs.read()
            stencil = np.zeros(image.shape).astype(image.dtype)
            cv2.fillPoly(stencil, [np.array(self.points)], (255,255,255))
            cropped_image= cv2.bitwise_and(image, stencil)        
            cv2.putText(cropped_image, fps_text, (5, 30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 1)
            detect(cropped_image,self.window_name) 
            if cv2.waitKey(50) == 27: # ESC hit
                break

        cv2.waitKey()
        cv2.destroyWindow(self.window_name);
        
if __name__ == "__main__":
    signin() #default screen
    w.mainloop()
   
        
    
    

    
