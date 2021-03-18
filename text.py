from iolib import Stuff

class Text:
    def __init__(self, data):
        self.data = data
        self.unique_strings = []
    
    def __get_line_indexes(self, line):
        indexes = []
        for r in range(len(self.data)):
            for c in range(len(self.data[r])):
                if self.data[r][c] == line:
                    indexes.append([r, c])
        return indexes

    def make_meta(self):
        ptrs = []
        unique_strings = []
        for r in range(len(self.data)):
            for c in range(len(self.data[r])):
                try:
                    unique_strings.index(self.data[r][c])
                except ValueError:
                    ptr = {}
                    ptr['line'] = self.data[r][c]
                    ptr['ptrs'] = self.__get_line_indexes(ptr['line'])
                    ptrs.append(ptr)
                    unique_strings.append(self.data[r][c])
        return ptrs
    
    def merge_meta(self, meta):
        for i in range(len(meta)):
            line = meta[i]['line']
            ptrs = meta[i]['ptrs']
            for j in range(len(ptrs)):
                ptr = ptrs[j]
                print(f'{ptr[0]}|{ptr[1]}|{line}')
                self.data[ptr[0]][ptr[1]] = line
        return self.data

class Table:
    def __init__(self, data):
        self.data = data
    def get_text(self):
        return Text(self.data['text'])

class Language:
    def __init__(self, data):
        self.data = data
    def get_table_by_id(self, id: int):
        return Table(self.data['tables'][id])

class File:
    def __init__(self, dump):
       self.dump = dump
    
    def get_language_by_id(self, id: int):
        return Language(self.dump['languages'][id])


file = File(Stuff.load_json("files\\dump.json"))

eng_eu_lang = file.get_language_by_id(2)

text = eng_eu_lang.get_table_by_id(0).get_text()
Stuff.dump_json("out.json", text.merge_meta(Stuff.load_json("files\\meta0.json")))
