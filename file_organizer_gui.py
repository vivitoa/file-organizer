import os
import shutil
import tkinter as tk
from tkinter import messagebox, filedialog

# Function to organize files
def organize_files(folder):
    file_categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Documents": [".pdf", ".docx", ".txt", ".pptx", ".ppsx", ".xlsx", ".doc", ".ppt", ".xls"],
        "Videos": [".mp4", ".mkv", ".avi", ".wmv"],
        "Music": [".mp3", ".wav", ".m4a"],
        "Applications": [".exe"],
        "Compressed Files": [".zip", ".rar"],
        "Torrent Files": [".tgz", ".torrent"]
    }

    for category in file_categories:
        category_path = os.path.join(folder, category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)

    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        if os.path.isfile(file_path):
            for category, extensions in file_categories.items():
                if any(filename.lower().endswith(ext) for ext in extensions):
                    shutil.move(file_path, os.path.join(folder, category))
                    break

    messagebox.showinfo("Success", "Files have been organized!")

# Function to ask user for folder
def select_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        organize_files(folder_selected)

# Create GUI window
root = tk.Tk()
root.title("File Organizer")

# Create and place the button
organize_button = tk.Button(root, text="Organize Files", command=select_folder)
organize_button.pack(pady=20)

# Run the GUI event loop
root.mainloop()
