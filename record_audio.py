import sounddevice as sd
import wavio
import time

def record_audio(filename, duration, sample_rate=22050):
    print("Recording will start in 3 seconds. Prepare yourself...")
    time.sleep(3)  # Countdown to start recording
    print("Recording...")

    # Record audio
    audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1)
    sd.wait()  # Wait until recording is finished

    # Save audio as .wav file
    wavio.write(filename, audio, sample_rate, sampwidth=2)
    print(f"Recording saved as {filename}")

# Example usage
if __name__ == "__main__":
    duration =10 # Duration in seconds for each sentence
    filename = "sentence017.wav"  # Update this filename for each new sentence
    record_audio(filename, duration)
