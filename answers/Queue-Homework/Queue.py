class Queue:
    def __init__(self,MAX_CAPACITY):
        self.queue=[]
        self.MAX_CAPACITY=MAX_CAPACITY

    def size(self):
        return len(self.queue)

    def is_Empty(self):
        if len(self.queue) == 0:
            return True
        return False

    def enQueue(self,item):
        if self.size() < self.MAX_CAPACITY:
            self.queue.append(item)
        raise Exception("Queue is full.impossible to add a new element")

    def deQueue(self,item):
        if not self.is_Empty():
            return self.queue.pop(0)
        raise IndexError ("the Queue is empty")





class MazeSolver:
    def __init__(self,maze):
        self.maze=maze
        self.rows=len(maze)
        self.cols=len(maze[0])
        self.start=None
        self.end=None

        #finding the start and end point
        for i in range(self.rows):
            for j in range(self.cols):
                if maze[i][j]=='S':
                    self.start=(i,j)
                elif maze[i][j]=='E':
                    self.end=(i,j)

    def move_valiation(self,row,col):
        return 0 <= row < self.rows and 0 <= col < self.cols and self.maze[row][col] == '0'
    #self.maze[row][col] == '0': This part checks if the cell at the specified row and column in the maze grid contains
    # an open path (represented by '0').
    #0 <= row < self.rows and 0 <= col < self.cols : So, 0 <= row < self.rows ensures that row is greater than or equal
    # to 0 and less than self.rows, meaning it's within the bounds of the rows of the maze.
    #So, 0 <= col < self.cols ensures that col is greater than or equal to 0 and less than self.cols, meaning it's
    # within the bounds of the columns of the maze.

    def find_shortest_path(self):
        # directions: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Initialize queue for BFS
        queue = Queue()
        queue.enqueue((self.start, 0))  # Add starting point and distance to queue
        visited = set()

        # Performing BFS starts
        while not queue.is_empty():
            (row, col), distance = queue.dequeue()

            # Check if reached the end
            if (row, col) == self.end:
                return distance

            # Explore neighboring cells
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc

                # Check if the move is valid and not visited
                if self.is_valid_move(new_row, new_col) and (new_row, new_col) not in visited:
                    queue.enqueue(((new_row, new_col), distance + 1))
                    visited.add((new_row, new_col))

        # If no path found
        return -1


