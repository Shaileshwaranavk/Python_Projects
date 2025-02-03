import tkinter as tk
from pygoogle_image import image

def download_images():
    query = entry_query.get()
    num = int(entry_number.get())

    image.download(query, num)


root = tk.Tk()
root.title("Image Downloader")
root.geometry("500x250")
root.configure(bg="grey")

frame = tk.Frame(root, bg="grey")
frame.pack(expand=True)

label_query = tk.Label(frame, text="Search Query:", font=("Arial", 12), bg="grey", fg="black")
label_query.grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_query = tk.Entry(frame, width=30, font=("Arial", 12))
entry_query.grid(row=0, column=1, padx=10, pady=10)

label_number = tk.Label(frame, text="Number of Images:", font=("Arial", 12), bg="grey", fg="black")
label_number.grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry_number = tk.Entry(frame, width=30, font=("Arial", 12))
entry_number.grid(row=1, column=1, padx=10, pady=10, sticky="w")

button_download = tk.Button(frame, text="Download Images", font=("Arial", 14), bg="green", fg="black", width=20, height=2, command=download_images)
button_download.grid(row=2, column=0, columnspan=2, pady=20)

root.mainloop()