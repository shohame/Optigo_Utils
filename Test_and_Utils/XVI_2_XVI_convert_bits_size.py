
import sys, os
current_file = os.path.abspath(__file__)
parent_dir = os.path.dirname(current_file)
parent_dir = os.path.dirname(parent_dir)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

import cv2
import numpy as np

from OptigoUtils.XVI.XVI_Reader import XVI_Reader
from OptigoUtils.XVI.XVI_Writer import XVI_Writer



def convert_xvi_from_12bits_to_8bits(src_file_name, dest_file_name):
    hXVI_src = XVI_Reader(src_file_name)
    src_header = hXVI_src.GetHeader()

    dest_header = src_header.copy()
    dest_header.bits_count = 8
    dest_header.frame_size = dest_header.frame_size // 2 - dest_header.width
    dest_header.height -= 1

    hXVI_dest = XVI_Writer(dest_file_name, dest_header)

    for frm_idx in range(hXVI_src.GetFrameCount()):
        print (frm_idx)
        frm = hXVI_src.ReadFrame(frm_idx, with_annotation=False)


        cv_img_uint8_ = cv2.normalize(frm, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
        cv_img_uint8 = cv2.equalizeHist(cv_img_uint8_)

        hXVI_dest.WriteFrame(cv_img_uint8)

    hXVI_dest.Close()
    hXVI_src.Close()




if __name__=="__main__":
    src_file_name = r'P:\work\Exec_2025.01.14_v45\HD_12_bpp_40.xvi'
    dest_file_name = r'P:\work\Exec_2025.01.14_v45\HD_8_bpp_40_1.xvi'
    convert_xvi_from_12bits_to_8bits(src_file_name, dest_file_name)


