def kmp(haystack,needle):
	if needle=="":
		return 0
	n=len(haystack)
	m=len(needle)
	lps=[0]*m

	prevLPS,i=0,1

	while i<m:
		if needle[i]==needle[prevLPS]:
			lps[i]=lps[prevLPS]+1
			i+=1
			prevLPS+=1

		elif prevLPS==0:
			lps[i]=0
			i+=1
		else:
			prevLPS=lps[prevLPS-1]


	i,j=0,0

	while i<n:
		if haystack[i]==needle[j]:
			i+=1
			j+=1

		elif j==0:
			i+=1

		else:
			j=lps[j-1]

		if j==m:
			return j


	return -1