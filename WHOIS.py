####install the whois packeg
import subprocess
import sys
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    import whois
except ImportError:
    install("python-whois")


    #####The orignal code with no gui or chatgpt modifcations simple 3 lines of code

# website= input("website URL: ")
# res = whois.whois(website)
# print(res)

   ######Code with GUI With the help of Chatgpt

import tkinter as tk
from tkinter import messagebox

class WhoisGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("WHOIS Lookup")
        self.root.geometry("400x300")
        self.root.config(bg="#2E4053")

        self.setup_ui()

    def setup_ui(self):
        self.url_label = tk.Label(self.root, text="Enter Website URL:", bg="#2E4053", fg="white", font=("Helvetica", 12))
        self.url_label.pack(pady=10)

        self.url_entry = tk.Entry(self.root, width=40, font=("Helvetica", 12))
        self.url_entry.pack(pady=10)

        self.lookup_button = tk.Button(self.root, text="Lookup", command=self.perform_lookup, bg="#5DADE2", fg="white", font=("Helvetica", 12))
        self.lookup_button.pack(pady=10)

        self.result_text = tk.Text(self.root, wrap=tk.WORD, font=("Helvetica", 10), bg="#34495E", fg="white")
        self.result_text.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

    def perform_lookup(self):
        domain = self.url_entry.get()
        if domain:
            try:
                domain_info = whois.whois(domain)
                self.result_text.delete(1.0, tk.END)
                self.result_text.insert(tk.END, str(domain_info))
            except Exception as e:
                messagebox.showerror("Error", f"Error performing WHOIS lookup: {e}")
        else:
            messagebox.showwarning("Input Error", "Please enter a website URL.")

if __name__ == "__main__":
    root = tk.Tk()
    app = WhoisGUI(root)
    root.mainloop()