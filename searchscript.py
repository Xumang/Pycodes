import os, glob

os.chdir("/Users/sumanghimire/Downloads/test")
for file in glob.glob("*.jpg"):
	print(file)

