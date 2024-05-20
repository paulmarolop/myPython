import tkinter as tk
from time import time
from typingspeed import TypingSpeedTest

def main():
    root = tk.Tk()
    app = TypingSpeedTest(root)
    app.run_test()
    root.mainloop()

if __name__ == "__main__":
    main()
