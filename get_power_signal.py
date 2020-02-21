from scipy.interpolate import interp1d
from scipy.io import wavfile
import numpy as np
import numpy.matlib

import matplotlib.pyplot as plot

def get_power_signal(audio_path):
    """
    This function performs a short term analysis to calculate the power of a signal. To do so, it uses a window
    (hanning) and a shift for the window. The power is then calculate per frame.
    :param audio_path Path to the audio (wav, it does not accept wav quantised at 16 bits)
    :return: an array of the power interpolated for the whole signal
    """
    frequency, signal = wavfile.read(audio_path)

    # Total samples in the signal
    samples = # how many samples in the signal?

    # Short term analysis. In seconds
    frame_length = 0.025  # window length
    frame_period = 0.010  # window shift

    # Number of samples per frame
    frame_period = # How many samples per 10ms?
    frame_length = # How many samples per 25ms?

    # Frames
    chunks = np.arange(0, samples - frame_length, frame_period)
    n_frames = chunks.size

    prev = chunks[0]
    frames = tuple()
    for x in chunks:
        frame = signal[prev:(x + frame_length)]
        frames += (np.transpose(frame),)
        prev = x + frame_period

    frames = np.column_stack(frames)
    power = np.sum(np.power(np.multiply(frames,
                                        numpy.matlib.repmat(np.hanning(frame_length).reshape((frame_length, 1)),
                                                            1, n_frames)), 2), axis=0) / frame_length

    # Interpolate
    points = np.append([1], 1 + chunks + np.ceil(frame_period / 2))
    points = np.append(points, [samples])

    # print("samples: " + str(samples))

    # Add limits (two extra points by copying the first and last values)
    power = np.append([power[0]], power)
    power = np.append(power, power[-1])

    # print("power: " + str(power.size))

    final_power = interp1d(points, power)(np.arange(1, samples + 1))

    return final_power

# Show the power spectrum
audio_path = "archivo_audio.wav"
frequency, signal = wavfile.read(audio_path)

samples = # how many samples in the signal?

plot.subplot(211)
plot.title("Espectrograma")

plot.plot(signal)
plot.xlabel("Muestra")
plot.ylabel("Amplitud")

power = get_power_signal(audio_path)
# Power threshold (average of power in the silence)
power_threshold = # average of power in the first samples

plot.subplot(212)
plot.plot(power)

plot.plot(np.ones(samples)*power_threshold, 'r')
plot.xlabel("Muestra")
plot.ylabel("Potencia")

plot.show()
