# -*- coding: utf-8 -*-
"""
Merge video files with moviepy with fade-in fade-out and add audio clips

"""
import cv2
import PIL
from moviepy.editor import VideoFileClip, concatenate_videoclips, vfx, AudioFileClip, afx, CompositeAudioClip, concatenate_audioclips, ImageClip, ImageSequenceClip

clip1 = VideoFileClip("Files/christmastree.mp4").subclip(10,
                                                         15).fx(vfx.fadein, 1).fx(vfx.fadeout, 1)
clip2 = VideoFileClip("Files/sausages.mp4").subclip(2,
                                                    4).fx(vfx.fadein, 1).fx(vfx.fadeout, 1)
clip3 = VideoFileClip("Files/pepper.mov").subclip(5,
                                                  10).fx(vfx.fadein, 1).fx(vfx.fadeout, 1)
clip4 = VideoFileClip("Files/Helen Chapel.m4v").subclip(10,
                                                        15).fx(vfx.fadein, 1).fx(vfx.fadeout, 1)
clip5 = VideoFileClip("Files/galapagos_sea.mov").subclip(5,
                                                         10).fx(vfx.fadein, 1).fx(vfx.fadeout, 1)
clip6 = VideoFileClip("Files/iguana.mov").subclip(1,
                                                  3).fx(vfx.fadein, 1).fx(vfx.fadeout, 1)

clip7 = ImageSequenceClip([])

"""
Add Audio with audio fade in and out, and changing audio when the clips change
"""
audio1 = AudioFileClip(
    "Files/christmastree.mp4").subclip(24, 29).fx(afx.audio_fadein, 1).fx(afx.audio_fadeout, 1)
audio2 = AudioFileClip(
    "Files/galapagos_sea.mov").subclip(5, 8).fx(afx.audio_fadein, 1).fx(afx.audio_fadeout, 1)
audio3 = AudioFileClip(
    "Files/mixkit-playful-10.mp3").subclip(1, 5).fx(afx.audio_fadein, 1).fx(afx.audio_fadeout, 1)

"""
Standardise frame rates, resolutions and codec
"""
target_fps = 30
target_resolution = (1920, 1080)
clips_to_combine = [clip1, clip2, clip3, clip4, clip5, clip6]


clips = []
for clip in clips_to_combine:
    # standardise frames per second00
    clip = clip.set_fps(target_fps)

    # standardise resolution
    clip = clip.resize(target_resolution, PIL.Image.Resampling.LANCZOS)

    # standardise audio
    tmp_audio = clip.audio

    if tmp_audio is not None:
        tmp_audio = tmp_audio.set_fps(44100)
        clip = clip.set_audio(tmp_audio)

    # remove potentially corrupt frames
    clip = clip.subclip(0, clip.duration - 0.1)
    clips.append(clip)


combined_mismatched_videos = concatenate_videoclips(
    clips)
combined_audio1 = concatenate_audioclips(
    [audio1, audio2, audio3, audio1, audio3, audio2])
combined_mismatched_videos.audio = CompositeAudioClip(
    [combined_audio1])

combined_mismatched_videos.write_videofile(
    "Files/final_video.mp4")

# ImageClips

images = []
image1 = ImageClip(
    "Files/IMG_1334.JPG").set_duration(3).fx(vfx.fadein, 1).fx(vfx.fadeout, 1)
image2 = ImageClip(
    "Files/2015-04-03 10.48.27.png").set_duration(3).fx(vfx.fadein, 1).fx(vfx.fadeout, 1)
image3 = ImageClip(
    "Files/IMG_1337.JPG").set_duration(3).fx(vfx.fadein, 1).fx(vfx.fadeout, 1)

images.append(image1)
images.append(image2)
images.append(image3)


image_video = concatenate_videoclips(images)
image_video.write_videofile(
    "Files/final_video_images.mp4", fps=target_fps)
# close down the clips and release them
clip1.close()
clip2.close()
clip3.close()
clip4.close()
clip5.close()
