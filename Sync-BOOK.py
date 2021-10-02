#Reading the BookMarks file
with open('/home/daniel/.config/BraveSoftware/Brave-Browser/Default/Bookmarks') as f:
	lines=f.readlines()
#tag children indcats start of folder

#adds line number tag children is found to list folder and folder name
i=0
folder=[]
markers=[]
while i < len(lines):
	if lines[i] == lines[5]:
		folder.append(i)
	if lines[i] == lines[46]:
		markers.append(i)	
	i+=1
print(markers)
