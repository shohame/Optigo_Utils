import json

from collections import namedtuple
from dataclasses import dataclass
from ctypes import c_uint16
from typing import NamedTuple
from struct import pack, unpack
@dataclass
class point:
    x: c_uint16
    y: c_uint16
    z: c_uint16
    w: c_uint16


p1 = point(1, 2, 3, 4)
print (p1)
p1.x







class vect(NamedTuple):
    x: c_uint16
    y: c_uint16
    z: c_uint16
    w: c_uint16


b = pack('4H', 12,13,14,15)

v1 = vect(2,3,4,5)

print (v1)


data_structure = namedtuple('a', 'b', 'c')

data = data_structure(1, 2, 3)


class XVI_Annotation():
    def __init__(self, h_file):
        self.annot_fields = 1
        pass

    def get_annot(self):
        pass





