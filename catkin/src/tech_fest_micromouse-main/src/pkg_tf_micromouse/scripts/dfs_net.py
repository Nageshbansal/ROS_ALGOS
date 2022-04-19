
from tracemalloc import start


def go_to(i, j):
    global path_so_far, end_i, end_j, a
    if i < 0 or j < 0 or i > len(a)-1 or j > len(a[0])-1:
        return
    # If we've already been there or there is a wall, quit
    if (i, j) in path_so_far or a[i][j] > 0:
        return
    path_so_far.append((i, j))
    a[i][j] = 2
    if (i, j) == (end_i, end_j):
        print("Found!")
        a_ = path_so_far
        turn(a_)
        path_so_far.pop()
        return
    else:
        go_to(i - 1, j)  # check top
        go_to(i + 1, j)  # check bottom
        go_to(i, j + 1)  # check right
        go_to(i, j - 1)  # check left
    path_so_far.pop()
    return
def turn(a_):
    for i_ in range(1,len(a_)-1):
        prev_pt = a_[i_-1]
        curr_pt = a_[i_]
        next_pt = a_[i_+1]
        if prev_pt[0]!=next_pt[0] and prev_pt[1]!=next_pt[1]:
            turns.append(curr_pt)
    turns.append((end_i,end_j))
    print(turns)


def final_call(map,x_i,y_i,x_f,y_f):
    global start_i
    global start_j
    global a
    global end_j 
    global end_j
    a = map
    start_i = x_i
    start_j 


a = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0 ,0, 0, 0, 1, 0, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0 ,0, 0, 0, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0 ,0, 0, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],]

turns = []
path_so_far = []
start_i, start_j = 1,1
end_i, end_j = 5,19

go_to(start_i,start_j)