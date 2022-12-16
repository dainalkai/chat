import os

#讀取檔案
def read_file(filename):
	chat = []
	name = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			if 'Allen' in line:
				name = line.strip()
				continue # 繼續
			elif 'Tom' in line:
				name = line.strip()
				continue	
			chat.append([name, line])	
	return chat

#寫入檔案
def write_file(outputfile, chat):
	with open(outputfile, 'w', encoding='utf-8') as f:
		for p in chat:
			f.write(p[0] + ': ' + p[1] )

def main():
	filename = '075 input.txt'
	outputfile = 'output.txt'
	if os.path.isfile(filename):
		print('有找到檔案!!')
		chat = read_file(filename)
	else:
		print('沒有找到檔案.....')				
	write_file(outputfile, chat)

main ()			


