import os
import subprocess
import uuid

from celery import shared_task

from config import celery_app
from config.settings import base
from online_cinema.encoder.convert import convert_to_mp4
from online_cinema.encoder.models import Video


@celery_app.task()
def convert_video(video_path_out):
    width = 720
    # video = Video.objects.get(pk=video_id)
    # video_path_out = video.filepath
    filename = "video.mov"
    video_path_input = os.path.join(base.ROOT_DIR, "online_cinema/videofiles/")
    name, _ = os.path.splitext(filename)

    convert_to_mp4(filename, video_path_input, video_path_out, width)
    # command = ['ffmpeg', '-i', f"{video_path_input}{filename}", '-vf',
    # "scale='min(1280,iw)':min'(720,ih)':force_original_aspect_ratio=decrease,pad=1280:720:-1:-1:color=black",
    # '-acodec', 'aac', f"{video_path_out}/{name}_{width}.mp4"]
    # subprocess.call(command)
