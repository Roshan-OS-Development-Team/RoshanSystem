import os

line_count: int = 0


def count_lines(filepath: str):
    global line_count
    with os.scandir(filepath) as files:
        for file in files:
            if (
                file == ".idea"
                or file == ".vscode"
                or file == "__pycache__"
                or file == "textures"
            ):
                continue
            elif file.is_dir():
                count_lines(file.path)
            elif file.is_file() and file.name.endswith((".py", ".qss", ".json", ".html")):
                try:
                    with open(file.path, "r") as f:
                        line_count += sum(1 for line in f)
                except UnicodeDecodeError:
                    continue


count_lines(os.path.abspath(os.path.dirname(__file__)))
print(f"{line_count:,}")
