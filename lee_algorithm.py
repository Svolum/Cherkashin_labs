from collections import deque  
  
  
def print_grid(grid):  
    for row in grid:  
        print(" ".join(f"{str(cell).rjust(2)}" for cell in row))  
    print()  
  
  
def lee_algorithm_diagonal(grid, start, end):  
    rows = len(grid)  
    cols = len(grid[0])  
  
    wave_map = [row[:] for row in grid]  
  
    if wave_map[start[0]][start[1]] == -1 or wave_map[end[0]][end[1]] == -1:  
        return None, []  
  
    wave_map[start[0]][start[1]] = 1  
    queue = deque([start])  
      
      
    directions = [  
        (-1, 0), (1, 0), (0, -1), (0, 1),  # Прямые  
        (-1, -1), (-1, 1), (1, -1), (1, 1)  # Диагонали  
    ]  
      
  
    found = False  
    while queue:  
        x, y = queue.popleft()  
  
        if (x, y) == end:  
            found = True  
            break  
        for dx, dy in directions:  
            nx, ny = x + dx, y + dy  
  
            if 0 <= nx < rows and 0 <= ny < cols and wave_map[nx][ny] == 0:  
                wave_map[nx][ny] = wave_map[x][y] + 1  
                queue.append((nx, ny))  
  
    if not found:  
        return wave_map, []  
  
    path = [end]  
    x, y = end  
  
    while (x, y) != start:  
        for dx, dy in directions:  
            nx, ny = x + dx, y + dy  
  
            if 0 <= nx < rows and 0 <= ny < cols:  
                if wave_map[nx][ny] == wave_map[x][y] - 1:  
                    path.append((nx, ny))  
                    x, y = nx, ny  
                    break  
  
    path.reverse()  
    return wave_map, path  
  
  
if __name__ == "__main__":  
    # grid = [  
    #     [0, 0, 0, -1, 0],    #     [0, -1, 0, -1, 0],    #     [0, -1, 0, 0, 0],    #     [0, 0, -1, -1, 0],    #     [-1, 0, 0, 0, 0]    # ]    grid = [  
        [0, 0, 0, 0, 0],  
        [0, 0, 0, 0, 0],  
        [0, 0, -1, -1, 0],  
        [-1, 0, 0, -1, 0],  
        [0, 0, 0, 0, 0]  
    ]  
  
    start_point = (0, 0)  
    end_point = (4, 4)  
  
    print("Исходная карта (-1 это стены):")  
    print_grid(grid)  
  
    wave_map, path = lee_algorithm_diagonal(grid, start_point, end_point)  
  
    print("Карта после распространения волны:")  
    print_grid(wave_map)  
  
    if path:  
        print(f"Найден кратчайший путь! Длина: {len(path) - 1} шагов.")  
        print("Координаты:", path)  
        print("\nВизуализация пути (S-старт, F-финиш, *-путь):")  
  
        for x, y in path:  
            grid[x][y] = " *"  
        grid[start_point[0]][start_point[1]] = " S"  
        grid[end_point[0]][end_point[1]] = " F"  
  
        print_grid(grid)  
    else:  
        print("Путь до финиша не существует")
