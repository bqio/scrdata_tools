import argparse
from iolib import read_u32, read_u16, read_nt_str, dump_json

langRelativeOfs = 0
tableRelativeOfs = 0


def unpack_default_ptrs_table(len):
    table = []
    for _ in range(len):
        ptr = [read_u32(f), read_u32(f)]
        table.append(ptr)
    return table


def unpack_default_table_header():
    header = {}
    header['magic'] = read_u32(f)
    header['tableSize'] = read_u16(f)
    header['flagSize'] = read_u16(f)
    header['numOfMsg'] = read_u16(f)
    header['ptrSize'] = read_u16(f)
    header['headerSize'] = read_u32(f)
    header['flags'] = list(f.read(header['flagSize']))
    return header


def unpack_t0_ptrs_table(len):
    table = []
    for _ in range(len):
        ptr = {}
        ptr['line1'] = read_u32(f)
        ptr['line2'] = read_u32(f)
        ptr['line3'] = read_u32(f)
        ptr['voice1'] = read_u32(f)
        ptr['voice2'] = read_u32(f)
        ptr['voice3'] = read_u32(f)
        ptr['portrait'] = read_u32(f)
        ptr['unk'] = read_u32(f)
        table.append(ptr)
    return table


def unpack_t1_ptrs_table(len):
    table = []
    for _ in range(len):
        ptr = {}
        ptr['line1'] = read_u32(f)
        ptr['line2'] = read_u32(f)
        ptr['line3'] = read_u32(f)
        ptr['line4'] = read_u32(f)
        ptr['line5'] = read_u32(f)
        ptr['line6'] = read_u32(f)
        ptr['line7'] = read_u32(f)
        ptr['line8'] = read_u32(f)
        table.append(ptr)
    return table


def unpack_t2_ptrs_table(len):
    table = []
    for _ in range(len):
        ptr = {}
        ptr['line1'] = read_u32(f)
        ptr['line2'] = read_u32(f)
        ptr['line3'] = read_u32(f)
        ptr['line4'] = read_u32(f)
        ptr['line5'] = read_u32(f)
        ptr['line6'] = read_u32(f)
        ptr['line7'] = read_u32(f)
        ptr['line8'] = read_u32(f)
        ptr['unk'] = read_u32(f)
        ptr['unk1'] = read_u32(f)
        ptr['unk2'] = read_u32(f)
        ptr['unk3'] = read_u32(f)
        table.append(ptr)
    return table


def unpack_t3_ptrs_table(len):
    table = []
    for _ in range(len):
        ptr = {}
        ptr['line1'] = read_u32(f)
        ptr['line2'] = read_u32(f)
        ptr['unk'] = read_u32(f)
        ptr['unk1'] = read_u32(f)
        ptr['unk2'] = read_u32(f)
        table.append(ptr)
    return table


def unpack_t4_ptrs_table(len):
    table = []
    for _ in range(len):
        ptr = {}
        ptr['line'] = read_u32(f)
        ptr['unk'] = read_u32(f)
        ptr['unk1'] = read_u32(f)
        ptr['unk2'] = read_u32(f)
        table.append(ptr)
    return table


def unpack_t6_ptrs_table(len):
    table = []
    for _ in range(len):
        ptr = {}
        ptr['line1'] = read_u32(f)
        ptr['line2'] = read_u32(f)
        ptr['line3'] = read_u32(f)
        ptr['line4'] = read_u32(f)
        ptr['line5'] = read_u32(f)
        ptr['line6'] = read_u32(f)
        ptr['line7'] = read_u32(f)
        table.append(ptr)
    return table


def unpack_t7_ptrs_table(len):
    table = []
    for _ in range(len):
        ptr = {}
        ptr['unk'] = read_u32(f)
        ptr['unk1'] = read_u32(f)
        ptr['unk2'] = read_u32(f)
        table.append(ptr)
    return table


def unpack_t0_text_table(len):
    table = []
    for _ in range(len):
        lines = []
        lines.append(read_nt_str(f))
        lines.append(read_nt_str(f))
        lines.append(read_nt_str(f))
        table.append(lines)
    return table


def unpack_t1_text_table(len):
    table = []
    for _ in range(len):
        lines = []
        lines.append(read_nt_str(f))
        lines.append(read_nt_str(f))
        lines.append(read_nt_str(f))
        lines.append(read_nt_str(f))
        lines.append(read_nt_str(f))
        lines.append(read_nt_str(f))
        lines.append(read_nt_str(f))
        lines.append(read_nt_str(f))
        table.append(lines)
    return table


def unpack_t3_text_table(len):
    table = []
    for _ in range(len):
        lines = []
        lines.append(read_nt_str(f))
        lines.append(read_nt_str(f))
        table.append(lines)
    return table


def unpack_t4_text_table(len):
    table = []
    for _ in range(len):
        lines = []
        lines.append(read_nt_str(f))
        table.append(lines)
    return table


def unpack_t6_text_table(len):
    table = []
    for _ in range(len):
        lines = []
        lines.append(read_nt_str(f))
        lines.append(read_nt_str(f))
        lines.append(read_nt_str(f))
        lines.append(read_nt_str(f))
        lines.append(read_nt_str(f))
        lines.append(read_nt_str(f))
        lines.append(read_nt_str(f))
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
    f.seek(f.tell()+3)  # flags padding
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
    f.seek(f.tell()+1)  # flags padding
    t6['textPtrs'] = unpack_t6_ptrs_table(t6['header']['numOfMsg'])
    t6['text'] = unpack_t6_text_table(t6['header']['numOfMsg'])
    return t6


def unpack_t7():
    print('Exporting table 7...')
    t7 = {}
    t7['header'] = unpack_default_table_header()
    f.seek(f.tell()+1)  # flags padding
    t7['textPtrs'] = unpack_t7_ptrs_table(t7['header']['numOfMsg'])
    return t7


def unpack_language():
    language = {}
    language['header'] = {}
    language['header']['numOfTables'] = read_u32(f)
    language['tablePtrs'] = unpack_default_ptrs_table(
        language['header']['numOfTables'])
    language['tables'] = []
    language['tables'].append(unpack_t0())
    tableRelativeOfs = langRelativeOfs + language['tablePtrs'][1][0]
    f.seek(tableRelativeOfs)
    language['tables'].append(unpack_t1())
    tableRelativeOfs = langRelativeOfs + language['tablePtrs'][2][0]
    f.seek(tableRelativeOfs)
    language['tables'].append(unpack_t2())
    tableRelativeOfs = langRelativeOfs + language['tablePtrs'][3][0]
    f.seek(tableRelativeOfs)
    language['tables'].append(unpack_t3())
    tableRelativeOfs = langRelativeOfs + language['tablePtrs'][4][0]
    f.seek(tableRelativeOfs)
    language['tables'].append(unpack_t4())
    tableRelativeOfs = langRelativeOfs + language['tablePtrs'][5][0]
    f.seek(tableRelativeOfs)
    language['tables'].append(unpack_t5())
    tableRelativeOfs = langRelativeOfs + language['tablePtrs'][6][0]
    f.seek(tableRelativeOfs)
    language['tables'].append(unpack_t6())
    tableRelativeOfs = langRelativeOfs + language['tablePtrs'][7][0]
    f.seek(tableRelativeOfs)
    language['tables'].append(unpack_t7())
    return language


def unpack():
    file = {}
    file['header'] = {}
    file['header']['numOfLang'] = read_u32(f)
    file['langPtrs'] = unpack_default_ptrs_table(
        file['header']['numOfLang'])
    file['languages'] = []
    for i in range(file['header']['numOfLang']):
        print(f'Exporting language {i}...')
        f.seek(file['langPtrs'][i][0])
        global langRelativeOfs
        langRelativeOfs = f.tell()
        file['languages'].append(unpack_language())
    dump_json("dump.json", file)


print("scrdata tools\nby bqio 2021")

parser = argparse.ArgumentParser()
parser.add_argument(
    "file", help="file path", type=str)
parser.add_argument(
    "u", help="unpack", type=str)
args = parser.parse_args()

f = open(args.file, 'rb')

if (args.u):
    unpack()
