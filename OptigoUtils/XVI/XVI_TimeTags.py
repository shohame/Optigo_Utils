import struct
from struct import pack
import copy as copy_
import numpy as np
from struct import unpack, calcsize
from .XVI_General import *


class XVI_TimeTags:
    def __init__(self, h_file, frame_count, frame_size):
        self.Marker  = 0
        self.Year    = 0
        self.Month   = 0
        self.Day     = 0
        self.Hour    = 0
        self.Min     = 0
        self.Second  = 0
        self.MiliSec = 0
        self.deltaFromFirstFrame = []
        self._read_time_tags(h_file, frame_count, frame_size)

    def copy(self):
        new_obj = copy_.deepcopy(self)
        return new_obj

    @staticmethod
    def calc_time_tags_size(frame_count):
        return (calcsize(TT_STRUCTURE_STR) + 4 * frame_count)
    @staticmethod
    def get_time_tags_header_size():
        return calcsize(TT_STRUCTURE_STR)

    def update(self, time_date, msec_diff_arr):
        pass


    def _read_time_tags(self, h_file, frame_count, frame_size):

        try:
            h_file.seek(XVI_HEADER_SIZE + np.int64(frame_count) * frame_size)
            b_tt =h_file.read(struct.calcsize(TT_STRUCTURE_STR))
            tt_struct = unpack(TT_STRUCTURE_STR, b_tt)

            (self.Marker, self.Year, self.Month, self.Day,
             self.Hour, self.Min, self.Second, self.MiliSec) = tt_struct

            if TT_MARKER_Idnt != self.Marker:
                raise 0
            tt = h_file.read(4 * frame_count)

            self.deltaFromFirstFrame = list(unpack(f'<{frame_count}I', tt))

        except Exception as e:
            print_warning( "Can't find suitable time tags structure!")


def WriteTimeTag(self, h_file):
        if TT_MARKER_Idnt != self.Marker:
            raise ('Incorrect Time Tag Marker!')
        b_self = pack ('<8I', self.Marker, self.Year, self.Month, self.Day, self.Hour, self.Min, self.Second, self.MiliSec)
        n = len(self.deltaFromFirstFrame)
        b_self += pack(f'<{n}I', *self.deltaFromFirstFrame)
        h_file.write(b_self)
