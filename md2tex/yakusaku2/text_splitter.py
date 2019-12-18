"""
エクセルの行をコピーして入力すると、
pythonの配列に適した形のテキストをクリップボードに貼り付ける
"""

import pyperclip

a = input('input\n>> ')
pyperclip.copy(','.join(a.split('\t')))
print('copied!')
