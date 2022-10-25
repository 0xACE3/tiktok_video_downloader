import os
import time
import sys
from logo import LOGO

try:
    from rgbprint.gradient import gradient_print
    from TikTokApi import (TikTokApi, exceptions)
except ImportError as e:
    print(f"[Error] {e}")
    print("[Install Dependencies]!")
    time.sleep(2)
    sys.exit(0)


api = TikTokApi()


def vinput():
    os.system('cls')
    os.system('Title TikTok Video Downloader  -  @0xHaris')
    gradient_print(LOGO, start_color="red", end_color="pink")
    response = input('\x1b[38;2;0;255;0m[-] Enter video id:\033[0;00m ')
    video_name = input('\x1b[38;2;0;255;0m[-] Enter the file-name of the video:\033[0;00m ')

    try:
        video_id = int(response.strip())
        return [video_id, video_name]
    except Exception as e:
        print(f"{e}\n", "Please Enter integer value: \033[0;00m")
        vinput()


def write_video(name, video_bytes):
    path = os.path.join(os.path.dirname(__file__), "videos")
    if not os.path.exists(path):
        os.mkdir(path)

    with open(os.path.join(path, f"{name}.mp4"), 'wb') as f:
        f.write(video_bytes)
        print("\x1b[38;2;0;255;0m[-] The video has been downloaded successfully.\033[0;00m")


def main():
    try:
        resp = vinput()
        vid = api.video(id=resp[0])
        write_video(resp[1], vid.bytes())
    except exceptions.TikTokException as e:
        print("\x1b[38;2;255;0;0m[Error] The video not found.\n {}\033[0;00m".format(e))


if __name__ == '__main__':
    main()
