import os
import cv2
import xlrd
import xlwt
import tqdm
import argparse
import numpy as np

from data_aug import *
from typing import Dict


# The annotations in .xls file should be <xyxy> format
def read_np_from_xls(xls_path: str) -> Dict[str, np.ndarray]:
    rd_sheet = xlrd.open_workbook(xls_path).sheet_by_index(0)
    n_rows = rd_sheet.nrows
    n_class = 2
    annots_dict = {}
    for i in range(1, n_rows):
        row = rd_sheet.row_values(i)
        filename = row[0]
        annots = np.empty(shape=(0, 5))
        for j in range(n_class):
            boxes = []
            boxes_str = row[j + 1].strip('[]').split(';')
            for box_str in boxes_str:
                if box_str == '':
                    continue
                position_tuple_4 = box_str.split(',')

                x1 = float(position_tuple_4[0])
                y1 = float(position_tuple_4[1])
                x2 = float(position_tuple_4[2])
                y2 = float(position_tuple_4[3])
                boxes.append([x1, y1, x2, y2, float(j)])

            if len(boxes) != 0:
                annots = np.append(annots, np.array(boxes), axis=0)

        annots_dict[filename] = annots
    return annots_dict


def store_np_into_xls(output_filename: str, annots_dict: Dict[str, np.ndarray]) -> None:
    if not output_filename.endswith('.xls'):
        print('*** only .xls format is supported! ***')
        return
    wt_workbook = xlwt.Workbook()
    wt_sheet = wt_workbook.add_sheet('augmented_gt')
    wt_sheet.write(0, 0, 'filename')
    wt_sheet.write(0, 1, 'abandoned')
    wt_sheet.write(0, 2, 'normal')
    count = 1
    for key in annots_dict:
        wt_sheet.write(count, 0, key)
        abandoned_strs = []
        normal_strs = []
        annots_list = annots_dict[key].astype(np.int).tolist()
        for arr in annots_list:
            if arr[4] == 0:
                abandoned_strs.append(','.join(map(str, arr[:4])))
            else:
                normal_strs.append(','.join(map(str, arr[:4])))
        ret_abandoned_str = '[' + ';'.join(abandoned_strs) + ']'
        ret_normal_str = '[' + ';'.join(normal_strs) + ']'
        wt_sheet.write(count, 1, ret_abandoned_str)
        wt_sheet.write(count, 2, ret_normal_str)

        count += 1

    wt_workbook.save(output_filename)


parser = argparse.ArgumentParser()
parser.add_argument('--image_input_dir', dest='ds', type=str, required=True)
parser.add_argument('--gt_file', dest='gt', type=str, required=True)
parser.add_argument('--image_output_dir', dest='img_ot', type=str, default='./augmented_images')
parser.add_argument('--draw_bbs', action='store_true')

parser.add_argument('--type_of_aug', help='type in {rotate20, horizontal_flip, scale1_3, translate_30p} is available',
                    type=str, required=True)

ops_dict = {
    # 'rotate20': RandomRotate(20),
    'horizontal_flip': RandomHorizontalFlip(1),
    'scale1_3': RandomScale(0.3, diff=True),
    'translate_30p': RandomTranslate(0.3, diff=True),
    'hflip_and_translate': Sequence([RandomHorizontalFlip(1), RandomTranslate()]),
    'scale_30p_and_hflip': Sequence([RandomScale((0.1, 0.3), diff=True), RandomHorizontalFlip(1)])
}

if __name__ == '__main__':
    args = parser.parse_args()
    annotation_dict = read_np_from_xls(args.gt)
    new_annotation_dict = {}

    os.makedirs(os.path.join(args.img_ot, args.type_of_aug, 'images'), 0o777, True)
    
    if args.type_of_aug not in ops_dict.keys():
        print('only types in %s are available' % ops_dict.keys())

    original_filenames = os.listdir(args.ds)
    for fn in tqdm.tqdm(original_filenames):
        # transform bgr to rgb
        img = cv2.imread(os.path.join(args.ds, fn))[:, :, ::-1]
        # read annotations of img
        annots = annotation_dict[fn]

        img_, annots_ = ops_dict[args.type_of_aug](img.copy(), annots.copy())

        # whether or not draw bounding boxes
        if args.draw_bbs:
            img_ = draw_rect(img_, annots_)

        new_fn = '{}_{}'.format(args.type_of_aug, fn)
        new_annotation_dict[new_fn] = annots_
        cv2.imwrite(os.path.join(args.img_ot, args.type_of_aug, 'images', new_fn), img_[:, :, ::-1])

    store_np_into_xls(os.path.join(args.img_ot, args.type_of_aug, 'aug_gt.xls'), new_annotation_dict)
