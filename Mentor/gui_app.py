import tkinter as tk
from tkinter import scrolledtext
from dotenv import load_dotenv
import google.generativeai as palm
import os

# Load environment variables from .env file
load_dotenv()

# Configure PaLM API using API key from .env
palm.configure(api_key=os.getenv("PALM_API_KEY"))

# Default configuration for the API
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
        self.root.title("Mentor Email Writer")

        # Customize font and background
        self.custom_font = ('Arial', 12)
        self.root.configure(bg='#F0F0F0')

        # Title Label
        self.label = tk.Label(root, text="Welcome to Mentor App!", font=self.custom_font, bg='#F0F0F0')
        self.label.pack(pady=10)

        # Chat Display Area
        self.chat_display = scrolledtext.ScrolledText(root, width=50, height=10, font=self.custom_font, bg='white')
        self.chat_display.pack(pady=10)

        # User Input Entry
        self.user_input_entry = tk.Entry(root, width=40, font=self.custom_font)
        self.user_input_entry.pack(pady=10)

        # Send Button
        self.send_button = tk.Button(root, text="Send", command=self.send_message, font=self.custom_font)
        self.send_button.pack(pady=10)

        # Store conversation history
        self.messages = []

    def send_message(self):
        user_input = self.user_input_entry.get()
        self.user_input_entry.delete(0, tk.END)

        if user_input.strip() == "":
            return  # Ignore empty messages

        self.messages.append(user_input)

        try:
            response = palm.chat(
                **defaults,
                context=MyApp.context,
                examples=[],
                messages=self.messages
            )
            ai_response = response.last
            self.display_ai_message(ai_response)
        except Exception as e:
            self.display_ai_message(f"Error: {e}")

    def display_ai_message(self, message):
        self.chat_display.insert(tk.END, "AI: " + message + "\n")
        self.chat_display.yview(tk.END)

# Main entry point
if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()
