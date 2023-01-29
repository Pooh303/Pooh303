"""EZ"""
import urllib.request
from PIL import Image
import time
import keyboard as key

def main():
  urllib.request.urlretrieve(
  'https://github.com/Pooh303/Pooh303/blob/main/IMG_0079.jpg?raw=true',
   "hey.png")
  img = Image.open("hey.png")
  while True:
    time.sleep(0)
    img.show()
    if key.is_pressed('q'):
      print("Stop doing that!")
      break

main()
