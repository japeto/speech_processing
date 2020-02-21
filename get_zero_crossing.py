from scipy.interpolate import interp1d
from scipy.io import wavfile
import numpy as np

import matplotlib.pyplot as plot

def get_zero_crossing(audio_path):
    """
    This function performs a short term analysis to calculate the zero crossing in a signal. To do so, it uses a window
    (hanning) and a shift for the window. The zero crossing is then calculate per frame.
    :param audio_path Path to the audio (wav, it does not accept wav quantised at 16 bits)
    :return: an array of the zero crossing rate interpolated for the whole signal
    """
    frequency, signal = wavfile.read(audio_path)

    # Total samples in the signal
    samples = # how many samples in the signal?

    # Short term analysis. In seconds
    frame_length = 0.025  # window length
    frame_period = 0.010  # window shift

    # Number of samples per frame
    frame_period =  # How many samples per 10ms?
    frame_length =  # How many samples per 25ms?

    # Frames
    chunks = np.arange(0, samples - frame_length, frame_period)
    n_frames = chunks.size

    # Zero crossing changes
    sign_signal = np.append([0], np.sign(signal))
    sign_signal = sign_signal[1:] - sign_signal[:-1]
    sign_signal = np.where(sign_signal > 0, np.ones(samples), np.zeros(samples))

    prev = chunks[0]
    frames = tuple()
    for x in chunks:
        frame = sign_signal[prev:(x + frame_length)]
        frames += (np.transpose(frame),)
        prev = x + frame_period

    frames = np.column_stack(frames)
    # Normalise scale
    zero_crossing = np.sum(frames, axis=0)*(frequency/frame_length)

    # Interpolate
    points = np.append([1], 1 + chunks + np.ceil(frame_period / 2))
    points = np.append(points, [samples])

    # Add limits (two extra points by copying the first and last values)
    zero_crossing = np.append([zero_crossing[0]], zero_crossing)
    zero_crossing = np.append(zero_crossing, zero_crossing[-1])
    final_zero_crossing = interp1d(points, zero_crossing)(np.arange(1, samples + 1))

    return final_zero_crossing

# Show zero crossing spectrum
audio_path = "archivo_audio.wav"
frequency, signal = wavfile.read(audio_path)

samples = # how many samples in the signal?

plot.subplot(211)
plot.title("Espectrograma")

plot.plot(signal)
plot.xlabel("Muestra")
plot.ylabel("Amplitud")

zero_crossing = get_zero_crossing(audio_path)
zero_crossing_threshold = 1800

plot.subplot(212)
plot.plot(zero_crossing)
plot.plot(np.ones(samples)*zero_crossing_threshold, 'r')
plot.xlabel("Muestra")
plot.ylabel("Cruce Cero")

plot.show()