import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wavfile
import threading
import queue
from sshkeyboard import listen_keyboard, stop_listening

# Paramètres audio
samplerate = 44100
channels = 1
filename1 = "enregistrement_piste1.wav"
filename2 = "enregistrement_piste2.wav"

# États globaux
recording1 = False
recording2 = False
audio_queue = queue.Queue()
recorded_data1 = []
recorded_data2 = []
continue_listening = True

# Callback pour le flux audio
def audio_callback(indata, frames, time, status):
    if recording1 or recording2:
        audio_queue.put(indata.copy())

# Démarrer le flux audio
stream = sd.InputStream(samplerate=samplerate, channels=channels, callback=audio_callback)
stream.start()

# Thread pour collecter l'audio
def audio_collector():
    global recorded_data1, recorded_data2, continue_listening
    while continue_listening:
        if recording1 or recording2:
            try:
                data = audio_queue.get(timeout=0.1)
                # On sait qu'une seule piste est active à la fois
                if recording1:
                    recorded_data1.append(data)
                elif recording2:
                    recorded_data2.append(data)
                # Si aucune piste active, on jette les données
            except queue.Empty:
                pass
        else:
            while not audio_queue.empty():
                audio_queue.get()
            sd.sleep(100)

collector_thread = threading.Thread(target=audio_collector, daemon=True)
collector_thread.start()

# Fonction déclenchée à chaque touche
def on_key(key):
    global recording1, recording2, recorded_data1, recorded_data2, continue_listening

    # Toggle enregistrement piste 1
    if key == '1':
        # Si on commençait la piste 2, on l'arrête
        if recording2:
            recording2 = False
            print("⏹️ Piste 2 interrompue.")
            recorded_data2.clear()
        recording1 = not recording1
        if recording1:
            recorded_data1 = []
            print("🔴 Piste 1 : enregistrement démarré...")
        else:
            print("⏹️ Piste 1 : enregistrement arrêté.")
            if recorded_data1:
                audio = np.concatenate(recorded_data1, axis=0)
                # wavfile.write(filename1, samplerate, audio)
                # print(f"💾 Piste 1 sauvegardée dans {filename1}")
                # Lecture de l'enregistrement
                print("▶️ Lecture de l'enregistrement...")
                sd.play(audio, samplerate)
                sd.wait()
                print("🔈 Lecture terminée.")

    # Toggle enregistrement piste 2
    elif key == '2':
        # Si on commençait la piste 1, on l'arrête
        if recording1:
            recording1 = False
            print("⏹️ Piste 1 interrompue.")
            recorded_data1.clear()
        recording2 = not recording2
        if recording2:
            recorded_data2 = []
            print("🔴 Piste 2 : enregistrement démarré...")
        else:
            print("⏹️ Piste 2 : enregistrement arrêté.")
            if recorded_data2:
                audio = np.concatenate(recorded_data2, axis=0)
                #wavfile.write(filename2, samplerate, audio)
                #print(f"💾 Piste 2 sauvegardée dans {filename2}")
                # Lecture de l'enregistrement
                print("▶️ Lecture de l'enregistrement...")
                sd.play(audio, samplerate)
                sd.wait()
                print("🔈 Lecture terminée.")
    # Quitter le programme
    elif key in ['q', 'esc']:
        print("🛑 Arrêt du programme.")
        recording1 = False
        recording2 = False
        continue_listening = False
        stream.stop()
        stop_listening()
        return False  # arrête listen_keyboard

    return True  # continue l'écoute par défaut

print("🎹 Commandes :")
print("   '1' start/stop piste 1")
print("   '2' start/stop piste 2")
print("   'l' lecture en boucle de la dernière piste enregistrée")
print("   'q' ou 'esc' pour quitter")

# Lancer l'écoute clavier
listen_keyboard(on_press=on_key)
