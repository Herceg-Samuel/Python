## Rename Images

# Problem

I wanted to rename a lot of images.
Doing it manually is not feasable.
Decided to use python to do it for me.
Indexing starts at 1.

# Usage

Paste your file path with the folder included

```
folder_path = r"/path/to/your/folder"
```

```python
        #name can be changed to desired one
        new_name = f"product{count}{ext}"
        new_path = os.path.join(folder, new_name)
```
