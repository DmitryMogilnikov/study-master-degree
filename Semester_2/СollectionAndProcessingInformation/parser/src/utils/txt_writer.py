from pathlib import Path


def write_txt(output_path, text):
    with open(output_path, 'w') as txt_file:
        txt_file.write(text)


def get_output_path(path: str) -> str:
    output_file_name = Path(path).stem
    output_path = '../../files/outputs/'
    return f'{output_path}/{output_file_name}.txt'
