import subprocess


# Take 3 segments of the BBB video using bento4.
# We take 1 fragment of 4 seconds (4000 ms) of the same video in 3 different resolutions.
subprocess.run('mp4fragment --fragment-duration 4000 bento4_ex2/BBB_720.mp4 bento4_ex2/BBB_720_frag.mp4', shell=True)
subprocess.run('mp4fragment --fragment-duration 4000 bento4_ex2/BBB_480.mp4 bento4_ex2/BBB_480_frag.mp4', shell=True)
subprocess.run('mp4fragment --fragment-duration 4000 bento4_ex2/BBB_360x240.mp4 bento4_ex2/BBB_360x240_frag.mp4', shell=True)

# Optional command. We display info of one video to confirm that the video is fragmented.
subprocess.run('mp4info bento4_ex2/BBB_720_frag.mp4', shell=True)

# Use DASH to package the 3 videos into a DASH MPD file.
subprocess.run('mp4dash --mpd-name bento4_ex2/BBB_bento4.mpd bento4_ex2/BBB_720_frag.mp4 bento4_ex2/BBB_480_frag.mp4'
               ' bento4_ex2/BBB_360x240_frag.mp4', shell=True)
