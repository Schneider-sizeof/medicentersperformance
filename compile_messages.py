"""Compile .po to .mo using Babel."""
from babel.messages.mofile import write_mo
from babel.messages.pofile import read_po
import os

locale_dir = 'locale'
for lang in ['en', 'ar', 'fr']:
    po_path = os.path.join(locale_dir, lang, 'LC_MESSAGES', 'django.po')
    mo_path = os.path.join(locale_dir, lang, 'LC_MESSAGES', 'django.mo')
    with open(po_path, 'r', encoding='utf-8') as po_file:
        catalog = read_po(po_file)
    with open(mo_path, 'wb') as mo_file:
        write_mo(mo_file, catalog)
    print(f'Compiled: {mo_path} ({len(catalog)} messages)')

print('Done!')
