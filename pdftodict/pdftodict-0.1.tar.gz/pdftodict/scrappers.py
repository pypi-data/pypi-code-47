from utils import PDFReader


class ScrapeData:
    def __init__(self, border=10):
        self.border = border

    @property
    def pdf(self):
        return PDFReader.get_pdf()
    
    @property
    def width(self):
        return PDFReader.get_width()
    
    @property
    def height(self):
        return PDFReader.get_height()

    def get_from_page_bbox(self, page, bbox):
        data = self.pdf.pq(
            'LTPage[pageid="{}"] :in_bbox("{}, {}, {}, {}")'.format(page, *bbox))
        data = [x[0].layout for x in data.items()]

        return data

    def get_data_y_pos(self, page, bbox):
        double_dot_founded = False
        tempo_data = self.get_from_page_bbox(page, bbox)
        value = tempo_data[0].get_text().strip()
        new_y = 0

        while not double_dot_founded:
            bbox[2] += 10
            tempo_data = self.get_from_page_bbox(page, bbox)

            for x in tempo_data:
                try:
                    if x.get_text().strip().find(value) == -1:

                        double_dot_founded = True
                        new_y = x.bbox[0]
                        break
                except AttributeError:
                    continue
        bbox[2] = new_y - self.border
        return bbox

    def get_data_x_pos(self, page, bbox):
        tempo_data = self.get_from_page_bbox(page, bbox)
        curr_len = len(tempo_data)

        while curr_len == len(tempo_data):
            curr_len = len(tempo_data)
            bbox[1] -= 10
            tempo_data = self.get_from_page_bbox(page, bbox)

        bbox[0] = bbox[2] - 10
        bbox[1] += 10
        bbox[2] = self.width

        return bbox

    def get_str_result(self, result_data):
        res = ''
        for x in result_data:
            try:
                append_data = x.get_text().strip()
                if append_data[0] == ':':
                    append_data = append_data[1:].strip()
                if not append_data in res:
                    res += append_data + ' '
            except AttributeError:
                continue

        return res.strip()

    def get_inline_data(self, page, val):
        data = self.pdf.pq(
            'LTPage[pageid="{}"] :contains("{}")'.format(page, val)
        ).items()
        data = [x[0].layout for x in data]

        bbox = list(data[0].bbox)

        bbox[0] -= self.border
        bbox[1] -= self.border
        bbox[2] += self.border
        bbox[3] += self.border

        bbox = self.get_data_y_pos(page, bbox)

        bbox = self.get_data_x_pos(page, bbox)

        result_data = self.get_from_page_bbox(page, bbox)

        str_result_data = self.get_str_result(result_data)

        return str_result_data

    def get_principal_activities(self):
        return {}
    