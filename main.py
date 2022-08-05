import os
import time
try:
    from TikTokApi import TikTokApi
except ImportError as e:
    os.system('pip install TikTokApi')
    time.sleep(60)
    os.system('python -m playwright install')


api = TikTokApi()


def vinput():
    os.system('cls')
    os.system('Title TikTok Video Downloader  -  @EdgeShoT')

    response = input('\x1b[38;2;0;255;0mEnter video id: ')
    video_name = input('Enter the name of the video wanna saved with:\033[0;00m ')

    try:
        video_id = int(response.strip())
    except Exception as e:
        print("Enter a number", e)
        vinput()

    return [video_id, video_name]


def write_vid(name, bytes):
    if not os.path.exists('./videos'):
        os.mkdir('videos')

    with open(f"./videos/{name}.mp4", 'wb') as f:
        f.write(bytes)


def main():
    resp = vinput()
    vid = api.video(id=resp[0])
    write_vid(resp[1], vid.bytes())


if __name__ == '__main__':
    main()
