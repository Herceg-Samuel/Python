import os

folder_path = r"/path/to/your/folder"   # ← Change this to your folder


def rename_images(folder):
    files = sorted(os.listdir(folder))
    count = 1

    for file in files:
        old_path = os.path.join(folder, file)

        # Skip directories
        if os.path.isdir(old_path):
            continue

        # Get the file extension
        _, ext = os.path.splitext(file)
        
        # Only rename image extensions (optional)
        if ext.lower() not in [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"]:
            continue

        #name can be changed to desired one
        new_name = f"product{count}{ext}"
        new_path = os.path.join(folder, new_name)

        os.rename(old_path, new_path)
        count += 1

    print("Renaming completed!")

rename_images(folder_path)
