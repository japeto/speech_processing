import matplotlib.pyplot as plot
from scipy.io import wavfile

# Read the signal
sampling, signal = wavfile.read("archivo_de_audio.wav")

# Show both spectrogram and waveform in the same figure.
plot.subplot(211)
plot.title("Espectrograma")

# Waveform
plot.plot(signal)
plot.xlabel("Muestra")
plot.ylabel("Amplitud")

plot.subplot(212)

# Spectrogram short window -> broadband analysis (better time resolution)
plot.specgram(signal, Fs=sampling, NFFT=512) 
plot.axis(ymin=0, ymax=10000)
plot.xlabel("Tiempo")
plot.ylabel("Frecuencia")

# plot.savefig("espectrograma_10kHz.png")
plot.show()
