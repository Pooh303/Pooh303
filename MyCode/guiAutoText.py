import tkinter as tk
import pyautogui as auto
import time
import keyboard as key

root= tk.Tk()

canvas1 = tk.Canvas(root, width=400, height=300)
canvas1.pack()

times = tk.Entry(root)
speed = tk.Entry(root)
entry1 = tk.Entry(root)

canvas1.create_text(200, 40, text="บรรทัดที่1 จำนวนครั้งที่ต้องการให้พิมพ์")
canvas1.create_text(200, 60, text="บรรทัดที่2 ความไวในการพิมพ์เริ่มตั้งแต่ 0 = ไวสุด")
canvas1.create_text(200, 80, text="บรรทัดที่3 ข้อความที่ต้องการ(อะไรก็ได้)")
canvas1.create_text(200, 100, text='"หยุดโปรแกรมด้วยการกดปุ่ม Q ค้างไว้"')
canvas1.create_window(200, 130, window=times)
canvas1.create_window(200, 155, window=speed)
canvas1.create_window(200, 180, window=entry1)

def get_word():
    how_many = int(times.get())
    if how_many == 0:
        how_many = 1000
    y1 = int(speed.get())
    if y1 == "":
        y1 = 0
    x1 = entry1.get()
    x2 = str(x1)
    while True:
        if key.is_pressed('q'):
                break
        for _ in range(how_many):
            if key.is_pressed('q'):
                break
            auto.write(x2)
            time.sleep(y1)
            if key.is_pressed('q'):
                break
            auto.press('enter')
            time.sleep(y1)
            if key.is_pressed('q'):
                break
        if key.is_pressed('q'):
                break
        time.sleep(y1)
        if key.is_pressed('q'):
                break
        auto.hotkey('ctrl', 'a', 'backspace')
        if key.is_pressed('q'):
                break

button1 = tk.Button(text='start', command=get_word)
button2 = tk.Button(text="Quit", command=root.destroy)


canvas1.create_window(200, 210, window=button1)
canvas1.create_window(200, 240, window=button2)
root.mainloop()
