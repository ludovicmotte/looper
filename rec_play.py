import sounddevice as sd
from scipy.io.wavfile import write, read

# Sélectionne le périphérique "default" ou "pulse"
sd.default.device = 'default'  # ou 'pulse'

# Paramètres
fs = 44100
duration = 5  # secondes
filename = 'output.wav'

# Enregistrement
print("🎙️ Enregistrement...")
recording = sd.rec(int(duration * fs), samplerate=fs, channels=2, dtype='int16')
sd.wait()
write(filename, fs, recording)
print(f"✅ Enregistrement terminé : {filename}")

# Lecture
print("🔊 Lecture...")
fs, data = read(filename)
sd.play(data, fs)
sd.wait()
print("✅ Lecture terminée.")
