from machine import PWM, Pin
import time

beep = Pin(16, Pin.OUT)

beeper = PWM(beep)

tone_names = "A A# B C C# D D# E F F# G G#".split(" ")
freqs = [ 110 * pow(2, 1/12) ** i for i in range(12) ]
durations = { "S": 0.25, "E": 0.5, "Q": 1, "H": 2, "F": 4}

freqmap = dict(zip(tone_names, freqs))
bpm = 100

def play_tone(name):
    duration = name[-1:]
    octave = int(name[-2:-1])
    name_ = name[:-2]
    
    print("%s %d" % (name, octave))
    
    beeper.freq(int(freqmap[name_]) * 2**octave)
    beeper.duty_u16(2**14)
    time.sleep(60 / bpm * durations.get(duration))
    beeper.duty_u16(0)
    
def play_tones(tones):
    for tone in tones:
        if (tone == "|"):
            time.sleep(1)
        else:
            play_tone(tone)
        
play_tones("C2Q E2S F2S G2E B3Q C4S B4S C4S B4S C4Q".split(" "))