# -*- coding: utf-8 -*-
"""
Merge video files with moviepy with fade-in fade-out and add audio clips

"""
import PIL
from moviepy.editor import concatenate_videoclips, CompositeVideoClip, vfx, AudioFileClip, afx, concatenate_audioclips, ImageClip


def resize_image_maintain_aspect(clip, target_width, target_height):
    # Load the image
    # clip = ImageClip(image_path)

    # Calculate scaling factor
    scale_w = target_width / clip.w
    scale_h = target_height / clip.h
    scale = min(scale_w, scale_h)

    # Resize the image
    resized_clip = clip.resize(scale)

    # Create a background clip
    bg_clip = ImageClip(size=(target_width, target_height), color=(0, 0, 0))

    # Position the resized image on the background
    final_clip = CompositeVideoClip([bg_clip, resized_clip.set_position('center')])

    return final_clip


def clean_up_video_clips(clips_to_combine, target_fps=30, target_resolution=(1920, 1080)):
    clips = []
    for clip in clips_to_combine:
        # standardise frames per second00
        clip = clip.set_fps(target_fps)

        # standardise resolution
        #clip = clip.resize(target_resolution, PIL.Image.Resampling.LANCZOS)
        clip = resize_image_maintain_aspect(clip, target_resolution.width, target_resolution.height)

        # standardise audio
        tmp_audio = clip.audio

        if tmp_audio is not None:
            tmp_audio = tmp_audio.set_fps(44100)
            clip = clip.set_audio(tmp_audio)

        # remove potentially corrupt frames
        clip = clip.subclip(0, clip.duration - 0.1)
        clips.append(clip)
    return clips

# ImageClips


audio1 = AudioFileClip(
    "Files/mixkit-playful-10.mp3").subclip(0, 5).fx(afx.audio_fadein, 1).fx(afx.audio_fadeout, 1)
audio2 = AudioFileClip(
    "Files/mixkit-piano-horror-671.mp3").subclip(10, 15).fx(afx.audio_fadein, 1).fx(afx.audio_fadeout, 1)
audio3 = AudioFileClip(
    "Files/mixkit-playful-10.mp3").subclip(7, 12).fx(afx.audio_fadein, 1).fx(afx.audio_fadeout, 1)

combined_audio1 = concatenate_audioclips(
    [audio1, audio2, audio3])


audio15 = AudioFileClip(
    "Files/mixkit-playful-10.mp3").subclip(0, 15).fx(afx.audio_fadein, 1).fx(afx.audio_fadeout, 1)

images = []
image1 = ImageClip(
    "Files/IMG_1334.JPG").set_duration(5).fx(vfx.fadein, 1).fx(vfx.fadeout, 1)
image2 = ImageClip(
    "Files/2015-04-03 10.48.27.png").set_duration(5).fx(vfx.fadein, 1).fx(vfx.fadeout, 1)
image3 = ImageClip(
    "Files/IMG_1337.JPG").set_duration(5).fx(vfx.fadein, 1).fx(vfx.fadeout, 1)

image1.audio = audio1
image2.audio = audio2
image3.audio = audio3

images.append(image1)
images.append(image2)
images.append(image3)

final_images = clean_up_video_clips(images)


image_video = concatenate_videoclips(final_images)
image_video.write_videofile(
    "Files/final_video_images_with_audio.mp4")

image_video2 = concatenate_videoclips(final_images)
image_video2.audio = audio15
image_video2.write_videofile(
    "Files/final_video_images_with_audio2.mp4")

image_video3 = concatenate_videoclips(final_images)
image_video3.audio = combined_audio1
image_video3.write_videofile(
    "Files/final_video_images_with_audio3.mp4")
