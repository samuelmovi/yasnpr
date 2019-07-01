# 							Yet Another	SecurityNow! Podcast Retriever
# Retrieves copies of podcasts (hi- and lo-def), of the show notes, and the transcripts
#
# Python3

# Naming conventions:
# mp3 file: https://media.grc.com/sn/sn-001.mp3
# lo-fi mp3: https://media.grc.com/sn/sn-001-lq.mp3
# show notes: https://www.grc.com/sn/notes-001.htm  until 177, then https://www.grc.com/sn/sn-432-notes.pdf
# transcripts: https://www.grc.com/sn/sn-001.txt


import os
import requests


# downloader functions
def download_mp3(number, path):
	done = False
	try:
		digits = len(str(number))
		if digits == 1:
			url = 'https://media.grc.com/sn/sn-00' + str(number) + '.mp3'
			filename = 'sn-00' + str(number) + '.mp3'
		elif digits == 2:
			url = 'https://media.grc.com/sn/sn-0' + str(number) + '.mp3'
			filename = 'sn-0' + str(number) + '.mp3'
		elif digits == 3:
			url = 'https://media.grc.com/sn/sn-' + str(number) + '.mp3'
			filename = 'sn-' + str(number) + '.mp3'
		else:
			print('\n[!] Error: Podcast Number Out of Range\n')
			return done

		saveto = path + '/' + filename
		if os.path.exists(saveto):
			while not done:
				choice = str(input('[!] File already exists\n[?] Overwrite (y/n): '))
				if choice is 'y':
					r = requests.get(url, stream=True)
					if r.status_code is 200:
						with open(saveto, 'wb') as file:
							print('[#] Attempting MP3 download...')
							for chunk in r.iter_content(4096):
								file.write(chunk)
							print('\n[#] MP3 file {} succesfully downloaded :-)'.format(filename))
							done = True
					else:
						print("\n[!] Communication with server unsuccessful: Code {}\n".format(r.status_code))
				elif choice is 'n':
					print('[#] Skipping file download...')
					done = True
				else:
					print('[!] Wrong input, try again...')
		else:
			r = requests.get(url, stream=True)
			if r.status_code is 200:
				with open(saveto, 'wb') as file:
					print('[#] Attempting MP3 download...')
					for chunk in r.iter_content(4096):
						file.write(chunk)
					print('\n[#] MP3 file {} succesfully downloaded :-)'.format(filename))
					done = True
			else:
				print("\n[!] Communication with server unsuccessful: Code {}\n".format(r.status_code))
	except Exception as e:
		print("\n[!] Error downloading MP3: {}\n".format(e))

	return done


def download_loq(number, path):
	done = False
	try:
		# set url depending on the number's digit length
		digits = len(str(number))
		if digits == 1:
			url = 'https://media.grc.com/sn/sn-00' + str(number) + '-lq.mp3'
			filename = 'sn-00' + str(number) + '-lq.mp3'
		elif digits == 2:
			url = 'https://media.grc.com/sn/sn-0' + str(number) + '-lq.mp3'
			filename = 'sn-0' + str(number) + '-lq.mp3'
		elif digits == 3:
			url = 'https://media.grc.com/sn/sn-' + str(number) + '-lq.mp3'
			filename = 'sn-' + str(number) + '-lq.mp3'
		else:
			print('\n[!] Podcast Number Out of Range\n')
			return done

		saveto = path + '/' + filename
		if os.path.exists(saveto):
			while not done:
				choice = str(input('[!] File already exists\n[?] Overwrite (y/n): '))
				if choice is 'y':
					r = requests.get(url, stream=True)
					if r.status_code is 200:
						with open(saveto, 'wb') as file:
							print('[#] Attempting Lo-Q MP3 download...')
							for chunk in r.iter_content(4096):
								file.write(chunk)
							print('\n[#] Lo-Q MP3 file {} succesfully downloaded :-)'.format(filename))
							done = True
					else:
						print("\n[!] Communication with server unsuccessful: Code {}\n".format(r.status_code))
				elif choice is'n':
					print('[#] Skipping file download...')
					done = True
				else:
					print('[!] Wrong input, try again...')
		else:
			r = requests.get(url, stream=True)
			if r.status_code is 200:
				with open(saveto, 'wb') as file:
					print('[#] Attempting Lo-Q MP3 download...')
					for chunk in r.iter_content(4096):
						file.write(chunk)
					print('\n[#] Lo-Q MP3 file {} succesfully downloaded :-)'.format(filename))
					done = True
			else:
				print("\n[!] Communication with server unsuccessful: Code {}\n".format(r.status_code))
	except Exception as e:
		print("\n[!] Error downloading Lo-Q MP3: {}\n".format(e))
	return done


def download_notes(number, path):
	done = False

	try:
		digits = len(str(number))
		if digits == 1:
			url = 'https://www.grc.com/sn/notes-00' + str(number) + '.htm'
			filename = 'notes-00' + str(number) + '.htm'
		elif digits == 2:
			url = 'https://www.grc.com/sn/notes-0' + str(number) + '.htm'
			filename = 'notes-0' + str(number) + '.htm'
		elif digits == 3:
			if number < 432:
				url = 'https://www.grc.com/sn/notes-' + str(number) + '.htm'
				filename = 'notes-' + str(number) + '.htm'
			if number >= 432:
				url = 'https://www.grc.com/sn/sn-' + str(number) + '-notes.pdf'
				filename = 'sn-' + str(number) + '-notes.pdf'
		else:
			print('\n[!] Podcast Number Out of Range\n')
			return done
		saveto = path + '/' + filename
		if os.path.exists(saveto):
			while not done:
				choice = str(input('[!] File already exists\n[?] Overwrite (y/n): '))
				if choice is'y':
					r = requests.get(url, stream=True)
					if r.status_code is 200:
						with open(saveto, 'wb') as file:
							print('[#] Attempting Show-Notes download...')
							for chunk in r.iter_content(4096):
								file.write(chunk)
						print('\n[#] Show-Notes file {} succesfully downloaded :-)'.format(filename))
						done = True
					else:
						print("\n[!] Communication with server unsuccessful: Code {}\n".format(r.status_code))
				elif choice is'n':
					print('[#] Skipping file download...')
					done = True
				else:
					print('[!] Wrong input, try again...')
		else:
			r = requests.get(url, stream=True)
			if r.status_code is 200:
				with open(saveto, 'wb') as file:
					print('[#] Attempting Show-Notes download...')
					for chunk in r.iter_content(4096):
						file.write(chunk)
				print('\n[#] Show-Notes file {} succesfully downloaded :-)'.format(filename))
				done = True
			else:
				print("\n[!] Communication with server unsuccessful: Code {}\n".format(r.status_code))
	except Exception as e:
		print("\n[!] Error downloading show notes: {}\n".format(e))

	return done


def download_transcript(number, path):
	done = False
	try:
		digits = len(str(number))
		if digits == 1:
			url = 'https://www.grc.com/sn/sn-00' + str(number) + '.txt'
			filename = 'transcript-00' + str(number) + '.txt'
		elif digits == 2:
			url = 'https://www.grc.com/sn/sn-0' + str(number) + '.txt'
			filename = 'transcript-0' + str(number) + '.txt'
		elif digits == 3:
			url = 'https://www.grc.com/sn/sn-' + str(number) + '.txt'
			filename = 'transcript-' + str(number) + '.txt'
		else:
			print('\n    !!!!!     !!!!!\n[!] Podcast Number Out of Range\n       !!!!!!    !!!!!')
			return done
		saveto = path + '/' + filename
		if os.path.exists(saveto):
			while not done:
				choice = str(input('[!] File already exists\n[?] Overwrite (y/n): '))
				if choice is'y':
					r = requests.get(url, stream=True)
					if r.status_code is 200:
						with open(saveto, 'wb') as file:
							print('[#] Attempting transcript download...')
							for chunk in r.iter_content(4096):
								file.write(chunk)
						print('\n[#] Transcript file {} succesfully downloaded :-)'.format(filename))
						done = True
					else:
						print("\n[!] Communication with server unsuccessful: Code {}\n".format(r.status_code))
				elif choice is'n':
					print('[#] Skipping file download...')
					done = True
				else:
					print('[!] Wrong input, try again...')
		else:
			r = requests.get(url, stream=True)
			if r.status_code is 200:
				with open(saveto, 'wb') as file:
					print('[#] Attempting transcript download...')
					for chunk in r.iter_content(4096):
						file.write(chunk)
				print('\n[#] Transcript file {} succesfully downloaded :-)'.format(filename))
				done = True
			else:
				print("\n[!] Communication with server unsuccessful: Code {}\n".format(r.status_code))
	except Exception as e:
		print("\n[!] Error downloading transcript: {}".format(e))

	return done


def main():
	# print('\nCurrent process\'s groupID: %s' % str(os.getgid()))
	# print('Current process\'s userID: %s' % str(os.getuid()))
	# print('Current process\'s processID: %s' % str(os.getpid()))
	# print('Current process\'s Owner: %s' % str(os.getlogin()))

	print('\n\n\t\tWelcome to the SecurityNow Podcast Retriever!!! \n\n')

	done = False

	while not done:
		try:
			print('\n[#] Please select: \n\t[1] Full podcast copy\n\t[2] Single podcast copy\n\t[0] Exit')
			choice = int(input('\n[?]Your choice: '))

			path = str(os.getcwd()) + '/SN/'

			if os.path.exists(path) is False:
				os.makedirs(path)

			if choice is 1:
				last = input('\n[#] Please input number of last published podcast: ')
				print('\nDownloading podcasts (+ content) to: {}'.format(path))
				count = 0
				while count < last:

					count += 1
					path = str(os.getcwd()) + '/SN/' + count
					os.makedirs(path)

					download_mp3(count, path)
					download_loq(count, path)
					download_notes(count, path)
					download_transcript(count, path)
					print('\n[#] Podcast #{} succesfully downloaded!'.format(count))
			elif choice is 2:
				podcast = input('\n[#] Please introduce number of podcast to download: ')
				try:
					podcast = int(podcast)
					path = str(os.getcwd()) + '/SN/' + str(podcast)
					os.makedirs(path)
					print('\n[#] Downloading podcast + content to: {}'.format(path))

					download_mp3(podcast, path)
					download_loq(podcast, path)
					download_notes(podcast, path)
					download_transcript(podcast, path)

					print('\n[#] Podcast succesfully downloaded!!')
				except Exception as e:
					print("[!!] You messed up with your input: ".format(e))
			elif choice is 0:
				done = True
				break
			else:
				print('\n[!!!] Wrong Choice!')
		except Exception as e:
			print("\n[!!!] Error processing your request: ".format(e))
			exit()
	print("[#] Exiting program now...")


if __name__ == '__main__':
	main()
