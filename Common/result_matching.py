# -*- utf-8 -*-
# @Create Data: 2024/4/19 15:53
# @Author: guangyang219579
# @File: result_matching.py
import base64
import os
import numpy as np
import cv2
from get_script_directory import get_script_directory


def get_imp_from_base64(base64data):
    imgData = base64.b64decode(base64data)
    nparr = np.fromstring(imgData, np.uint8)
    img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return img_np


def matchImgByTemplate(data, templatepath, threshold=0.9, x_range=[0, 1], y_range=[0, 1]):
    if type(data).__name__ == 'str' and os.path.exists(data):
        # img_rgb = ac.imread(data)
        img_rgb = cv2.imread(data)
    else:
        img_rgb = get_imp_from_base64(data)
    h_o, w_o, _ = img_rgb.shape
    # cv2.imwrite('D:/temp/o.jpg', img_rgb)
    print(templatepath)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(get_script_directory() + templatepath, 0)
    w, h = template.shape[::-1]
    # Perform match operations.
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    # Specify a threshold
    # 这里的0.7表示匹配度
    # threshold = 0.5
    # Store the coordinates of matched area in a numpy array
    loc = np.where(res >= threshold)
    x = loc[0]
    y = loc[1]
    # Draw a rectangle around the matched region.
    if len(x) and len(y):
        for pt in zip(*loc[::-1]):
            # 这里会把匹配到的位置用矩形框给框选出来
            # print('x=', x_range[0] * w_o, pt[0], x_range[1] * w_o, 'y=', y_range[0] * h_o, pt[1], y_range[1] * h_o)
            if not (pt[0] >= x_range[0] * w_o and pt[0] <= x_range[1] * w_o) or not (
                    pt[1] >= y_range[0] * h_o and pt[1] <= y_range[1] * h_o):
                continue
            print('I found ' + templatepath)
            cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)
            cv2.imwrite("D:/temp/0320.jpg", img_rgb)
            return int(pt[0] + w / 2), int(pt[1] + h / 2)
    else:
        print('there is no ' + templatepath)
        return -1, -1
