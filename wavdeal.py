from pydub import AudioSegment

# 读取音频文件
audio = AudioSegment.from_file("taohuaxiao.mp3")

# 对声音进行变声处理
octave_down = audio._spawn(audio.raw_data, overrides={
    "frame_rate": int(audio.frame_rate / 1.5)
})

# 导出处理后的音频文件
octave_down.export("output_audio.mp3", format="mp3")
