class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        #https://leetcode.com/problems/sudoku-solver/discuss/1417073/97-faster-oror-Clean-and-Concise-oror-Well-Explained
        '''
        The simple idea here is to fill a position and take the updated board as the new board and check if this new board has a possible solution.
If there is no valid solution for our new board we revert back to our previous state of the board and try by filling the next possible solution.

Checking if a value is valid in the respective empty slot:
Before intialising a value to our empty spot we need to check if that value is valid at that spot. For that we should check three cases:

If value is already present in the row
If value is already presnt in the column
If value is already presnt in the smaller(3*3)box .(This is a bit tricky)
        '''
        # some constant variables
        BOARD_SIZE = 9
        EMPTY_CELL = "."
        CELL_VALUES = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        
        rowRecords, colRecords = defaultdict(set), defaultdict(set)
        blockRecords = defaultdict(set)
        
        # use a deque to store the empty cells for dfs 
        emptyCells = collections.deque([])
        
        # populate all the initialized data structures
        # this iteration takes O(1)
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                # if . add it to emptyCells
                if board[i][j] == EMPTY_CELL:
                    emptyCells.append([i, j])
                    continue
                
                #
                rowRecords[i].add(board[i][j])
                colRecords[j].add(board[i][j])
                blockRecords[(i // 3, j // 3)].add(board[i][j])
        
        # define the dfs function
        def isValid(cval, ridx, cidx, block):
            if cval in rowRecords[ridx]:
                return False
            if cval in colRecords[cidx]:
                return False
            if cval in blockRecords[block]:
                return False
            return True
        
        def dfs():
            #base
            if not emptyCells:
                return True
            
            ridx, cidx = emptyCells[0]
            block = (ridx//3, cidx//3)
            
            for n in CELL_VALUES:
                # check if the current value is a valid input
                if isValid(n, ridx, cidx, block):
                    board[ridx][cidx] = n
                    # update records
                    rowRecords[ridx].add(n)
                    colRecords[cidx].add(n)
                    blockRecords[block].add(n)
                    
                    emptyCells.popleft()
                    
                    if dfs():
                        return True
                    else:
                        # revert to previous state
                        board[ridx][cidx] = EMPTY_CELL
                        rowRecords[ridx].discard(n)
                        colRecords[cidx].discard(n)
                        blockRecords[block].discard(n)
                        emptyCells.appendleft((ridx, cidx))
            
            # none of the value is valid
            return False
         # pupolate the board using dfs
        dfs()
