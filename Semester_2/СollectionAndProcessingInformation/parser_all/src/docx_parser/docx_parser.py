import docx
import re

from src.abstract_parser.abstract_parser import AbstractParser
from src.utils.path_checker import check_path
from src.utils.txt_writer import write_txt, get_output_path


class ParserDOCX(AbstractParser):
    text: str = ''
    path: str

    def extract_all_text(self, path):
        check_path(path, suffix='.docx')

        self.path = path

        document = docx.Document(path)
        self.text = '\n'.join(par.text for par in document.paragraphs)
        self.text = '\n'.join(
            line.strip() for line in re.findall(r'.{1,100}(?:\s+|$)', self.text)
        )

        if self.text:
            return self.text
