#Program which behaves as sqlite3.exe file.

import sqlite3
import sys
from printy import printy

print("SQLite version 3.33.0 2020-08-14 13:23:32")
print("Enter \".help\" for usage hints.")

def get_connection(data_base):
	connection = sqlite3.connect(data_base)
	return connection


if len(sys.argv) == 2:
	data_base_name = sys.argv[1]
else:
	print("Connected to a ", end = "")
	printy("transient in-memory database", "r", end = "")
	print(".")
	print("Use \".open FILENAME\" to reopen on a persistent database.")
	data_base_name = 'temporary.db'

connection = get_connection(data_base_name)

while True:

	query = input("sqlite3> ")

	if query[0] == '.':
		if query == '.quit':
			connection.close()
			quit()
		elif query[:5] == '.open':
			connection.close()
			data_base_name = query[6:]
			connection = get_connection(data_base_name)

		elif query == '.table':

			cursor = connection.execute("SELECT name FROM sqlite_master WHERE type='table';")

			tables = cursor.fetchall()

			for table in tables:
				print(str(table[0]) + "    " , end = "")
			print("\t")
		else:
			print("Query not handled or invalid syntax.")
			continue
	else:
		try:
			cursor = connection.execute(query.replace(";", ""))
			output = cursor.fetchall()
			connection.commit()
		except:
			print("Invalid query/syntax")
			continue
		if output != []:
			for record in output:
				length_of_record = len(record)
				for index in range(length_of_record):
					print(record[index], end = "")
					if index != length_of_record - 1:
						print("|", end = "")
				print("\t")
