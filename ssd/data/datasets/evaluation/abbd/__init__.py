import json
import logging
import os
from datetime import datetime
from .box_utils import iou_of
import torch
import numpy as np


def abbd_evaluation(dataset, predictions, output_dir, iteration=None):
    abbd_results = []
    class_mapper = dataset.class_mapper
    total_num = 0
    sum_IoU = 0
    sum_AP50 = 0
    sum_AP75 = 0
    # for i, prediction in enumerate(predictions):
    #     img_info = dataset.get_img_info(i)
    #     prediction = prediction.resize((img_info['width'], img_info['height'])).numpy()
    #     boxes, labels, scores = prediction['boxes'], prediction['labels'], prediction['scores']
    #
    #     image_id, (gt_boxes, gt_labels) = dataset.get_annotation(i)
    #     new_boxes = boxes.tolist()
    #     labels = labels.tolist()
    #     scores = scores.tolist()
    #     print('labels: ', labels)
    #     print('gt_labels: ', gt_labels)
    #     abbd_results.extend(
    #         [
    #             {
    #                 "image_id": image_id,
    #                 "category_id": class_mapper[labels[k]],
    #                 "bbox": [box[0], box[1], box[2] - box[0], box[3] - box[1]],  # to xywh format
    #                 "score": scores[k],
    #             }
    #             for k, box in enumerate(new_boxes)
    #         ]
    #     )
    #     boxes = torch.from_numpy(boxes)
    #     gt_boxes = torch.from_numpy(gt_boxes)
    #     gt_labels = torch.from_numpy(gt_labels)
    #     n_class1 = 0
    #     for j in gt_labels:
    #         if j == 1:
    #             n_class1 += 1
    #     n_class2 = len(gt_labels) - n_class1
    #     class1_boxes = []
    #     class2_boxes = []
    #     count1 = 0
    #     count2 = 0
    #
    #     for j, lb in enumerate(labels):
    #         if lb == 1:
    #             if count1 < n_class1:
    #                 class1_boxes.append(np.array(boxes[j]))
    #                 count1 += 1
    #         elif lb == 2:
    #             if count2 < n_class2:
    #                 class2_boxes.append(np.array(boxes[j]))
    #                 count2 += 1
    #
    #     class1_boxes = torch.from_numpy(np.array(class1_boxes))
    #     class2_boxes = torch.from_numpy(np.array(class2_boxes))
    #     # print(gt_labels, n_class1, n_class2)
    #     ious_list = []
    #     if n_class1 > 0:
    #         ious1 = iou_of(gt_boxes[:n_class1], class1_boxes)
    #         ious_list.append(ious1)
    #     if n_class2 > 0:
    #         if len(class2_boxes) > 0:
    #             ious2 = iou_of(gt_boxes[n_class1:], class2_boxes)
    #             ious_list.append(ious2)
    #         else:
    #             total_num += n_class2
    #
    #     for ious in ious_list:
    #         for iou in ious.tolist():
    #             total_num += 1
    #             sum_IoU += iou
    #             if iou > 0.5:
    #                 sum_AP50 += 1
    #             if iou > 0.75:
    #                 sum_AP75 += 1
    #
    # json_result_file = os.path.join(output_dir, 'bbox' + '.json')
    logger = logging.getLogger("SSD.inference")
    # logger.info('Writing results to {}...'.format(json_result_file))
    # with open(json_result_file, "w") as f:
    #     json.dump(abbd_results, f)
    #
    # result_strings = []
    keys_map = {
        'mAP': sum_IoU,
        'AP50': sum_AP50,
        'AP75': sum_AP75,
    }

    metrics = {}
    for key in keys_map:
        metrics[key] = keys_map[key]
        logger.info('{:<10}: {}'.format(key, round(keys_map[key], 3)))
        # result_strings.append('{:<10}: {}'.format(key, round(keys_map[key], 3)))

    # if iteration is not None:
    #     result_path = os.path.join(output_dir, 'result_{:07d}.txt'.format(iteration))
    # else:
    #     result_path = os.path.join(output_dir, 'result_{}.txt'.format(datetime.now().strftime('%Y-%m-%d_%H-%M-%S')))

    # with open(result_path, "w") as f:
    #     f.write('\n'.join(result_strings))

    return dict(metrics=metrics)
