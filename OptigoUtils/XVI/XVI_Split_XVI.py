from .XVI_Globals import *
from .XVI_Reader import XVI_Reader
from .XVI_Writer import XVI_Writer

def XVI_Split_XVI(src_file_name, dest_file_name, frame_start, frame_stop, frame_gap=1):

    hXVI_src = XVI_Reader(src_file_name)
    src_header = hXVI_src.GetHeader()

    hXVI_dest = XVI_Writer(dest_file_name, src_header)

    for i in range(frame_start, frame_stop, frame_gap):
        frm = hXVI_src.ReadFrame(i)
        hXVI_dest.WriteFrame(frm)

    tt_src = hXVI_src.GetTimeTags()
    tt_dest = sTimeTags(tt_src)
    tt_dest.deltaFromFirstFrame = tt_src.deltaFromFirstFrame[frame_start:frame_stop:frame_gap]
    header_dest = hXVI_dest.GetHeader()
    header_dest.frame_rate = int(header_dest.frame_rate / frame_gap)

    hXVI_dest.WriteTimeTag(tt_dest)

    hXVI_dest.Close()

    hXVI_src.Close()


import sys

if __name__=='__main__':
    src_file_name = sys.argv[1]
    dest_file_name = sys.argv[2]
    frame_start = int(sys.argv[3])
    frame_stop = int(sys.argv[4])

    if len(sys.argv)>4:
        frame_gap = int(sys.argv[5])
    else:
        frame_gap = 1

    XVI_Split_XVI(src_file_name, dest_file_name, frame_start, frame_stop, frame_gap)



"""    
    src_file_name = '.\Raw_Data\Sample.XVI'
    dest_file_name = '.\Raw_Data\Sample_cut.XVI'
    frame_start = 1
    frame_stop = 8
    frame_gap = 2
    XVI_Split_XVI(src_file_name, dest_file_name, frame_start, frame_stop, frame_gap)
"""


