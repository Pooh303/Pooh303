import pyautogui as auto
import time
import keyboard

text = input("Enter your text : ")
while True:
    auto.write(text)
    auto.press('enter')
    time.sleep(2)

    if keyboard.is_pressed('q'):  # if key 'q' is pressed 
        print("finish the loop!")
        break  # finishing the loop
    else:
        print("Hold 'q' to stop the loop")
