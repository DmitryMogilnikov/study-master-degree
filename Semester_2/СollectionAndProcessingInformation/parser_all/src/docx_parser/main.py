from docx_parser import ParserDOCX
from src.utils.txt_writer import write_txt

if __name__ == '__main__':
    path = input('File path to parse:')
    docx_parser = ParserDOCX()

    docx_parser.extract_all_text(path)

    docx_parser.extract_all_text(path)
    write_txt(docx_parser)
