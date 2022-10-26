import os

import ffmpeg


def convert_to_mp4(filename, video_path_input, video_path_out, width):
    name, _ = os.path.splitext(filename)
    format = "mp4"
    input = ffmpeg.input(f"{video_path_input}{filename}")
    video_input = input.video
    audio_input = input.audio

    audio_codec = "aac"
    new_res_video_input = video_input.filter(
        "scale", size="hd1080", force_original_aspect_ratio="decrease"
    )
    video_with_pads = new_res_video_input

    try:
        out, err = (
            ffmpeg.input(f"{video_path_input}{filename}")
            .output(
                video_with_pads,
                audio_input,
                f"{video_path_out}/{name}_{width}.{format}",
                format=format,
                acodec=audio_codec,
            )
            .run(
                quiet=True,
                overwrite_output=True,
                capture_stdout=True,
                capture_stderr=True,
            )
        )
    except Exception as error:
        return str(error)
