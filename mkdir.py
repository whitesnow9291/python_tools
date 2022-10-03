from os import mkdir
from os.path import join
import math

destionation = r'./output'

deep = 3
total_file_count = 3000
current_file_count = 0
sub_folder_count = 10

def generateFiles(start, end, current_deep, parent_path):
    global current_file_count
    global sub_folder_count
    global total_file_count
    global deep
    if current_deep == deep:
        for n in range(end-start+1):
            dir_path = join(parent_path, f'{start+n}')
            mkdir(dir_path)
    else:
        vol_a_group = sub_folder_count ** (current_deep - 1)
        group_count = math.ceil((end - start + 1) / vol_a_group)

        for n in range(group_count):
            start_dir = (start -1) + n * vol_a_group + 1
            end_dir = (start -1) + min((n+1) * vol_a_group, total_file_count)
            dir_name = f'{start_dir}-{end_dir}'
            dir_path = join(parent_path, dir_name)
            mkdir(dir_path)
            generateFiles(start_dir, end_dir, current_deep+1, dir_path)


def main():
    vol_a_group = sub_folder_count ** (deep - 1)
    group_count = math.ceil(total_file_count / vol_a_group)
    for n in range(group_count):
        start_dir = n * vol_a_group + 1
        end_dir = min((n+1) * vol_a_group, total_file_count)
        dir_name = f'{start_dir}-{end_dir}'
        dir_path = join(destionation, dir_name)
        mkdir(dir_path)
        generateFiles(start_dir, end_dir, 2, dir_path)
if __name__ == "__main__":
    main()