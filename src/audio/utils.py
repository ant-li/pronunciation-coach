import numpy as np
import matplotlib.pyplot as plt

def plot_waveform(audio, sr, title="Waveform", figsize=(10, 3)):
    t = np.arange(len(audio)) / sr
    plt.figure(figsize=figsize)
    plt.plot(t, audio)
    plt.xlabel("Time (seconds)")
    plt.ylabel("Amplitude")
    plt.title(title)
    plt.tight_layout()
    plt.show()

# x = audio data
def audio_stats(x, sr, name):
    x = x.astype(np.float32)
    dur = len(x) / sr
    peak = float(np.max(np.abs(x)))
    rms = float(np.sqrt(np.mean(x**2)))
    print(f"{name}: sr={sr}, seconds={dur:.3f}, peak={peak:.3f}, rms={rms:.3f}")

# x = audio data
def global_rms(x):
    return np.sqrt(np.mean(x**2))
    
#user_x = user audio data
#base_x = baseline (either tts or mw api pronunciation) audio data
#function scales the baseline audio to the user's loudness
def normalize_base_loudness(user_x,base_x):
    user_x = user_x.astype("float32")
    base_x = base_x.astype("float32")

    user_rms = global_rms(user_x)
    base_rms = global_rms(base_x)

    scale = user_rms / (base_rms) #+ 1e-9) #might need this if any of the baseline audios might be silent.. don't think this will happen though
    mw_norm = base_x * scale

    return mw_norm
    
