from scenedetect import detect, AdaptiveDetector, split_video_ffmpeg
video_path = 'data/top_gun.mp4'
output_path = 'data'
scene_list = detect(video_path, AdaptiveDetector())
print(scene_list)
split_video_ffmpeg(video_path, scene_list, output_path)
