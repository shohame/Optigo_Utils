
_EMUS_PER_PT = 12700

class PPTX_TextLine():

    __slots__ = ['ltwh', 'text' ,'font', 'hlink']

    def __init__(self, ltwh, font):
        self.ltwh = ltwh  # left, top, width, height
        self.text = ''
        self.font = font
        self.hlink = ''

class PPTX_Image():

    __slots__ = ['ltwh', 'file_path', 'hlink']

    def __init__(self, ltwh):
        self.ltwh = ltwh  # left, top, width, height
        self.file_path = ''
        self.hlink = ''


class PPTX_Slide:

    def __init__(self, size, configuration):


        self.top_lines: list[PPTX_TextLine] = []
        self.images: list[list[PPTX_Image]] = []

        text_lines = configuration['text_lines']
        images = configuration['images']
        dy = 0

        dy = self._setup_top_liens(size, text_lines, dy)
        dy += 100000
        dy = self._setup_images(size, images, dy)

    def get_lines_iterator(self):
        return self.top_lines

    def get_images_iterator(self):
        return self.images

    def set_line(self, line_idx, txt, hlink=''):
        self.top_lines[line_idx].text = txt
        self.top_lines[line_idx].hlink = hlink

    def set_image(self, x, y, file_path, hlink=''):
        self.images[y][x].file_path = file_path
        self.images[y][x].hlink = hlink

    def _setup_top_liens(self, size, text_lines, dy):

        for text_line in text_lines:
            font = text_line['font']
            l = 0
            t = dy
            w = size[0]
            h = font['size'] * _EMUS_PER_PT
            new_line = PPTX_TextLine((l, t, w, h), font)
            dy += h
            self.top_lines.append(new_line)
        return dy

    def _setup_images(self, size, images, dy):
        partition_x = images['partition_x']
        partition_y = images['partition_y']

        w, h = size
        h = h - dy

        pw, ph = w // sum(partition_x), h // sum(partition_y)

        for part_y in partition_y:
            dx = 0
            images_line = []
            h = ph * part_y
            for part_x in partition_x:
                l = dx
                t = dy
                w = pw * part_x

                new_image = PPTX_Image((l, t, w, h))
                images_line.append(new_image)
                dx += w
            self.images.append(images_line)
            dy += h
        return dy


if __name__ == '__main__':

    l = PPTX_TextLine((1,2,3,4), 'hi')
    l.a = 7
