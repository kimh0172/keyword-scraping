#open default browser to google search
import webbrowser
import pyautogui
import time
#Input Keywords and Client Website
keyword = input('Enter your keyword\n')
client_website = input('Your client website\n')
url = 'https://google.com/search?q=' + keyword
webbrowser.open(url)
#search for keywords
pyautogui.click(1128,1027)
time.sleep(10)
pyautogui.hotkey('command','f')
time.sleep(2)
pyautogui.hotkey('command','a')
time.sleep(2)
pyautogui.write(client_website)
time.sleep(5)
def screenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save(keyword + '.png')
screenshot()
