from pdf_parser import PDF_parser

if __name__ == '__main__':
    pdf_path = input('File path to parse:')
    pdf_parser = PDF_parser(pdf_path)

    pdf_parser.extract_all_text()
