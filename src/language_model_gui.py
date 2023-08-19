import tkinter as tk
from language_model_assistant import LanguageModelAssistant 

"""
  +-------------+         +------------------+           +------------------+         +------------------+
  |  record.py  | ------> | voice-to-text.py | ------> | text-to-chatgpt.py | ------> | text-to-voice.py |
  +-------------+         +------------------+           +------------------+         +------------------+
"""

class App:

    def __init__(self, master):
        self.lma = LanguageModelAssistant()
        self.master = master
        master.title("Language Model Assistant")
        master.geometry("400x200")

        self.transcribed_text = tk.StringVar()
        self.transcribed_text.set("Transcribed text will appear here")

        self.transcribed_label = tk.Label(master, textvariable=self.transcribed_text)
        self.transcribed_label.pack()

        self.record_button = tk.Button(master, text="Record", command=self.lma.record)
        self.record_button.pack()
        # set the 
        

        self.send_button = tk.Button(master, text="Send", command=self.lma.text_to_chatgpt)
        self.send_button.pack()

        self.textbox = tk.Text(master, height=5, width=50)
        self.textbox.pack()
        

        self.chatgpt_reply = ""


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()