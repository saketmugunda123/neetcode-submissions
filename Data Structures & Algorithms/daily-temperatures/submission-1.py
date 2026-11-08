class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        #store indexes in the stack

        #answerArr
        answer = [0]*len(temperatures)

        stack = []
        for i,temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                curr = stack.pop()
                length = i - curr 
                answer[curr] = length
            stack.append(i)
        return answer

        
            


