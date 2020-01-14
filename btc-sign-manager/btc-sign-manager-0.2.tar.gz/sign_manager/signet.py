import os
import textwrap
from collections import OrderedDict
from tempfile import NamedTemporaryFile
from typing import Collection

import fitz
from PIL import Image, ImageDraw, ImageFont
from django.conf import settings
from django.utils.timezone import now as tz_now
from typing.io import BinaryIO

from sign_manager.utils import format_date, parse_certificate


class TextLine:
    """
    Text string class for drawings
    """

    def __init__(self,
                 draw_object: ImageDraw,
                 text, necessary_width: int,
                 font: ImageFont,
                 font_color_rgb: tuple = (0, 0, 0),
                 sub_lines_vertical_indent: int = 2,
                 line_vertical_indent: int = 0):

        self.draw_object = draw_object
        self.font = font
        self.text = text
        self.font_color_rgb = font_color_rgb
        self.necessary_width = necessary_width
        self.sub_lines_vertical_indent = sub_lines_vertical_indent
        self.line_indent = line_vertical_indent

        self.text_width, self.text_height = draw_object.textsize(self.text, font=self.font)
        self.full_text_height = self.text_height + self.line_indent
        self.symbol_width = self.text_width / len(self.text)
        self.lines = textwrap.wrap(self.text, width=int(self.necessary_width // self.symbol_width))
        self.line = self.lines[:1][0]
        self.sub_lines = self.lines[1:]

    def draw(self, cursor_y_pos: int, cursor_x_pos: int, inner_vertical_indent: int) -> int:
        """
        Метод для рисования текста
        :param cursor_y_pos: int, начальная y-координата курсора-рисования
        :param cursor_x_pos: int, x-координата курсора-рисования
        :param inner_vertical_indent: int, рассчитанный отступ для строк текста
        :return: int, отступ для следующей строки 'TextLine'
        """
        indent = 0
        self.draw_object.text((cursor_x_pos, cursor_y_pos), self.line, fill=self.font_color_rgb, font=self.font)
        indent += self.full_text_height
        if self.sub_lines:
            indent += self.sub_lines_vertical_indent
        for sub_line in self.sub_lines:
            self.draw_object.text((cursor_x_pos, indent + cursor_y_pos), sub_line, fill=self.font_color_rgb,
                                  font=self.font)
            indent += self.sub_lines_vertical_indent + self.full_text_height
        indent += inner_vertical_indent
        return indent


class SignetCreator:
    """

    """

    @classmethod
    def draw_text_block(cls,
                        draw_object: ImageDraw,
                        title: str,
                        data_dict: dict,
                        block_height: int,
                        block_width: int,
                        y_coord: int = 10, x_coord: int = 15, font_size: int = 20,
                        font_path: str = '/assets/fonts/TimesNewRoman/TimesNewRomanBold.ttf',
                        font_color_rgb: tuple = (0, 0, 0)) -> None:
        """
        Функция для генерации временного файла изображения с данными 'data_dict'
        :param draw_object: Pillow-объект изображения
        :param block_height: доступная высота исходного изображения
        :param block_width: доступная ширина исходного изображения
        :param data_dict: словарь со строками для вывода
        :param title: заголовок блока
        :param y_coord: y-координата для текста
        :param x_coord: x-координата для текста
        :param font_size: размер шрифта
        :param font_path: путь к файлу шрифта
        :param font_color_rgb: цвет шрифта в формате 'rgb'
        :return: None
        """

        info_dict = OrderedDict(data_dict)
        text_lines = []
        text_lines_full_height = 0
        font = ImageFont.truetype(font_path, font_size)

        text_lines.append(TextLine(draw_object, title, block_width, font, font_color_rgb, line_vertical_indent=5))
        for info_string in info_dict.values():
            text_line = TextLine(draw_object, info_string, block_width, font, font_color_rgb)
            text_lines_full_height += text_line.full_text_height
            text_lines.append(text_line)

        text_lines_len = len(text_lines)
        lines_inner_vertical_indent = int((block_height - text_lines_full_height) / text_lines_len)

        # Подпись изображения данными
        cursor_pos = y_coord
        for line_object in text_lines:
            cursor_pos += line_object.draw(cursor_pos, x_coord, lines_inner_vertical_indent)

    @classmethod
    def insert_image_to_pdf(cls,
                            image_filepath: str,
                            pdf_filepath: str,
                            result_pdf_path: str,
                            image_coords: tuple,
                            pages_numbers: Collection = None) -> BinaryIO:
        """
        Функция для вставки изображения в pdf-файл
        :param image_filepath: путь до файла изображения
        :param pdf_filepath: путь до pdf-файла
        :param result_pdf_path: путь сохранения pdf-файла с изображением
        :param image_coords: координаты изображения,
        x0, y0, x1, y1 (1- левый верхний угол, 2 - нижний правый угол прямоугольника)
        :param pages_numbers: пересисление страниц для вставки изображения
        :return: BinaryIO
        """

        doc = fitz.open(pdf_filepath)
        if doc.isPDF:
            rect = fitz.Rect(image_coords)
            pix = fitz.Pixmap(image_filepath)
            pages = [doc[page_number] for page_number in pages_numbers] if pages_numbers else doc
            for page in pages:
                page.insertImage(rect, pixmap=pix, overlay=True)
            doc.save(result_pdf_path)
        return doc

    @classmethod
    def draw_pdf_signet(cls,
                        sign_cert_data: dict,
                        image_height: int,
                        image_width: int,
                        border_width: int) -> NamedTemporaryFile:
        """
        Функция для рисования данных в документе
        :param sign_cert_data: данные сертификата
        :param image_height: высота изображения
        :param image_width: ширина изображения
        :param border_width: размер границы
        :return: NamedTemporaryFile
        """

        owner_fio = parse_certificate(sign_cert_data.get('cert_subject_name'), 'CN=')
        owner_org = parse_certificate(sign_cert_data.get('cert_subject_name'), 'O=')
        owner_org_inn = parse_certificate(sign_cert_data.get('cert_subject_name'), 'INN=')
        cert_serial_number = sign_cert_data.get('cert_serial_number')
        cert_valid_from_date = sign_cert_data.get('cert_valid_from_date')
        cert_valid_to_date = sign_cert_data.get('cert_valid_to_date')

        data = OrderedDict()
        data['cert_info_first_block'] = dict(
            cert_owner_fio=f'Владелец: {owner_fio}',
            cert_owner_org=f'Организация: {owner_org} {owner_org_inn}',
            created=f'Подписано: {format_date(tz_now().date())}',
        )
        data['cert_info_second_block'] = dict(
            cert_serial_number=f'Серийный номер: {cert_serial_number}',
            cert_validity=f'Срок действия: {format_date(cert_valid_from_date)} - {format_date(cert_valid_to_date)}',
        )

        font_path = os.path.join(settings.ROOT_DIR, 'assets/fonts/TimesNewRoman/TimesNewRomanBold.ttf')
        image = Image.new('RGB', (image_width, image_height), (255, 255, 255))
        draw = ImageDraw.Draw(image)
        draw.rectangle(((0, 0), (image_width, image_height)), fill='white', outline=(0, 0, 0), width=border_width)

        cls.draw_text_block(draw,
                            'Данные электронной подписи',
                            data['cert_info_first_block'],
                            block_height=80,
                            block_width=image_width,
                            y_coord=5,
                            x_coord=10,
                            font_size=18,
                            font_path=font_path)

        cls.draw_text_block(draw,
                            'Данные сертификата',
                            data['cert_info_second_block'],
                            block_height=40,
                            block_width=image_width,
                            y_coord=125, x_coord=10,
                            font_size=18,
                            font_path=font_path)

        temp_image_file = image._dump()
        return temp_image_file
