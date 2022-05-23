import os 

currentDir = os.getcwd()
files = os.listdir(currentDir)

#txt file collection
filelist = {}

#find txt file 
for root, dirs, files in os.walk(currentDir):
	for file in files: 
		if(file.endswith( ".txt" ) and file != "result.txt"):
			filelist[file] = os.path.join(root,file)

#sort keys
sortedFileList = sorted(filelist.keys())