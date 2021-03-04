#  David Ström, Lund, 2021-03-04

from gridbot import checkArgs, walk

def testGridSize():
	assert checkArgs(['0', '1', '0', '0', 'N', 'R']) == False, "Should be False"
	assert checkArgs(['2', '-3', '0', '0', 'N', 'R']) == False, "Should be False"
	assert checkArgs(['1', '1', '0', '0', 'N', 'R']) == True, "Should be True"
	assert checkArgs(['2', '3', '0', '0', 'N', 'R']) == True, "Should be True"
	assert checkArgs(['f', '3', '0', '0', 'N', 'R']) == False, "Should be False"
	assert checkArgs(['3', '3', '0', '.', 'N', 'R']) == False, "Should be False"

def testGridPosition():
	assert checkArgs(['1', '1', '0', '-1', 'N', 'R']) == False, "Should be False"
	assert checkArgs(['1', '1', '0', '0', 'N', 'R']) == True, "Should be True"
	assert checkArgs(['4', '4', '0', '4', 'N', 'R']) == False, "Should be False"
	assert checkArgs(['4', '4', '3', '0', 'N', 'R']) == True, "Should be True"

def testDirection():
	assert checkArgs(['3', '3', '0', '0', 'N', 'R']) == True, "Should be True"
	assert checkArgs(['3', '3', '0', '0', 'f', 'R']) == False, "Should be False"

def testMovementString():
	assert checkArgs(['3', '3', '0', '0', 'N', 'RLLFLRF']) == True, "Should be True"
	assert checkArgs(['3', '3', '0', '0', 'N', 'RLFDRF']) == False, "Should be False"

def testMovementExamples():
	assert walk([4, 4], [1, 2], 0, ['R','F','R','F','F','R','F','R','F']) == ([1, 3], 'N'), "Should be [1, 3] N"
	assert walk([4, 4], [0, 0], 1, ['R','F','L','F','F','L','R','F']) == ([3, 1], 'E'), "Should be [3, 1] E"

def testMovementBoundaries():
	assert walk([6, 3], [0, 0], 0, ['F']) == ([0, 0], 'N'), "Should be [0, 0] N"
	assert walk([6, 3], [0, 0], 1, ['F']*7) == ([6, 0], 'E'), "Should be [6, 0] E"
	assert walk([6, 3], [0, 0], 2, ['F']*4) == ([0, 3], 'S'), "Should be [0, 3] S"
	assert walk([6, 3], [0, 0], 3, ['F']) == ([0, 0], 'W'), "Should be [0, 0] W"

def testMovementCircular():
	assert walk([8, 8], [5, 5], 0, ['F', 'R']*8) == ([5, 5], 'N'), "Should be [5, 5] N"
	assert walk([8, 8], [5, 5], 0, ['F', 'F', 'L']*8) == ([5, 5], 'N'), "Should be [5, 5] N"

def main():
	testGridSize()
	print('ALL GRID SIZE TESTS PASSED')
	testGridPosition()
	print('ALL GRID POSITION TESTS PASSED')
	testDirection()
	print('ALL STARTING DIRECTION TESTS PASSED')
	testMovementString()
	print('ALL MOVEMENT STRING TESTS PASSED')
	testMovementExamples()
	print('ALL MOVEMENT EXAMPLE TESTS PASSED')
	testMovementBoundaries()
	print('ALL MOVEMENT BOUNDARY TESTS PASSED')
	testMovementCircular()
	print('ALL CIRCULAR MOVEMENT TESTS PASSED')

	print('--------------------------------------\nALL TESTS PASSED')

if __name__ == "__main__":
    main()