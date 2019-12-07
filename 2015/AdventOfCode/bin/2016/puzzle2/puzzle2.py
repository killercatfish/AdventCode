import sys

def build_list(filename):
	f = open(filename, 'rU')
	#list of the individual lines
	s = f.read().splitlines()
	print s
	return s
	
def find_code(filename):
	code_list = build_list(filename)
	
	key = 5
	combo = []
	
	#access each individual keypress
	for i in code_list:
		for j in range(len(i)):
			direction = i[j]
			print direction
			
			if direction == 'U':
				if key != 1 and key != 2 and key != 3:
					key -= 3
			elif direction == 'D':
				if key != 7 and key != 8 and key != 9:
					key += 3
			elif direction == 'L':
				if key != 1 and key != 4 and key != 7:
					key -= 1
			else:
				if key != 3 and key != 6 and key != 9:
					key += 1
			print key
		combo.append(key)
	print combo
	
def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [filename to import]'
    sys.exit(1)
    
  find_code(args[0])

if __name__ == '__main__':
  main()