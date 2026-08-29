import os

lines: int = 0
item_count: int = 0
chars: int = 0

def count_lines(filepath: str):
    global lines, item_count, chars
    with os.scandir(filepath) as entries:
        for entry in entries:
            if entry.name == ".vscode" or entry.name == ".idea" or entry.name == "__pycache__":
                continue
            elif entry.is_dir():
                count_lines(entry.path)
            elif entry.is_file() and entry.name.endswith((".py", ".qss", ".json", ".html")):
                with open(entry.path, "r") as f:
                    lines += sum(1 for line in f)

                with open(entry.path, "r") as f:
                    chars += sum(1 for _ in range(len(f.read())))

            item_count += 1

count_lines(".")
print(f"{lines:,}")
print(f"{item_count:,}")
print(f"{chars:,}")
