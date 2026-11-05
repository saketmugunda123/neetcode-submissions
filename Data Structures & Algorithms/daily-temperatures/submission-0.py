class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        answer = [0] * len(temperatures)

        #store indexes on the stack so when you pop, so when you find a value bigger,
        #you compare the currindex vs the bigger one to determine where to place
        stack = []
        for i, temp in enumerate(temperatures):
            #making sure the stack stays in decreasing order (monotonic)

            while stack and temp > temperatures[stack[-1]]:
                index = stack.pop()
                answer[index] = i - index 
            stack.append(i)
        return answer
        
            


