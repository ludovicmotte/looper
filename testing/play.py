import sounddevice as sd
from scipy.io.wavfile import write, read

# Sélectionne le périphérique "default" ou "pulse"
sd.default.device = 'default'  # ou 'pulse'

# Paramètres
fs = 44100
filename = 'bass.wav'

# Lecture
print("🔊 Lecture...")
fs, data = read(filename)
sd.play(data, fs)
sd.wait()
print("✅ Lecture terminée.")
