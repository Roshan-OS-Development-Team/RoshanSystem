import os


def get_qss_styles(filepath: str):
    styles: dict[str, str] = {}
    with os.scandir(filepath) as files:
        for file in files:
            if file.is_file() and file.name.endswith(".qss"):
                with open(file.path, "r") as f:
                    styles[file.name.removesuffix(".qss")] = f.read().strip()
            else:
                continue

    return styles
