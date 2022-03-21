#this file is in development and is not finished. This however, should be, once finished, run better than the current version on Microsoft Edge.

'''
this is a version two of the automation and is currently working as the standard version. This includes bug fixes that are
patching the bugs in version 1 and will be published as an official release for standard screen laptops and will be the first public
version. Version 1 will be publicized, however will not be supported. Version 2 will not be supported on all devices either.
Use at your own risk, and thank you for downloading!
'''

import pyautogui, time

#replace this with your contact information
firstname = "Ethan"
lastname = "Yip"
email = "eyip28@rutgersprep.org"
#this is asking for how many mb is your upload!
internetspeed = 30

'''--------------------------Do not change anything past this point----------------------------'''

#calculates time to wait to adjust for internet speed
delay = internetspeed/2*internetspeed

'''
TO DO: fix the delay thingie
'''

#minimizes VSC or the application runner.
pyautogui.moveTo(1778, 11)
pyautogui.click()


#opens a new tab
pyautogui.moveTo(379,12)
pyautogui.click()

#types the url and enters it
pyautogui.moveTo(407,64)
pyautogui.click()
pyautogui.typewrite('https://docs.google.com/forms/u/2/d/e/1FAIpQLSd77fD-rpiTAKHj08jlkJVZKmjg5rlHN5DGsuZRYtVtnBomHg/viewform')
pyautogui.press('enter')

#calculates the loading time based off your average internet speed
time.sleep(delay)

#types your firstname
pyautogui.click(633,483)
pyautogui.typewrite(firstname)
time.sleep(delay)
pyautogui.click(1151,447)

#types your lastname
pyautogui.moveTo(675,664)
time.sleep(delay)
pyautogui.click()
pyautogui.typewrite(lastname)
pyautogui.click(1187,878)

#types your email
pyautogui.moveTo(600,878)
time.sleep(delay)
pyautogui.click()
pyautogui.typewrite(email)

