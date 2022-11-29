import os
import shutil

import ffmpeg_streaming
from celery.utils.log import get_task_logger
from ffmpeg_streaming import S3, Bitrate, Formats, Representation, Size

from config import celery_app
from config.settings import base
from online_cinema.encoder.models import ConvertTask, Video

_144p = Representation(Size(256, 144), Bitrate(95 * 1024, 64 * 1024))
_240p = Representation(Size(426, 240), Bitrate(150 * 1024, 94 * 1024))
_360p = Representation(Size(640, 360), Bitrate(276 * 1024, 128 * 1024))
_480p = Representation(Size(854, 480), Bitrate(750 * 1024, 192 * 1024))
_720p = Representation(Size(1280, 720), Bitrate(2048 * 1024, 320 * 1024))
_1080p = Representation(Size(1920, 1080), Bitrate(4096 * 1024, 320 * 1024))
_2k = Representation(Size(2560, 1440), Bitrate(6144 * 1024, 320 * 1024))
_4k = Representation(Size(3840, 2160), Bitrate(17408 * 1024, 320 * 1024))

logger = get_task_logger(__name__)


def update_video_inf(self, retval, task_id, args, kwargs):
    video_id, convert_task_id, *_ = args
    video = Video.objects.get(pk=video_id)
    video.status = "RD"
    video.item.season.card.is_available = True
    video.save()
    task_result = ConvertTask.objects.get(pk=convert_task_id)
    task_result.output = retval
    task_result.save(update_fields=["output"])
    logger.info(f"Changed status {retval}")


def save_to_cloud(s3):
    s3.upload_directory(f"{base.MEDIA_ROOT}/", bucket_name=base.BUCKET_NAME)
    shutil.rmtree(f"{base.MEDIA_ROOT}/")


@celery_app.task(on_success=update_video_inf)
def convert_video_to_hls(video_id, task_id, filename):
    s3 = S3(
        endpoint_url="http://minio:9000",
        aws_access_key_id=base.AWS_ACCESS_KEY,
        aws_secret_access_key=base.AWS_SECRET_KEY,
    )
    # fake filename for demonstration
    filename = "wlg.mp4"
    name = os.path.basename(filename)

    video = ffmpeg_streaming.input(s3, bucket_name=base.BUCKET_NAME, key=filename)
    hls = video.hls(Formats.h264())
    hls.representations(_144p, _240p, _360p, _480p, _720p)  # _1080p, _2k, _4k)

    logger.info("Start of converting")
    hls.output(f"{base.MEDIA_ROOT}/{name}.m3u8")
    logger.info("End of converting.")

    logger.info("Upoloading into a cloud...")
    save_to_cloud(s3)

    output_path = f"{name}.m3u8"
    return output_path
