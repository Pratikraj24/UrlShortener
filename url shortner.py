import pyshorteners
from tkinter import *
from tkinter import messagebox

# Create the main window
win = Tk()
win.geometry("500x350")
win.configure(bg="sky blue")
win.title("URL Shortener")

def short():
    url = entry1.get()
    if url:
        try:
            s = pyshorteners.Shortener().tinyurl.short(url)
            entry2.delete(0, END)
            entry2.insert(END, s)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    else:
        messagebox.showwarning("Warning", "Please enter a URL")

def copy_to_clipboard():
    shortened_url = entry2.get()
    if shortened_url:
        win.clipboard_clear()
        win.clipboard_append(shortened_url)
        messagebox.showinfo("Copied", "Shortened URL copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "No URL to copy")

# Label for entering user URL
Label(win, text="Enter Your URL Link", font=("Helvetica", 18, "bold"), bg="black", fg="white").pack(fill="x", pady=10)

# Entry box for URL input
entry1 = Entry(win, font=("Helvetica", 14), bd=3, width=50)
entry1.pack(pady=10)

# Button to trigger the URL shortening
Button(win, text="Shorten URL", font=("Helvetica", 12, "bold"), bg="blue", fg="white", width=14, command=short).pack(pady=10)

# Entry box for displaying the shortened URL
entry2 = Entry(win, font=("Helvetica", 14), bg="sky blue", width=40, bd=0)
entry2.pack(pady=10)

# Button to copy the shortened URL
Button(win, text="Copy URL", font=("Helvetica", 12, "bold"), bg="green", fg="white", width=14, command=copy_to_clipboard).pack(pady=10)

# Run the Tkinter event loop
win.mainloop()
