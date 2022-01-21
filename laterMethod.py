import pyautogui as pag
import time
from datetime import datetime
import pyperclip
from helpers import clear, findImageTimeout, findImage

pag.PAUSE, totalSeconds, count, timePerLink = 0, 0, 0, 0
# count = 0
# timePerLink = 0
least = 10

while True:
    # starting timer for link generation
    t1 = time.time()

    if count == 0:
        x1, y1 = findImageTimeout("./images/newMeeting.png", grayscale=True)
        pag.moveTo(x1, y1, duration=0.2, tween=pag.easeInElastic)
        pag.doubleClick(x1, y1)
    else:
        pag.moveTo(x1, y1, duration=0.2, tween=pag.easeInElastic)
        pag.doubleClick()
        # pag.press("enter", presses=2)
        # pag.press("tab", presses=1)
        # pag.hotkey("shift", "tab")
        # pag.press("tab", presses=7)

    # creating a new meeting
    # pag.doubleClick(findImageTimeout(
    #     "./images/newMeeting.png", grayscale=False))
    # pag.click(findImageTimeout("./images/link.png"))

    # if findImage("./images/couldntGet.png") != (-1, -1):
    #     # exists
    #     pag.click(x, y)
    #     continue

    # time.sleep(0.5)
    # Point(x=802, y=562)
    # Point(x=1155, y=613)
    link = pyperclip.paste()
    if len(link) == 36:
        with open("./out/allLinks.txt", "a+") as f:
            f.write(f"{link}\n")

    tToLoad = time.time()

    while True:
        try:
            copyX, copyY = pag.center(pag.locate("./images/copy.png", pag.screenshot(
                region=(802, 562, 353, 50)), confidence=0.9, grayscale=True))
            print(copyX, copyY)
            break
        except TypeError:
            continue

    tLoading = time.time() - tToLoad
    pag.click(copyX + 802, copyY + 562)

    # pag.click(findImageTimeout("./images/copy.png"))

    if count == 0:
        x, y = findImageTimeout("./images/cross.png")
        pag.click(x, y)
    else:
        pag.click(x, y)

    # ending timer for link generation
    # tactual = round(time.time() - t1, 3)
    # try:
    #     t = timePerLink - (time.time() - t1)
    #     time.sleep(t)
    # except ValueError:
    #     pass

    timeCalc = time.time()
    totalSeconds += round(timeCalc - t1, 3)
    count += 1

    if round(timeCalc - t1, 3) < least:
        least = round(timeCalc - t1, 3)

    if count % 1 == 0:

        clear()
    # Padded time: {round(t, 3)}s
    # Actual time: {tactual}s
        print(f"""
    Latest link: {link[-12:]}

    Links processed this session: {count} links
    Current session duration: {time.strftime('%H:%M:%S', time.gmtime(round(totalSeconds, 3)))}
    Average time per link: {round(totalSeconds / count, 3)}s
    Least time this session: {least}s

    Time for 5000 links: {time.strftime('%H:%M:%S', time.gmtime(round(totalSeconds / count, 3) * 5000))}
    Time till 5000 links: {time.strftime('%H:%M:%S', time.gmtime(round(totalSeconds / count, 3) * (5000 - count)))}

    Time to load a link: {round(tLoading, 5)}s
    Time to process a link: {round((timeCalc - t1) - tLoading, 5)}s
    Total time for a link: {round(timeCalc - t1, 3)}s

    Current Time: {datetime.now().strftime('%H:%M:%S')}""")
