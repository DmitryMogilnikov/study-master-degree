import httplib2
from bs4 import BeautifulSoup, SoupStrainer

from src.abstract_parser.abstract_parser import AbstractParser
from src.utils.path_checker import check_path


class ParserHTML(AbstractParser):
    text: str = ''

    def __init__(self, path):
        check_path(path, suffix='.html')
        self.path = path

    @staticmethod
    def tag_visible(element):
        if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
            return False
        return True

    def extract_all_text(self):
        with open(self.path, "r") as file:
            contents = file.read()

            soup = BeautifulSoup(contents, 'lxml')
            text = soup.findAll(text=True)
            text = filter(self.tag_visible, text)
            print("\n".join(t.strip() for t in text))

        if self.text:
            return self.text


"""    def extract_all_links(self, path: str) -> str:
        check_path(path, suffix='.html')

        http = httplib2.Http()
        status, response = http.request('http://www.nytimes.com')

        for link in BeautifulSoup(response, parse_only=SoupStrainer('a')):
            if link.has_attr('href'):
                print(link['href'])"""
