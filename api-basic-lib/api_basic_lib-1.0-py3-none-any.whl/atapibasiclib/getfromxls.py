import xlrd
import os
def getdatafromxls(filename):
    file = xlrd.open_workbook(filename)
    table = file.sheet_by_name('testcases')
    rows = table.nrows
    cols = len(table.row_values(0))
    #存放列名
    filedname_list = []
    for c in range(cols):
        filedname_list.append(table.row_values(0)[c])
    print('filedname_list=%s'% filedname_list)
    row_dict = {}
    table_list = list(range(rows-1))
    for i in range(rows-1):
        for j in range(cols):
            row_dict[filedname_list[j]] = table.row_values(i+1)[j]
        table_list[i] = row_dict
        row_dict = {}
    return table_list

def get_case_data(filepath):
    # case_path = os.path.join(os.path.dirname(__file__), r'files\apiCase.xls')
    book = xlrd.open_workbook(filepath)
    sheet = book.sheet_by_name('testcases')
    case = []
    for i in range(0, sheet.nrows):
        case.append(sheet.row_values(i))
    print('cases=%s'% case)
    return case

#======================================
if __name__=='__main__':
    get_case_data('../datafiles/basicApi.xlsx')