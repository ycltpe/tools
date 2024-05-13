from pydub import AudioSegment
from pydub.effects import speedup

# 读取音频文件
audio = AudioSegment.from_file("output_audio.mp3")

# 加快音频播放速度（2倍）
fast_audio = speedup(audio, playback_speed=1.5)

# 减慢音频播放速度（0.5倍）
# slow_audio = slowdown(audio, playback_speed=0.5)

# 导出处理后的音频文件
fast_audio.export("output_audio_fast.mp3", format="mp3")
# slow_audio.export("output_audio_slow.wav", format="wav")