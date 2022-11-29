import os

from celery.utils.log import get_task_logger

from config import celery_app
from config.settings import base
from minio import Minio

logger = get_task_logger(__name__)


@celery_app.task()
def file_upload(input_task):
    client = Minio(
        endpoint="minio:9000",
        access_key="minio",
        secret_key="miniostorage",
        secure=False,
    )

    found = client.bucket_exists(base.BUCKET_NAME)
    if not found:
        client.make_bucket(base.BUSCET_NAME)

    fake_input_path = base.STATIC_ROOT
    source_path = os.path.join(fake_input_path, "wlg.mp4")

    _, name = os.path.split(source_path)
    client.fput_object(
        base.BUCKET_NAME,
        name,
        source_path,
    )
    logger.info(f"{source_path} is uploaded!")
    return found
