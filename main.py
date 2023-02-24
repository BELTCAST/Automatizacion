import pyautogui 
import time 

def spotify_likes_cleaner():

    pyautogui.hotkey("win", "r")
    time.sleep(2)
    pyautogui.write('spotify.exe')
    pyautogui.press('enter')
    time.sleep(5)
    counter = 0
    options_button = pyautogui.click(x=59,y=345, button = "right")
    delete_button = pyautogui.locateCenterOnScreen('images/spotify/delete_button.png')
    conf_button = pyautogui.locateCenterOnScreen('images/spotify/delete_conf.png')
    while counter <= 20:
        pyautogui.click(options_button)
        time.sleep(1) #Abrir seccion opciones
        pyautogui.click(delete_button)
        time.sleep(1)
        pyautogui.click(conf_button)
        counter += 1
        print(f'{counter} playlist borradas')

def messenger_marketplace_cleaner():
    pyautogui.hotkey('win', 'r')
    time.sleep(1)
    pyautogui.write('opera.exe "https://www.facebook.com/messages"')
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.click(pyautogui.locateCenterOnScreen('images/messenger/marketplace.png'))
    options = pyautogui.locateCenterOnScreen('images/messenger/options.png')
    delete_chat = pyautogui.locateCenterOnScreen('images/messenger/delete_chat.png')
    confirmation = pyautogui.locateCenterOnScreen('images/messenger/delete_confirmation.png')
    counter = 0

    while counter <= 1:
        pyautogui.moveTo(x= 333,y= 209)
        time.sleep(3)
        pyautogui.click(options)
        time.sleep(3)
        pyautogui.click(delete_chat)
        time.sleep(3)
        pyautogui.click(confirmation)
        counter += 1
    print(options)
    print(delete_chat)
    print(confirmation)


messenger_marketplace_cleaner()
