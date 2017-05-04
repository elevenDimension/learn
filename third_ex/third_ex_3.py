# Constructor
def tree(label, branches=[]):
 return [label] + list(branches)
# Selectors
def label(tree):
 return tree[0]
def branches(tree):
 return tree[1:]
def is_leaf(t):
	return len(t)==1

def square_tree(t):
	num=int(t[0]) #初始化num，确保参数为数字
	if(is_leaf(t)):
		return tree(num*num); #节点为叶子时，直接返回节点值的平方
	else:
		tmp=[]
		for k in range(1,len(t)):			#遍历子节点
			tmp = tmp+[square_tree(t[k])]	#组合子节点
		return tree(num*num,tmp);			#第一个参数代表节点，第二个参数代表子节点列表

def height(t):
	if(is_leaf(t)):
		return 1; 	#为叶子时高度为1
	else:
		num = 0;
		for k in range(1,len(t)):		#遍历子节点
			numOne = height(t[k])		#获取子节点高度
			num = (numOne, num)[numOne<=num]  #对比两个子节点高度，取高度值较大的（numOne<=num为true时返回num）
		return 1+num;					#返回高度为1+子节点最大高度

def tree_max(t):
	num=int(t[0])			#初始化num，确保参数为数字
	if(is_leaf(t)):
		return num;			#节点为叶子时，直接返回当前节点值	
	else:
		for k in range(1,len(t)):
			numOne = tree_max(t[k])				#获取子节点的最大值
			num = (numOne, num)[numOne<=num]	#对比子节点的值，取较大者（numOne<=num为true时返回num）
		return num;								#返回最大的子节点值

#请使用t作为示例，因为square_tree和tree_max函数的前提是节点值均为数字，如果为字符串将报错
t = tree('1',
		[
			tree('2',
				[
					tree('32'), 
					tree('41')
				]
			),
 			tree('5'),
 			tree('6',
	 			[
	 				tree('7'), 
	 				tree('8')
				])
		]
	)
t2 = tree('subjects',
		[
			tree('sciences',
				[
					tree('biology'), tree('chemistry')
				]
			),
 			tree('philosophy'),
 			tree('languages',
 			[
 				tree('Chineses'), 
 				tree('English')
			])
		]
	)
print(t)
print(tree_max(t))