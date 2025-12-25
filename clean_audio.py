import numpy as np
from scipy.io import wavfile
from scipy.signal import butter, lfilter

# 1. Load the Noisy File
rate, data = wavfile.read("test_noise.wav")

# 2. Design the Filter (Butterworth Low Pass Filter)
# This removes high-frequency static (noise) but keeps the low-frequency beep (signal)
def low_pass_filter(data, cutoff, fs, order=5):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    y = lfilter(b, a, data)
    return y

# We cut off everything above 1000Hz
cutoff_frequency = 1000 
cleaned_data = low_pass_filter(data, cutoff_frequency, rate)

# 3. Save the Clean Result
cleaned_data_int = np.int16(cleaned_data / np.max(np.abs(cleaned_data)) * 32767)
wavfile.write("result_clean.wav", rate, cleaned_data_int)

print("Success! created 'result_clean.wav'. Go listen to it!")