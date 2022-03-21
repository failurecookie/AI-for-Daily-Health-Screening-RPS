print("This has edge support, chrome and other browsers may work but not supported")
import pyautogui, time

#human time to finish health screening: 20 sec
#robot time to finish health screening: 10 sec

print("declare variables")

'''
USER SUPPORT: 
To use this by yourself, please replace the firstname, lastname and email to yours!
Then, if you are using edge, everything should work!
'''

firstname = "Ethan"
lastname = "Yip"
email = "eyip28@rutgersprep.org"

def click (x,y):
    pyautogui.mouseDown(x,y)
    pyautogui.mouseUp()
def clickwrite(x,y,text):
    pyautogui.mouseDown(x,y)
    time.sleep(0.5)
    pyautogui.typewrite(text)
    time.sleep(0.5)
    pyautogui.mouseUp()

pyautogui.moveTo(1778, 11)
pyautogui.click()
print("Minimizes VSC")
pyautogui.moveTo(379,12)
pyautogui.click()
print("Opens New Tab (Edge)")
pyautogui.moveTo(407,64)
pyautogui.click()
pyautogui.typewrite('https://docs.google.com/forms/u/2/d/e/1FAIpQLSd77fD-rpiTAKHj08jlkJVZKmjg5rlHN5DGsuZRYtVtnBomHg/viewform')
pyautogui.press('enter')
time.sleep(1)
print("Opens health screening! Filling in form!")
time.sleep(1)
print("Begin Filling in the Form")
pyautogui.mouseDown(672,469)
pyautogui.click()
time.sleep(0.5)
pyautogui.typewrite(firstname)
pyautogui.mouseUp()
click(442,540)
click(624,662)
pyautogui.click()
pyautogui.typewrite(lastname)
click(521,772)
click(627,871)
pyautogui.click()
pyautogui.typewrite(email)
pyautogui.scroll(-150)
for i in range (2):
    pyautogui.moveTo(719,893)
    pyautogui.click()
    time.sleep(0.5)
click(600,900)
click(590,1000)
pyautogui.click()
time.sleep(1)
click(663,505)
time.sleep(0.1)
pyautogui.click()
click(669, 719)
pyautogui.click()
click(732,605)
time.sleep(0.1)
pyautogui.click()
time.sleep(0.6)
pyautogui.scroll(-300)
click(593,721)
pyautogui.click()
click(593, 937)
time.sleep(1)
pyautogui.scroll(-1000)
time.sleep(0.1)
click(594,160)
pyautogui.click()
click(594,384)
pyautogui.click()





