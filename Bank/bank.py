import requests
import json
import csv
from flask import Flask, request, redirect, render_template


response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data=response.json()

#print(data)

currency_data = data[0]['rates']

print(currency_data[0]['currency'])

data_file = open('currency.csv', 'w')

csv_writer = csv.writer(data_file)

count = 0

for emp in currency_data:
	if count == 0:

		header = emp.keys()
		csv_writer.writerow(header)
		count += 1

	
	csv_writer.writerow(emp.values())

data_file.close()

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def set():
	result = 0
	if request.method=='POST':
		
		value = request.form.get('currency')
		many = request.form.get('many')
		print(value)
		print(many)
		result=f"{float(value)*float(many):.2f} PLN"
	return render_template("form.html", result=result, data=currency_data, title="Currency calculator")

if __name__ == '__main__':
    app.run(debug=False)