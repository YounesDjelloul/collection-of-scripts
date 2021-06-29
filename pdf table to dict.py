import tabula

# list of files
files = ['Verrerie.pdf']

# initializing the Final dict
fresh_dic = {}

for file in files:

	# Reading the file
	df = tabula.read_pdf(file, pages='all')

	# Loop through all tables
	for n in range(0, len(df)):

		# Getting the table and transforming it to a dict
		dic = df[n].to_dict()

		# getting the Référence dict
		référence = list(dic.values())[0]

		# getting the products name dict
		products = list(dic.values())[1]

		# looping through the dicts to clarify them
		for i in range(1, len(products)):

			key   = référence[i]
			value = products[i]

			fresh_dic[key] = value

f = open("fresh_dic.txt", "a")
f.write(str(fresh_dic))
f.close()