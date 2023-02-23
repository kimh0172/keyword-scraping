#open default browser to google search
import webbrowser
import pyautogui
import time
#Input Google Params
keyword = input('enter your keyword\n')
url = 'https://google.com/search?q=' + keyword
webbrowser.open(url)
#search for keywords
pyautogui.click(1128,1027)
time.sleep(10)
pyautogui.hotkey('command','f')
time.sleep(2)
pyautogui.hotkey('command','a')
time.sleep(2)
pyautogui.write('vasgroup')
time.sleep(5)
def screenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save(keyword + '.png')
screenshot()
