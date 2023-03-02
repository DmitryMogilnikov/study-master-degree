from pdf_parser import ParserPDF

if __name__ == '__main__':
    pdf_path = input('File path to parse:')
    pdf_parser = ParserPDF()

    pdf_parser.extract_all_text(pdf_path)
