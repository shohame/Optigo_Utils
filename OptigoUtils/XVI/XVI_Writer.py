from .XVI_Reader import *
from struct import pack

class XVI_Writer:
    def __init__(self, file_name, header: XVI_Header):

        assert isinstance(header, XVI_Header), "Header must be XVI_Header class."

        self._file_name = file_name
        self._h_file = open(self._file_name, "wb")

        self._header = header.copy()  # copy header using copy constructor
        self._h_file.seek(XVI_HEADER_SIZE) # the header will be writen at the end
        self._number_of_frames = 0

    def GetHeader(self):
        return self._header

    def WriteFrame(self, I):
        N = self._header.height * self._header.width
        I2 = np.reshape(I, N)
        if (self._header.bits_count == 8):
            f_str = pack('B' * N, *I2)
        elif (self._header.bits_count > 8 and self._header.bits_count <= 16):
            f_str = pack('h' * N, *I2)
        else:
            assert False, "Unsupported bits size."
        self._h_file.write(f_str)
        self._number_of_frames += 1

    def Close(self):
        # First write the header with the correct frame_count:
        self._header.frame_count = self._number_of_frames
        self._write_header()
        self._h_file.close()

    def _write_header(self):
        self._h_file.seek(0)
        header = self._header
        b_header = pack('<8I',header.major_version, header.minor_version, header.frame_size, header.bits_count,
             header.width, header.height, header.frame_rate, header.frame_count)
        self._h_file.write(b_header)
        self._h_file.seek(XVI_HEADER_REMARKS_POS)
        if len(header.remarks)>0:
            self._h_file.write(header.remarks[:XVI_HEADER_SIZE - XVI_HEADER_REMARKS_POS].encode())

