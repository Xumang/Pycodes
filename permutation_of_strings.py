
def toString(list):
	return ''.join(list)


def permutation(a, f, l):   #a= string, f=start index of string, l=last index of string
	if f==l:
		print (toString(a))
	else :
		for i in range(f, l+1):
			a[f], a[i] = a[i], a[f]
			permutation (a,f+1,l)
			a[f],a[i] = a[i],a[f] #backtrack

string ="abcde"
n = len(string)
a = list(string)
permutation(a, 0, n-1) 


