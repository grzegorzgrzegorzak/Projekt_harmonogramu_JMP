from os import path, environ
from sys import path as sys_path

sys_path.append("/PYTHON/Projekt_harmonogramu_JMP/Harmonogram")
environ.setdefault('DJANGO_SETTINGS_MODULE',
                   'Harmonogram.Harmonogram.settings')

import django

django.setup()

import json
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter

import django

django.setup()

# from Harmonogram.schedule.models import Store


wb = load_workbook(
    filename="D:\Python\Projekt_harmonogramu_JMP\Harmonogram prac JMP (1).xlsx",
    data_only=True)

sheet = wb["2022"]

list_of_values = [i for i in sheet[1]]
# print(list_of_values, len(list_of_values), list_of_values[1].value)

print(list_of_values)

# for i in list_of_values(
#     if i[ ]
# )


print(sheet["A2"].value)


def cell_value(searching_name, counting):
    for i in list_of_values:
        if i.value == searching_name:
            letter = get_column_letter(i.column)
            return sheet[f"{letter}{counting}"].value


def get_street_or_number(string=str, position=int):
    if string:
        values = string.split()
        if len(values) == 1:
            return str(*values) if position == 0 else None
        elif len(values) == 2 and values[-1].isdigit():
            return values[position]
        elif len(values) == 2 and not values[-1].isdigit():
            return "".join(values) if position == 0 else None
        else:
            if position == 1:
                return values[-1]
            else:
                return "".join(values[:-1])

    else:
        return None

# def change_date()


def create_json():
    list_of_data = []
    for i in range(2, sheet.max_row):
        x = {
            "model": "schedule.store",
            "pk": i,
            "fields": {
                "store_number": f'{cell_value("Nr sklepu", i)}',
                "store_city": f'{cell_value("Miasto dostawy", i)}',
                "store_street": f'{get_street_or_number(cell_value("Ulica dostawy", i), 0)}',
                "store_street_number": f'{get_street_or_number(cell_value("Ulica dostawy", i), 1)}',
                "zip_code": f'{cell_value("Kod pocztowy", i)}',
                # "date_start_installation": f'{cell_value("Start montażu - dostawa listy zmiennej i mebli", i)}{cell_value("Miesiac montażu", i)}',
            }
        }
        list_of_data.append(x)
        with open("json_file.json", "w", encoding='utf-8') as outfile:
            json.dump(list_of_data, outfile, ensure_ascii=False)
        file = open("json_file.json", mode="r")
    return file


print(cell_value("Miasto dostawy", 5))
print(create_json())

