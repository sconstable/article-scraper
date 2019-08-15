from html.parser import HTMLParser
import requests
import argparse
import os


class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.print_me = False

    def handle_starttag(self, tag, attrs):
        if tag == "p":
            self.print_me = True

    def handle_endtag(self, tag):
        if tag == "p":
            self.print_me = False
            if not file_name:
                print("")
            else:
                file_handle.write(os.linesep)

    def handle_data(self, data):
        if self.print_me:
            if not file_name:
                print(data)
            else:
                file_handle.write(data)
                file_handle.write(os.linesep)


htmlparser = MyHTMLParser()
argparser = argparse.ArgumentParser()
argparser.add_argument("url", type=str)
argparser.add_argument("--output", dest='output', type=str, help="filename to write to")
args = argparser.parse_args()
file_name = None

if args.output:
    file_name = args.output
    file_handle = open(file_name, 'w')
htmlparser.feed(requests.get(args.url).text)
