import time, pyautogui
import PySimpleGUI as sg
import multiprocessing


def KeepUI():
    
    sg.theme('Dark Blue 3')
    layout = [
        [sg.Text('\n\nKeep-Me-Up is now running.\n\n Leave This Pc to Me i wil Take Care of It from Now\n\n')]
    ]
    window = sg.Window('Keep-Me-Up', layout,size=(500,200), icon="https://cdn.discordapp.com/attachments/970350017074327603/991023150605148180/loading.jpg")
    
    p2 = multiprocessing.Process(target = dontsleep)
    p2.start()
    
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
            if p2.is_alive(): 
                p2.terminate()
            break

def dontsleep():
    while True:
        pyautogui.press('volumedown')
        time.sleep(2)
        pyautogui.press('volumeup')
        time.sleep(40)



if __name__ == '__main__':
    p1 = multiprocessing.Process(target = KeepUI)
    p1.start()
