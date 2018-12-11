serial_no = 5791 ## Input

width = 300
subgrid_size = 3 ## Part 1 subgrid

def grid_sum(x,y,subgrid_size,grid):
    sum = 0
    for i in range(x,x+subgrid_size):
        for j in range(y,y+subgrid_size):
            sum+=grid[i][j]
    return sum
    
def create_subgrid(subgrid_size, grid):
    subgrid_sums = [[0 for _ in range(width-subgrid_size+1)] for _ in range(width-subgrid_size+1)]
    for x in range(len(subgrid_sums)):
        for y in range(len(subgrid_sums)):
            subgrid_sums[x][y] = grid_sum(x,y,subgrid_size,grid)
    return subgrid_sums

def get_max_elem_coords(grid):
    matrix_max = 0
    max_x, max_y = None, None
    for x in range(len(grid)):
        for y in range(len(grid)):
            cur = grid[x][y]
            if cur > matrix_max:
                matrix_max = cur
                max_x, max_y = x+1, y+1
    return max_x, max_y, matrix_max

grid = [[None for _ in range(width)] for _ in range(width)]
for x in range(width):
    for y in range(width):
        rack_id = (x+1)+10
        power_tmp = ((rack_id*(y+1))+serial_no)*rack_id
        power = int(repr((power_tmp//100))[-1])-5
        grid[x][y] = power

subgrid_sums = create_subgrid(subgrid_size, grid)
max_x, max_y, value = get_max_elem_coords(subgrid_sums)

print(f"Max power at {max_x},{max_y}: {value}")

global_max = 0
global_max_x, global_max_y, grid_size = None, None, None
for subgrid_size in range(1, width+1):
    subgrid_sums = create_subgrid(subgrid_size, grid)
    max_x, max_y, local_value = get_max_elem_coords(subgrid_sums)
    if local_value > global_max:
        grid_size = subgrid_size
        global_max_x, global_max_y, global_max = max_x, max_y, local_value
    print(f"{subgrid_size}. Current max power at {global_max_x},{global_max_y},{grid_size}: {value}")
    
print(f"Global max power at {global_max_x},{global_max_y},{grid_size}: {value}")