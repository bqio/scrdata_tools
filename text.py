from iolib import Stuff


def get_text_by_id(dump_file: str, lang_id: int, table_id: int):
    data = Stuff.load_json(dump_file)
    return data['languages'][lang_id]['tables'][table_id]['text']


data = get_text_by_id("files\\dump.json", 2, 0)
print(data)
