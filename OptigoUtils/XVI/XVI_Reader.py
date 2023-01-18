import numpy as np
from struct import unpack
import os
from .XVI_Globals import *


def Read_XVI_Header(xvi_file_name):
    h_xviHeader = XVI_Reader(xvi_file_name)
    header = h_xviHeader.GetHeader()
    h_xviHeader.Close()
    return header

class XVI_Reader:
    def __init__(self, file_name):
        self.file_name = file_name
        self.file_size = os.path.getsize(self.file_name)
        self.hFile = open(self.file_name, "rb")
        self.header = self._read_header()
        self.TimeTags = self._read_time_tags()

    def GetHeader(self):
        return self.header

    def GetTimeTags(self):
        return self.TimeTags

    def Close(self):
        self.hFile.close()

    def GetFrameCount(self):
        return self.header.frame_count

    def ReadFrame(self, FrameIdx, with_annotation=True):

        self.hFile.seek(XVI_HEADER_SIZE + FrameIdx * self.header.frame_size)

        frm = self.hFile.read(self.header.frame_size)
        if (self.header.bits_count == 8):
            frm = unpack('B' * (len(frm)), frm)
        elif (self.header.bits_count > 8 and self.header.bits_count <= 16):
            frm = unpack('h' * (len(frm) // 2), frm)
        else:
            assert False, "Unsupported bits size."
        try:
            frm = np.reshape(frm, [self.header.height, self.header.width])
        except:
            return None
        if (with_annotation == False):
            frm = frm[:-1, :]
        return (frm)

    def _read_header(self):
        header = sHeader()
        self.hFile.seek(0)
        b_header = self.hFile.read(4 * 8)

        i_header = unpack('<8I', b_header)

        (header.major_version, header.minor_version, header.frame_size, header.bits_count,
         header.width, header.height, header.frame_rate, header.frame_count) = i_header

        self.hFile.seek(XVI_HEADER_REMARKS_POS)
        b_remarks = self.hFile.read(XVI_HEADER_SIZE - XVI_HEADER_REMARKS_POS)
        header.remarks = b_remarks.split(b'\x00')[0].decode('utf-8')
        return header

    def _read_time_tags(self):
        self.hFile.seek(XVI_HEADER_SIZE + self.header.frame_count * self.header.frame_size)
        TimeTags = sTimeTags()
        TimeTags.Marker = int.from_bytes(self.hFile.read(4), "little")

        if TT_MARKER_Idnt != TimeTags.Marker:
            return []

        b_tt = self.hFile.read(4 * 7)
        i_ii = unpack('<7I', b_tt)

        (TimeTags.Year, TimeTags.Month, TimeTags.Day,
         TimeTags.Hour, TimeTags.Min, TimeTags.Second, TimeTags.MiliSec) = i_ii

        tt = self.hFile.read(4 * self.header.frame_count)

        TimeTags.deltaFromFirstFrame = unpack(f'<{self.header.frame_count}I', tt)
        return TimeTags

