import time
import mido
import numpy as np
import pyaudio
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
p = pyaudio.PyAudio()
NotesToPlay = []
play = []
volume = 1 # range [0.0, 1.0]
fs = 44100  # sampling rate, Hz, must be integer
duration = 5.0  # in seconds, may be float
f = 440.0  # sine frequency, Hz, may be float

def LoadMidi(filePath):
    mid = mido.MidiFile(filePath, clip=True, ticks_per_beat=800)
    for msg in mid:
        
        try:
            if msg.type == "note_on" :
                print(msg)
                NotesToPlay.append([msg.note, msg.time, msg.velocity])
            else: continue
        except:
            continue

LoadMidi("Omori_-_172_DUET_Solo_Violin.mid")
# LoadMidi("Howls_moving_castle_for_flute_solo.mid")
def wave(f,t, y):
    samples = (np.sin(2 * np.pi * np.arange(fs * t) * f / fs)).astype(np.float32)
    output_bytes = ((y * samples).tobytes())
    return output_bytes
def sine_x(f):
    stream.write(i)



for i,v,y in NotesToPlay:
    # if y == 0: 
    #     play.append(wave(0, v , y/ 100)) 

    # else:
    play.append(wave(note[i],v, y/ 100))
 
stream = p.open(format=pyaudio.paFloat32, channels=1, rate=fs, output=True)
for i in play:
    
    sine_x(i)

stream.close()
# sine_x(440, 1)
# sine_x(220, 1)
p.terminate()
