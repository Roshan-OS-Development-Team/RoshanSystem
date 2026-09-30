import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

lines: dict[str, int] = {}
files: dict[str, int] = {"folders": 0}
chars: dict[str, int] = {}

foldersOrFilesToIgnore = {".vscode", ".idea", "__pycache__", "line_counter.py", "cmake-build-debug", "cmake-build-release", "build"}

def count_lines(filepath: str):
    with os.scandir(filepath) as entries:
        for entry in entries:
            if entry.name in foldersOrFilesToIgnore:
                continue
            elif entry.is_dir():
                count_lines(entry.path)
                files["folders"] += 1
            elif entry.is_file() and entry.name.endswith((".py", ".qss", ".json", ".html", ".cpp", ".h")):
                if not lines.get(entry.name.split(".")[-1]):
                    lines[entry.name.split(".")[-1]] = 0

                if not chars.get(entry.name.split(".")[-1]):
                    chars[entry.name.split(".")[-1]] = 0

                if not files.get(entry.name.split(".")[-1]):
                    files[entry.name.split(".")[-1]] = 0

                with open(entry.path, "r") as f:
                    lines[entry.name.split(".")[-1]] += sum(1 for line in f)

                with open(entry.path, "r") as f:
                    chars[entry.name.split(".")[-1]] += sum(1 for char in f.read())

                files[entry.name.split(".")[-1]] += 1

count_lines(".")

print()

total = sum(lines.values())

for key, line_count in lines.items():
    print(f"{key} files makes up {line_count / total:.2%} of lines of code in this project\nIt has exactly {line_count:,} lines")

print(f"\nTotal amount of lines: {total:,}")

print()

total = sum(files.values())

for key, file_count in files.items():
    print(f"{key} has {file_count / total:.2%} of the files in this project\nIt has exactly {file_count:,} files")
    
print()

print(f"Total amounts of folders or files: {total:,}")

print()

total = sum(chars.values())

for key, char_count in chars.items():
    print(f"{key} has {char_count / total:.2%} of the chars in this project\nIt has exactly {char_count:,} chars")

print(f"\nTotal amounts of chars: {total:,}")

total = 0

print()
input("Press enter to exit")
