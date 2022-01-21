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
        pag.doubleClick(x1, y1)
    else:
        pag.moveTo(x1, y1, duration=0.5, tween=pag.easeOutElastic)
        pag.doubleClick()

    # creating a new meeting
    # pag.doubleClick(findImageTimeout(
    #     "./images/newMeeting.png", grayscale=False))
    # pag.click(findImageTimeout("./images/link.png"))
    tToLoad = time.time()

    link = pyperclip.paste()
    if len(link) == 36:
        with open("./out/allLinks.txt", "a+") as f:
            f.write(f"{link}\n")

    # time.sleep(0.5)

    if findImage("./images/couldntGet.png") != (-1, -1):
        # exists
        pag.click(x, y)
        continue


    copyX, copyY = findImageTimeout("./images/copy.png")
    tLoading = time.time() - tToLoad
    pag.click(copyX, copyY)
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
