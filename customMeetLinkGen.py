import pyautogui as pag
import time
import cursor
from datetime import datetime
import pyperclip
from helpers import forceFind, clear, writeToFile, findImage
cursor.hide()

# opening edge
time.sleep(2)
pag.PAUSE = 0.5
pag.press("winleft")
pag.write("edge")
pag.press("enter")
pag.hotkey("winleft", "up")

pag.PAUSE = 0.02
totalSeconds = 0
count = 0
reloadX, reloadY = forceFind("./images/reload.png")

while True:
    t1 = time.time()

    # go to url to create new link
    pag.click(reloadX + 100, reloadY)
    pag.write("m", interval=0)
    pag.press("enter")

    # creating a new meeting
    x, y = forceFind("./images/newMeeting.png")
    pag.click(x, y)
    time.sleep(0.5)
    pag.click(x, y + 75)

    # as soon as the link appears in url bar
    forceFind("./images/recording.png")
    while x != -1 and y != -1:
        x, y = findImage("./images/url.png")

    pag.click(reloadX + 100, reloadY)
    pag.hotkey("ctrl", "x")
    time.sleep(0.01)
    link = pyperclip.paste()

    if len(link) == 36:
        writeToFile("./out/allLinks.txt",
                    "a+",
                    f"{link}\n",
                    "w")

        totalSeconds += round(time.time() - t1, 3)
        count += 1

        clear()
        print(f"""
    Latest link: {link[-12:]}
    Latest time for a link: {round(time.time() - t1, 3)}s

    Links processed this session: {count} links
    Current session duration: {round(totalSeconds, 3)}s
    Average time per link: {round(totalSeconds/count, 3)}s

    Time: {datetime.now().strftime('%H:%M:%S')}
    """)
# 6.658
