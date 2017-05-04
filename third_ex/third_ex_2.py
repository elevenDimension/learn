def ab_plus_c(a,b,c):
	if b==0:
		return c
	else:
		return a+ab_plus_c(a,b-1,c)

a = input("please input a:")
b = input("please input b:")
c = input("please input c:")
result = ab_plus_c(int(a),int(b),int(c))
print(result)