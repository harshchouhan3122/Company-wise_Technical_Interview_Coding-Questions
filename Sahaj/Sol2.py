def can_deliver_water(villages, water_needs, capacity, max_trips):
    trips = 0
    water_left = capacity
    
    for i in range(villages):
        if water_needs[i] > capacity:
            return False
        if water_left < water_needs[i]:
            trips += 1
            water_left = capacity
        water_left -= water_needs[i]
    
    if water_left > 0:
        trips += 1
    
    return trips <= max_trips

def calculate_spillage(villages, water_needs, max_trips):
    left, right = 1, sum(water_needs)
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        if can_deliver_water(villages, water_needs, mid, max_trips):
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    
    if result == -1:
        return -1
    
    spillage = 0
    trips = 0
    water_left = result
    
    for i in range(villages):
        if water_needs[i] > result:
            return -1
        if water_left < water_needs[i]:
            trips += 1
            spillage += water_left
            water_left = result
        water_left -= water_needs[i]
    
    if water_left > 0:
        trips += 1
        spillage += water_left
    
    return spillage

# Input
N = int(input())
water_needs = list(map(int, input().split()))
M = int(input())

# Output
result = calculate_spillage(N, water_needs, M)
print(result)
