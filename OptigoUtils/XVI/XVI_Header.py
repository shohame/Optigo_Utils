from struct import unpack, calcsize
import copy as copy_
import numpy as np
from .XVI_General import *
from .XVI_TimeTags import XVI_TimeTags


class XVI_Header:
    def __init__(self, h_file=None, file_size=0):
        self.major_version  = 0
        self.minor_version  = 0
        self.frame_size     = 0
        self.bits_count     = 0
        self.width          = 0
        self.height         = 0
        self.frame_rate     = 0
        self.frame_count    = 0
        self.remarks = ''

        if h_file is not None:
            self.read_header(h_file, file_size)

    def read_header(self, h_file, file_size):
        h_file.seek(0)
        b_header = h_file.read(calcsize(HEADER_STRUCTURE_STR))
        i_header = unpack(HEADER_STRUCTURE_STR, b_header)

        (self.major_version,
         self.minor_version,
         self.frame_size,
         self.bits_count,
         self.width,
         self.height,
         self.frame_rate,
         self.frame_count) = i_header

        pixel_size = int(np.ceil(self.bits_count/8))
        calc_file_size_no_tt = XVI_HEADER_SIZE +  self.frame_count * self.width * self.height * pixel_size
        calc_file_size_with_tt = calc_file_size_no_tt + XVI_TimeTags.calc_time_tags_size(self.frame_count)

        if file_size != calc_file_size_no_tt and file_size != calc_file_size_with_tt:
            print_warning("The file size does not fit the header properties (frame_count, width, height).")

        h_file.seek(XVI_HEADER_REMARKS_POS)
        b_remarks = h_file.read(XVI_HEADER_SIZE - XVI_HEADER_REMARKS_POS)
        self.remarks = b_remarks.split(b'\x00')[0].decode('utf-8')

    def copy(self):
        new_obj = copy_.copy(self)
        return new_obj