import os
from tqdm import tqdm  # Import tqdm for progress bar

def create_if_not_exist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def move(folder_name, files):
    count = 0
    for file in tqdm(files, desc=f"Moving to {folder_name}", unit="file"):
        destination = os.path.join(folder_name, file)
        # os.replace() is used to move files or directories
        try:
            os.replace(file, destination)
            count += 1
        except Exception as e:
            print(f"Error moving {file} to {folder_name}: {e}")
    return count

files = os.listdir()
# We don't want to include main.py in any other file so we use this command 
files.remove("main.py")

create_if_not_exist('Images')
create_if_not_exist('Docs')
create_if_not_exist('Media')
create_if_not_exist('Others')

# Get image file extensions
img_exts = [".png", ".jpg", ".jpeg", ".gif"]
images = [file for file in files if os.path.splitext(file)[1].lower() in img_exts]

# Get document file extensions
doc_exts = [".txt", ".docx", ".doc", ".pdf"]
docs = [file for file in files if os.path.splitext(file)[1].lower() in doc_exts]

# Get media file extensions
media_exts = [".mp4", ".mp3", ".flv"]
medias = [file for file in files if os.path.splitext(file)[1].lower() in media_exts]

# Collect files that do not match any of the specified extensions
others = []
for file in files:
    ext = os.path.splitext(file)[1].lower()
    if (ext not in img_exts) and (ext not in doc_exts) and (ext not in media_exts) and os.path.isfile(file):
        others.append(file)

# Move files to their respective folders with progress bar
image_count = move("Images", images)
doc_count = move("Docs", docs)
media_count = move("Media", medias)
other_count = move("Others", others)

# Summary of moved files
print(f"\nSummary of files moved:")
print(f"Images: {image_count}")
print(f"Documents: {doc_count}")
print(f"Media: {media_count}")
print(f"Others: {other_count}")
