import os
import sys
import subprocess

go = raw_input("Would you like to make a Shodan search? [y/n]: ") == 'y'
path = ""
keep_file_path = False

while go:
	term = raw_input("Please input your search term: ")
	number = raw_input("Please input the number of search results you want downloaded: ")
	
	if not keep_file_path:
		print("Please enter the full path of where you want to save the files. ")
		path = raw_input("Example - \"/root/Desktop/jsonFiles/\": ")
	
	if os.path.isfile(path + 'shodan_search_index_file.txt'):
		index_file = open(path + 'shodan_search_index_file.txt', 'r')
		index = index_file.read()
		index_file.close()
		index_file = open(path + 'shodan_search_index_file.txt', 'w')
		index_file.write(str(int(index) + 1))
		index_file.close()
	else:
		index_file = open(path + 'shodan_search_index_file.txt', 'w')
		index_file.write('2')
		index_file.close()
		index = 1
	
	filename = 'search_' + str(index) + '_' + term + '[' + str(number) + ']'
	subprocess.Popen(['shodan', 'download', '--limit', str(number), path + filename, term])
	
	print("Successful Search | Saved Under: " + filename)
	
	final_question = "Would you like to:\n"
	final_question = final_question + "-1. Search with the Same File Path\n"
	final_question = final_question + "-2. Search with a Different File Path\n"
	final_question = final_question + "-3. Exit\n"
	final_response = raw_input(final_question)

	if final_response == '1':
		keep_file_path = True
	elif final_response == '2':
		keep_file_path = False
	elif final_response == '3':
		go = False

