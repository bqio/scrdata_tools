import argparse
from iolib import Reader, Stuff, Writer

langRelativeOfs = 0
tableRelativeOfs = 0

def unpack_default_ptrs_table(len):
    table = []
    for _ in range(len):
        ptr = [r.read_u32(), r.read_u32()]
        table.append(ptr)
    return table

def unpack_default_table_header():
    header = {}
    header['magic'] = r.read_u32()
    header['tableSize'] = r.read_u16()
    header['flagSize'] = r.read_u16()
    header['numOfMsg'] = r.read_u16()
    header['ptrSize'] = r.read_u16()
    header['headerSize'] = r.read_u32()
    header['flags'] = list(r.read(header['flagSize']))
    return header

def unpack_t0_ptrs_table(len):
    table = []
    for _ in range(len):
        ptr = {}
        ptr['line1'] = r.read_u32()
        ptr['line2'] = r.read_u32()
        ptr['line3'] = r.read_u32()
        ptr['voice1'] = r.read_u32()
        ptr['voice2'] = r.read_u32()
        ptr['voice3'] = r.read_u32()
        ptr['portrait'] = r.read_u32()
        ptr['unk'] = r.read_u32()
        table.append(ptr)
    return table

def unpack_t1_ptrs_table(len):
    table = []
    for _ in range(len):
        ptr = {}
        ptr['line1'] = r.read_u32()
        ptr['line2'] = r.read_u32()
        ptr['line3'] = r.read_u32()
        ptr['line4'] = r.read_u32()
        ptr['line5'] = r.read_u32()
        ptr['line6'] = r.read_u32()
        ptr['line7'] = r.read_u32()
        ptr['line8'] = r.read_u32()
        table.append(ptr)
    return table

def unpack_t2_ptrs_table(len):
    table = []
    for _ in range(len):
        ptr = {}
        ptr['line1'] = r.read_u32()
        ptr['line2'] = r.read_u32()
        ptr['line3'] = r.read_u32()
        ptr['line4'] = r.read_u32()
        ptr['line5'] = r.read_u32()
        ptr['line6'] = r.read_u32()
        ptr['line7'] = r.read_u32()
        ptr['line8'] = r.read_u32()
        ptr['unk'] = r.read_u32()
        ptr['unk1'] = r.read_u32()
        ptr['unk2'] = r.read_u32()
        ptr['unk3'] = r.read_u32()
        table.append(ptr)
    return table

def unpack_t3_ptrs_table(len):
    table = []
    for _ in range(len):
        ptr = {}
        ptr['line1'] = r.read_u32()
        ptr['line2'] = r.read_u32()
        ptr['unk'] = r.read_u32()
        ptr['unk1'] = r.read_u32()
        ptr['unk2'] = r.read_u32()
        table.append(ptr)
    return table

def unpack_t4_ptrs_table(len):
    table = []
    for _ in range(len):
        ptr = {}
        ptr['line'] = r.read_u32()
        ptr['unk'] = r.read_u32()
        ptr['unk1'] = r.read_u32()
        ptr['unk2'] = r.read_u32()
        table.append(ptr)
    return table

def unpack_t6_ptrs_table(len):
    table = []
    for _ in range(len):
        ptr = {}
        ptr['line1'] = r.read_u32()
        ptr['line2'] = r.read_u32()
        ptr['line3'] = r.read_u32()
        ptr['line4'] = r.read_u32()
        ptr['line5'] = r.read_u32()
        ptr['line6'] = r.read_u32()
        ptr['line7'] = r.read_u32()
        table.append(ptr)
    return table

def unpack_t7_ptrs_table(len):
    table = []
    for _ in range(len):
        ptr = {}
        ptr['unk'] = r.read_u32()
        ptr['unk1'] = r.read_u32()
        ptr['unk2'] = r.read_u32()
        table.append(ptr)
    return table

def unpack_t0_text_table(len):
    table = []
    for _ in range(len):
        lines = []
        lines.append(r.read_nt_utf8_str())
        lines.append(r.read_nt_utf8_str())
        lines.append(r.read_nt_utf8_str())
        table.append(lines)
    return table

def unpack_t1_text_table(len):
    table = []
    for _ in range(len):
        lines = []
        lines.append(r.read_nt_utf8_str())
        lines.append(r.read_nt_utf8_str())
        lines.append(r.read_nt_utf8_str())
        lines.append(r.read_nt_utf8_str())
        lines.append(r.read_nt_utf8_str())
        lines.append(r.read_nt_utf8_str())
        lines.append(r.read_nt_utf8_str())
        lines.append(r.read_nt_utf8_str())
        table.append(lines)
    return table

def unpack_t3_text_table(len):
    table = []
    for _ in range(len):
        lines = []
        lines.append(r.read_nt_utf8_str())
        lines.append(r.read_nt_utf8_str())
        table.append(lines)
    return table

def unpack_t4_text_table(len):
    table = []
    for _ in range(len):
        lines = []
        lines.append(r.read_nt_utf8_str())
        table.append(lines)
    return table

def unpack_t6_text_table(len):
    table = []
    for _ in range(len):
        lines = []
        lines.append(r.read_nt_utf8_str())
        lines.append(r.read_nt_utf8_str())
        lines.append(r.read_nt_utf8_str())
        lines.append(r.read_nt_utf8_str())
        lines.append(r.read_nt_utf8_str())
        lines.append(r.read_nt_utf8_str())
        lines.append(r.read_nt_utf8_str())
        table.append(lines)
    return table

def unpack_t0():
    print('Exporting table 0...')
    t0 = {}
    t0['header'] = unpack_default_table_header()
    t0['textPtrs'] = unpack_t0_ptrs_table(t0['header']['numOfMsg'])
    t0['text'] = unpack_t0_text_table(t0['header']['numOfMsg'])
    return t0

def unpack_t1():
    print('Exporting table 1...')
    t1 = {}
    t1['header'] = unpack_default_table_header()
    t1['textPtrs'] = unpack_t1_ptrs_table(t1['header']['numOfMsg'])
    t1['text'] = unpack_t1_text_table(t1['header']['numOfMsg'])
    return t1

def unpack_t2():
    print('Exporting table 2...')
    t2 = {}
    t2['header'] = unpack_default_table_header()
    t2['textPtrs'] = unpack_t2_ptrs_table(t2['header']['numOfMsg'])
    t2['text'] = unpack_t1_text_table(t2['header']['numOfMsg'])
    return t2

def unpack_t3():
    print('Exporting table 3...')
    t3 = {}
    t3['header'] = unpack_default_table_header()
    r.skip(3)  # flags padding
    t3['textPtrs'] = unpack_t3_ptrs_table(t3['header']['numOfMsg'])
    t3['text'] = unpack_t3_text_table(t3['header']['numOfMsg'])
    return t3

def unpack_t4():
    print('Exporting table 4...')
    t4 = {}
    t4['header'] = unpack_default_table_header()
    t4['textPtrs'] = unpack_t4_ptrs_table(t4['header']['numOfMsg'])
    t4['text'] = unpack_t4_text_table(t4['header']['numOfMsg'])
    return t4

def unpack_t5():
    print('Exporting table 5...')
    t5 = {}
    t5['header'] = unpack_default_table_header()
    t5['textPtrs'] = unpack_t4_ptrs_table(t5['header']['numOfMsg'])
    t5['text'] = unpack_t4_text_table(t5['header']['numOfMsg'])
    return t5

def unpack_t6():
    print('Exporting table 6...')
    t6 = {}
    t6['header'] = unpack_default_table_header()
    r.skip(1)  # flags padding
    t6['textPtrs'] = unpack_t6_ptrs_table(t6['header']['numOfMsg'])
    t6['text'] = unpack_t6_text_table(t6['header']['numOfMsg'])
    return t6

def unpack_t7():
    print('Exporting table 7...')
    t7 = {}
    t7['header'] = unpack_default_table_header()
    r.skip(1)  # flags padding
    t7['textPtrs'] = unpack_t7_ptrs_table(t7['header']['numOfMsg'])
    return t7

def unpack_language():
    language = {}
    language['header'] = {}
    language['header']['numOfTables'] = r.read_u32()
    language['tablePtrs'] = unpack_default_ptrs_table(
        language['header']['numOfTables'])
    language['tables'] = []
    language['tables'].append(unpack_t0())
    tableRelativeOfs = langRelativeOfs + language['tablePtrs'][1][0]
    r.seek(tableRelativeOfs)
    language['tables'].append(unpack_t1())
    tableRelativeOfs = langRelativeOfs + language['tablePtrs'][2][0]
    r.seek(tableRelativeOfs)
    language['tables'].append(unpack_t2())
    tableRelativeOfs = langRelativeOfs + language['tablePtrs'][3][0]
    r.seek(tableRelativeOfs)
    language['tables'].append(unpack_t3())
    tableRelativeOfs = langRelativeOfs + language['tablePtrs'][4][0]
    r.seek(tableRelativeOfs)
    language['tables'].append(unpack_t4())
    tableRelativeOfs = langRelativeOfs + language['tablePtrs'][5][0]
    r.seek(tableRelativeOfs)
    language['tables'].append(unpack_t5())
    tableRelativeOfs = langRelativeOfs + language['tablePtrs'][6][0]
    r.seek(tableRelativeOfs)
    language['tables'].append(unpack_t6())
    tableRelativeOfs = langRelativeOfs + language['tablePtrs'][7][0]
    r.seek(tableRelativeOfs)
    language['tables'].append(unpack_t7())
    return language

def unpack():
    file = {}
    file['header'] = {}
    file['header']['numOfLang'] = r.read_u32()
    file['langPtrs'] = unpack_default_ptrs_table(
        file['header']['numOfLang'])
    file['languages'] = []
    for i in range(file['header']['numOfLang']):
        print(f'Exporting language {i}...')
        r.seek(file['langPtrs'][i][0])
        global langRelativeOfs
        langRelativeOfs = r.tell()
        file['languages'].append(unpack_language())
    print('Saving as json...')
    Stuff.dump_json("files\\dump.json", file)
    print('Done.')

def pack_default_ptrs_table(ptrs_table):
    for i in range(len(ptrs_table)):
        w.write_u32(ptrs_table[i][0]) # ptr
        w.write_u32(ptrs_table[i][1]) # size

def pack_default_table_header(h):
    w.write_u32(h['magic'])
    w.write_u16(h['tableSize'])
    w.write_u16(h['flagSize'])
    w.write_u16(h['numOfMsg'])
    w.write_u16(h['ptrSize'])
    w.write_u32(h['headerSize'])
    w.write(bytearray(h['flags']))

def pack_t0_ptrs_table(tp):
    for i in range(len(tp)):
        w.write_u32(tp[i]['line1'])
        w.write_u32(tp[i]['line2'])
        w.write_u32(tp[i]['line3'])
        w.write_u32(tp[i]['voice1'])
        w.write_u32(tp[i]['voice2'])
        w.write_u32(tp[i]['voice3'])
        w.write_u32(tp[i]['portrait'])
        w.write_u32(tp[i]['unk'])

def pack_t1_ptrs_table(tp):
    for i in range(len(tp)):
        w.write_u32(tp[i]['line1'])
        w.write_u32(tp[i]['line2'])
        w.write_u32(tp[i]['line3'])
        w.write_u32(tp[i]['line4'])
        w.write_u32(tp[i]['line5'])
        w.write_u32(tp[i]['line6'])
        w.write_u32(tp[i]['line7'])
        w.write_u32(tp[i]['line8'])

def pack_t2_ptrs_table(tp):
    for i in range(len(tp)):
        w.write_u32(tp[i]['line1'])
        w.write_u32(tp[i]['line2'])
        w.write_u32(tp[i]['line3'])
        w.write_u32(tp[i]['line4'])
        w.write_u32(tp[i]['line5'])
        w.write_u32(tp[i]['line6'])
        w.write_u32(tp[i]['line7'])
        w.write_u32(tp[i]['line8'])
        w.write_u32(tp[i]['unk'])
        w.write_u32(tp[i]['unk1'])
        w.write_u32(tp[i]['unk2'])
        w.write_u32(tp[i]['unk3'])

def pack_t3_ptrs_table(tp):
    for i in range(len(tp)):
        w.write_u32(tp[i]['line1'])
        w.write_u32(tp[i]['line2'])
        w.write_u32(tp[i]['unk'])
        w.write_u32(tp[i]['unk1'])
        w.write_u32(tp[i]['unk2'])

def pack_t4_ptrs_table(tp):
    for i in range(len(tp)):
        w.write_u32(tp[i]['line'])
        w.write_u32(tp[i]['unk'])
        w.write_u32(tp[i]['unk1'])
        w.write_u32(tp[i]['unk2'])

def pack_t6_ptrs_table(tp):
    for i in range(len(tp)):
        w.write_u32(tp[i]['line1'])
        w.write_u32(tp[i]['line2'])
        w.write_u32(tp[i]['line3'])
        w.write_u32(tp[i]['line4'])
        w.write_u32(tp[i]['line5'])
        w.write_u32(tp[i]['line6'])
        w.write_u32(tp[i]['line7'])

def pack_t7_ptrs_table(tp):
    for i in range(len(tp)):
        w.write_u32(tp[i]['unk'])
        w.write_u32(tp[i]['unk1'])
        w.write_u32(tp[i]['unk2'])

def pack_t0_text_table(tt):
    for i in range(len(tt)):
        for j in range(3):
            w.write_nt_utf8_str(tt[i][j])

def pack_t1_text_table(tt):
    for i in range(len(tt)):
        for j in range(8):
            w.write_nt_utf8_str(tt[i][j])

def pack_t3_text_table(tt):
    for i in range(len(tt)):
        for j in range(2):
            w.write_nt_utf8_str(tt[i][j])

def pack_t4_text_table(tt):
    for i in range(len(tt)):
        for j in range(1):
            w.write_nt_utf8_str(tt[i][j])

def pack_t6_text_table(tt):
    for i in range(len(tt)):
        for j in range(7):
            w.write_nt_utf8_str(tt[i][j])

def pack_t0(t):
    print('Importing table 0...')
    pack_default_table_header(t['header'])
    pack_t0_ptrs_table(t['textPtrs'])
    pack_t0_text_table(t['text'])

def pack_t1(t):
    print('Importing table 1...')
    pack_default_table_header(t['header'])
    pack_t1_ptrs_table(t['textPtrs'])
    pack_t1_text_table(t['text'])

def pack_t2(t):
    print('Importing table 2...')
    pack_default_table_header(t['header'])
    pack_t2_ptrs_table(t['textPtrs'])
    pack_t1_text_table(t['text'])

def pack_t3(t):
    print('Importing table 3...')
    pack_default_table_header(t['header'])
    w.skip(3)
    pack_t3_ptrs_table(t['textPtrs'])
    pack_t3_text_table(t['text'])

def pack_t4(t):
    print('Importing table 4...')
    pack_default_table_header(t['header'])
    pack_t4_ptrs_table(t['textPtrs'])
    pack_t4_text_table(t['text'])

def pack_t5(t):
    print('Importing table 5...')
    pack_default_table_header(t['header'])
    pack_t4_ptrs_table(t['textPtrs'])
    pack_t4_text_table(t['text'])

def pack_t6(t):
    print('Importing table 6...')
    pack_default_table_header(t['header'])
    w.skip(1)
    pack_t6_ptrs_table(t['textPtrs'])
    pack_t6_text_table(t['text'])

def pack_t7(t):
    print('Importing table 7...')
    pack_default_table_header(t['header'])
    w.skip(1)
    pack_t7_ptrs_table(t['textPtrs'])

def pack_language(l):
    w.write_u32(l['header']['numOfTables'])
    pack_default_ptrs_table(l['tablePtrs'])
    pack_t0(l['tables'][0])
    w.seek(l['tablePtrs'][1][0] + langRelativeOfs)
    pack_t1(l['tables'][1])
    w.seek(l['tablePtrs'][2][0] + langRelativeOfs)
    pack_t2(l['tables'][2])
    w.seek(l['tablePtrs'][3][0] + langRelativeOfs)
    pack_t3(l['tables'][3])
    w.seek(l['tablePtrs'][4][0] + langRelativeOfs)
    pack_t4(l['tables'][4])
    w.seek(l['tablePtrs'][5][0] + langRelativeOfs)
    pack_t5(l['tables'][5])
    w.seek(l['tablePtrs'][6][0] + langRelativeOfs)
    pack_t6(l['tables'][6])
    w.seek(l['tablePtrs'][7][0] + langRelativeOfs)
    pack_t7(l['tables'][7])

def pack():
    w.write_u32(j['header']['numOfLang'])
    pack_default_ptrs_table(j['langPtrs'])
    for i in range(j['header']['numOfLang']):
        print(f'Importing language {i}...')
        w.seek(j['langPtrs'][i][0])
        global langRelativeOfs
        langRelativeOfs = w.tell()
        pack_language(j['languages'][i])
    print('Done.')

print("scrdata tools\nby bqio 2021")

parser = argparse.ArgumentParser()
parser.add_argument(
    "file", help="file path", type=str)
parser.add_argument(
    "-u", help="unpack", action="store_true")
parser.add_argument(
    "-p", help="pack", action="store_true")
args = parser.parse_args()

r = None
w = None
j = None

if args.u:
    r = Reader(open(args.file, 'rb'))
    unpack()
    r.close()

if args.p:
    w = Writer(open('files\\scrdata_n.bin', 'wb'))
    j = Stuff.load_json(args.file)
    pack()
    w.close()
