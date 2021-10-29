import pyautogui as pt
from time import sleep


pt.FAILSAFE = True


def nav_to_any_image(image, clicks, off_x=0, off_y=0):
    position = pt.locateCenterOnScreen(image, confidence=0.8)

    if position is None:
        print(f'{image} not found')
        return 0
    else:
        pt.moveTo(position, duration=.2)
        pt.moveRel(off_x, off_y, duration=.2)
        pt.click(clicks=clicks, interval=.1)
        return 1


def close_pycharm_open_chrome():
    nav_to_any_image('Images/minimize.png', 1)
    sleep(1)
    nav_to_any_image('Images/googleChrome.png', 2)
    sleep(1)


def check_maximize():
    nav_to_any_image('Images/maximize.png', 1)
    sleep(1)


def click_search_box_and_open_linkedin():
    nav_to_any_image('Images/reload.png', 1, 60)
    sleep(1)
    pt.typewrite('https://www.linkedin.com/login', interval=.1)
    pt.typewrite('\n')
    sleep(3)
    nav_to_any_image('Images/signIn.png', 1, 60)


def enter_credentials():
    nav_to_any_image('Images/email.png', 3, 0, 20)
    sleep(1)
    pt.typewrite('*', interval=.1)   # enter email
    nav_to_any_image('Images/logo.png', 1, 0, 70)
    nav_to_any_image('Images/password.png', 3, 0, 20)
    sleep(1)
    pt.typewrite('*', interval=.1)   # enter password
    nav_to_any_image('Images/signInButton.png', 1)


def connect():
    nav_to_any_image('Images/messageArrow.png', 1)
    nav_to_any_image('Images/myNetwork.png', 1)
    sleep(3)
    pt.press('down', presses=12)
    sleep(5)
    for i in range(12):
        nav_to_any_image('Images/connect.png', 1)
        sleep(2)
        nav_to_any_image('Images/cancel.png', 1)
        sleep(1)
        if i % 4 == 0:
            pt.press('down', presses=6)
            sleep(2)


sleep(1)
close_pycharm_open_chrome()
sleep(2)
check_maximize()
sleep(1)
click_search_box_and_open_linkedin()
sleep(5)
enter_credentials()
sleep(10)
connect()
