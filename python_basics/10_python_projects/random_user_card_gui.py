import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import requests
from io import BytesIO

# 🔸 GUI Window Setup
root = tk.Tk()
root.title("🎲 Random User Card")
root.geometry("300x350")

# 🔸 Variables to Hold Data
name_var = tk.StringVar()
email_var = tk.StringVar()

# 🔸 Image Label Placeholder (initial blank)
image_label = tk.Label(root)
image_label.pack(pady=10)

# 🔸 Name & Email Labels
ttk.Label(root, text="Name:", font=("Arial", 10)).pack()
ttk.Label(root, textvariable=name_var, font=("Arial", 12, "bold")).pack()

ttk.Label(root, text="Email:", font=("Arial", 10)).pack()
ttk.Label(root, textvariable=email_var, font=("Arial", 10)).pack()

# 🔸 Function to Fetch User from API
def fetch_user():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json().get('data', {})
        print(data)  # Debugging purpose

        # Get full name
        full_name = f"{data['name']['title']} {data['name']['first']} {data['name']['last']}"
        email = data.get('email', 'No Email')

        # Get image URL from nested dictionary
        img_url = data.get('picture', {}).get('large')

        name_var.set(full_name)
        email_var.set(email)

        if img_url:
            try:
                img_response = requests.get(img_url)
                img_data = img_response.content
                img = Image.open(BytesIO(img_data)).resize((100, 100))
                photo = ImageTk.PhotoImage(img)

                image_label.config(image=photo)
                image_label.image = photo  # Prevent garbage collection
            except Exception as e:
                print("Image Error:", e)
                image_label.config(text="Image Load Error")
        else:
            image_label.config(image='', text="No Image Found")
    else:
        name_var.set("Error fetching user")
        email_var.set("Try again later")

ttk.Button(root, text="Fetch Random User", command=fetch_user).pack(pady=20)

# GUI window launch karega
root.mainloop()
