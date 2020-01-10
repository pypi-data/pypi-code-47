from .lk_logger import lk


def json_2_excel(ifile='../temp/in.json', ofile='../temp/out.xlsx',
                 header=None, auto_index=False, purify_values=False):
    """
    SPEC:
        支持的数据格式:
            [<list|str|int|float row>, ...]
            {key: <str|int|float value>}
        不支持的:
            [<dict row>, ...]
            {key: <list value>} (未来将尽快支持)
            {key: <dict value>}
    """
    from .excel_writer import ExcelWriter
    from .read_and_write import read_json
    
    reader = read_json(ifile)
    writer = ExcelWriter(ofile)
    if header:
        writer.writeln(*header)
    
    if isinstance(reader, list):
        for row in reader:
            writer.writeln(
                *row, auto_index=auto_index, purify_values=purify_values
            )
    else:  # dict
        for k, v in reader.items():
            writer.writeln(
                k, v, auto_index=auto_index, purify_values=purify_values
            )
    
    writer.save()


def excel_2_json(ifile='../temp/in.xlsx', ofile='../temp/out.json',
                 key='index'):
    """
    将 excel 转换为 json.
    ARGS:
        ifile
        ofile
        key: 主键依据. 默认是行号, 因为行号是不重复的, 适合作为字典的键. 您也可
        以定义表格中的某个字段为主键. 另外, 如果 key 设为空字符串, 则以列表形式
        输出每一行.
    IN: ifile
    OT: ofile
    """
    from .excel_reader import ExcelReader
    from .read_and_write import write_json
    
    reader = ExcelReader(ifile)
    writer = {}
    
    if key == 'index':
        if key not in reader.get_header():
            mode = 0
        else:
            mode = 1
    elif key == '':
        # 如果 key 为空字符串, 则以列表形式输出每一行
        writer = tuple(reader.row_values(rowx) for rowx in reader.get_range(1))
        write_json(writer, ofile)
        return
    else:
        mode = 2
    
    for rowx in reader.get_range(1):
        row = reader.row_dict(rowx)
        
        if mode == 0:
            writer[rowx] = row
        elif mode == 1:
            writer[row['index']] = row
        elif mode == 2:
            # noinspection PyBroadException
            try:
                writer[row[key]] = row
            except Exception:
                lk.logt('[data_converter][W0536]',
                        'cannot convert this row because of KeyError',
                        row, key, h='parent')
    
    write_json(writer, ofile)


def excel_2_json_kv(ifile='../temp/in.xlsx', ofile='../temp/out.json',
                    header=False):
    """
    将 excel 转换为 json 文件. 要求 excel 只有两列数据 (占据第一, 第二列位置),
    且目标数据位于 sheet 1. 最后转换的结果是以第一列为 keys, 第二列为 values.
    """
    from .excel_reader import ExcelReader
    from .read_and_write import write_json
    
    reader = ExcelReader(ifile)
    
    offset = 0 if header else 1
    
    writer = {k: v for k, v in zip(
        reader.col_values(0, offset),
        reader.col_values(1, offset)
    )}
    
    write_json(writer, ofile)


# ------------------------------------------------

# noinspection PyUnresolvedReferences
def pdf_2_txt(ifile, ofile, page_start=0, page_end=0, dump_images=''):
    """
    extract plain text from pdf file.
    ARGS:
        ifile: 要传入的 pdf 文件路径, 以 '.pdf' 结尾.
        ofile: 要输出的文本文件路径. 以 '.txt' 结尾.
        page_start: 开始页. 从 0 开始数.
        page_end: 结束页. 从 0 开始数. 当为 0 时, 表示导出到最后一页.
        dump_images: 是否导出 pdf 中的图片. 传入一个目录. 空字符串表示不导出.
    REF: https://github.com/pdfminer/pdfminer.six/blob/master/tools/pdf2txt.py
    IN: ifile
    OT: ofile
    """
    from pdfminer import layout
    from pdfminer.converter import TextConverter
    from pdfminer.image import ImageWriter
    from pdfminer.pdfdocument import PDFDocument
    from pdfminer.pdfinterp import PDFPageInterpreter, PDFResourceManager
    from pdfminer.pdfpage import PDFPage
    from pdfminer.pdfparser import PDFParser
    
    laparams = layout.LAParams()
    image_writer = ImageWriter(dump_images) if dump_images else None
    # NOTE: 我对 pdfminer.image 的源码 (
    # C:\Common\devenv\python_messy_libs\Lib\site-packages\pdfminer\image.py) 进
    # 行了修改, 增加了 self.picno 变量以避免导出时的图片名重复, 详见源码中的
    # "LKDO" 标记.
    
    reader = open(ifile, 'rb')
    writer = open(ofile, 'w', encoding='utf-8')
    
    manager = PDFResourceManager(caching=False)
    device = TextConverter(manager, writer, codec='utf-8', laparams=laparams,
                           imagewriter=image_writer)
    interpreter = PDFPageInterpreter(manager, device)
    parser = PDFParser(reader)
    doc = PDFDocument(parser, caching=False)
    
    if not doc.is_extractable:
        lk.logt('[data_converter][E0906]', 'extraction forbidden', ifile,
                h='parent')
        raise Exception
    
    for pageno, page in enumerate(PDFPage.create_pages(doc)):
        if pageno < page_start:
            continue
        if page_end and pageno > page_end:
            break
        lk.loga(pageno, h='parent')
        interpreter.process_page(page)
    
    if dump_images:
        lk.loga(f'there are {image_writer.picno} images dumped', h='parent')
    
    device.close()
    reader.close()
    writer.close()


# noinspection PyUnresolvedReferences
def pdf_2_excel(ifile, ofile, page_start=0, page_end=0, indicator=True):
    """
    IN: ifile
    OT: ofile

    ARGS:
        ifile: postfixed with '.pdf'
        ofile: postfixed with '.xlsx'
        page_start: count from 0
        page_end: 0 means 'auto detect all pages'
        indicator: True means adding pageno, tableno and lineno fields

    REF: https://www.jianshu.com/p/f33233e4c712
    """
    import pdfplumber
    from .excel_writer import ExcelWriter
    
    reader = pdfplumber.open(ifile)
    writer = ExcelWriter(ofile or ifile.replace('.pdf', '.xlsx'))
    
    if indicator:
        writer.writeln('pageno', 'tableno', 'lineno')
    
    if page_end == 0:
        pages = reader.pages[page_start:]
    else:
        pages = reader.pages[page_start:page_end]
    
    pageno = tableno = lineno = 0
    
    for p in pages:
        pageno += 1
        lk.logd(f'pageno = {pageno}, lineno = {lineno}', h='parent')
        for table in p.extract_tables():
            tableno += 1
            for row in table:
                lineno += 1
                if indicator:
                    writer.writeln(pageno, tableno, lineno, *row)
                else:
                    writer.writeln(*row)
    
    reader.close()
    writer.save()
