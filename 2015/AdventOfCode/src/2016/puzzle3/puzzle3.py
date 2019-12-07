import sys
import re

def build_list(filename):
	f = open(filename, 'rU')
	#list of the individual lines
	s = f.read()
	#split by number groups
	match = re.findall(r'(\d+)',s)
	
	if not match:
		print 'usage: [file must contain data]'
		sys.exit(1)

	return match
	
def find_triangles(filename):
	triangle_list = build_list(filename)

	triangles_found = []
	
	#from 0 to length count by 3
	for i in xrange(0,len(triangle_list),3):
			a = int(triangle_list[i])
			b = int(triangle_list[i + 1])
			c = int(triangle_list[i + 2])
			print a
			print b
			print c
			if int(a) + int(b) > int(c) and int(a) + int(c) > int(b) and int(c) + int(b) > int(a) and int(a) + int(c) > int(b):
				triangles_found.append((a,b,c))
				
	print triangles_found
	print 'Found ' + str(len(triangles_found)) + ' triangles'
	
def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [filename to import]'
    sys.exit(1)
    
  find_triangles(args[0])

if __name__ == '__main__':
  main()