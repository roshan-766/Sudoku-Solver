def sudoku(sg):
    l=[1,2,3,4,5,6,7,8,9]
    for i in range(0,len(sg)):
        for k in range(0,len(sg[i])):
            if sg[i][k]=="?":
                    for j in range(0,9):
                        if j>=i:
                            j=j+1
                        if j >=9:
                            break
                        for n in l:
                            if sg[j][k] == n:
                                l.remove(n)
                    sg[i][k] =l[0]
                    l=[1,2,3,4,5,6,7,8,9]
    print(sg)
sudoku_grid =[
    [5,3,4,6,7,8,9,1,2],
    [6,7,2,1,9,5,3,4,8],
    ["?",9,8,3,4,2,5,6,7],
    [8,5,9,7,6,1,4,2,3],
    [4,2,"?",8,5,3,7,9,1],
    [7,1,3,9,"?",4,8,5,6],
    [9,6,1,5,3,"?",2,8,4],
    [2,8,7,4,1,9,6,3,5],
    [3,4,5,2,8,6,1,"?",9]]

sudoku(sudoku_grid)
