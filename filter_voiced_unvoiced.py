import matplotlib.pyplot as plot
from scipy.io import wavfile
import numpy as np

from get_power_signal import get_power_signal
from get_zero_crossing import get_zero_crossing

audio_path = "archivo_de_audio.wav"
# audio_path = "sample.wav"
frequency, signal = wavfile.read(audio_path)
samples = # how many samples in the signal?

plot.subplot(311)
plot.title("Espectrograma")

plot.plot(signal)
plot.xlabel("Muestra")
plot.ylabel("Amplitud")

power = get_power_signal(audio_path)
power_threshold = # average of power in the first samples
print(power_threshold)

plot.subplot(312)
plot.plot(power)

plot.plot(np.ones(samples)*power_threshold, 'r')
plot.xlabel("Muestra")
plot.ylabel("Potencia")

zero_crossing = get_zero_crossing(audio_path)
zero_crossing_threshold = 1800

plot.subplot(313)
plot.plot(zero_crossing)
plot.plot(np.ones(samples)*zero_crossing_threshold, 'r')
plot.xlabel("Muestra")
plot.ylabel("Cruce Cero")

# Voiced identification
voiced = np.where(np.logical_and(zero_crossing<zero_crossing_threshold, power>power_threshold),
         np.ones(samples), np.zeros(samples))
voiced_part =np.multiply(signal,voiced)
plot.subplot(311)
plot.plot(voiced_part)

plot.show()
# plot.savefig("clasificacion.png")