import tkinter as tk
from time import time
from sentences import sentences_bank
import random

class TypingSpeedTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        
        self.test_text = f"{sentences_bank[random.randint(0, len(sentences_bank) - 1)]['text']}"
        self.start_time = 0
        self.end_time = 0
        
        self.text_label = tk.Label(root, text=self.test_text, wraplength=400)
        self.text_label.pack(pady=20)
        
        self.text_entry = tk.Entry(root, font=("Helvetica", 16), width=50)
        self.text_entry.pack(pady=10)
        self.text_entry.bind("<Return>", self.calculate_speed)
        
        self.result_label = tk.Label(root, text="", font=("Helvetica", 14))
        self.result_label.pack(pady=20)

    def calculate_speed(self, event):
        self.end_time = time()
        typed_text = self.text_entry.get()
        word_count = len(typed_text.split())
        time_elapsed = self.end_time - self.start_time
        wpm = round((word_count / time_elapsed) * 60, 2)
        self.result_label.config(text=f"Your typing speed: {wpm} WPM")

    def run_test(self):
        self.start_time = time()
        self.text_entry.focus()