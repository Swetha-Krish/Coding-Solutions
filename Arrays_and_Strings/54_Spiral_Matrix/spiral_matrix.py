class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix); n = len(matrix[0])
        i = 0; j = 0
        UP = 0; RIGHT = 1; DOWN = 2 ; LEFT = 3 ;
        UP_WALL = 0
        DOWN_WALL = m 
        RIGHT_WALL = n
        LEFT_WALL = -1 
        ans = [] 
        DIRECTION = RIGHT 

        while len(ans) != m*n: 
            if DIRECTION == RIGHT:  
                while j < RIGHT_WALL:
                    ans.append(matrix[i][j])
                    j += 1
                i +=1 ; j -= 1
                RIGHT_WALL -= 1 
                DIRECTION = DOWN 
                
            elif DIRECTION == DOWN:  
                while i < DOWN_WALL:
                    ans.append(matrix[i][j])
                    i += 1
                i -=1 ; j -= 1
                DOWN_WALL -=1 
                DIRECTION = LEFT
                
            elif DIRECTION == LEFT:  
                while j > LEFT_WALL:
                    ans.append(matrix[i][j])
                    j -= 1
                i -=1 ; j +=1
                LEFT_WALL +=1 
                DIRECTION = UP 
                
            else:  
                while i > UP_WALL:
                    ans.append(matrix[i][j])
                    i -= 1
                i +=1 ; j +=1
                UP_WALL +=1 
                DIRECTION = RIGHT
        return ans
    


    
    # Time Complexity: O(n * m)
    # Space Complexity: O(1)