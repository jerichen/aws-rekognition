# -*- coding:utf-8 -*-
from settings import *
from modules.read_excel import *
from modules.rekognition import *
import xlrd
import xlwt

if __name__ == "__main__":
    print('--------------------------------------------------')
    print('表單數量：', excel_data.nsheets)
    print('表單名稱：', excel_data.sheet_names())
    print('表單 %s 共 %d 行 %d 列' % (sheet_0.name, sheet_0.nrows, sheet_0.ncols))

    for i in range(1, sheet_0.nrows):
        IMAGE_FILE = os.path.join(os.getenv('IMAGES_PATH'), sheet_0.cell_value(i, 0) + '.jpg')
        print('--------------------------------------------------')
        print('第 %s 行第 1 列: %s' % (i, sheet_0.cell_value(i, 0)))
        print('圖片名稱 : ' + IMAGE_FILE)

        lists = ['Nature', 'Outdoors', 'Countryside', 'Hill', 'Slope', 'Mountain', 'Plateau', 'Mountain', 'Range']


        # labels = detect_labels(IMAGE_FILE)
        # if type(labels) is list:
        #     for label in labels:
        #         print(label['Name'])
        # else:
        #     print('call api fail')

        break

    # print('Done...')
