import os 

products = []
#用if 比對檔案是否存在, with讀取檔案
if os.path.isfile('products.csv'):
	print('find it')
	with open('products.csv', 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue
			name, price=line.strip().split(',')
			products.append([name, price])
	print(products)		
else:
	print('file not')





#使用者輸入資料
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入價格:')
	price = int(price)
	products.append([name, price])
print(products)

#印出所有購買記錄
for p in products:
	print(p[0], '的價格是', p[1])

#寫入檔案
with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ','+ str(p[1]) + '\n')
