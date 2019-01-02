#oz to gram calculator & lb to gram calculator & oz to ml calculator
#oz - gram = 1:28.34
#oz - ml = 1:28.41
#lb to gram =  1: 453
#from tkinter


def ozToml(ozm):
	ounce = 0
	ounce = ozm
	ml = 28.41
	finval = ounce * ml
	print(str(finval) + " ml")

def ozTog(ozl):
	ounce = 0
	ounce = ozl
	gram = 28.34
	finval = ounce * gram
	print(str(finval) + " grams")
	


def _main_ ():

	options = int(input("pick: \n 1, oz to gram \n 2. oz to ml \n type in 1 or 2 for your choice"))
	#choice = (input("How many OZ did the recipe say?: "))


	if options == 1:

		choice = (input("How many OZ did the recipe say?: \n"))

		if isinstance(float(choice), float) == True:

			ozTog(float(choice))
		else:
			print("please stop\n")
	elif options == 2:

		choice = (input("How many OZ did the recipe say?: \n"))

		if isinstance(float(choice), float) == True:
			ozToml(float(choice))
		else:
			print("not a number")
	else:
		print("please input something valid"
			)




_main_()