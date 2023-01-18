


XVI_HEADER_SIZE = 1024
XVI_HEADER_REMARKS_POS = 512
TT_MARKER_Idnt  = 0x13572468


class sHeader:
    def __init__(self, header = None):
        if header is None:
            self.major_version  = 0
            self.minor_version  = 0
            self.frame_size     = 0
            self.bits_count     = 0
            self.width          = 0
            self.height         = 0
            self.frame_rate     = 0
            self.frame_count    = 0
            self.remarks = ''
        else:
            self.major_version  = header.major_version
            self.minor_version  = header.minor_version
            self.frame_size     = header.frame_size
            self.bits_count     = header.bits_count
            self.width          = header.width
            self.height         = header.height
            self.frame_rate     = header.frame_rate
            self.frame_count    = header.frame_count
            self.remarks        = header.remarks


class sTimeTags:
    def __init__(self, tt = None):
        if tt is None:
            self.Marker  = 0
            self.Year    = 0
            self.Month   = 0
            self.Day     = 0
            self.Hour    = 0
            self.Min     = 0
            self.Second  = 0
            self.MiliSec = 0
            self.deltaFromFirstFrame = []
        else:
            self.Marker  = tt.Marker
            self.Year    = tt.Year
            self.Month   = tt.Month
            self.Day     = tt.Day
            self.Hour    = tt.Hour
            self.Min     = tt.Min
            self.Second  = tt.Second
            self.MiliSec = tt.MiliSec
            self.deltaFromFirstFrame = tt.deltaFromFirstFrame.copy()


