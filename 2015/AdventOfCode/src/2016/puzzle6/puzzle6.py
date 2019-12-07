import sys
import re

def build_list(filename):
	f = open(filename, 'rU')
	#list of the individual lines
	s = f.read().splitlines()

	return s
	
def find_message(filename):
	message_lines = build_list(filename)
	
	letter_list = parse_letters(message_lines)
	
	print_list(letter_list)
	
	ordered_letters = get_max(letter_list)
	
	#find_message_big(ordered_letters)
	
	find_message_small(ordered_letters)
	
def parse_letters(message_lines):
	letter_list = []
	for i in message_lines:
		word = []
		for j in i:
			word.append(j)
		letter_list.append(word)
	
	return letter_list

def find_message_big(letter_list):
	for i in letter_list:
		print i[0][0]
		
def find_message_small(letter_list):
	for i in letter_list:
		print i[-1][0]


#find the letters with dictionary
def get_max(message_lines):
	#put a dict of each in the list
	ordered_letters = []
	
	#iterate through length of one input line
	for i in range(len(message_lines[0])):
		#print i
		
		#get each letter
		letters = {}
		#iterate through length of total inputs
		for j in range(len(message_lines)):
			#print j
			#going down through columns
			if message_lines[j][i] in letters:
				letters[message_lines[j][i]] += 1
			else:
				letters[message_lines[j][i]] = 1
		#Sorts the list by alphabetical and key value and returns the list of keys and values
		sorted_x = [k for k, v in sorted(letters.iteritems(), key=lambda(k, v): (-v, k))]
		sorted_y = [v for k, v in sorted(letters.iteritems(), key=lambda(k, v): (-v, k))]
		#combine the two
		finished = zip(sorted_x,sorted_y)
		ordered_letters.append(finished)
	
	#print_list(ordered_letters)
	return ordered_letters
		
	
		
def print_list(to_print):
	for i in to_print:
		print i
	
	
	
  
def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [filename to import]'
    sys.exit(1)
    
  find_message(args[0])

if __name__ == '__main__':
  main()