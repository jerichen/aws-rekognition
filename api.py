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

    # 寫入新的excel title
    new_sheet.write(0, 0, 'webid')
    new_sheet.write(0, 1, 'Image No.')
    new_sheet.write(0, 2, '圖片名稱')
    new_sheet.write(0, 3, 'labes')

    for i in range(1, sheet_0.nrows):
        IMAGE_FILE = os.path.join(os.getenv('IMAGES_PATH'), sheet_0.cell_value(i, 0) + '.jpg')
        print('--------------------------------------------------')
        print('圖片名稱 : ' + IMAGE_FILE)

        new_sheet.write(i, 0, sheet_0.cell_value(i, 0))
        new_sheet.write(i, 1, sheet_0.cell_value(i, 1))
        new_sheet.write(i, 2, IMAGE_FILE)

        labels = detect_labels(IMAGE_FILE)
        if type(labels) is list:
            j = 2
            for label in labels:
                j += 1
                new_sheet.write(i, j, label['Name'])
        else:
            print('call api fail')

        # labels = ['Nature', 'Outdoors', 'Countryside', 'Hill', 'Slope', 'Mountain', 'Plateau', 'Mountain', 'Range']
        # j = 2
        # for label in lists:
        #     j += 1
        #     new_sheet.write(i, j, label)

        print('--------------------------------------------------')
        break

    new_excel.save('images-labels.xls')
    print('Done..............')
