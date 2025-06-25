from pymongo import MongoClient
from bson import ObjectId
from bson.errors import InvalidId
# from dotenv import load_dotenv
# import os

# 🔐 Replace with your real credentials (OR use .env securely)
# load_dotenv()
# client = MongoClient(os.getenv("MONGO_URI"))



db = client["ytmanager"]
video_collection = db["videos"]

def add_video(name, time):
    video_collection.insert_one({"name": name, "time": time})
    print("✅ Video added successfully.")

def list_videos():
    videos = list(video_collection.find())
    if not videos:
        print("📭 No videos found.")
    for video in videos:
        print(f"🎥 ID: {video['_id']} | Name: {video['name']} | Time: {video['time']}")

def update_video(video_id, new_name, new_time):
    try:
        result = video_collection.update_one({'_id': ObjectId(video_id)}, {"$set": {"name": new_name, "time": new_time}})
        if result.modified_count:
            print("✅ Video updated successfully.")
        else:
            print("⚠️ No matching video found or no changes made.")
    except InvalidId:
        print("❌ Invalid video ID format.")
    except Exception as e:
        print("❌ Error updating video:", e)

def delete_video(video_id):
    try:
        result = video_collection.delete_one({"_id": ObjectId(video_id)})
        if result.deleted_count:
            print("🗑️ Video deleted successfully.")
        else:
            print("⚠️ No video found with that ID.")
    except InvalidId:
        print("❌ Invalid video ID format.")
    except Exception as e:
        print("❌ Error deleting video:", e)

def main():
    while True:
        print("\n🎬 Youtube Manager App")
        print("1. List all videos")
        print("2. Add a new video")
        print("3. Update a video")
        print("4. Delete a video")
        print("5. Exit the app")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter the video name: ").strip()
            time = input("Enter the video time: ").strip()
            if name and time:
                add_video(name, time)
            else:
                print("❗ Video name and time cannot be empty.")
        elif choice == '3':
            video_id = input("Enter the video ID to update: ").strip()
            name = input("Enter the new name: ").strip()
            time = input("Enter the new time: ").strip()
            if name and time:
                update_video(video_id, name, time)
            else:
                print("❗ Name and time cannot be empty.")
        elif choice == '4':
            video_id = input("Enter the video ID to delete: ").strip()
            delete_video(video_id)
        elif choice == '5':
            confirm = input("Are you sure you want to exit? (y/n): ").lower()
            if confirm == 'y':
                print("👋 Exiting. Goodbye!")
                break
        else:
            print("❗ Invalid choice, try again.")

if __name__ == "__main__":
    main()
