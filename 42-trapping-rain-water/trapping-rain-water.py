class Solution:
    def trap(self, height: List[int]) -> int:
        leftmax = height[0]
        rightmax = height[len(height)-1]
        leftpointer = 0
        rightpointer = len(height)-1

        i = 0
        water = 0
        while i<len(height):
            print(i)
            print(leftpointer,rightpointer)
            print(leftmax,rightmax)
            print("water",water)
            if leftpointer >= rightpointer:
                break
            if leftmax <= rightmax:
                i=leftpointer+1
                leftpointer = i
                if height[i] > leftmax:
                    leftmax = height[i]
                else:
                    water += leftmax-height[i]
            elif leftmax > rightmax:
                i = rightpointer-1
                rightpointer=i
                if height[i] > rightmax:
                    rightmax = height[i]
                else:
                    water += rightmax - height[i]

        return water