import os


#讀取檔案
def read_file(filename):
	chat = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:		
			chat.append(line.strip())	
	return chat


#轉換檔案加寫入檔案
def convert(chat):
	name = None
	Allen_work_count = 0
	Allen_sticker_count = 0
	Allen_picture_count = 0
	Viki_work_count = 0
	Viki_sticker_count = 0
	Viki_picture_count = 0
	for line in chat:
		s = line.split(' ')# 遇到空白鍵切一刀 split會變清單
		time = s[0]
		person = s[1]
		if person == 'Allen':
			if s[2] == '貼圖':
				Allen_sticker_count += 1
			elif s[2] == '圖片':
				Allen_picture_count += 1	
			for m in s[2:]:
				Allen_work_count += len(m)
		elif person == 'Viki':
			if s[2] == '貼圖':
				Viki_sticker_count += 1
			elif s[2] == '圖片':
				Viki_picture_count += 1
			for m in s[2:]:
				Viki_work_count += len(m)
	print('Allen說了', Allen_work_count, '個字')
	print('Allen傳了', Allen_sticker_count, '張貼圖')
	print('Allen傳了', Allen_picture_count, '張照片')		
	print('Viki說了', Viki_work_count, '個字')
	print('Viki傳了', Viki_sticker_count, '張貼圖')
	print('Viki傳了', Viki_picture_count, '張照片')
	with open('lineoutput.txt', 'w', encoding='utf-8') as f:
		f.write('Allen說了'+  str(Allen_work_count) + '個字' + '\n' +
				'Allen傳了'+ str(Allen_sticker_count) + '張貼圖' + '\n' +
				'Allen傳了' + str(Allen_picture_count) + '張照片' + '\n' +
				'Viki說了' + str(Viki_work_count) + '個字' + '\n' +
				'Viki傳了' + str(Viki_sticker_count) + '張貼圖' + '\n' +
				'Viki傳了' + str(Viki_picture_count) + '張照片' + '\n')			
	



def main():
	filename = '076 -LINE-Viki.txt'
	if os.path.isfile(filename):
		print('有找到檔案!!')
		chat = read_file(filename)
	else:
		print('沒有找到檔案.....')
	chat = convert(chat)				


main ()			