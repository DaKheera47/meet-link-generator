import pyautogui as pag
import time
import cursor
from datetime import datetime
import pyperclip
from helpers import findImageTimeout, clear, writeToFile
cursor.hide()

pag.PAUSE = 0.1
totalSeconds = 0
count = 0

while True:
    # starting timer for link generation
    t1 = time.time()

    # creating a new meeting
    x1, y1 = findImageTimeout("./images/newMeeting.png")
    pag.click(x1, y1)
    time.sleep(0.1)
    pag.click(x1, y1)
    x, y = findImageTimeout("./images/copy.png")
    pag.click(x, y)
    link = pyperclip.paste()
    pag.click(x1, y1)

    if len(link) == 36:
        writeToFile("./out/allLinks.txt",
                    "a+",
                    f"{link}\n",
                    "w")

        # ending timer for link generation
        timeCalc = round(time.time(), 3)

        totalSeconds += round(timeCalc - t1, 3)
        count += 1

        clear()
        print(f"""
    Latest link: {link[-12:]}
    Latest time for a link: {round(timeCalc - t1, 3)}s

    Links processed this session: {count} links
    Current session duration: {round(totalSeconds, 3)}s
    Average time per link: {round(totalSeconds / count, 3)}s

    Time: {datetime.now().strftime('%H:%M:%S')}
    """)
