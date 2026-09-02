import os

lines: dict[str, int] = {}
file_count: dict[str, int] = {"folders": 0}
chars: dict[str, int] = {}

def count_lines(filepath: str):
    global lines, file_count, chars
    with os.scandir(filepath) as entries:
        for entry in entries:
            if entry.name == ".vscode" or entry.name == ".idea" or entry.name == "__pycache__":
                continue
            elif entry.is_dir():
                count_lines(entry.path)
                file_count["folders"] += 1
            elif entry.is_file() and entry.name.endswith((".py", ".qss", ".json", ".html")):
                if not lines.get(entry.name.split(".")[-1]):
                    lines[entry.name.split(".")[-1]] = 0

                if not chars.get(entry.name.split(".")[-1]):
                    chars[entry.name.split(".")[-1]] = 0

                if not file_count.get(entry.name.split(".")[-1]):
                    file_count[entry.name.split(".")[-1]] = 0

                with open(entry.path, "r") as f:
                    lines[entry.name.split(".")[-1]] += sum(1 for line in f)

                with open(entry.path, "r") as f:
                    chars[entry.name.split(".")[-1]] += sum(1 for char in f.read())

                file_count[entry.name.split(".")[-1]] += 1

count_lines(".")
print(file_count)
print(lines)
print(chars)
