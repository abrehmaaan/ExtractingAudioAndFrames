import moviepy.editor  #as mp
video = moviepy.editor.VideoFileClip('video.mp4')   #mp.Videofileflip
audio = video.audio
audio.write_audiofile('audio.mp3')