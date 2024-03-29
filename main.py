from ast import Load
from cgi import test
import wave
import matplotlib
import math
import struct
import mido
import numpy
import time



note = {
    127: 12543.85,
    126: 11839.82,
    125: 11175.3,
    124: 10548.08,
    123: 9956.06,
    122: 9397.27,
    121: 8869.84,
    120: 8372.02,
    119: 7902.13,
    118: 7458.62,
    117: 7040,
    116: 6644.88,
    115: 6271.93,
    114: 5919.91,
    113: 5587.65,
    112: 5274.04,
    111: 4978.03,
    110: 4698.64,
    109: 4434.92,
    108: 4186.01,
    107: 3951.07,
    106: 3729.31,
    105: 3520,
    104: 3322.44,
    103: 3135.96,
    102: 2959.96,
    101: 2793.83,
    100: 2637.02,
    99: 2489.02,
    98: 2349.32,
    97: 2217.46,
    96: 2093,
    95: 1975.53,
    94: 1864.66,
    93: 1760,
    92: 1661.22,
    91: 1567.98,
    90: 1479.98,
    89: 1396.91,
    88: 1318.51,
    87: 1244.51,
    86: 1174.66,
    85: 1108.73,
    84: 1046.5,
    83: 987.77,
    82: 932.33,
    81: 880,
    80: 830.61,
    79: 783.99,
    78: 739.99,
    77: 698.46,
    76: 659.26,
    75: 622.25,
    74: 587.33,
    73: 554.37,
    72: 523.25,
    71: 493.88,
    70: 466.16,
    69: 440,
    68: 415.3,
    67: 392,
    66: 369.99,
    65: 349.23,
    64: 329.63,
    63: 311.13,
    62: 293.66,
    61: 277.18,
    60: 261.63,
    59: 246.94,
    58: 233.08,
    57: 220,
    56: 207.65,
    55: 196,
    54: 185,
    53: 174.61,
    52: 164.81,
    51: 155.56,
    50: 146.83,
    49: 138.59,
    48: 130.81,
    47: 123.47,
    46: 116.54,
    45: 110,
    44: 103.83,
    43: 98,
    42: 92.5,
    41: 87.31,
    40: 82.41,
    39: 77.78,
    38: 73.42,
    37: 69.3,
    36: 65.41,
    35: 61.74,
    34: 58.27,
    33: 55,
    32: 51.91,
    31: 49,
    30: 46.25,
    29: 43.65,
    28: 41.2,
    27: 38.89,
    26: 36.71,
    25: 34.65,
    24: 32.7,
    23: 30.87,
    22: 29.14,
    21: 27.5,
    20: 25.96,
    19: 24.5,
    18: 23.12,
    17: 21.83,
    16: 20.6,
    15: 19.45,
    14: 18.35,
    13: 17.32,
    12: 16.35,
    11: 15.43,
    10: 14.57,
    9:13.75,
    8:12.98,
    7:12.25,
    6:11.56,
    5:10.91,
    4:10.3,
    3:9.72,
    2:9.18,
    1:8.66,
    0:8.18,

}



bits = 16
sample_rate = 41000

NotesToPlay = []
audio = []
def LoadMidi(filePath):
    mid = mido.MidiFile(filePath, clip=True, ticks_per_beat=800)
    for msg in mid:
        try:
            if msg.type == "note_on":
                NotesToPlay.append([msg.note, msg.time])
            else: continue
        except:
            continue

LoadMidi("Omori_-_172_DUET_Solo_Violin.mid")

def sine_x(amp, freq, time):
    return int(1000 * math.sin(2 * math.pi * (freq * time) * freq / sample_rate))
    # return int(round(amp * math.sin(2 * math.pi * freq * time)))

def save_wav(file_name):
    # Open up a wav file
    wav_file=wave.open(file_name,"w")

    # wav params
    nchannels = 1

    sampwidth = 1

    # 44100 is the industry standard sample rate - CD quality.  If you need to
    # save on file size you can adjust it downwards. The stanard for low quality
    # is 8000 or 8kHz.
    nframes = len(audio)
    print(nframes)
    comptype = "NONE"
    compname = "not compressed"
    wav_file.setparams((nchannels, sampwidth, sample_rate, nframes, comptype, compname))
    for sample in audio:
        # print(sample)
        wav_file.writeframes(struct.pack('h', sample))

    wav_file.close()

class Tone:
    def sine(frequency, duration=1, speaker=None):


        num_samples = round(duration * sample_rate)

        #setup our numpy array to handle 16 bit ints, which is what we set our mixer to expect with "bits" up above
        buf = numpy.zeros((num_samples, 2), dtype = numpy.int16)
        amplitude = 2 ** (bits - 1) - 1
        for s in range(num_samples):
            t = float(s) / sample_rate    # time in seconds
            sine = sine_x(amplitude, frequency, t)
            audio.append(int(sine))
    

    for i,v in NotesToPlay:     
        sine(note[i], v)

    print("Downloading")
    save_wav("test.wav")
    print("Finished")
        
