import pyautogui as pag
import time
from datetime import datetime, timedelta
import pyperclip
from helpers import clear, forceFind, findImage, findImageTimeout, loop_until_image_not_found
from cv2 import imread

# MODE = "shaheer30"
MODE = "goodboy"

pag.PAUSE = 0
points = {
    "newMeeting": pag.Point(x=286, y=665) if MODE == "shaheer30" else pag.Point(x=866, y=443),
    "cross": pag.Point(x=1176, y=452),
}
REGIONS = {
    "copy_btn": (786, 558, 414, 100),
    "left_new_meeting": (127, 606, 240, 100),
}

session_start_time = time.perf_counter()

FILENAME = "./out/2024-allLinks-test.txt" if MODE == "shaheer30" else "./out/2024-allLinks.txt"


class Session:
    def __init__(this):
        this.total_seconds = 0
        this.link_count = 0
        this.least = float("inf")
        this.file = open(FILENAME, "a+")
        this.last_link = ""
        this.curr_link_start_time = time.perf_counter()
        this.curr_link_total_time = 0
        this.curr_link_processing_time = 0
        this.curr_link_loading_time = 0
        this.curr_link = ""
        this.meeting_x = 0
        this.meeting_y = 0
        this.copy_x = 0
        this.copy_y = 0
        this.curr_link_loading_start_time = 0
        this.curr_link_processsing_start_time = 0
        this.unaccounted_time = 0
        this.copy_image = imread("./images/copy.png")

    def __del__(this):
        this.file.close()

    def save_link(this):
        # If the link is the same as the last link, skip it
        if this.curr_link == this.last_link:
            return

        # Update the last link
        this.last_link = this.curr_link

        # save the link
        if len(this.curr_link) == 36:
            this.file.write(f"{this.curr_link}\n")

        return this.curr_link

    def print_session_details(this):
        session_duration = timedelta(seconds=time.perf_counter() - session_start_time)
        avg_time_per_link = (
            this.total_seconds / this.link_count if this.link_count > 0 else 0
        )
        est_time_for_5k = avg_time_per_link * 5000
        est_time_remaining = avg_time_per_link * (5000 - this.link_count)

        print(
            f"""
Session Details:
Links processed this session:    {this.link_count} links
Current session duration:        {str(datetime.fromtimestamp(session_duration.total_seconds()).strftime('%H:%M:%S')) + f":{session_duration.microseconds // 1000:03d}ms"}
Average time per link:           {round(avg_time_per_link, 3)}s
Least time this session:         {round(this.least, 3)}s
Est time for 5k links:           {time.strftime('%H:%M:%S', time.gmtime(est_time_for_5k))}
Est time remaining for 5k links: {time.strftime('%H:%M:%S', time.gmtime(est_time_remaining))}
Current Time:                    {datetime.now().strftime('%H:%M:%S')}
"""
        )

    def print_link_details(this):
        if len(this.curr_link) == 36:
            calculated_time_spent = (
                this.curr_link_processing_time + this.curr_link_loading_time
            )
            this.unaccounted_time = this.curr_link_total_time - calculated_time_spent

            print(
                f"""
Link Details:
Latest link:                     {this.curr_link[-12:]}
Time to process a link:          {round(this.curr_link_processing_time, 5)}s
Time to find the copy button:    {round(this.curr_link_loading_time, 5)}s
Unaccounted time:                {round(this.unaccounted_time, 5)}s
Total time for this link:        {round(this.curr_link_total_time, 3)}s
"""
            )

    def update_session_stats(this):
        this.total_seconds += this.curr_link_total_time
        this.link_count += 1
        if this.curr_link_total_time < this.least:
            this.least = this.curr_link_total_time

    def process_link(this):
        this.update_session_stats()
        this.print_link_details()
        this.curr_link_start_time = time.perf_counter()

    def run(this):
        while True:
            # wait for the modal to close
            loop_until_image_not_found(this.copy_image, region=REGIONS["copy_btn"])

            pag.doubleClick(points["newMeeting"])

            # Measure time to process the link
            this.curr_link_loading_start_time = time.perf_counter()
            this.copy_x, this.copy_y = findImageTimeout(
                this.copy_image, 10, region=REGIONS["copy_btn"]
            )
            this.curr_link_loading_time = (
                time.perf_counter() - this.curr_link_loading_start_time
            )

            this.print_session_details()

            # If no "Copy" button found
            if this.copy_x == -1 or this.copy_y == -1:
                pag.press("esc")
                continue

            pag.click(this.copy_x, this.copy_y)
            # press esc to close the modal asap so it can play the closing animation while we process
            pag.press("esc")

            # Get the copied link
            this.curr_link = pyperclip.paste()

            if this.curr_link == "":  # if the link is empty, skip it
                continue
            if this.curr_link == this.last_link:  # if the link is the same as the last link, skip it
                continue
            if len(this.curr_link) != 36:  # if the link is not 36 characters long, skip it'
                continue

            # Measure time to process the link
            this.curr_link_processsing_start_time = time.perf_counter()
            this.save_link()
            # calculate time to process the link
            this.curr_link_processing_time = (
                time.perf_counter() - this.curr_link_processsing_start_time
            )
            this.curr_link_total_time = time.perf_counter() - this.curr_link_start_time

            # Process and print details
            this.process_link()


# Usage remains the same
session = Session()
session.run()
