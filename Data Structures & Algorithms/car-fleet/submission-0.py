class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        distance_to_target = [target-x for x in position]
        time_to_distance = [a/b for a,b in zip(distance_to_target,speed)]
        paired = sorted(zip(position, speed, time_to_distance), key = lambda x: x[0], reverse = True)
        sorted_pos = [x[0] for x in paired]
        sorted_speed = [x[1] for x in paired]
        sorted_time = [x[2] for x in paired]
        stack = [sorted_time[0]]
        fleet = 1
        # print(sorted_pos)
        # print(sorted_speed)
        # print(sorted_time)

        for i in range(1, len(sorted_time)):
                time_car_ahead = stack[-1]
                current_car_time = sorted_time[i]
                if current_car_time > time_car_ahead:
                    fleet += 1
                    stack.append(current_car_time)
                    
        return fleet



                


