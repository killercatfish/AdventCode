import sys
import re
#to help sort dict
import operator

def build_list(filename):
	f = open(filename, 'rU')
	#list of the individual lines
	s = f.read().splitlines()

	return s
	
#gets the room name and checksum
def parse_words(filename):
	#split by number groups
	f = open(filename, 'rU')
	s = f.read()
	match = re.findall(r'[a-z-]+',s)
	
	if not match:
		print 'usage: [file must contain data]'
		sys.exit(1)

	
	#print match
	
	return match

#make a list of just the sector names, with no dashes
def get_sector(word_list):
	names = []
	
	#skip odds, since those are the check sums.
	for i in xrange(0,len(word_list),2):
		#remove the dashes from the current room name
		temp = re.sub('-','',word_list[i])
		names.append(temp)
		
	return names

#get the check sum for each room
def get_checksums(word_list):
	checksums = []
	
	#skip evens, since those are room names.
	for i in xrange(1,len(word_list),2):
		checksums.append(word_list[i])
		
		
	return checksums
	
#get the room key/number
def get_num(filename):
	#split by number groups
	f = open(filename, 'rU')
	s = f.read()
	match = re.findall(r'[0-9]+',s)
	
	if not match:
		print 'usage: [file must contain data]'
		sys.exit(1)

	
	#print match

	return match
	
	
def order_letters(names):
	#put a dict of each in the list
	ordered_letters = []
	
	#get each word
	for i in names:
		#print i
		#get each letter
		letters = {}
		for j in i:
			#print j
			if j in letters:
				letters[j] += 1
			else:
				letters[j] = 1
		#Sorts the list by alphabetical and key value and returns the list of keys and values
		sorted_x = [k for k, v in sorted(letters.iteritems(), key=lambda(k, v): (-v, k))]
		sorted_y = [v for k, v in sorted(letters.iteritems(), key=lambda(k, v): (-v, k))]
		#combine the two
		finished = zip(sorted_x,sorted_y)
		ordered_letters.append(finished)
	
	#print ordered_letters
	return ordered_letters
	
	
def remove_space(word_list):
	names = []
	
	#skip odds, since those are the check sums.
	for i in xrange(0,len(word_list),2):
		#remove the dashes from the current room name
		temp = re.sub('-',' ',word_list[i])
		names.append(temp)
		
	return names
	
	
def shift_names(real_rooms):
	'''
	print ord('a')
	print ord(' ')
	print ord('z')
	a = 'p'
	print ord(a)
	print chr(ord(a)+1)
	'''
	#print real_rooms
	#fill new_names with tuples containing shifted room names and keys
	new_names = []
	counter = 0
	for i in real_rooms:
		temp = ''
		shift = int(i[1]) % 26
		#print shift
		for j in range(len(i[0])):
			if ord(i[0][j]) == 32:
				temp += ' '
			else:
				c = chr(ord(i[0][j])+shift)
				if ord(c) > 122:
					c = chr(ord(c)-26)
				temp += c
		#print temp
		#print real_rooms[counter][0]
		new_names.append((temp,real_rooms[counter][1]))
		counter += 1		
		
	#print new_names
	return new_names
	
def sector_sums(filename):
	room_list = build_list(filename)
	#print room_list
	
	word_list = parse_words(filename)
	
	sector_names = get_sector(word_list)
	
	checksums = get_checksums(word_list)
	
	nums = get_num(filename)
	"""
	print 'word_list: '
	print word_list
	print ''
	
	print 'sector_names: '
	print sector_names
	print ''
	
	print 'checksums: '
	print checksums
	print ''
	
	print 'nums: '
	print nums
	print ''
	"""
	#make a list of dicts of the letters ordered by max to min
	ordered_letters = order_letters(sector_names)
	
	#replace dashes with spaces in word_list
	room_names = remove_space(word_list)
	
	#print ordered_letters
	real_rooms = []
	sum = 0
	for i in range(len(sector_names)):
		#print i
		#print ordered_letters[i]
		#print checksums[i]
		
		#print ordered_letters[i][0][0]
		#print checksums[i][0]
		
		if (		ordered_letters[i][0][0] == checksums[i][0]
				and	ordered_letters[i][1][0] == checksums[i][1]
				and ordered_letters[i][2][0] == checksums[i][2]
				and ordered_letters[i][3][0] == checksums[i][3]
				and ordered_letters[i][4][0] == checksums[i][4]
				):
			sum+=int(nums[i])
			#making a list of the room names and their checksums that are real rooms
			real_rooms.append((room_names[i],nums[i])) 
	print 'the sum is: ' + str(sum)
		
	#print real_rooms
	
	shifted_names = shift_names(real_rooms)
		#check individual checksums through loop
		#for j in range(len(checksums[i])):
			#print checksums[i][j]
			
	#print shifted_names
	
	#search for north...
	for i in shifted_names:
		if re.search(r'north',i[0]):
			print i
	
	
def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [filename to import]'
    sys.exit(1)
    
  sector_sums(args[0])

if __name__ == '__main__':
  main()