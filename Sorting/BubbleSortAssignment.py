# Andrew Donnell - bubble sort assignment

def bubbleSort(alist):
	passnum = len(alist)-1 
	swap = True
	while passnum > 0 and swap:
		swap = False
		for i in range(passnum):
			if alist[i]>alist[i+1]:
				swap = True
				temp = alist[i]
				alist[i] = alist[i+1]
				alist[i+1] = temp
		passnum -= 1

alist = [54,26,93,17,77,31,44,55,20]
print "\n", alist, "\n\nBubble Sort:"
bubbleSort(alist)
print(alist)