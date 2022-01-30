import pyautogui as pag
import time
from datetime import datetime
import pyperclip
from helpers import clear, forceFind, findImage, findImageTimeout

pag.PAUSE, totalSeconds, count, timePerLink = 0, 0, 0, 0
least = 10
points = {
    "newMeeting": pag.Point(x=266, y=643),
    "cross": pag.Point(x=1147, y=477),
}

while True:
    t1 = time.time()

    # pag.doubleClick(points["newMeeting"], duration=0.15)
    time.sleep(0.05)
    pag.press("down")
    time.sleep(0.3)
    pag.press("enter")

    tToLoad = time.time()
    copyX, copyY = findImageTimeout(
        "./images/copy.png", 5, (1100, 562, 353, 50))
    tLoading = time.time() - tToLoad

    # if no copy button
    if copyX == -1 or copyY == -1:
        pag.click(points["cross"])
        continue

    pag.click(copyX, copyY)
    pag.click(points["cross"])

    # calculations
    timeCalc = time.time()
    totalSeconds += round(timeCalc - t1, 3)
    count += 1

    if round(timeCalc - t1, 3) < least:
        least = round(timeCalc - t1, 3)

    link = pyperclip.paste()

    if len(link) == 36:
        with open("./out/allLinks.txt", "a+") as f:
            f.write(f"{link}\n")

        with open("./out/out.txt", "w+") as f:
            f.write(f"""
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

    Current Time: {datetime.now().strftime('%H:%M:%S')}\n""")
