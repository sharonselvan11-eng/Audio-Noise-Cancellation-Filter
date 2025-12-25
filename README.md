# Satellite Audio Noise Cancellation 🛰️📡

## Overview
This project simulates a satellite communication system where a signal is corrupted by atmospheric noise during transmission. I designed a **Butterworth Low Pass Filter** using Python to successfully remove high-frequency static and recover the original audio signal.

## How It Works
1.  **Signal Generation:** Creates a clean audio tone (simulating a command signal).
2.  **Noise Simulation:** Adds Gaussian white noise to simulate channel interference.
3.  **Filtration:** Applies a digital Low Pass Filter (LPF) to suppress frequencies above 1000Hz.

## Technologies Used
* **Python**
* **NumPy** (Mathematical operations)
* **SciPy** (Signal processing & WAV file handling)
* **Matplotlib** (Visualizing the waveforms)

## How to Run
1.  Install dependencies:
    ```bash
    pip install numpy scipy matplotlib
    ```
2.  Run the noise generator:
    ```bash
    python generate_noise.py
    ```
3.  Run the filter to clean the audio:
    ```bash
    python clean_audio.py
    ```

## Results
* **`test_noise.wav`**: The corrupted signal (Input).
* **`result_clean.wav`**: The recovered signal (Output).
*
