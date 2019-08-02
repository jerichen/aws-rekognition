# -*- coding:utf-8 -*-
import xlrd
import xlwt
import boto3

if __name__ == "__main__":
    # 打開 xlsx 文件
    excel_data = xlrd.open_workbook("missdata.xlsx")

    # 取得第一張表的名稱
    row_data = excel_data.sheets()[0]
    print('表單數量：', excel_data.nsheets)
    print('表單名稱：', excel_data.sheet_names())

    # 取得第一個表單
    sheet_0 = excel_data.sheet_by_index(0)
    print('表單 %s 共 %d 行 %d 列' % (sheet_0.name, sheet_0.nrows, sheet_0.ncols))
    for i in range(1, sheet_0.nrows):
        print('第%s行第1列: %s' % (i, sheet_0.cell_value(i, 0)))
        print('images/%s.jpg' % sheet_0.cell_value(i, 0))
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
