
import win32clipboard
import os
import time
import pyautogui as pag
pag.PAUSE = 0


def findImage(imageUrl: str, confidence: int = 0.90):
    try:
        x, y = pag.locateCenterOnScreen(
            f"{imageUrl}", confidence=confidence, grayscale=True)
    except TypeError:
        x, y = -1, -1

    return (x, y)


def forceFind(imageUrl: str, grayscale: bool = True):
    while True:
        try:
            x, y = pag.locateCenterOnScreen(
                f"{imageUrl}", confidence=0.9, grayscale=grayscale)
        except TypeError:
            continue
        return (x, y)


def findImageTimeout(imageUrl: str, timeout: int, region: tuple, grayscale: bool = True):
    i = 1
    rate = 10

    while True:
        if i <= (timeout * rate):
            try:
                t1 = time.time()

                if region:
                    # search in given area
                    x, y = pag.center(pag.locate(f"{imageUrl}", pag.screenshot(
                        region=region), confidence=0.9, grayscale=grayscale))
                    return (x + region[0], y + region[1])

                else:
                    # search center on screen
                    x, y = pag.locateCenterOnScreen(
                        f"{imageUrl}", confidence=0.9, grayscale=grayscale)
                    return (x, y)

            except TypeError:
                # make every iteration 1s
                i += 1
                try:
                    # print((1 / rate) - (time.time() - t1))
                    time.sleep((1 / rate) - (time.time() - t1))
                except:
                    continue

        else:
            return (-1, -1)


def clear():
    os.system("cls" if os.name == "nt" else "clear")
