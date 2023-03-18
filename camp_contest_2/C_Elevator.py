num_test_cases = int(input())

for _ in range(num_test_cases):
    floor_time, elevator_time, elevator_level = list(map(int, input().split()))
    
    total_stairs_time = 4 * floor_time
    total_elevator_time = ((elevator_level - 0) * elevator_time) + (4 * elevator_time)
    elevator_stairs_time = (elevator_level * floor_time) + ((4 - elevator_level) * elevator_time)
        
    print(min(total_stairs_time, total_elevator_time, elevator_stairs_time))