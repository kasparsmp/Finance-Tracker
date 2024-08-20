import csv
import gspread

gc = gspread.service_account()
sh = gc.open("Personal Finances")
print(sh.sheet1.get('A1'))


Month = "january"

File = f"2024_{Month}.csv"

Food = {"BoomCafe LV-1050 Riga", "NAC UN ED, AUDEJU IELA LV-1050 RIGA", "Latvijas 1. Rokkafejni LV-1050 Riga"}
Transport = {"HOLM BANK LATVIA SIA", "MOBILLY SIA", ""}

with open(File, mode="r", encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file) #delimiter=";"
    header = next(csv_reader)
    for row in csv_reader:
        date = row[0]
        name = row[1]
        payment_information = row[2]
        amount = float(row[3])
        if name in Food:
            category = "Food"
        else:
            category = "other"
        transaction = (date, name, payment_information, amount, category)

        print(transaction)