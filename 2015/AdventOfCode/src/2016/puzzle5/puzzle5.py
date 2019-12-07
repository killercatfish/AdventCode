import sys
import re
#MD5
import hashlib


def computeMD5hash(string):
	m = hashlib.md5(string.encode())
	#print m.hexdigest()
	return m.hexdigest()
  
#part 1
def calc_combo(string):
	counter = 0
	password = ''
	
	while len(password) < 8:
		temp = string + str(counter)
		#print temp
		h = computeMD5hash(temp)
		#print str(h[:5])
		if str(h[:5]) == '00000':
			found = string + str(counter)
			print h
			print found
			password += h[5]
		counter += 1
	print password
  
  
#part 2  
def calc_real_combo(string):
	counter = 0
	#keep a dictionary of the inputs locations
	password = {}
	pw_length = 0
	while pw_length < 8:
		temp = string + str(counter)
		#print temp
		h = computeMD5hash(temp)
		#print str(h[:5])
		if str(h[:5]) == '00000':
			found = string + str(counter)
			print h
			print found
			print h[5]
			print h[6]
			#if the 6th digit of hex is a digit, check if its less than 8
			#since we have 8 digits for our password
			if h[5].isdigit() and int(h[5]) < 8:
				
				#if h[5] isnt already in the password list, go and add h[6]
				if int(h[5]) not in password:
					password[int(h[5])] = h[6]
					pw_length += 1
					print password
		counter += 1
	s = sorted(password)
	print 'found password: '
	print password
	print ''
	print 'sorted: '
	print s
	
	
  
def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [filename to import]'
    sys.exit(1)
    
  calc_real_combo(args[0])

if __name__ == '__main__':
  main()