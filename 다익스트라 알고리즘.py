# -*- coding: utf-8 -*-
"""
Created on Sat May 25 11:11:07 2019

@author: User
"""
inf=1000000
n=8 #마지막 노드 번호 (갯수-1)
graph = [[0,4,inf,inf,inf,inf,inf,8,inf],[4,0,8,inf,inf,inf,inf,11,inf],
         [inf,8,0,7,inf,4,inf,inf,2],[inf,inf,7,0,9,14,inf,inf,inf],
         [inf,inf,inf,9,0,10,inf,inf,inf],[inf,inf,4,14,10,0,2,inf,inf],
         [inf,inf,inf,inf,inf,2,0,1,6],[8,11,inf,inf,inf,inf,1,0,7],
         [inf,inf,2,inf,inf,inf,6,7,0]] 

for i in range(n+1):
    for j in range(n+1):
        if graph[i][j]==0 and i != j:
            graph[i][j]=inf


d=list()
for i in range (n+1):
    d.insert(i,0)   
v=list()
for i in range (n+1):
    v.insert(i,0)

#-------------------------------------------

#입력 달라지면 수정할 건 여기까지

#거리 동점이면 더 먼저나온 인덱스부터 방문. d[i]<min 이니까.
def getShortestIndex ():        #방문 안한 노드 중 최소거리. 매번 d[]가 바뀐 다음에 새로운 최소거리 구하는거니까 input변수도 없음.
    min = inf
    for i in range(n+1):
        if d[i]<= min and not v[i]:   #거리 리스트 d[]에서 min보다 작고 방문 안했으면(v[i]가 false)
            min=d[i] 
            global index
            index=i
        
    return index

def dijkstra (starting):
     # 시작점 거리 리스트 d에 대입중
    for i in range(n+1):
        d[i]=graph[starting][i]
    v[starting]= 1                  #initial d      
    #처음 노드 방문한 리스트에 넣음
    
    #여기까지 initial setting
    
    for i in range(n) :  #반복횟수 (initial node 제외)  
        current=getShortestIndex()  #방문할 노드=제일 현재거리 짧은 노드 
        v[current]=1    #제일 짧은 거리 가진 노드를 방문한 리스트에 추가
        
        #거리 업데이트 하는 과정
        for j in range(n+1) :     
            if d[current]+graph[current][j]<d[j] and not v[j]:
                d[j]= d[current]+graph[current][j]
                print(d)
        
   

      
dijkstra(3)         

print("---------------------------------")
print(d)