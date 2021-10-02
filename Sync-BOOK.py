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

#Function outputs urls in a given range
def URL(ss,es):
	url=[]
	i=ss
	while i <= es:
		if lines[i] == lines[24]:
			url.append(lines[i+1])
		i+=1
	return url

#addes urls to bookurl
Bookurl=[]
j=0
while j < len(folder):
	Bookurl.append(URL(folder[j],markers[j]))
	j+=1

textfile=open('urls.txt','w')
for i in Bookurl:
	for j in i:
		textfile.write(j)
textfile.close()
