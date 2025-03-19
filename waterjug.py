def dfs(x, y, action, target, visited, path):
	if (x, y) in visited:
		return False

	if x==target or y==target:
		return True

	visited.add((x, y))
	path.append((x, y))

	if dfs(5, y, 'Fill Jug1', target, visited, path):
		return True

	if dfs(x, 3, 'Fill Jug2', target, visited, path):
		return True

	move = min(x, 3-y)
	if dfs(x-move, y+move, 'Pour from Jug1 to Jug2', target, visited, path):
		return True

	move = min(y, 5-x)
	if dfs(x+move, y-move, 'Pour from Jug2 to Jug1', target, visited, path):
		return True

	if dfs(0, y, 'Empty Jug1', target, visited, path):
		return True

	if dfs(x, 0, 'Empty Jug2', target, visited, path):
		return True

	path.pop()
	return False

def solve(target):
	visited = set()
	path = []
	action = 'Starting state'
	if dfs(0, 0, action, target, visited, path):
		print("Solution path:")
		for a, b, act in path:
			print("Jug1:", a, "Jug2:", b, "->", act)
	else:
		print("No solution found!")

solve(4)
