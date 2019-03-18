import csv
import locale

filename = "C:\\Users\\IosephKnecht\\PycharmProjects\\task_4\\amount_list.csv"


def sort_list(dict_reader):
    rows = list()
    for row in dict_reader:
        rows.append(row)

    return sorted(rows, key=lambda row: row.get('born_year'))


def calculate_sum(rows):
    sum_list = list()
    last_value = 0

    for row in rows:
        amount = row.get('amount')
        sum_list.append(int(amount) + last_value)
        last_value += int(amount)

    return sum_list


def insert_sum(dict_writer, rows, column_name):
    sum_list = calculate_sum(rows)
    iterator = iter(sum_list)

    for row in rows:
        row.update({column_name: iterator.__next__()})

    dict_writer.writeheader()
    dict_writer.writerows(rows)


def custom_print(row):
    locale.setlocale(locale.LC_ALL, row.get('locale'))
    amount = locale.currency(abs(int(row.get('amount'))), grouping=True)

    print('First name = {0}\n'
          'Last name = {1}\n'
          'Second name = {2}\n'
          'Born year = {3}\n'
          'Amount = {4}\n'.format(row.get('name'), row.get('lastname'), row.get('secondname'), row.get('born_year'),
                                  amount))


with open(filename, 'r+') as input_stream:
    reader = csv.DictReader(input_stream)

    sorted_list = sort_list(reader)
    sum_list = calculate_sum(sorted_list)

    with open(filename, 'w+') as output_stream:
        headers = sorted_list[0].keys()
        writer = csv.DictWriter(output_stream, sorted_list[0].keys())

        insert_sum(writer, sorted_list, 'sum')

        for row in sorted_list:
            custom_print(row)
