#!/usr/bin/env python3

import sys

from pathlib import Path



encodings = ['utf-8','cp949','euc-kr','latin1','cp1252']



root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('.')

if not root.exists():

    print('Root path does not exist:', root)

    sys.exit(1)



count_converted = 0

count_checked = 0



for p in root.rglob('*'):

    if p.is_file() and p.suffix.lower() in {'.py', '.ipynb', '.txt', '.md'}:

        count_checked += 1

        b = p.read_bytes()

        # try utf-8 first

        detected = None

        for enc in encodings:

            try:

                s = b.decode(enc)

                detected = enc

                break

            except Exception:

                continue

        if detected is None:

            print(f'Could not decode: {p} (skipping)')

            continue

        if detected != 'utf-8':

            bak = p.with_name(p.name + '.bak')

            try:

                bak.write_bytes(b)

            except Exception as e:

                print(f'Failed to write backup for {p}: {e}')

            try:

                p.write_text(s, encoding='utf-8')

                print(f'Converted {p} from {detected} -> utf-8')

                count_converted += 1

            except Exception as e:

                print(f'Failed to write utf-8 for {p}: {e}')

        else:

            # ensure we write as normalized utf-8 (removes BOM if present)

            try:

                p.write_text(s, encoding='utf-8')

            except Exception as e:

                print(f'Failed to normalize utf-8 for {p}: {e}')



print('---')

print(f'Checked files: {count_checked}')

print(f'Converted files: {count_converted}')

print('Backups created with suffix .bak next to original files')

