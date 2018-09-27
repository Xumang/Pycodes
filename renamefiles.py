import os
# import numpy as np

# # File location
# direc = ("/Users/sumanghimire/Downloads/Cali Trip")

# # Sequence number initialization
# count = 1 

# # read file one by one
# for img in os.listdir(direc):
# 	f1 = cv2.imread("/Users/sumanghimire/Downloads/test" + img) #read images
# 	cv2.imwrite("/Users/sumanghimire/Downloads/resu" + "%d.jpg" % count , f1) #write images to folder
# 	count = count +1


def rename_files():
	file_list = os.listdir("/Users/sumanghimire/Downloads/test")
	print(file_list)
	# saved_path = os.getcwd()
	# print("Current wirking directory is " + saved_path)
	# os.chdir("Users/sumanghimire/Downloads/resu") 

	for file_name in file_list:
		os.rename(file_name, file_name.lstrip())
	os.chdir(saved_path)



rename_files()

# str = "     this is string example....wow!!!     ";
# print str.lstrip()
# str = "88888888this is string example....wow!!!8888888";
# print str.lstrip('8')