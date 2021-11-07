
import win32clipboard
import os
import time
import pyautogui as pag
DELAY = 0.45


def getCopied():
    # delay is required as a measure to prevent `ctrl + x` mixing with the hotkey entered
    time.sleep(DELAY)

    win32clipboard.OpenClipboard()
    try:
        # getting current data for resetting clipboard later
        prevClip = win32clipboard.GetClipboardData()
    except TypeError:
        win32clipboard.SetClipboardData(win32clipboard.CF_UNICODETEXT, " ")
    win32clipboard.CloseClipboard()

    # get currently selected text
    pag.hotkey("ctrl", "x")
    time.sleep(0.3)

    # get clipboard data
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()

    # resetting clipboard data to previous content
    try:
        win32clipboard.SetClipboardData(
            win32clipboard.CF_UNICODETEXT, prevClip)
    except:
        print("line 36: prevClip set error")

    win32clipboard.CloseClipboard()
    return data


def findImage(imageUrl: str, confidence: int = 0.90):
    while True:
        try:
            x, y = pag.locateCenterOnScreen(
                f"{imageUrl}", confidence=confidence, grayscale=True)
        except TypeError:
            continue
        break

    return (x, y)


def findImageTimeout(imageUrl: str, timeout: int = 60 * 15, confidence: int = 0.90):
    i = 1
    while True:
        if i <= timeout:
            try:
                x, y = pag.locateCenterOnScreen(
                    f"{imageUrl}", confidence=confidence)
            except TypeError:
                i += 1
                continue
            break
        else:
            return (-1, -1)

    return (x, y)


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def writeToFile(fileName, openMode, data, alternateOpenMode):
    try:
        with open(fileName, openMode) as f:
            f.write(data)
    except FileNotFoundError:
        with open(fileName, alternateOpenMode) as f:
            f.write(data)
