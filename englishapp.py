import tkinter as tk
from tkinter import messagebox

class ITSupportChat:
    def __init__(self, root):
        self.root = root
        self.root.title("IT Support Chat")

        self.conversation_text = tk.Text(root, height=10, width=50, wrap=tk.WORD)
        self.conversation_text.pack(pady=10)

        self.options = ["My computer is running very slow", "I have a problem with my printer", "I need to install new software on my computer"]
        self.client_choice = tk.StringVar()
        self.client_choice.set(self.options[0])

        self.option_menu = tk.OptionMenu(root, self.client_choice, *self.options)
        self.option_menu.pack(pady=10)

        self.btn_send = tk.Button(root, text="Send", command=self.respond_to_client)
        self.btn_send.pack(pady=10)

        self.conversation = []
        self.current_step = 0
        self.setup_conversation()

    def setup_conversation(self):
        self.conversation = [
            ("informatico", "Hello! How can I help you?")
        ]
        self.display_next_message()

    def display_next_message(self):
        if self.current_step < len(self.conversation):
            speaker, message = self.conversation[self.current_step]
            self.conversation_text.insert(tk.END, f"{speaker.capitalize()}: {message}\n\n")
            self.current_step += 1
            if speaker == "cliente":
                self.option_menu.config(state=tk.NORMAL)
                self.btn_send.config(state=tk.NORMAL)
            else:
                self.option_menu.config(state=tk.DISABLED)
                self.btn_send.config(state=tk.DISABLED)
        else:
            self.conversation_text.insert(tk.END, "Conversation ended.")

    def respond_to_client(self):
        client_choice = self.client_choice.get()
        if client_choice == "My computer is running very slow":
            self.conversation.append(("informatico", "Have you tried deleting unnecessary files?"))
        elif client_choice == "I have a problem with my printer":
            self.conversation.append(("informatico", "Is it displaying any error messages?"))
        elif client_choice == "I need to install new software on my computer":
            self.conversation.append(("informatico", "Do you have the installation disk or file?"))
        else:
            self.conversation.append(("informatico", "I'm sorry, I didn't understand."))
            return

        self.display_next_message()


if __name__ == "__main__":
    root = tk.Tk()
    chat = ITSupportChat(root)
    root.mainloop()
