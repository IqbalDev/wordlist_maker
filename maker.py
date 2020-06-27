# -*- coding UTF-8 -*-
# Author     : Iqbal Dev
# Name Tools : Wordlist Maker

import os
import sys

count = 1
i = 1


def gawe():
	global count, i
	try:
		os.system('cls' if os.name == 'nt' else 'clear')
		print '''
      Coded By Iqbal ID
  =========================
  { 1 } Tambah Data
  { 2 } Data Baru
  =========================
     	'''
		pil = raw_input(" Pilih Opsi : ")
		print ""
		if pil == '1':
			def tambah():
				i = 1
				while True:
					data = raw_input(" " + str(i) + " [OP. 1] Input Kata : ")
					if data == '' or data == ' ':
						break
					data_masuk = open('word.txt', 'a').write(data + '\n')
					i += 1
				tambah()
			tambah()

		elif pil == '2': 
			os.remove('word.txt')
			def baru():
				i = 1
				while True:
					data = raw_input(" " + str(i) + " [OP. 2] Input Kata : ")
					if data == '' or data == ' ':
						break
					data_masuk = open('word.txt', 'a').write(data + '\n')
					i +=1
				baru()
			baru()
		else:
			gawe()
		print " Selesai...."

	except KeyboardInterrupt:
		print "\n"
		with open('word.txt', 'r') as dev:	
			for no in dev:
				no1 = no.replace('\n', '')
				print " " + str(count) + " " + no1
				count += 1
				time.sleep(0.1)
		jml = open('word.txt', 'r').readlines()
		jmk = open('word.txt', 'r').read()
		jm = jmk.replace(' ', '').replace('\n', '').replace('  ', '')

		print "\n Jumlah kata : " + str(len(jml)) + '\n'
		print " Jumlah Huruf : " + str(len(jm)) + '\n'
		print " Data Tersimpan Di File (word.txt)" + '\n'
		sys.exit()

	except IOError:
		pass

def main():
	gawe()

if __name__=="__main__":
	main()
