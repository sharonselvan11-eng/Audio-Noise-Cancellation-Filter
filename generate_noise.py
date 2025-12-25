import numpy as np
from scipy.io.wavfile import write

# 1. Setup audio parameters
rate = 44100  
duration = 5  
t = np.linspace(0, duration, int(rate * duration), endpoint=False)

# 2. Create a "Clean" Tone 
tone1 = np.sin(2 * np.pi * 440 * t) # Note A
tone2 = np.sin(2 * np.pi * 550 * t) # Note C#
clean_audio = (tone1 + tone2) * 0.3

# 3. Add harsh static noise
noise = np.random.normal(0, 0.2, clean_audio.shape)
noisy_audio = clean_audio + noise

# 4. Save to a WAV file
scaled_noise = np.int16(noisy_audio / np.max(np.abs(noisy_audio)) * 32767)
write("test_noise.wav", rate, scaled_noise)

print("Done! Created 'test_noise.wav'. Go to your folder and play it!")