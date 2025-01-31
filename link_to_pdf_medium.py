import pdfkit
import tkinter as tk
from tkinter import filedialog

def save_webpage_as_pdf(url):
    root = tk.Tk()
    root.withdraw
    output_pdf = filedialog.asksaveasfilename(defaultextension=".pdf",
                                              filetypes=[("PDF files", "*.pdf"),("All files", "*.*")],
                                              title="Save PDF As")
    if not output_pdf:
        print("No file selected. Exiting.")
        return
    try:
        options = {
            'enable-local-file-access': True,
            'quiet': ''

        }
        pdfkit.from_url(url, output_pdf , options=options)
        print(F"PDF successfuly saved as : {output_pdf}")
    except Exception as e:
        print(f"Error Occured: {e}")
url = input("Enter the URL of the Webpage (HTML/PHP/Others):  ")
save_webpage_as_pdf(url)