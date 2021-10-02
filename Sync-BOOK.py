#Reading the BookMarks file
with open('/home/daniel/.config/BraveSoftware/Brave-Browser/Default/Bookmarks') as f:
	lines=f.readlines()
#tag children indcats start of folder

#adds line number tag children is found to list folder
i=0
folder=[]
while i < len(lines):
	if lines[i] == lines[5]:
		folder.append(i)
	i+=1

#print(folder)	
print(lines[folder[2]])
	
