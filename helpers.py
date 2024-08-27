import pyscreeze
import os
import time
import pyautogui as pag

pag.PAUSE = 0


def findImage(imageUrl: str, confidence: int = 0.90):
    try:
        x, y = pag.locateCenterOnScreen(
            f"{imageUrl}", confidence=confidence, grayscale=True
        )
    except TypeError:
        x, y = -1, -1

    return (x, y)


def forceFind(
    imageUrl: str, grayscale: bool = True, confidence: int = 0.90, region: tuple = None
):
    while True:
        try:
            if region:
                x, y = pag.center(
                    pag.locate(
                        f"{imageUrl}",
                        pag.screenshot(region=region),
                        confidence=confidence,
                        grayscale=grayscale,
                    )
                )
                return (x + region[0], y + region[1])
            else:
                x, y = pag.locateCenterOnScreen(
                    f"{imageUrl}", confidence=confidence, grayscale=grayscale
                )
                return (x, y)
        except pag.ImageNotFoundException:
            continue


def findImageTimeout(
    imageUrl: str,
    timeout: int,
    region: tuple = None,
    grayscale: bool = True,
    confidence: int = 0.90,
    rate: int = 100,
):
    if not region:
        region = (0, 0, pag.size()[0], pag.size()[1])

    start_time = time.perf_counter()

    while True:
        try:
            if region:
                # search in given area
                x, y = pag.center(
                    pag.locate(
                        needleImage=imageUrl,
                        haystackImage=pag.screenshot(region=region),
                        confidence=confidence,
                        grayscale=grayscale,
                    )
                )
                return (x + region[0], y + region[1])

            else:
                # search center on screen
                x, y = pag.locateCenterOnScreen(
                    f"{imageUrl}", confidence=confidence, grayscale=grayscale
                )
                return (x, y)

        except pag.ImageNotFoundException:
            if time.perf_counter() - start_time > timeout:
                return (-1, -1)


# keep looping until image not found
def loop_until_image_not_found(
    image_url: str, timeout: float = 10, confidence: float = 0.9, region: tuple = None
):
    """
    Keeps looping until the specified image is not found on the screen or the timeout is reached.

    Args:
    image_url (str): Path to the image file to search for.
    timeout (float): Maximum time in seconds to keep searching. Defaults to 10 seconds.
    confidence (float): Confidence level for image matching. Defaults to 0.9.
    region (tuple): Region of the screen to search in (left, top, width, height). Defaults to None (full screen).

    Returns:
    bool: True if the image was not found before timeout, False if the image is still present after timeout.
    """
    start_time = time.perf_counter()

    while True:
        try:
            if region:
                pag.locate(
                    needleImage=image_url,
                    haystackImage=pag.screenshot(region=region),
                    confidence=confidence,
                )

            else:
                pag.locateOnScreen(image_url, confidence=confidence)

            # If the image is found, check if we've exceeded the timeout
            if time.perf_counter() - start_time > timeout:
                return False  # Timeout reached, image still present
        except pag.ImageNotFoundException:
            # Image not found, exit the loop
            return True


def clear():
    os.system("cls" if os.name == "nt" else "clear")
