import pyautogui 
import time 

def spotify_likes_cleaner():

    pyautogui.hotkey("win", "r")
    time.sleep(2)
    pyautogui.write('spotify.exe')
    pyautogui.press('enter')
    time.sleep(5)
    biblioteca = pyautogui.locateOnScreen("C:\Users\okins\Documents\Coding\Automatizacion\images\biblioteca_spotify.png")
    time.sleep(2)
    print(biblioteca)



spotify_likes_cleaner()


5
