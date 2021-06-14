import os
import xlrd
import numpy as np
import torch.utils.data

from PIL import Image
from ssd.structures.container import Container


class MyDataset(torch.utils.data.Dataset):
    class_names = (
        '__background__',
        'abandon_building',
        'normal_building'
    )

    def __init__(self, data_dir, ann_file, transform=None, target_transform=None):
        ''' Dataset for abandon buildings
        '''
        self.data_dir = data_dir
        self.ann_file = ann_file
        self.transform = transform
        self.target_transform = target_transform
        
        self.ids = self._get_image_ids()
        self.ann_map = self._build_annotation_map()
        self.class_mapper = {i: class_name for i, class_name in enumerate(self.class_names)}

    def __getitem__(self, index):
        image_id = self.ids[index]
        boxes, labels = self._get_annotation(image_id)
        image = self._read_image(image_id)
        if self.transform:
            image, boxes, labels = self.transform(image, boxes, labels)
        if self.target_transform:
            boxes, labels = self.target_transform(boxes, labels)
        targets = Container(
            boxes=boxes,
            labels=labels,
        )
        return image, targets, index

    def __len__(self):
        return len(self.ids)

    def _build_annotation_map(self):
        ann_map = {}
        sheet = xlrd.open_workbook(self.ann_file).sheet_by_index(0)
        n_rows = sheet.nrows
        # remove '__background__'
        n_class = len(self.class_names) - 1
        for i in range(n_rows):
            # skip the title row
            if i == 0:
                continue
            row = sheet.row_values(i)
            boxes = []
            labels = []
            for j in range(n_class):
                boxes_str = row[j+1].strip('[]').split(';')
                for box_str in boxes_str:
                    if box_str == '':
                        continue
                    position_tuple_4 = box_str.split(',')
                    x1 = float(position_tuple_4[0])
                    y1 = float(position_tuple_4[1])
                    x2 = float(position_tuple_4[2])
                    y2 = float(position_tuple_4[3])
                    boxes.append([x1, y1, x2, y2])
                    labels.append(j+1)
            ann_map[row[0]] = (
                np.array(boxes, dtype=np.float32),
                np.array(labels, dtype=np.int64)
            )
        return ann_map

    def _get_image_ids(self):
        return os.listdir(self.data_dir)

    def _get_annotation(self, image_id):
        return self.ann_map[image_id]

    def _read_image(self, image_id):
        image_file = os.path.join(self.data_dir, image_id)
        image = Image.open(image_file).convert("RGB")
        image = np.array(image)
        return image

    def get_img_info(self, index):
        image_id = self.ids[index]
        image_file = Image.open(os.path.join(self.data_dir, image_id))
        return {"height": image_file.height, "width": image_file.width}

    def get_annotation(self, index):
        image_id = self.ids[index]
        return image_id, self._get_annotation(image_id)
