import webbrowser
import pyautogui
import time
# creating an empty list
# number of elements as input
input_string = input("Enter your keyword, separated by comma ")
list  = input_string.split(",")
client_website = input('Your client website\n')
pyautogui.click(1128,1027)
# loop to perform scraping and screenshot
for keyword in list:
    url = 'https://google.com/search?q=' + keyword
    webbrowser.open_new_tab(url)
    #search for keywords
    time.sleep(10)
    pyautogui.hotkey('command','f')
    time.sleep(2)
    pyautogui.hotkey('command','a')
    time.sleep(2)
    pyautogui.write(client_website)
    time.sleep(10)
    def screenshot():
        screenshot = pyautogui.screenshot()
        screenshot.save(keyword + '.png')
    screenshot()
