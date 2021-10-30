import pyautogui as pag
import time
import win32clipboard
import os
import cursor

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


def findImageTimeout(imageUrl: str, timeout: int = 60, confidence: int = 0.90):
    i = 1
    while True:
        if i <= timeout:
            try:
                x, y = pag.locateCenterOnScreen(
                    f"{imageUrl}", confidence=confidence)
            except TypeError:
                time.sleep(1)
                i += 1
                continue
            break
        else:
            return (-1, -1)

    return (x, y)


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


cursor.hide()
time.sleep(3)
pag.PAUSE = 0.3
pag.press("winleft")
pag.write("edge")
pag.press("enter")
time.sleep(3)
totalSeconds = 0
count = 0

while True:
    t1 = time.time()
    x, y = findImageTimeout("./images/reload.png")
    pag.click(x + 100, y)
    pag.write("meet.google.com", interval=0)
    pag.press("enter")

    pag.click(findImageTimeout("./images/newMeeting.png"))
    pag.click(findImageTimeout("./images/plus.png"))
    x1, y1 = findImageTimeout("./images/recording.png")
    x, y = findImageTimeout("./images/reload.png")
    pag.click(x + 100, y)
    link = getCopied()

    if len(link) == 36:
        with open("./out/allLinks.txt", "a+") as file:
            file.write(f"{link}\n")

        totalSeconds += round(time.time() - t1, 3)
        count += 1

        summary = f"""
    Latest link: {link[-12:]}
    Latest time for a link: {round(time.time() - t1, 3)}s

    Links processed this session: {count} links
    Current session duration: {round(totalSeconds, 3)}s
    Average time per link: {round(totalSeconds/count, 3)}s
    """
        clear()
        print(summary)
