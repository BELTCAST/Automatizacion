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


#Borrador de chats de messenger
#Iconos

def run():
    user = int(input('cuantas conversaciones deseas eliminar?:'))
    deleted_chats = 0
    # # pyautogui.hotkey('win')
    # # time.sleep(1)
    # # pyautogui.write('messenger')
    # # pyautogui.press('enter')
    # # time.sleep(2)
    # # marketplace = pyautogui.locateCenterOnScreen('images/messenger/marketplace.png')
    # # time.sleep(2)
    # # pyautogui.click(marketplace)
    # # time.sleep(2)

    while deleted_chats <= user:
        pyautogui.rightClick(x=270, y=310)
        time.sleep(1)
        pyautogui.doubleClick(x=385, y=247)
        time.sleep(1)
        pyautogui.click(x=596, y=415)
        deleted_chats += 1
        print(f'chats eliminados :{deleted_chats} ')
    
if __name__ == '__main__':
    run()