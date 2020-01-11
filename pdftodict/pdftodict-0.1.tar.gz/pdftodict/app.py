from pprint import pprint
from scrappers import ScrapeData
from utils import PDFReader


class PDFScrapper:
    inline_datas = {
        'business': {
            "The Following Are The Brief Particulars of": [
                'Name of Business',
                'Former Name(s) if any',
                'Date of Change of Name',
                'Registration No',
                'Registration Date',
                'Commencement Date',
                'Status of Business',
                'Status Date',
                'Renewal Date',
                'Expiry Date',
                'Renewal via GIRO',
                'Constitution of Business',
                'Principal Place of Business',
                'Date of Change of Address'
            ]
        }
    }

    def __init__(self):
        self.scrapper = ScrapeData()

    def start(self, path, b_type="business"):
        result_data = dict()

        PDFReader.load_pdf(path)
        pdf = PDFReader.get_pdf()
        if not pdf:
            print('Invalid PDF!')
            return
        print("PDF has opened successfully!")

        print('Processing inline datas...')
        inline_data = dict()
        for attr_name, attr_fields in self.inline_datas[b_type].items():
            tempo_datas = dict()
            for v in attr_fields:
                tempo_datas[v] = self.scrapper.get_inline_data(1, v)
            inline_data[attr_name] = tempo_datas
        result_data.update(inline_data)

        print('Processing principal activities...')
        principal_activities = self.scrapper.get_principal_activities()
        result_data.update(principal_activities)

        pprint(result_data)
        return result_data
