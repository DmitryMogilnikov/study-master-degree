import docx
import re

from src.abstract_parser.abstract_parser import AbstractParser
from src.utils.path_checker import check_path
from src.utils.txt_writer import write_txt, get_output_path


class ParserDOCX(AbstractParser):

    @staticmethod
    def extract_all_text(path):
        check_path(path, suffix='.docx')
        document = docx.Document(path)
        text = '\n'.join(par.text for par in document.paragraphs)
        text = '\n'.join(
            line.strip() for line in re.findall(r'.{1,100}(?:\s+|$)', text)
        )

        if text:
            write_txt(get_output_path(path=path), text)
