import tkinter as tk
from tkinter import filedialog, messagebox
import speech_recognition as sr

def transcribe_audio(file_path):
    """Transcribes audio from the provided file path using SpeechRecognition."""
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(file_path) as source:
            audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data)
        return text
    except sr.UnknownValueError:
        return "Speech was unintelligible."
    except sr.RequestError as e:
        return f"API error: {e}"

def open_file():
    """Opens a file dialog to select an audio file."""
    file_path = filedialog.askopenfilename(
        filetypes=[("Audio Files", "*.wav")]
    )
    if file_path:
        try:
            transcription = transcribe_audio(file_path)
            output_text.delete(1.0, tk.END)
            output_text.insert(tk.END, transcription)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

# Create the main window
root = tk.Tk()
root.title("Speech-to-Text System")
root.geometry("600x400")

# Add a label
label = tk.Label(root, text="Speech-to-Text System", font=("Arial", 16))
label.pack(pady=10)

# Add a button to open audio file
open_button = tk.Button(root, text="Open Audio File", command=open_file, font=("Arial", 12))
open_button.pack(pady=10)

# Add a text box to display transcription
output_text = tk.Text(root, wrap=tk.WORD, height=15, font=("Arial", 12))
output_text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Add a quit button
quit_button = tk.Button(root, text="Quit", command=root.quit, font=("Arial", 12))
quit_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
