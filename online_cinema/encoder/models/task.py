from django.db import models


class ConvertTask(models.Model):
    output = models.FileField()
    file_format = models.CharField(max_length=100)
    video = models.ForeignKey(
        "Video", on_delete=models.CASCADE, related_name="convert_tasks"
    )
