# Reformats the csv file so that no unintended spaces are there.
def clean_white_space(file_name):
	# read all contents of the file
	with open(file_name, "r") as csv_file:
		lines = csv_file.readlines()
	# delete whitespace
	lines = [line.replace(" ", "") for line in lines]
	# write edited content to file
	with open(file_name, "w") as csv_file:
		csv_file.writelines(lines)


if __name__ == "__main__":
	clean_white_space("./item.csv")