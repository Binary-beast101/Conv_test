from smbus import SMBus
from tkinter import *
import tkinter
import tkinter.font as tkFont
from PIL import ImageTk,Image
import serial


ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
ser.flush()


window = tkinter.Tk()
window.geometry("800x480")
#window.resizable(0,0)
window.title("Next Health Bed Functions")
window.configure(background="white")

#creating frames fo transfers
top_frame = tkinter.Frame(window,width=800,height=120)
top_frame.pack(side=TOP)

#creating frames for bed functions
btn_frame=tkinter.Frame(window,width=800,height=360, bg="white")
btn_frame.pack()

#function definations
def stop_motor():
    ser.write(b"stop\n")
    
def head_slide_up():
    ser.write(b"HeadConvClk\n")

def head_slide_down():
    ser.write(b"HeadConvAntiClk\n")

def feet_slide_up():
    ser.write(b"FootConvClk\n")
    
def feet_slide_down():
    ser.write(b"FootConvAntiClk\n")

def head_incline_up():
    ser.write(b"stop\n")

def head_incline_down():
    ser.write(b"stop\n")

def feet_incline_up():
    ser.write(b"stop\n")

def feet_incline_down():
    ser.write(b"stop\n")

def raise_bed():
    ser.write(b"stop\n")
    
def lower_bed():
    ser.write(b"stop\n")

def slide_actuator_left():
    ser.write(b"stop\n")

def slide_actuator_right():
    ser.write(b"stop\n")

def rotate_actuator_CW():
    ser.write(b"stop\n")

def rotate_actuator_CCW():
    ser.write(b"stop\n")
    
def two_motors_CW():
    ser.write(b"BothConvClk\n")
    
def two_motors_CCW():
    ser.write(b"BothConvAntiClk\n")
    

#top frame
transfer_in_butn=tkinter.Button(top_frame, text="Transfer INTO Bed",width=41, height=3,bg="green",fg="white", font="Ariel 10 bold").grid(row=0,column=0,padx=1,pady=1)
transfer_out_butn=tkinter.Button(top_frame, text="Transfer OUT of Bed",width=41, height=3,bg="blue", fg="white",font="Ariel 10 bold").grid(row=0,column=1,padx=1,pady=1)

#images
#icon = tkinter.PhotoImage(file="/home/pi/Desktop/Shantanu_GUI/HERL_logo.png")
#icon=icon.resize((80,45),Image.ANTIALIAS)

#ROW1
Head_con_up=tkinter.Button(btn_frame, text="Head slide UP",font="Ariel 12",width=15,height=2,bg="cyan3",command= head_slide_up).grid(row=0,column=0,padx=5,pady=5)
Head_con_down=tkinter.Button(btn_frame, text="Head slide Down", font="Ariel 12",width= 15,height=2,bg="cyan3", command=head_slide_down).grid(row=0,column=1,padx=5,pady=5)

space1=tkinter.Label(btn_frame, text="",font="Ariel 12",width=5,height=2,bg="white").grid(row=0,column=2,padx=5,pady=5)

Head_act_up=tkinter.Button(btn_frame, text="Head incline UP",font="Ariel 12",width=15,height=2,bg="LightPink2",command = head_incline_up).grid(row=0,column=3,padx=5,pady=5)
Head_act_down=tkinter.Button(btn_frame, text="Head inlcine Down", font="Ariel 12",width= 15,height=2,bg="LightPink2", command= head_incline_down).grid(row=0,column=4,padx=5,pady=5)
#Row2
Foot_con_up=tkinter.Button(btn_frame, text="Feet slide UP",font="Ariel 12",width=15,height=2,bg="SlateBlue2", command= feet_slide_up).grid(row=1,column=0,padx=5,pady=5)
Foot_con_down=tkinter.Button(btn_frame, text="Feet slide Down", font="Ariel 12",width= 15,height=2,bg="SlateBlue2", command= feet_slide_down).grid(row=1,column=1,padx=5,pady=5)

space2=tkinter.Label(btn_frame, text="",font="Ariel 12",width=5,height=2,bg="white").grid(row=1,column=2,padx=5,pady=5)

Foot_act_up2=tkinter.Button(btn_frame, text="Feet incline UP",font="Ariel 12",width=15,height=2,bg="Orchid1", command= feet_incline_up).grid(row=1,column=3,padx=5,pady=5)
Foot_act_down2=tkinter.Button(btn_frame, text="Feet incline Down", font="Ariel 12",width= 15,height=2,bg="Orchid2",command=feet_incline_down).grid(row=1,column=4,padx=5,pady=5)

#ROW3
Lift_act_up=tkinter.Button(btn_frame, text="Raise Bed",font="Ariel 12",width=15,height=2,bg="SeaGreen1",command= raise_bed).grid(row=2,column=0,padx=5,pady=5)
Lift_act_down=tkinter.Button(btn_frame, text="Lower Bed", font="Ariel 12",width= 15,height=2,bg="SeaGreen1", command= lower_bed).grid(row=2,column=1,padx=5,pady=5)

space3=tkinter.Label(btn_frame, text="",font="Ariel 12",width=5,height=2,bg="white").grid(row=2,column=2,padx=5,pady=5)

Slide_act_L=tkinter.Button(btn_frame, text="Slide Actuator Left",font="Ariel 12",width=15,height=2,bg="Yellow2", command=slide_actuator_left).grid(row=2,column=3,padx=5,pady=5)
Slide_act_R=tkinter.Button(btn_frame, text="Slide Actuator Right", font="Ariel 12",width= 15,height=2,bg="Yellow2",command=slide_actuator_right).grid(row=2,column=4,padx=5,pady=5)

#ROW4
Rot_act_Clk=tkinter.Button(btn_frame, text="Rotate CW",font="Ariel 12",width=15,height=2,bg="aquamarine2", command= rotate_actuator_CW).grid(row=3,column=0,padx=5,pady=5)
Rot_act_anti=tkinter.Button(btn_frame, text="Rotate CCW", font="Ariel 12",width= 15,height=2,bg="aquamarine2", command= rotate_actuator_CCW).grid(row=3,column=1,padx=5,pady=5)

space3=tkinter.Label(btn_frame, text="",font="Ariel 12",width=5,height=2,bg="white").grid(row=3,column=2,padx=5,pady=5)

Two_motors_Clk=tkinter.Button(btn_frame, text="2 Conveyers Clk",font="Ariel 12",width=15,height=2,bg="aquamarine2", command= two_motors_CW).grid(row=4,column=0,padx=5,pady=5)
Two_motors_anti=tkinter.Button(btn_frame, text="2 Conveyers CCK",font="Ariel 12",width=15,height=2,bg="aquamarine2", command= two_motors_CCW).grid(row=4,column=1,padx=5,pady=5)

mainloop()
