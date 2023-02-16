import os
import subprocess

link = input("enter YouTube link: ")

youtube_dl_output = subprocess.check_output("yt-dlp -g " + link, shell=True, executable="/bin/bash").decode("utf-8").strip()

file_name = input("enter the name of how the new file: ")

os.system("nohup ffmpeg -i " + youtube_dl_output + " -c:v copy -c:a copy " + file_name + ".mkv &")
