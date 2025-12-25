import numpy as np
import matplotlib.pyplot as plt
# 1. Simulate a clean signal (like a command sent to a satellite)
t = np.linspace(0, 1, 1000, endpoint=False)
clean_signal = np.sin(2 * np.pi * 10 * t)  # A simple wave
# 2. Add Noise (simulating interference from space/atmosphere)
noise = np.random.normal(0, 0.5, t.shape)
noisy_signal = clean_signal + noise
# 3. Simple Moving Average Filter (The "Noise Cancellation")
# This smooths out the rough noise to recover the signal
window_size = 20
filtered_signal = np.convolve(noisy_signal, np.ones(window_size)/window_size, mode='same')
# 4. Plot the results to see the difference
plt.figure(figsize=(10, 6))
plt.plot(t, noisy_signal, label='Noisy Signal (Received)', color='red', alpha=0.5)
plt.plot(t, clean_signal, label='Original Signal (Sent)', color='green', linestyle='dashed')
plt.plot(t, filtered_signal, label='Filtered Signal (Recovered)', color='blue', linewidth=2)
plt.legend()
plt.title("Satellite Signal Noise Cancellation Simulation")
plt.show()
