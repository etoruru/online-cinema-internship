import os

import ffmpeg

from config import celery_app
from online_cinema.encoder.models import Video

# def set_ready(self, retval, task_id, args, kwargs):
#     return retval + 1


@celery_app.task()
def convert_video(video_name, video_path):
    width = 1080
    filename = video_name
    name, _ = os.path.splitext(filename)

    input = ffmpeg.input(f"{video_path}{filename}")
    video_input = input.video
    audio_input = input.audio
    new_res_video_input = video_input.filter("scale", -1, width)

    video_output = ffmpeg.output(
        new_res_video_input,
        audio_input,
        f"{video_path}{name}_{width}.mp4",
        format="mp4",
        acodec="aac",
    )
    video_output.run()
