import numpy as np
import matplotlib.pyplot as plt

def compute_fft(f1, f2, sample_rate, duration):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)  # time vector
    s = np.sin(2 * np.pi * f1 * t) + np.sin(2 * np.pi * f2 * t)  # signal
    
    # Compute the FFT
    fft_values = np.fft.fft(s)
    fft_freq = np.fft.fftfreq(len(s), 1/sample_rate)
    
    # Get the magnitude spectrum
    fft_magnitude = np.abs(fft_values)
    
    # Plot the magnitude spectrum
    plt.figure(figsize=(10, 6))
    plt.plot(fft_freq, fft_magnitude)
    plt.title('FFT of the Signal')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude')
    plt.xlim(0, sample_rate / 2)  # only plot the positive frequencies
    plt.grid()
    plt.show()

    return fft_freq, fft_magnitude

# Parameters
f1 = 50  # Hz
f2 = 120  # Hz
sample_rate = 1000  # Hz
duration = 1  # second

# Compute and plot the FFT
compute_fft(f1, f2, sample_rate,duration)
