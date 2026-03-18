from src import Extract, Load

extract = Extract()
uni_thai = extract.extract_country("Thailand")
print(type(uni_thai))
print(uni_thai)

load = Load()
load.create_sqlite_table(uni_thai, "universities.db", "universidades_thailand")
