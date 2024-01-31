from django.shortcuts import render
import random
from datetime import datetime
import xlwt
from django.http import HttpResponse

def generate_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="sample.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Sheet')

    # Sheet header
    columns = ['Company Name', 'Company ID', 'Name', 'Amount', 'ABA Routing', 'Bank Account', 'Date', 'SEC']

    for col_num in range(len(columns)):
        ws.write(0, col_num, columns[col_num])

    # Sheet body
    for row_num in range(1, 100):  # let's say we want to generate 100 rows
        ws.write(row_num, 0, ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=random.randint(7, 14))))
        ws.write(row_num, 1, random.randint(1000000000, 9999999999))
        ws.write(row_num, 2, ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ ', k=random.randint(7, 15))))
        ws.write(row_num, 3, random.randint(-900, -100))
        ws.write(row_num, 4, random.randint(100000000, 999999999))
        ws.write(row_num, 5, random.randint(1000000000, 9999999999))
        ws.write(row_num, 6, datetime.now().strftime('%m/%d/%Y'))
        ws.write(row_num, 7, random.choice(['CCD', 'PPD']))

    wb.save(response)
    return response



