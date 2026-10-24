class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        cars_time = []
        stack=[]
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        cars.sort(reverse=True)
        
        for pos, time in cars:
            cars_time.append((target - pos) / time)
        for i in cars_time:
            if stack and  stack[-1]>= i:
                continue
            stack.append(i)
        return len(stack)


        