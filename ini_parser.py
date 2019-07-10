sample = """
[author]
name = xmonader
email = notxmonader@gmail.com
[general]
appname = configparser
version = 0.1
"""
sample = sample.splitlines()

class Parser:
    """Reading a text and parse it into proper format,
    then you can access it by dict accessing"""
    def __init__(self, sample):
        self.sample = sample

    def parse(self):
        lines = []
        for line in sample :
            line = line.strip()
            if line == "":
                continue
            else :
                lines.append(line)

        main_dict = {}
        section = ""
        for line in  lines:
            if line.startswith("["):
                section = ""
                section = line[1:-1]
                main_dict[section] = {}
            else:
                key , value = line.split("=")
                main_dict[section][key.strip()] = value.strip()
        return main_dict


text = Parser(sample)

from pprint import pprint
pprint(text.parse())