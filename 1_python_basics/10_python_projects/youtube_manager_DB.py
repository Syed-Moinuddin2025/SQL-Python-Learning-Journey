import sqlite3
import os

# ✅ Get absolute path to DB file in current folder
base_path = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(base_path, "youtube.db")

def init_db():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS videos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            duration TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_video():
    name = input("Enter video name: ")
    duration = input("Enter video duration (e.g. 5:30): ")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO videos (name, duration) VALUES (?, ?)", (name, duration))
    conn.commit()
    conn.close()
    print("Video added successfully.")

def list_videos():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM videos")
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        print("No videos found.")
    else:
        print("\nList of YouTube Videos:")
        for row in rows:
            print(f"{row[0]}. {row[1]} - Duration: {row[2]}")

def update_video():
    list_videos()
    try:
        video_id = int(input("Enter the video ID to update: "))
        new_name = input("Enter new video name: ")
        new_duration = input("Enter new duration (e.g. 5:30): ")

        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("UPDATE videos SET name = ?, duration = ? WHERE id = ?", (new_name, new_duration, video_id))
        conn.commit()
        conn.close()
        print("Video updated successfully.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def delete_video():
    list_videos()
    try:
        video_id = int(input("Enter the video ID to delete: "))
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
        conn.commit()
        conn.close()
        print("Video deleted successfully.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def main():
    init_db()
    while True:
        print("\n===== YouTube Video Manager (SQLite Version) =====")
        print("1. List all videos")
        print("2. Add a new video")
        print("3. Update a video")
        print("4. Delete a video")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            add_video()
        elif choice == '3':
            update_video()
        elif choice == '4':
            delete_video()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
