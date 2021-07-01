import math
import wave
import struct

freq = 1000.0
data_size = 40000*4
fname = "WaveTest2.wav"
frate = 44100.0
amp = 64000.0     # multiplier for amplitude

sine_list_x = []
for x in range(data_size):
    sine_list_x.append(math.sin(2*math.pi*freq*(x/frate)))

wav_file = wave.open(fname, "w")

nchannels = 1
sampwidth = 2
framerate = int(frate)
nframes = data_size
comptype = "NONE"
compname = "not compressed"

wav_file.setparams((nchannels, sampwidth, framerate, nframes,
    comptype, compname))

for s in sine_list_x:
    # write the audio frames to file
    wav_file.writeframes(struct.pack('h', int(s*amp/2)))

wav_file.close()
import os
os.startfile(fname)