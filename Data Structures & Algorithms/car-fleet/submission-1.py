class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars= []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        cars.sort(reverse =True)
        stack = []
        times =[]
        for pos, speed in cars:
            times.append((target- pos) / speed)
        for time in times:
            if stack and stack[-1] >= time:
                continue
            stack.append(time)
        return len(stack)




        