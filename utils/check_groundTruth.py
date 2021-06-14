import xlrd
import argparse
import os 

parser = argparse.ArgumentParser()
parser.add_argument('--gt', help='path of the ground truth file', required=True)
parser.add_argument('--image_dir', help='path of the directory that keeps all train_data', required=True)

if __name__ == '__main__':
    '''
        Remove images that exist in <image_dir> while not in <gt>
        --gt: path of the ground truth file 
        --image_dir: path of the directory containing dataset images
    '''
    args = parser.parse_args()
    image_file_list = os.listdir(args.image_dir)

    sheet = xlrd.open_workbook(args.gt).sheet_by_index(0)
    image_names = sheet.col_values(0)[1:]
    image_names_set = set()
    orphan_list = []
    count = 0
    for _, name in enumerate(image_names):
        image_names_set.add(name.lower())

    for _, file_name in enumerate(image_file_list):
        if not file_name.lower() in image_names_set:
            print(file_name)
            count += 1
            orphan_list.append(file_name)

    for _, file_name in enumerate(orphan_list):
        os.remove(os.path.join(args.image_dir, file_name))
