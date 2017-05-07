# coding: utf-8
"""
	author: brtgpy
"""

from PIL import Image

"""
	image process functions before ocr
"""

def split_img(img, img_data, img_width, img_height):
	"""
		图像中一般会含有多个数字，识别的时候只能根据每个字符的特征来进行判断，所以还要把图像中的字符独立的切割出来。
	"""
    imgs = []
    split_info = []
    left = right = top = bottom = 0
    y_set = set()
    for x in range(img_width):
        all_is_white = True
        for y in range(img_height):
            if img_data[x, y] == WHITE:
                continue
            all_is_white = False
            if not left:
                left = x
            y_set.add(y)
        if all_is_white and left and not right:
            right = x
            top = min(y_set)
            bottom = max(y_set)
            split_info.append((left, right, top, bottom))
            left = right = top = bottom = 0
            y_set = set()
    for left, right, top, bottom in split_info:
        box = (left, top - 1, right, bottom + 1)
        new_img = img.crop(box)
        imgs.append(new_img)
    return imgs