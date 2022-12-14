import subprocess

# HLS transport stream container using a segment of 10 seconds of BBB video
subprocess.run('ffmpeg -i BBB_short.mp4 -c:v h264 -flags +cgop -g 30 -hls_time 1 HLS_ex1/BBB_short.m3u8', shell=True)
