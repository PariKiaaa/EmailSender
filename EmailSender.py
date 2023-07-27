import smtplib
import tkinter as tk
from tkinter import messagebox

def send_email():
    gmail_user = email_entry.get()
    gmail_password = password_entry.get()
    to_emails = to_entry.get().split(',')
    subject = subject_entry.get()
    body = body_text.get("1.0", "end")

    email_text = f"""\
From: {gmail_user}
To: {", ".join(to_emails)}
Subject: {subject}

{body}
"""
# Create the main window
window = tk.Tk()
window.title("Email Sender")
window.geometry("400x400")
window.configure(bg="#f0f0f0")  # Set the background color

# Create and place the widgets with colorful styling
tk.Label(window, text="Email:", fg="blue", font=("Arial", 12, "bold"), bg="#f0f0f0").pack(pady=5)
email_entry = tk.Entry(window, font=("Arial", 12))
email_entry.pack()

tk.Label(window, text="Password:", fg="blue", font=("Arial", 12, "bold"), bg="#f0f0f0").pack(pady=5)
password_entry = tk.Entry(window, show="*", font=("Arial", 12))
password_entry.pack()

tk.Label(window, text="To (separate multiple emails with commas):", fg="blue", font=("Arial", 12, "bold"), bg="#f0f0f0").pack(pady=5)
to_entry = tk.Entry(window, font=("Arial", 12))
to_entry.pack()

tk.Label(window, text="Subject:", fg="blue", font=("Arial", 12, "bold"), bg="#f0f0f0").pack(pady=5)
subject_entry = tk.Entry(window, font=("Arial", 12))
subject_entry.pack()

tk.Label(window, text="Body:", fg="blue", font=("Arial", 12, "bold"), bg="#f0f0f0").pack(pady=5)
body_text = tk.Text(window, width=40, height=10, font=("Arial", 12))
body_text.pack()

send_button = tk.Button(window, text="Send Email", command=send_email, bg="green", fg="white", font=("Arial", 12, "bold"))
send_button.pack(pady=10)

# Start the main event loop
window.mainloop()
