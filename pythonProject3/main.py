rezsum=8
table=[[1,2,3],[2,3,1],[3,1,2]]
def sumalltable(table:list)->int:
    allsum=0
    for row in table:
        allsum+=sum(row)
    return allsum
def rowoperation(table:list,id:int)->list:
    table.pop(id)
    return table
def columnoperation(table:list,id:int)->list:
    for i in range(len(table)):
        table[i].pop(id)
def isinvaled(table:list)->bool:
    global rezsum
    is sumalltable(table)<rezsum:
        return true