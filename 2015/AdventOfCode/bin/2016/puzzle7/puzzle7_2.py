import sys
import re

def build_list(filename):
	f = open(filename, 'rU')
	#list of the individual lines
	s = f.read().splitlines()
	
	#print s
	
	return s
	
def check_tls(filename):
	message_lines = build_list(filename)

	inputs = split_inputs(message_lines)

	#print is_pal(inputs[2][0])
	true_list = find_pals(inputs)
	#print_list(true_list)
	
	#finds which are true and which are false, returns dict
	found = count_tls(true_list,inputs)
	#print_dict(found)
	#sys.exit(1)
	#counts how many are true
	print found
	count_true(found)
	
#makes a list of true false lists for parsed lines of input	
def find_pals(inputs):
	results = []
	for i in inputs:
		#print i
		result = []
		for j in i:
			#print j
			result.append(is_pal(j,i))
		results.append(result)
	#print_list(results)
	
	return results
			
#Make a dict of true or false tls
def count_tls(true_list,inputs):
	
	counted = {}
	#print_list(true_list)
	for i in range(len(true_list)):
		print true_list[i], inputs[i]
		counted[i] = False
		for j in range(len(true_list[i])):
			#print inputs[i], inputs[i][j], true_list[i]
			if j % 2 == 1 and true_list[i][j] == True:
				print inputs[i][j]
				if not has_rev(inputs[i],inputs[i][j]):
					print 'hello!'
					counted[i] = False
					break
			if j % 2 == 0 and true_list[i][j] == True:
				counted[i] = True
	print counted
	return counted

#count how many are true
def count_true(found):
	count = 0
	for value in found.itervalues():
		if value == True:
			count += 1
	print count
	
#returns true or false
#given a single string checks if it contains an ABBA
#sends all parts too
def is_pal(inputs,whole_list):
	#scan 3 letter groups since if ABA 
	for j in xrange(0,len(inputs)-2,1):
		forward = inputs[j:j+3]
		backward = forward[::-1]
		#print forward
		#print backward
		if forward == backward and forward[0] != forward[1]:
			if has_rev(whole_list,forward):
				return True
		#print '---'
	return False
		
def has_rev(whole_list,forward):
	s = forward[1] + forward[0] + forward[1]
	#print 's: ' + s
	for i in whole_list:
		#print 'i: ' + i
		for j in xrange(0,len(i)-2,1):
			#print 'i[j:j+3] ' + str(i[j:j+3])
			if s == i[j:j+3]:
				return True
	return False
		
#splits the input into groups deliminated by [ and ]
#odd positions represent good ABBA and even bad ABBA
def split_inputs(message_lines):
	parsed_message = []
	for i in message_lines:
		#print i
		match = re.findall(r'(\w+)+',i)
		if not match:
			print 'usage: [file must contain data]'
			sys.exit(1)	
		#print_list(match)
		#print '--------'
		parsed_message.append(match)
		
	return parsed_message		
		
def print_list(to_print):
	for i in to_print:
		print i
	
def print_dict(d):
	for k in d:
		print k, d[k]
	
def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [filename to import]'
    sys.exit(1)
    
  check_tls(args[0])

if __name__ == '__main__':
  main()