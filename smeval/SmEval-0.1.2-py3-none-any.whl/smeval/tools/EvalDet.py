import json
import numpy as np
import math


def jaccard(box_a, box_b):
    inter = intersect(box_a, box_b)

    A = inter.shape[0]
    B = inter.shape[1]

    area_a = np.expand_dims(((box_a[:, 2] - box_a[:, 0]) *
                             (box_a[:, 3] - box_a[:, 1])), axis=1)
    area_a = np.tile(area_a, (1, B))
    area_b = np.expand_dims(((box_b[:, 2] - box_b[:, 0]) *
                             (box_b[:, 3] - box_b[:, 1])), axis=0)
    area_b = np.tile(area_b, (A, 1))
    union = area_a + area_b - inter + 1e-4
    # print(union)
    return inter / union  # [A,B]


def intersect(box_a, box_b):
    A = box_a.shape[0]
    B = box_b.shape[0]

    box_a_expand = np.expand_dims(box_a[:, 2:], axis=1)
    box_a_expand = np.tile(box_a_expand, (1, B, 1))
    box_b_expand = np.expand_dims(box_b[:, 2:], axis=0)
    box_b_expand = np.tile(box_b_expand, (A, 1, 1))

    max_xy = np.minimum(box_a_expand, box_b_expand)

    box_a_expand = np.expand_dims(box_a[:, :2], axis=1)
    box_a_expand = np.tile(box_a_expand, (1, B, 1))
    box_b_expand = np.expand_dims(box_b[:, :2], axis=0)
    box_b_expand = np.tile(box_b_expand, (A, 1, 1))

    min_xy = np.maximum(box_a_expand, box_b_expand)
    inter = np.clip((max_xy - min_xy), a_min=0, a_max=1e10)
    return inter[:, :, 0] * inter[:, :, 1]


def get_bbox(file, class_name):
    file_read = open(file, 'r')
    imgs_box = {}
    for json_line in file_read.readlines():
        img_json = json.loads(json_line.strip())
        objs = img_json["label"][0]["data"]
        objs_info = []
        #   print(img_json['url'])
        for obj in objs:
            obj_class_conf = float(obj['scores'][0]) if len(obj['scores']) else 1.0
            obj_class_index = class_name.index(obj['class'][0])
            # if obj_class_conf<conf_thresold:
            #     continue
            obj_info = [obj['bbox'][0][0], obj['bbox'][0][1], obj['bbox'][2][0], obj['bbox'][2][1], obj_class_index,
                        obj_class_conf]
            objs_info.append(obj_info)
        objs_info = np.array(objs_info)
        imgs_box[img_json['url'].split('/')[-1]] = objs_info

    file_read.close()

    return imgs_box


def draw_pr_curve(rec, acc, class_name, models_name):
    from matplotlib import pyplot as plt
    plt.figure(figsize=[8, 8])

    for cls_index in range(len(rec[0])):
        img_row = math.ceil(math.sqrt(len(rec[0])))
        img_col = math.ceil(len(rec[0]) / img_row)
        plt.subplot(img_row, img_col, cls_index + 1)
        for i, (rec_model, acc_model) in enumerate(zip(rec, acc)):
            plt.title('class :{}'.format(class_name[cls_index]))
            plt.plot(rec_model[cls_index], acc_model[cls_index], label=models_name[i])
        plt.xlabel('rec')
        plt.ylabel('prec')
    plt.legend()
    plt.savefig('./pelee_960_4.jpg')
    plt.show()


def voc_ap(rec, prec, use_07_metric=False):
    if use_07_metric:
        # 11 point metric
        ap = 0.
        for t in np.arange(0., 1.1, 0.1):
            if np.sum(rec >= t) == 0:
                p = 0
            else:
                p = np.max(prec[rec >= t])
            ap = ap + p / 11.
    else:
        mrec = np.concatenate(([0.], rec, [1.]))
        mpre = np.concatenate(([0.], prec, [0.]))

        # compute the precision envelope
        for i in range(mpre.size - 1, 0, -1):
            mpre[i - 1] = np.maximum(mpre[i - 1], mpre[i])

        # to calculate area under PR curve, look for points
        # where X axis (recall) changes value
        i = np.where(mrec[1:] != mrec[:-1])[0]

        # and sum (\Delta recall) * prec
        ap = np.sum((mrec[i + 1] - mrec[i]) * mpre[i + 1])
    return ap


def cal_acc_recall(gt_file, infer_file, class_name, iou_threshold):
    all_objs_gt = get_bbox(gt_file, class_name)
    all_objs_bt = get_bbox(infer_file, class_name)
    tp_class = [[] for _ in range(len(class_name))]
    fp_class = [[] for _ in range(len(class_name))]
    gt_num = [0 for _ in range(len(class_name))]
    for i, name in enumerate(all_objs_gt):
        print(i)
        objs_gt = all_objs_gt[name]
        if not name in all_objs_bt.keys():
            continue
        objs_bt = all_objs_bt[name]
        if len(objs_gt) == 0 and len(objs_bt) == 0:
            continue
        elif len(objs_gt) == 0:
            for class_i in range(len(class_name)):
                fp_class.extend(list(objs_bt[np.where(objs_bt[..., 4] == class_i)][..., 5]))
        elif len(objs_bt) == 0:
            for class_i in range(len(class_name)):
                gt_num[class_i] += len(list(objs_gt[np.where(objs_gt[..., 4] == class_i)][..., 5]))
        else:
            iou = jaccard(objs_gt[..., :4], objs_bt[..., :4])

            for class_i in range(len(class_name)):
                gt_valid_index = np.where(objs_gt[..., 4] == class_i)[0]
                gt_num[class_i] += len(gt_valid_index)
                bt_valid_index = np.where((objs_bt[..., 4] == class_i))[0]
                gt_invalid_index = np.where(objs_gt[..., 4] != class_i)[0]
                bt_invalid_index = np.where((objs_bt[..., 4] != class_i))[0]

                iou_class = iou.copy()
                iou_class[..., bt_invalid_index] = 0
                iou_class[gt_invalid_index, ...] = 0
                match_gt_indexs, match_bt_indexs = np.where(
                    (iou_class == np.max(iou_class, axis=0)) * (iou_class > iou_threshold))

                # 选择匹配到统一gt框的最大iou作为gt框匹配到的dt框
                match_gt_index_max = {}
                match_bt_dict = {}
                for match_gt_index, match_bt_index in zip(match_gt_indexs, match_bt_indexs):
                    if not match_gt_index in match_gt_index_max.keys():
                        match_gt_index_max[match_gt_index] = iou_class[match_gt_index, match_bt_index]
                        match_bt_dict[match_gt_index] = match_bt_index
                    else:
                        if match_gt_index_max[match_gt_index] < iou_class[match_gt_index, match_bt_index]:
                            match_gt_index_max[match_gt_index] = iou_class[match_gt_index, match_bt_index]
                            match_bt_dict[match_gt_index] = match_bt_index

                match_bt_index_filter = set(match_bt_dict.values())

                no_match_bt = list(set(bt_valid_index).difference(match_bt_index_filter))

                tp = list(objs_bt[list(match_bt_index_filter), 5])
                fp = list(objs_bt[no_match_bt, 5])

                tp_class[class_i].extend(tp)
                fp_class[class_i].extend(fp)

    rec_all = []
    prec_all = []

    for class_i in range(len(class_name)):

        det_conf = []

        for conf in tp_class[class_i]:
            det_conf.append([conf, 1])

        for conf in fp_class[class_i]:
            det_conf.append([conf, 0])

        det_conf.sort(key=lambda x: float(x[0]), reverse=True)

        tp = list(np.array(det_conf, dtype=np.int)[..., 1])
        fp = [1 - t for t in tp]

        cumsum = 0
        for idx, val in enumerate(fp):
            fp[idx] += cumsum
            cumsum += val
        cumsum = 0
        for idx, val in enumerate(tp):
            tp[idx] += cumsum
            cumsum += val

        rec = tp[:]
        for idx, val in enumerate(tp):
            rec[idx] = float(tp[idx] + 1e-10) / (gt_num[class_i] + 1e-10)
        # print("len-recall", len(rec))
        prec = tp[:]
        for idx, val in enumerate(tp):
            prec[idx] = float(tp[idx] + 1e-10) / (fp[idx] + tp[idx] + 1e-10)

        rec_all.append(rec)
        prec_all.append(prec)
    return rec_all, prec_all


def det_eval(gt_file, bt_file, class_name, models_name, iou_threshold):
    """
    :param gt_file:  str input file like 'test/gt.json'
    :param bt_file:  [str] models like ['test/mdoel_1.json','test/mdoel_2.json']
    :param class_name:  [str] classification names like ['person', 'non-motor', 'car', 'tricycle']
    :param models_name:  [str] classification names like ['pelee-fp32','pelee-int8-1']
    :param iou_threshold: float eval iou threshold like 0.5
    :return:
    """
    recs = []
    precs = []
    for bt_file in bt_file:
        rec, prec = cal_acc_recall(gt_file, bt_file, class_name, iou_threshold)
        recs.append(rec)
        precs.append(prec)
    draw_pr_curve(recs, precs, class_name, models_name)
    for i in range(bt_file):
        print("==============================")
        for j, name in enumerate(class_name):
            print('model:{} class:{} ap:{}'.format(i, name, voc_ap(recs[i][j], precs[i][j])))


if __name__ == '__main__':
    det_eval('test/gt.json', ['test/mdoel_1.json', 'test/mdoel_2.json'], ['person', 'non-motor', 'car', 'tricycle'],
             ['pelee-fp32', 'pelee-int8-1'], 0.5)
