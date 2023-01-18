from struct import unpack, pack
from .XVI_Reader import *

class XVI_Writer:
    def __init__(self, file_name, header):
        self.file_name = file_name
        self.h_file = open(self.file_name, "wb")

        assert isinstance(header, sHeader), "Header must be sHeader class."
        self.header = sHeader(header)  # using copy constructor
        self.h_file.seek(XVI_HEADER_SIZE) # will write the header at the end
        self.written_frame_counter = 0

    def GetHeader(self):
        return self.header

    def WriteFrame(self, I):
        N = self.header.height * self.header.width
        I2 = np.reshape(I, N)
        if (self.header.bits_count == 8):
            f_str = pack('B' * N, *I2)
        elif (self.header.bits_count > 8 and self.header.bits_count <= 16):
            f_str = pack('h' * N, *I2)
        else:
            assert False, "Unsupported bits size."
        self.h_file.write(f_str)
        self.written_frame_counter += 1

    def WriteTimeTag(self, tt):
        if TT_MARKER_Idnt != tt.Marker:
            raise ('Incorrect Time Tag Marker!')
        b_tt = pack ('<8I', tt.Marker, tt.Year, tt.Month, tt.Day, tt.Hour, tt.Min, tt.Second, tt.MiliSec)
        n = len(tt.deltaFromFirstFrame)
        b_tt += pack(f'<{n}I', *tt.deltaFromFirstFrame)
        self.h_file.write(b_tt)

    def Close(self):
        # First write the header with the correct frame_count:
        self.header.frame_count = self.written_frame_counter
        self._write_header()
        self.h_file.close()

    def _write_header(self):
        self.h_file.seek(0)
        header = self.header
        b_header = pack('<8I',header.major_version, header.minor_version, header.frame_size, header.bits_count,
             header.width, header.height, header.frame_rate, header.frame_count)
        self.h_file.write(b_header)
        self.h_file.seek(XVI_HEADER_REMARKS_POS)
        if len(header.remarks)>0:
            self.h_file.write(header.remarks[:XVI_HEADER_SIZE - XVI_HEADER_REMARKS_POS].encode())

