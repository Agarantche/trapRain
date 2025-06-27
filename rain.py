class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: # Handle empty input
            return 0

        n = len(height)
        maxLeft = [0] * n
        maxRight = [0] * n
        totalWater = 0

        # Populate maxLeft (prefix maximums)
        currentMaxLeft = 0
        for i in range(n):
            currentMaxLeft = max(currentMaxLeft, height[i])
            maxLeft[i] = currentMaxLeft

        # Populate maxRight (suffix maximums)
        currentMaxRight = 0
        for i in range(n - 1, -1, -1): # Iterate from right to left
            currentMaxRight = max(currentMaxRight, height[i])
            maxRight[i] = currentMaxRight

        # Calculate trapped water for each position
        for i in range(n):
            # The actual boundary for trapping water is the minimum of the maxLeft and maxRight at this position
            boundaryHeight = min(maxLeft[i], maxRight[i])
            
            # Water trapped at this position is the difference between the boundary and the current bar's height
            waterTrapped = boundaryHeight - height[i]

            # If waterTrapped is negative, it means the bar is taller than or equal to its boundaries, so no water is trapped.
            if waterTrapped < 0:
                waterTrapped = 0
            
            totalWater += waterTrapped

        return totalWater
