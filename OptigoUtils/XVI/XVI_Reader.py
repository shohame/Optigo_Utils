import numpy as np
import os
from .XVI_Header import *
from .XVI_Header import XVI_Header
from .XVI_TimeTags import XVI_TimeTags
from struct import unpack

def Read_XVI_Header(xvi_file_name):
    h_xviHeader = XVI_Reader(xvi_file_name)
    header = h_xviHeader.GetHeader()
    h_xviHeader.Close()
    return header

class XVI_Reader:
    def __init__(self, file_name):
        self.file_name = file_name
        file_size = os.path.getsize(self.file_name)
        self.hFile = open(self.file_name, "rb")
        self.header = XVI_Header(self.hFile, file_size)
        self.TimeTags = XVI_TimeTags(self.hFile, self.header.frame_count, self.header.frame_size)

    def GetHeader(self):
        return self.header

    def GetTimeTags(self):
        return self.TimeTags

    def Close(self):
        self.hFile.close()

    def GetFrameCount(self):
        return self.header.frame_count

    def ReadFrame(self, FrameIdx, with_annotation=True):
        try:
            # Seek to the correct position in the file
            self.hFile.seek(XVI_HEADER_SIZE + np.int64(FrameIdx) * self.header.frame_size)

            # Read the frame data
            frm = self.hFile.read(self.header.frame_size)
            if not frm:
                raise ValueError("Failed to read frame data from file.")

            # Unpack the frame data based on the bit depth
            if self.header.bits_count == 8:
                frm = np.frombuffer(frm, dtype=np.uint8)
            elif 8 < self.header.bits_count <= 16:
                frm = np.frombuffer(frm, dtype=np.int16)
            else:
                raise ValueError(f"Unsupported bits size: {self.header.bits_count}")

            # Reshape the frame data into a 2D array
            expected_size = self.header.height * self.header.width
            if len(frm) != expected_size:
                raise ValueError(f"Frame data size mismatch: expected {expected_size}, got {len(frm)}")

            frm = frm.reshape(self.header.height, self.header.width)

            # Optionally remove the last row if annotations are not needed
            if not with_annotation:
                frm = frm[:-1, :]

            return frm

        except Exception as e:
            print(f"An error occurred while reading frame {FrameIdx}: {e}")
            return None



