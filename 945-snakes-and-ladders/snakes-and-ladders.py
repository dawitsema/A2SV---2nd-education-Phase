class Solution:
	def snakesAndLadders(self, board: List[List[int]]) -> int:
		n=len(board)
		start, end =1,n*n
		visited=set()
		queue=deque()
		queue.append((start,0))
		
		def find_coordinates(current_position):
			row = n - 1 - (current_position - 1) // n
			col = (current_position - 1) % n
			if row % 2 == n % 2:
				return (row, n - 1 - col)
			else:
				return (row, col)

		while queue:
			curr_pos, steps=queue.popleft()
			if curr_pos == end:
				return steps

			for dice in range(1,7):
				if curr_pos + dice >end:
					break
				next_row, next_col = find_coordinates(curr_pos + dice)
				if (next_row, next_col) not in visited:
					visited.add((next_row, next_col))
					if board[next_row] [next_col]!=-1:
						queue.append((board[next_row][next_col],steps+1))
					else:
						queue.append((curr_pos + dice,steps+1))
		return -1