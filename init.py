import sys
import re
import os

file_name = "./input.txt"

with open(file_name, encoding='utf-8') as f:
    data_lines = f.read()

# 文字列置換
data_lines = data_lines.replace("／", "")

# 同じファイル名で保存
with open(file_name, mode="w", encoding='utf-8') as f:
    f.write(data_lines)