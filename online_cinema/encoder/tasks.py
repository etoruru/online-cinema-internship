import os
import uuid

import ffmpeg_streaming
from celery.utils.log import get_task_logger
from ffmpeg_streaming import Formats

from config import celery_app
from config.settings import base
from online_cinema.encoder.models import ConvertTask, Video

logger = get_task_logger(__name__)


def update_video_inf(self, retval, task_id, args, kwargs):
    video_id, *_ = args
    video = Video.objects.get(pk=video_id)
    video.status = "RD"
    video.item.season.card.is_available = True
    video.save()
    task_result = ConvertTask(output=retval, file_format="hls", video=video)
    task_result.save()
    logger.info(f"Changed status {retval}")


def make_output_path():
    uid = str(uuid.uuid4())
    first_dir, _ = uid.split("-", maxsplit=1)
    return os.path.join(
        base.MEDIA_ROOT, "{}/{}/{}".format("videofiles", first_dir, uid)
    )


@celery_app.task(on_success=update_video_inf)
def convert_video_to_hls(video_id, source_file_path):
    # fake 2 lines
    fake_input_path = base.STATIC_ROOT
    source_file_path = os.path.join(fake_input_path, "video_720.mp4")

    output_path = make_output_path()
    filename = os.path.basename(source_file_path)
    name, _ = os.path.splitext(filename)

    video = ffmpeg_streaming.input(source_file_path)
    hls = video.hls(Formats.h264())
    hls.auto_generate_representations()

    logger.info("Start of converting")
    hls.output(f"{output_path}/{name}.m3u8", async_run=True)  # !
    logger.info("End of converting.")
    return f"{output_path}/{name}.m3u8"
