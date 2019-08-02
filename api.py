# -*- coding:utf-8 -*-
from settings import *
from modules.read_excel import *
from modules.rekognition import *
import xlrd
import xlwt

if __name__ == "__main__":
    print('表單數量：', excel_data.nsheets)
    print('表單名稱：', excel_data.sheet_names())
    print('表單 %s 共 %d 行 %d 列' % (sheet_0.name, sheet_0.nrows, sheet_0.ncols))

    for i in range(1, sheet_0.nrows):
        print('第%s行第1列: %s' % (i, sheet_0.cell_value(i, 0)))
        IMAGE_FILE = os.path.join(os.getenv('IMAGES_PATH'), sheet_0.cell_value(i, 0) + '.jpg')
        print(IMAGE_FILE)

        for label in detect_labels(IMAGE_FILE):
            print(label['Name'])

        break

    # 依 webid 取得照片
    # imageFile = 'images/TPG07329132.jpg'
    # client = boto3.client('rekognition')
    #
    # with open(imageFile, 'rb') as image:
    #     response = client.detect_labels(Image={'Bytes': image.read()})
    #
    # print('Detected labels in ' + imageFile)
    # for label in response['Labels']:
    #     print(label['Name'] + ' : ' + str(label['Confidence']))
    #
    # print('Done...')
