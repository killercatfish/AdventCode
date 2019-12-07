#Advent of Code Day 1 2016

import sys
import re

def get_location(args):
	
	directions = parse_dir(args)
	#facing stores the direction you are facing: N,S,E,W
	#position keeps your coordinate (x,y)
	#here we get the initial move to set the variables.
	facing = directions[0][0]
	
	visited = []
	
	if facing == 'R':
		facing = 'E'
		for i in range(int(directions[0][1])):
				visited.append((int(i),int(0)))
		position_x = directions[0][1]
		position_y = 0
	else:
		facing = 'N'
		for i in range(int(directions[0][1])):
				visited.append((int(0),int(i)))
		position_x = 0
		position_y = directions[0][1]
		
	#visited.append([(int(position_x),int(position_y))])	
	
	#print visited
	
	#print directions[0], len(directions[0])
	
	#print facing
	#print '(' + str(position_x) + ',' + str(position_y) + ')'
	directions = directions[1:]
	#print directions
	
	#print 'facing ' + facing + ' at position (' + str(position_x) + ',' + str(position_y) + ')'
	
	found_hq = []
	
	
	
	#print visited
	
	for d in directions:
		
		#Facing north...
		if facing == 'N':
			if d[0] == 'R':
				facing = 'E'
				temp = update_visited(position_x,position_y,'add',d[1],0)
				intersection = check_visited_again(visited,temp)
				if len(intersection) != 0:
					print intersection
					found_hq.extend(list(intersection)[0:])
				visited.extend(temp)
				position_x = int(position_x) + int(d[1])
			else:
				facing = 'W'
				temp = update_visited(position_x,position_y,'sub',d[1],0)
				intersection = check_visited_again(visited,temp)
				if len(intersection) != 0:
					print intersection
					found_hq.extend(list(intersection)[0:])
				visited.extend(temp)
				position_x = int(position_x) - int(d[1])
		#Facing south
		elif facing == 'S':
			if d[0] == 'R':
				facing = 'W'
				temp = update_visited(position_x,position_y,'sub',d[1],0)
				intersection = check_visited_again(visited,temp)
				if len(intersection) != 0:
					print intersection
					found_hq.extend(list(intersection)[0:])
				visited.extend(temp)
				position_x = int(position_x) - int(d[1])
			else:
				facing= 'E'
				temp = update_visited(position_x,position_y,'add',d[1],0)
				intersection = check_visited_again(visited,temp)
				if len(intersection) != 0:
					print intersection
					found_hq.extend(list(intersection)[0:])
				visited.extend(temp)
				position_x = int(position_x) + int(d[1])
		#Facing east
		elif facing == 'E':
			if d[0] == 'R':
				facing = 'S'
				temp = update_visited(position_x,position_y,'sub',0,d[1])
				intersection = check_visited_again(visited,temp)
				if len(intersection) != 0:
					print intersection
					found_hq.extend(list(intersection)[0:])
				visited.extend(temp)
				position_y = int(position_y) - int(d[1])
			else:
				facing = 'N'
				temp = update_visited(position_x,position_y,'add',0,d[1])
				intersection = check_visited_again(visited,temp)
				if len(intersection) != 0:
					print intersection
					found_hq.extend(list(intersection)[0:])
				visited.extend(temp)
				position_y = int(position_y) + int(d[1])
		#Facing west
		else:
			if d[0] == 'R':
				facing = 'N'
				temp = update_visited(position_x,position_y,'add',0,d[1])
				intersection = check_visited_again(visited,temp)
				if len(intersection) != 0:
					print intersection
					found_hq.extend(list(intersection)[0:])
				visited.extend(temp)
				position_y = int(position_y) + int(d[1])
			else:
				facing = 'S'
				temp = update_visited(position_x,position_y,'sub',0,d[1])
				intersection = check_visited_again(visited,temp)
				if len(intersection) != 0:
					print intersection
					found_hq.extend(list(intersection)[0:])
				visited.extend(temp)
				position_y = int(position_y) - int(d[1])
		#print 'facing ' + facing + ' at position (' + str(position_x) + ',' + str(position_y) + ')'
		
			
			
		
		#visited.append((int(position_x),int(position_y)))
	print found_hq
	how_far(found_hq[0][0],found_hq[0][1])
	#print visited
	#print facing
	#print '(' + str(position_x) + ',' + str(position_y) + ')'
	
	how_far(position_x,position_y)
	
	
def check_visited_again(old, new):
	#only true false!
	#print any(x in old for x in new)
	#Gives intersection of the two...
	return set(old).intersection(new)
	

def update_visited(x,y,add_sub,x_change,y_change):
	new_loc = []
	if x_change == 0 and str(add_sub) == 'add':
		for i in range(int(y_change)):
			new_loc.append((int(x),int(y)+i))
	elif x_change == 0 and str(add_sub) == 'sub':
		for i in range(int(y_change)):
			new_loc.append((int(x),int(y)-i))
	elif y_change == 0 and str(add_sub) == 'add':
		for i in range(int(x_change)):
			new_loc.append((int(x)+i,int(y)))	
	else:
		for i in range(int(x_change)):
			new_loc.append((int(x)-i,int(y)))
	return new_loc
	
def how_far(x,y):
	x_dist = abs(0 - int(x))
	y_dist = abs(0 - int(y))
	total_dist = x_dist + y_dist
	
	print 'You are ' + str(total_dist) + ' from the start'
	
def parse_dir(args):
	
	directions = []
	
	for i in args:
		temp = i[1:]
		#use regular expression to find all of the distance
		match = re.search(r'\d+',temp)
		#print match.group()
		directions.append((i[0],match.group()))

	#print directions
	
	return directions


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [List of directions]'
    sys.exit(1)

  get_location(args)
  
if __name__ == '__main__':
  main()
