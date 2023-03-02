from docx_parser import ParserDOCX

if __name__ == '__main__':
    path = input('File path to parse:')
    parser = ParserDOCX()

    parser.extract_all_text(path)
