#  David Ström, Lund, 2021-03-04

#  Welcomes the user and prompts for one input argument at
#  a time. Collects all arguments into an argument list and
#  returns the list.
def getArgs():
	# Get all user input
	print("Welcome to GridBot!\n--------------------")
	width = input("Enter the width of the grid: ")
	depth = input("Enter the depth of the grid: ")
	x_start = input("Enter the robot's initial x-coordinate: ")
	y_start = input("Enter the robot's initial y-coordinate: ")
	start_dir = input("Enter which direction the robot is facing (N, E, S, or W): ")
	movement_cmd = input("Enter the sequence of movement commands (L, R, or F)(Example: LLFRFL): ")
	print("--------------------")

	# Put user input in argument list
	args = [width, depth, x_start, y_start, start_dir, movement_cmd]
	return args


# Checks whether the given user inputs are according to
# the requirements for the program.
def checkArgs(args):
	# Allowed movement commands and starting directions
	allowed_cmds = set('LRF')
	allowed_dirs = ['N', 'E', 'S', 'W']

	# Check validity of grid size, starting position, starting direction, and movement commands
	if not args[0].isnumeric() or not args[1].isnumeric() or not args[2].isnumeric() or not args[3].isnumeric():
		print("Grid size and coordinates should be numerical")
		return False
	elif int(args[0]) < 1 or int(args[1]) < 1:
		print("The grid has to be at least 1x1")
		return False
	elif int(args[2]) < 0 or int(args[3]) < 0:
		print("You have to start on the grid")
		return False
	elif int(args[2]) >= int(args[0]) or int(args[3]) >= int(args[1]):
		print("You have to start on the grid")
		return False
	elif args[4] not in allowed_dirs:
		print("Only direction inputs N, E, S, or W allowed")
		return False
	elif not set(args[5]).issubset(allowed_cmds):
		print("Only the movement commands L, R, and F are allowed")
		return False
	else:
		return True

#  Takes the given arguments as input and returns an
#  index for the direction, the grid's dimensions, the
#  starting position coordinates, and the movement 
#  commands as separate chars in a list.
def parseArgs(args):
	# Parse grid size and starting position
	grid_max = [int(args[0])-1, int(args[1])-1]
	grid_position = [int(args[2]), int(args[3])]

	# Parse starting direction
	if args[4] == 'N': direction_id = 0
	elif args[4] == 'E': direction_id = 1
	elif args[4] == 'S': direction_id = 2
	elif args[4] == 'W': direction_id = 3

	# Parse movement string into separate commands
	input_list = list(args[5])

	return grid_max, grid_position, direction_id, input_list

#  Executes the movement commands given by the user and
#  returns the final positional coordinates and direction.
def walk(grid_max, grid_position, direction_id, input_list):
	direction_list = ['N', 'E', 'S', 'W']

	for input in input_list:
		# Check the directional input
		if input == 'R': direction_id += 1
		elif input == 'L': direction_id -= 1

		# Check that it is heading in the correct direction
		if direction_id == 4: direction_id = 0
		elif direction_id == -1: direction_id = 3

		# Check forward input
		if input == 'F': 
			# Move one step north unless at northern border
			if direction_id == 0 and grid_position[1] > 0:
				grid_position[1] -= 1
			# Move one step east unless at eastern border
			elif direction_id == 1 and grid_position[0] < grid_max[0]:
				grid_position[0] += 1
			# Move one step south unless at southern border
			elif direction_id == 2 and grid_position[1] < grid_max[1]:
				grid_position[1] += 1
			# Move one step west unless at western border
			elif direction_id == 3 and grid_position[0] > 0:
				grid_position[0] -= 1

	return grid_position, direction_list[direction_id]

def main():
	args = getArgs()
	# Check if input arguments are correct
	if checkArgs(args):
		print("Grid size:", args[0], "x", args[1], 
			"\nStarting position:", args[2], ",", args[3],
			"\nStarting direction:", args[4], 
			"\nMovement commands:", args[5])
		
		# Parse all arguments
		grid_max, grid_position, direction_id, input_list = parseArgs(args)
	
		# Get final position and direction after executing movement commands
		final_position, final_direction = walk(grid_max, grid_position, direction_id, input_list)
		print("---\nEnd position:", final_position[0], ",", final_position[1],
			"\nEnd direction:", final_direction)

	else:
		print("Invalid input!")

if __name__ == "__main__":
    main()



