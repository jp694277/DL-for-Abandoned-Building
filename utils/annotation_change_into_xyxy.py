import xlrd
import xlwt
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('--source', help='path of the source ground truth file', required=True)
parser.add_argument('--output_path', dest='ot', required=True)

if __name__ == '__main__':
    '''
        transform annotations of <xywh> format into <xyxy> format
    '''
    args = parser.parse_args()

    rd_sheet = xlrd.open_workbook(args.source).sheet_by_index(0)
    image_names = rd_sheet.col_values(0)[1:]
    image_names_set = set()
    orphan_list = []
    count = 0

    wt_workbook = xlwt.Workbook()
    wt_sheet = wt_workbook.add_sheet('xxyy')
    n_rows = rd_sheet.nrows
    n_class = 2
    wt_sheet.write(0, 0, 'filename')
    wt_sheet.write(0, 1, 'abandoned')
    wt_sheet.write(0, 2, 'normal')

    for i in range(n_rows):
        # skip the title row
        if i == 0:
            continue
        row = rd_sheet.row_values(i)
        wt_sheet.write(i, 0, row[0])
        for j in range(n_class):
            # write the filename
            boxes = []
            boxes_str = row[j + 1].strip('[]').split(';')
            for box_str in boxes_str:
                if box_str == '':
                    continue
                position_tuple_4 = box_str.split(',')
                x1 = str(int(position_tuple_4[0]) - 1)
                y1 = str(int(position_tuple_4[1]) - 1)
                x2 = str(int(position_tuple_4[0]) - 1 + int(position_tuple_4[2]))
                y2 = str(int(position_tuple_4[1]) - 1 + int(position_tuple_4[3]))
                boxes.append([x1, y1, x2, y2])
            ret_strs = []
            for box in boxes:
                ret_strs.append(','.join(box))
            ret_str = '[' + ';'.join(ret_strs) + ']'
            # write annotations of <xxyy> format
            wt_sheet.write(i, j+1, ret_str)
    wt_workbook.save(args.ot)
    print('Transform successfully!')



