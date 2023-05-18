import moviepy.editor as mp
import os
import shutil
from playsound import playsound
import numpy as np
import argparse

parser = argparse.ArgumentParser(description = 'Spotify Lite')
parser.add_argument('--append', action=argparse.BooleanOptionalAction)

args = parser.parse_args()


def dir_error_handling():
    main_list = os.listdir()
    if args.append is False:
        if 'audios' in main_list:
            shutil.rmtree('audios')
    os.makedirs('audios', exist_ok=True)
    print("Error Handling Done")


def audio_extractor():
    video_list = os.listdir('videos/')
    if len(video_list):
        for video in video_list:
            in_name = 'videos/' + video
            clip = mp.VideoFileClip(in_name)
            out_name = 'audios/' + video.split('.')[0] + '.mp3'
            clip.audio.write_audiofile(out_name)
    print("Audios Added")


def spotify_lite():
    audio_list = os.listdir('audios/')
    if len(audio_list):
        while (1):
            arr = np.arange(len(audio_list))
            np.random.shuffle(arr)
            for i in range(len(arr)):
                name = 'audios/' + audio_list[arr[i]]
                print("Now playing: ",arr[i],"-", audio_list[arr[i]].split('.')[0])
                playsound(name)



def main():
    dir_error_handling()
    audio_extractor()
    spotify_lite()


if __name__ == "__main__":
    main()
