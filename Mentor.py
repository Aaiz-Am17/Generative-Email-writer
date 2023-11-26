# gui_app.py
import tkinter as tk
from tkinter import scrolledtext
import google.generativeai as palm
import os

palm.configure(api_key="AIzaSyAn3jIMpAaeCWJFa5gudTgUj5GnqLVDkvU")

defaults = {
    'model': 'models/chat-bison-001',
    'temperature': 0.25,
    'candidate_count': 1,
    'top_k': 40,
    'top_p': 0.95,
}

class MyApp:
    context = "Given a topic, write emails in a concise, professional manner"

    def __init__(self, root):
        self.root = root
        self.root.title("Mentor App")

        # Customize font
        self.custom_font = ('Arial', 12)

        # Customize background
        self.root.configure(bg='#F0F0F0')  # Light gray background

        # Create GUI elements
        self.label = tk.Label(root, text="Welcome to Mentor App!", font=self.custom_font, bg='#F0F0F0')
        self.label.pack(pady=10)

        # Create a scrolled text widget for the chat display
        self.chat_display = scrolledtext.ScrolledText(root, width=50, height=10, font=self.custom_font, bg='white')
        self.chat_display.pack(pady=10)

        # Add an entry widget for user input
        self.user_input_entry = tk.Entry(root, width=40, font=self.custom_font)
        self.user_input_entry.pack(pady=10)

        # Create a button to send user input
        self.send_button = tk.Button(root, text="Send", command=self.send_message, font=self.custom_font)
        self.send_button.pack(pady=10)

        # Initialize messages list
        self.messages = []

    def send_message(self):
        user_input = self.user_input_entry.get()
        self.user_input_entry.delete(0, tk.END)

        self.messages.append(user_input)
        response = palm.chat(
            **defaults,
            context=MyApp.context,
            examples=[],
            messages=self.messages
        )
        ai_response = response.last
        self.display_ai_message(ai_response)

    def display_ai_message(self, message):
        self.chat_display.insert(tk.END, "AI: " + message + "\n")
        self.chat_display.yview(tk.END)

if __name__ == "__main__":
    root = tk.Tk()

    app = MyApp(root)
    root.mainloop()
