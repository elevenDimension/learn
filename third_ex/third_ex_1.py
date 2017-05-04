def keep_odds(f,num):
	for k in range(0,num):
		f(k)

def printNum(num):
	if num%2!=0:
		print(num)

num = input("please input number:")
keep_odds(printNum,int(num))