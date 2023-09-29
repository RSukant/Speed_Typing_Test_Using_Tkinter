import tkinter as tk
import random
import time

sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is a high-level programming language.",
    "Practice makes perfect.",
    "Coding is fun and challenging.",
    "I love programming!",
]

class TypingTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Speed Typing Test")
        
        self.label = tk.Label(root, text="Welcome to the Speed Typing Test!")
        self.label.pack(padx=500,pady=300)
        
        self.start_button = tk.Button(root, text="Start", command=self.start_typing_test)
        self.start_button.pack()
        
    def start_typing_test(self):
        self.label.config(text="")
        self.start_button.config(state=tk.DISABLED)
        
        sentence = random.choice(sentences)
        
        self.sentence_label = tk.Label(self.root, text=sentence)
        self.sentence_label.pack(pady=10)
        
        self.entry = tk.Entry(self.root)
        self.entry.pack()
        
        self.submit_button = tk.Button(self.root, text="Submit", command=self.submit)
        self.submit_button.pack()
        
        self.start_time = time.time()
        
    def submit(self):
        user_input = self.entry.get()
        end_time = time.time()
        
        elapsed_time = end_time - self.start_time
        words_per_minute = self.calculate_words_per_minute(sentences[0], user_input, elapsed_time)
        
        result_text = f"You typed at {words_per_minute:.2f} words per minute!"
        self.result_label = tk.Label(self.root, text=result_text)
        self.result_label.pack(pady=10)
        
        self.start_button.config(state=tk.NORMAL)
        
        self.sentence_label.destroy()
        self.entry.destroy()
        self.submit_button.destroy()
        
    def calculate_words_per_minute(self, actual_sentence, typed_sentence, elapsed_time):
        actual_words = actual_sentence.split()
        typed_words = typed_sentence.split()
        
        correct_words = 0
        
        for actual_word, typed_word in zip(actual_words, typed_words):
            if actual_word == typed_word:
                correct_words += 1
        
        words_per_minute = (correct_words / elapsed_time) * 60
        return round(words_per_minute, 2)

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingTestApp(root)
    root.mainloop()
