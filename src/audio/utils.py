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