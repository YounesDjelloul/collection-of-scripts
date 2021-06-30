import pandas as pd

# list of files
files = ['file 1', 'file n']

# initializing the Final dict
fresh_dic = {}

# looping through the Files
for file in files:

	# Getting the data
	data = pd.read_excel(file)

	# Turning data to Dataframe
	df   = pd.DataFrame(data, columns=['Référence', 'Designation'])

	# Turning DataFrame to dict
	dic  = df.to_dict()

	# getting the Référence dict
	référence = list(dic.values())[0]

	# getting the products name dict
	products = list(dic.values())[1]

	# looping through the dicts to clarify them
	for i in range(0, len(products)):
		key   = référence[i]
		value = products[i]

		fresh_dic[key] = value

# Saving the Final Data into a TXT file
f = open("fresh_dic.txt", "a")
f.write(str(fresh_dic))
f.close()