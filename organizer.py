from pathlib import Path
import shutil

CATEGORIES = {
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp"},
    "Videos": {".mp4", ".mkv", ".avi", ".mov", ".webm"},
    "Audio": {".mp3", ".wav", ".flac", ".m4a", ".ogg"},
    "Documents": {".pdf", ".doc", ".docx", ".txt", ".rtf"},
    "Archives": {".zip", ".rar", ".7z", ".tar", ".gz"},
}


def category_for(path):
    extension = path.suffix.lower()

    for category, extensions in CATEGORIES.items():
        if extension in extensions:
            return category

    return "Other"


def organize(folder):
    folder = Path(folder).expanduser().resolve()

    if not folder.is_dir():
        print("Folder not found.")
        return

    for item in folder.iterdir():

        if not item.is_file():
            continue

        category = category_for(item)
        destination = folder / category
        destination.mkdir(exist_ok=True)

        target = destination / item.name

        if target.exists():
            stem = item.stem
            suffix = item.suffix
            counter = 1

            while target.exists():
                target = destination / f"{stem}_{counter}{suffix}"
                counter += 1

        shutil.move(str(item), str(target))

        print(f"Moved: {item.name} -> {category}/")


if __name__ == "__main__":
    folder = input("Enter the folder path to organize: ").strip()
    organize(folder)
