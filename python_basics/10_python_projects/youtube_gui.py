import tkinter as tk
from tkinter import messagebox, simpledialog
import json

import os

# current folder path
base_path = os.path.dirname(__file__)
text_path = os.path.join(base_path, "youtubegui.txt")
DATA_FILE = "youtube_gui.txt"

# Load data
def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save data
def save_data(videos):
    with open(DATA_FILE, "w") as file:
        json.dump(videos, file, indent=4)

# GUI Application
class YouTubeManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Video Manager")

        self.videos = load_data()

        # Listbox
        self.listbox = tk.Listbox(root, width=50)
        self.listbox.pack(pady=10)

        # Buttons
        btn_frame = tk.Frame(root)
        btn_frame.pack()

        tk.Button(btn_frame, text="Add Video", width=15, command=self.add_video).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Update Video", width=15, command=self.update_video).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Delete Video", width=15, command=self.delete_video).grid(row=0, column=2, padx=5)

        self.load_to_listbox()

    def load_to_listbox(self):
        self.listbox.delete(0, tk.END)
        for video in self.videos:
            display_text = f"{video['name']} - {video['time']}"
            self.listbox.insert(tk.END, display_text)

    def add_video(self):
        name = simpledialog.askstring("Add Video", "Enter video name:")
        if name:
            time = simpledialog.askstring("Add Video", "Enter video duration (e.g. 5:30):")
            if time:
                self.videos.append({'name': name, 'time': time})
                save_data(self.videos)
                self.load_to_listbox()
                messagebox.showinfo("Success", "Video added successfully.")

    def update_video(self):
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showwarning("Warning", "Select a video to update.")
            return
        index = selected[0]
        current_video = self.videos[index]

        new_name = simpledialog.askstring("Update Video", "Enter new video name:", initialvalue=current_video['name'])
        if new_name:
            new_time = simpledialog.askstring("Update Video", "Enter new duration:", initialvalue=current_video['time'])
            if new_time:
                self.videos[index] = {'name': new_name, 'time': new_time}
                save_data(self.videos)
                self.load_to_listbox()
                messagebox.showinfo("Success", "Video updated successfully.")

    def delete_video(self):
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showwarning("Warning", "Select a video to delete.")
            return
        index = selected[0]
        confirm = messagebox.askyesno("Confirm", f"Delete '{self.videos[index]['name']}'?")
        if confirm:
            del self.videos[index]
            save_data(self.videos)
            self.load_to_listbox()
            messagebox.showinfo("Deleted", "Video deleted successfully.")

# Run App
if __name__ == "__main__":
    root = tk.Tk()
    app = YouTubeManagerApp(root)
    root.mainloop()
