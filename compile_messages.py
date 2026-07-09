"""Compile .po files to .mo files without requiring GNU gettext.
Properly handles escape sequences in header metadata so Python's
gettext can detect charset=UTF-8."""
import struct
import array
import os
import re


def unescape(s):
    """Convert PO escape sequences to actual characters."""
    s = s.replace('\\n', '\n')
    s = s.replace('\\t', '\t')
    s = s.replace('\\\\', '\\')
    s = s.replace('\\"', '"')
    return s


def compile_po(po_path, mo_path):
    messages = {}
    msgid = msgstr = None
    in_msgid = in_msgstr = False

    with open(po_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line.startswith('msgid "'):
                if msgid is not None and msgstr is not None:
                    messages[unescape(msgid)] = unescape(msgstr)
                msgid = line[7:-1]
                msgstr = None
                in_msgid = True
                in_msgstr = False
            elif line.startswith('msgstr "'):
                msgstr = line[8:-1]
                in_msgid = False
                in_msgstr = True
            elif line.startswith('"') and line.endswith('"'):
                s = line[1:-1]
                if in_msgid:
                    msgid += s
                elif in_msgstr:
                    msgstr += s
            else:
                if msgid is not None and msgstr is not None:
                    messages[unescape(msgid)] = unescape(msgstr)
                    msgid = msgstr = None
                in_msgid = in_msgstr = False
        if msgid is not None and msgstr is not None:
            messages[unescape(msgid)] = unescape(msgstr)

    # Build .mo file
    keys = sorted(messages.keys())
    offsets = []
    ids = strs = b''
    for key in keys:
        id_bytes = key.encode('utf-8')
        str_bytes = messages[key].encode('utf-8')
        offsets.append((len(ids), len(id_bytes), len(strs), len(str_bytes)))
        ids += id_bytes + b'\0'
        strs += str_bytes + b'\0'

    keystart = 7 * 4 + 16 * len(keys)
    valuestart = keystart + len(ids)
    koffsets = []
    voffsets = []
    for o1, l1, o2, l2 in offsets:
        koffsets += [l1, o1 + keystart]
        voffsets += [l2, o2 + valuestart]
    offsets_array = koffsets + voffsets

    output = struct.pack('Iiiiiii',
        0x950412de,
        0,
        len(keys),
        7 * 4,
        7 * 4 + len(keys) * 8,
        0, 0
    )
    output += array.array('i', offsets_array).tobytes()
    output += ids + strs

    with open(mo_path, 'wb') as f:
        f.write(output)
    
    # Verify charset is in the header
    header = messages.get('', '')
    charset_match = re.search(r'charset=(\S+)', header)
    charset = charset_match.group(1) if charset_match else 'NOT FOUND'
    print(f'Compiled {po_path} -> {mo_path} ({len(keys)} entries, charset={charset})')


if __name__ == '__main__':
    for lang in ['en', 'ar', 'fr']:
        po = f'locale/{lang}/LC_MESSAGES/django.po'
        mo = f'locale/{lang}/LC_MESSAGES/django.mo'
        if os.path.exists(po):
            compile_po(po, mo)
