import pyautogui as pag
import time
import cursor
from datetime import datetime
import pyperclip
from helpers import findImage, clear, writeToFile, findImageTimeout
cursor.hide()

pag.PAUSE = 0.1
totalSeconds = 0
count = 0
timePerLink = 4
while True:
    # starting timer for link generation
    t1 = time.time()

    # creating a new meeting
    x1, y1 = findImage("./images/newMeeting.png")
    pag.click(x1, y1)
    pag.click(findImage("./images/link.png"))
    x, y = findImageTimeout("./images/copy.png")

    if x != -1 and y != -1:
        pag.click(x, y)
    else:
        pag.click(x1, y1)
        time.sleep(0.2)
        continue

    link = pyperclip.paste()
    pag.click(x1, y1)

    if len(link) == 36:
        writeToFile("./out/allLinks.txt",
                    "a+",
                    f"{link}\n",
                    "w")

        # ending timer for link generation
        tactual = round(time.time() - t1, 3)
        try:
            t = timePerLink - (time.time() - t1)
            time.sleep(t)
        except ValueError:
            pass

        timeCalc = time.time()
        totalSeconds += round(timeCalc - t1, 3)
        count += 1

        clear()
        print(f"""
    Latest link: {link[-12:]}
    Latest time for a link: {round(timeCalc - t1, 3)}s

    Links processed this session: {count} links
    Current session duration: {round(totalSeconds, 3)}s
    Average time per link: {round(totalSeconds / count, 3)}s

    Padded time: {round(t, 3)}s
    Actual time: {tactual}s

    Time: {datetime.now().strftime('%H:%M:%S')}
""")
