from pathlib import Path


def check_path(path, suffix):
    if not Path(path).is_file():
        raise FileNotFoundError("Incorrect path to file")
    if not Path(path).suffix == suffix:
        raise TypeError("File has incorrect type")
