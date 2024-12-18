# -*- coding: utf-8 -*-
"""
Experiment with moviepy

"""
import PIL
from moviepy.editor import VideoFileClip, concatenate_videoclips, vfx, AudioFileClip, afx, CompositeAudioClip, concatenate_audioclips
from moviepy.video.fx.all import resize

clip1 = VideoFileClip("Files/christmastree.mp4").subclip(10, 15)
clip2 = VideoFileClip("Files/sausages.mp4").subclip(2, 4)
clip3 = VideoFileClip("Files/pepper.mov").subclip(5, 10)
clip4 = VideoFileClip("Files/Helen Chapel.m4v").subclip(10, 15)
clip5 = VideoFileClip("Files/galapagos_sea.mov").subclip(5, 10)
clip6 = VideoFileClip("Files/iguana.mov").subclip(1, 3)

# combinedclips = concatenate_videoclips([clip1, clip2, clip3, clip4])
# combinedclips.write_videofile("Files/combinedclips.mp4")

combinedclips2 = concatenate_videoclips([clip5, clip3, clip6])
combinedclips2.write_videofile("Files/basic_combined_mov_clips.mp4")

"""
Add Fade in fade out
"""

clip7 = VideoFileClip("Files/galapagos_sea.mov").subclip(5,
                                                         10).fx(vfx.fadein, 1).fx(vfx.fadeout, 1)
clip8 = VideoFileClip("Files/iguana.mov").subclip(1,
                                                  3).fx(vfx.fadein, 1).fx(vfx.fadeout, 1)
clip9 = VideoFileClip("Files/pepper.mov").subclip(5,
                                                  10).fx(vfx.fadein, 1).fx(vfx.fadeout, 1)

combinedclips3 = concatenate_videoclips([clip9, clip7, clip9, clip8, clip9])
combinedclips3.write_videofile("Files/combined_matched_clips_with_fade.mp4")

"""
Add Audio with audio fade in and out, and changing audio when the clips change
"""
audio = AudioFileClip(
    "Files/christmastree.mp4").subclip(10, 15).fx(afx.audio_fadein, 1).fx(afx.audio_fadeout, 1)
audio2 = AudioFileClip(
    "Files/galapagos_sea.mov").subclip(5, 8).fx(afx.audio_fadein, 1).fx(afx.audio_fadeout, 1)
audio3 = AudioFileClip(
    "Files/galapagos_sea.mov").subclip(1, 5).fx(afx.audio_fadein, 1).fx(afx.audio_fadeout, 1)

combined_audio = concatenate_audioclips([audio, audio3, audio, audio2, audio])

combinedclips3.audio = CompositeAudioClip(
    [combined_audio])
combinedclips3.write_videofile("Files/combined_matched_clips_fade_audio.mp4")

"""
Standardise frame rates, resolutions and codec
"""
target_fps = 30
target_resolution = (1920, 1080)
clips_to_combine = [clip1, clip2, clip3, clip4, clip5, clip6]

cliptest = resize(clip2, newsize=target_resolution)
cliptest = clip2.resize(target_resolution, PIL.Image.Resampling.LANCZOS)

clips = []
for clip in clips_to_combine:
    # standardise frames per second00
    clip = clip.set_fps(target_fps)
    # standardise resolution
    clip = clip.resize(target_resolution, PIL.Image.Resampling.LANCZOS)
    # clip = resize(clip, height=1080, width=1920)
    # standardise audio
    tmp_audio = clip.audio
    if tmp_audio is not None:
        tmp_audio = audio.set_fps(44100)
        clip = clip.set_audio(tmp_audio)
    # remove potentially corrupt frames
    clip = clip.subclip(0, clip.duration - 0.1)
    clips.append(clip)


combined_mismatched_videos = concatenate_videoclips(
    clips)
combined_audio1 = concatenate_audioclips(
    [audio, audio2, audio3, audio, audio3, audio2])
combined_mismatched_videos.audio = CompositeAudioClip(
    [combined_audio1])

combined_mismatched_videos.write_videofile(
    "Files/combined-mismatch-clips_audio.mp4")
