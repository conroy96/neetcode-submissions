class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [
            (1,0),
            (-1,0),
            (0,1),
            (0,-1),
        ]
        total =0
        seen= set()
        def dfs(row,col):
            if 0 > row or row >= len(grid):
                return
            
            if 0 > col or col >= len(grid[row]):
                return

            if grid[row][col] =="0":
                return
            if (row,col) in seen:
                return 
            seen.add((row,col))
            
            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change

                dfs(new_row,new_col)
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] =="1" and (row,col) not in seen:
                    total +=1
                    dfs(row,col)
        return total

            

            