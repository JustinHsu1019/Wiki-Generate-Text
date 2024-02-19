import os, codecs
from tqdm import tqdm
from opencc import OpenCC

folderpath = "wiki_zh"
filename01 = "DataSet_INI.txt"
filename02 = "DataSet.txt"
cc = OpenCC('s2t')

def read_and_combine_files(root_folder, output_file):
    with codecs.open(output_file, 'w', encoding='utf-8') as outfile:
        all_files = [os.path.join(root, file) for root, _, files in os.walk(root_folder) for file in files]

        for file_path in tqdm(all_files, desc="Processing files"):
            with codecs.open(file_path, 'r', encoding='utf-8', errors='ignore') as infile:
                content = infile.read()
                outfile.write(content)
                outfile.write('\n')

def convert_simplified_to_traditional(file_path, output_path):
    total_lines = sum(1 for _ in open(file_path, 'r', encoding='utf-8'))
    
    with open(file_path, 'r', encoding='utf-8') as file:
        with open(output_path, 'w', encoding='utf-8') as output_file:
            for line in tqdm(file, total=total_lines, desc="Converting"):
                traditional_line = cc.convert(line)
                output_file.write(traditional_line)

read_and_combine_files(folderpath, filename01)
convert_simplified_to_traditional(filename01, filename02)
