import pyttsx3
import os
import time

def print_banner():
    banner = """
    ╔══════════════════════════════════════════════════════╗
    ║          Voice Spoofing Simulator v1.0                ║
    ║   Coded by Pakistani Ethical Hacker: Mr. Sabaz Ali Khan  ║
    ║                                                      ║
    ║   Simulate voice manipulation with text-to-speech!    ║
    ╚══════════════════════════════════════════════════════╝
    """
    print(banner)
    time.sleep(1)

def initialize_engine():
    engine = pyttsx3.init()
    return engine

def list_voices(engine):
    voices = engine.getProperty('voices')
    print("\nAvailable Voices:")
    for index, voice in enumerate(voices):
        print(f"{index}: {voice.name} (ID: {voice.id})")
    return voices

def set_voice_properties(engine, voice_index, rate, volume, pitch):
    voices = engine.getProperty('voices')
    if 0 <= voice_index < len(voices):
        engine.setProperty('voice', voices[voice_index].id)
    engine.setProperty('rate', rate)
    engine.setProperty('volume', volume)
    # Pitch is not directly supported in pyttsx3, but we can simulate it
    print(f"\nSimulating pitch adjustment to {pitch} (Note: pyttsx3 has limited pitch control)")

def speak_text(engine, text):
    engine.say(text)
    engine.runAndWait()

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print_banner()
    
    engine = initialize_engine()
    voices = list_voices(engine)
    
    while True:
        print("\nVoice Spoofing Simulator Menu:")
        print("1. Select Voice")
        print("2. Set Speech Rate (words per minute)")
        print("3. Set Volume (0.0 to 1.0)")
        print("4. Set Pitch (simulated, 0.5 to 2.0)")
        print("5. Enter Text to Speak")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ")
        
        if choice == '1':
            try:
                voice_index = int(input("Enter voice index (from available voices): "))
                if voice_index < 0 or voice_index >= len(voices):
                    print("Invalid voice index!")
                else:
                    print(f"Selected voice: {voices[voice_index].name}")
            except ValueError:
                print("Please enter a valid number!")
                
        elif choice == '2':
            try:
                rate = int(input("Enter speech rate (default 200): "))
                if rate < 50 or rate > 500:
                    print("Rate must be between 50 and 500!")
                else:
                    print(f"Speech rate set to {rate}")
            except ValueError:
                print("Please enter a valid number!")
                
        elif choice == '3':
            try:
                volume = float(input("Enter volume (0.0 to 1.0): "))
                if volume < 0.0 or volume > 1.0:
                    print("Volume must be between 0.0 and 1.0!")
                else:
                    print(f"Volume set to {volume}")
            except ValueError:
                print("Please enter a valid number!")
                
        elif choice == '4':
            try:
                pitch = float(input("Enter pitch multiplier (0.5 to 2.0): "))
                if pitch < 0.5 or pitch > 2.0:
                    print("Pitch must be between 0.5 and 2.0!")
                else:
                    print(f"Pitch set to {pitch} (simulated)")
            except ValueError:
                print("Please enter a valid number!")
                
        elif choice == '5':
            text = input("Enter text to speak: ")
            if not text.strip():
                print("Text cannot be empty!")
            else:
                try:
                    voice_index = voice_index if 'voice_index' in locals() else 0
                    rate = rate if 'rate' in locals() else 200
                    volume = volume if 'volume' in locals() else 1.0
                    pitch = pitch if 'pitch' in locals() else 1.0
                    set_voice_properties(engine, voice_index, rate, volume, pitch)
                    print(f"Speaking: {text}")
                    speak_text(engine, text)
                except Exception as e:
                    print(f"Error during speech: {e}")
                
        elif choice == '6':
            print("\nThank you for using Voice Spoofing Simulator by Mr. Sabaz Ali Khan!")
            break
        else:
            print("Invalid choice! Please select 1-6.")

if __name__ == "__main__":
    main()