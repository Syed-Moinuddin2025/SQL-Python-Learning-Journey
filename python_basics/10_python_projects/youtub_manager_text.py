import json
import os

# current folder path
base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, "youtube.txt")
# Load data from file
def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save data to file
def save_data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file, indent=4)

# List all videos
def list_all_videos(videos):
    if not videos:
        print("\n❌ No videos found.")
        return
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']}")

# Add a new video
def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video duration (e.g. 5:30): ")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)
    print("✅ Video added successfully.")

# Update a video
def update_video(videos):
    list_all_videos(videos)
    try:
        index = int(input("Enter the video number to update: ")) - 1
        if 0 <= index < len(videos):
            new_name = input("Enter new video name: ")
            new_time = input("Enter new video duration: ")
            videos[index]['name'] = new_name
            videos[index]['time'] = new_time
            save_data_helper(videos)
            print("✅ Video updated.")
        else:
            print("❌ Invalid video number.")
    except ValueError:
        print("❌ Please enter a valid number.")

# Delete a video
def delete_video(videos):
    list_all_videos(videos)
    try:
        index = int(input("Enter the video number to delete: ")) - 1
        if 0 <= index < len(videos):
            deleted = videos.pop(index)
            save_data_helper(videos)
            print(f"🗑️ Deleted: {deleted['name']}")
        else:
            print("❌ Invalid video number.")
    except ValueError:
        print("❌ Please enter a valid number.")

# Main menu
def main():
    videos = load_data()
    while True:
        print("\n🎬 YouTube Manager | Choose an option")
        print("1. List all YouTube videos")
        print("2. Add a YouTube video")
        print("3. Update a YouTube video")
        print("4. Delete a YouTube video")
        print("5. Exit")

        choice = input("Enter your choice: ")

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                print("👋 Exiting YouTube Manager.")
                break
            case _:
                print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()

print("Running from:", os.getcwd())