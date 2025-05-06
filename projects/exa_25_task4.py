def read_file(file_path: str) -> str:
    with open(file_path) as file:
        return file.read()