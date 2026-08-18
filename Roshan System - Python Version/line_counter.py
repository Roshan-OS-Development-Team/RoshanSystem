import os

lines: int = 0

def count_lines(filepath: str):
    global lines
    with os.scandir(filepath) as entries:
        for entry in entries:
            if entry.name == ".vscode" or entry.name == ".idea" or entry.name == "__pycache__":
                continue
            elif entry.is_dir():
                count_lines(entry.path)
            elif entry.is_file() and entry.name.endswith((".py", ".qss", ".json", ".html")):
                with open(entry.path, "r") as f:
                    lines += sum(1 for line in f)

count_lines(".")
print(lines)
