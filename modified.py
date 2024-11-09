import pywhatkit as kit
import pyautogui
import time

def send_whatsapp_message_continuously(phone_number, message, count, delay=2):
    kit.sendwhatmsg_instantly(phone_number, message)
    time.sleep(5) 

    for _ in range(count):
        pyautogui.typewrite(message)
        pyautogui.press('enter')
        time.sleep(delay) 

phone_number = "+923190713035"  
message = "Laiba... :)" 
count = 10  
delay = 2  

send_whatsapp_message_continuously(phone_number, message, count, delay)





