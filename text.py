from iolib import Stuff


def dump_text_by_id(lang_id: int, table_id: int):
    data = Stuff.load_json("dump.json")
    Stuff.dump_json(f'lang{lang_id}_table{table_id}_text.json',
                    data['languages'][lang_id]['tables'][table_id]['text'], 2)


# Main
dump_text_by_id(2, 0)
