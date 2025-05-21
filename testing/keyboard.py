from sshkeyboard import listen_keyboard, stop_listening

recording = False

def press(key):
    global recording
    if key == '1':
        recording = not recording
        if recording:
            print("🔴 Enregistrement démarré...")
        else:
            print("⏹️ Enregistrement arrêté.")
            print("▶️ Lecture...")
    elif key in ['q', 'esc']:
        print("🛑 Arrêt du programme.")
        stop_listening()

print("Appuyez sur '1' pour démarrer/arrêter l'enregistrement. Appuyez sur 'q' ou 'esc' pour quitter.")
listen_keyboard(on_press=press)
