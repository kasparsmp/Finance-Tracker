import csv
import gspread
import time


Month = "january"

File = f"2024_{Month}.csv"

Food = {"BoomCafe LV-1050 Riga", "NAC UN ED, AUDEJU IELA LV-1050 RIGA", "Latvijas 1. Rokkafejni LV-1050 Riga"}
Transport = {"HOLM BANK LATVIA SIA", "MOBILLY SIA", ""}

transactions = []


def main():
    try:
        with open(File, mode="r", encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file)  # delimiter=";"
            header = next(csv_reader)
            for row in csv_reader:
                if len(row) < 4:
                    continue
                date = row[0]
                name = row[1]
                payment_information = row[2]
                try:
                    amount = float(row[3])
                except ValueError:
                    amount = 0.0
                if name in Food:
                    category = "Food"
                else:
                    category = "Other"
                transaction = (date, name, payment_information, amount, category)
                transactions.append(transaction)
            return transactions
    except FileNotFoundError:
        print(f"File '{File}' not found.")
    except csv.Error:
        print(f"Error reading CSV file '{File}'.")


try:
    gc = gspread.service_account()
    sh = gc.open("Personal Finances")
    print(sh.sheet1.get('A1'))

    wks = sh.worksheet(f"{Month}")
    rows = main()
    if rows is not None:
        for row in rows:
            wks.insert_rows([row[0], row[1], row[3], row[4]], 8)
            time.sleep(2)
except gspread.SpreadsheetNotFound:
    print("Spreadsheet 'Personal Finances' not found.")
