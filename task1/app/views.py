from django.shortcuts import render
import csv


def inflation_view(request):
    template_name = 'inflation.html'

    with open('inflation_russia.csv', 'r', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file, delimiter=';')

        data_list = []
        for row in reader:
            data_list.append(row)

    months = data_list.pop(0)
    filtered_data_list = []

    for data_line in data_list:
        year = data_line[0]
        inflation = data_line[1:13]
        for i, item in enumerate(inflation):
            if item != '':
                inflation[i] = float(item)
        summ = data_line[13]

        filtered_data_list.append({'year': year, 'inflation': inflation, 'summ': summ})

    context = {
        'head': months,
        'data': filtered_data_list
    }

    return render(request, template_name,
                  context)
