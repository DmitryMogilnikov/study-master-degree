import io
from pathlib import Path

from pdfminer.layout import LAParams
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter, PDFResourceManager
from pdfminer.pdfpage import PDFPage
from src.utils.txt_writer import write_txt


class PDF_parser:
    def __init__(self, pdf_path: str):
        self.pdf_path = pdf_path
        self.output_file_name = Path(self.pdf_path).stem
        self.output_path: str = '../../files/outputs/'

    def check_path(self):
        if not Path(self.pdf_path).is_file():
            raise FileNotFoundError("Incorrect path to file")
        if not Path(self.pdf_path).suffix == '.pdf':
            raise TypeError("File has incorrect type")

    def extract_all_text(
            self,
            caching: bool = True,
            codec: str = "utf-8",
    ):
        self.check_path()
        laparams = LAParams()

        with open(self.pdf_path, 'rb') as file:
            resource_manager = PDFResourceManager()
            output_string = io.StringIO()
            converter = TextConverter(
                resource_manager,
                output_string,
                codec=codec,
                laparams=laparams
            )
            interpreter = PDFPageInterpreter(resource_manager, converter)

            for page in PDFPage.get_pages(file, caching=caching):
                interpreter.process_page(page)
            text = output_string.getvalue()

        if text:
            write_txt(f'{self.output_path}/{self.output_file_name}.txt', text)

    def extract_images(self,):
        pass
