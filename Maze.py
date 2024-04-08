from pyamaze import maze,agent,COLOR,textLabel
from queue import PriorityQueue
from pyamaze import maze,agent,textLabel,COLOR
from collections import deque


##encontrar el camino más corto con dijsltra pasando por los puntod tour trip###
def TourTrip(m,*h,start=None):
    if start is None:
        start=(m.rows,m.cols)
        

    hurdles=[(i.position,i.cost) for i in h]

    unvisited={n:float('inf') for n in m.grid}
    unvisited[start]=0
    visited={}
    revPath={}
    while unvisited:
        currCell=min(unvisited,key=unvisited.get)
        visited[currCell]=unvisited[currCell]
        if currCell==m._goal:
            break
        for d in 'EWNS':
            if m.maze_map[currCell][d]==True:
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                elif d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                elif d=='S':
                    childCell=(currCell[0]+1,currCell[1])
                elif d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                if childCell in visited:
                    continue
                tempDist= unvisited[currCell]+1
                for hurdle in hurdles:
                    if hurdle[0]==currCell:
                        tempDist+=hurdle[1]

                if tempDist < unvisited[childCell]:
                    unvisited[childCell]=tempDist
                    revPath[childCell]=currCell
        unvisited.pop(currCell)
    
    fwdPath={}
    cell=m._goal
    while cell!=start:
        fwdPath[revPath[cell]]=cell
        cell=revPath[cell]
    
    return fwdPath,visited[m._goal]
 
 
###camino más corto sin considerar semaforización###           
def dijkstra(m,*h,start=None):
    if start is None:
        start=(m.rows,m.cols)

    hurdles=[(i.position,i.cost) for i in h]

    unvisited={n:float('inf') for n in m.grid}
    unvisited[start]=0
    visited={}
    revPath={}
    while unvisited:
        currCell=min(unvisited,key=unvisited.get)
        visited[currCell]=unvisited[currCell]
        if currCell==m._goal:
            break
        for d in 'EWNS':
            if m.maze_map[currCell][d]==True:
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                elif d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                elif d=='S':
                    childCell=(currCell[0]+1,currCell[1])
                elif d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                if childCell in visited:
                    continue
                tempDist= unvisited[currCell]+1
                for hurdle in hurdles:
                    if hurdle[0]==currCell:
                        tempDist+=hurdle[1]

                if tempDist < unvisited[childCell]:
                    unvisited[childCell]=tempDist
                    revPath[childCell]=currCell
        unvisited.pop(currCell)
    
    fwdPath={}
    cell=m._goal
    while cell!=start:
        fwdPath[revPath[cell]]=cell
        cell=revPath[cell]
    
    return fwdPath,visited[m._goal]

def AConSemaforizacion(m,*h,start=None):
    if start is None:
        start=(m.rows,m.cols)

    hurdles=[(i.position,i.cost) for i in h]

    unvisited={n:float('inf') for n in m.grid}
    unvisited[start]=0
    visited={}
    revPath={}
    while unvisited:
        currCell=min(unvisited,key=unvisited.get)
        visited[currCell]=unvisited[currCell]
        if currCell==m._goal:
            break
        for d in 'EWNS':
            if m.maze_map[currCell][d]==True:
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                elif d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                elif d=='S':
                    childCell=(currCell[0]+1,currCell[1])
                elif d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                if childCell in visited:
                    continue
                tempDist= unvisited[currCell]+1
                for hurdle in hurdles:
                    if hurdle[0]==currCell:
                        tempDist+=hurdle[1]

                if tempDist < unvisited[childCell]:
                    unvisited[childCell]=tempDist
                    revPath[childCell]=currCell
        unvisited.pop(currCell)
    
    fwdPath={}
    cell=m._goal
    while cell!=start:
        fwdPath[revPath[cell]]=cell
        cell=revPath[cell]
    
    return fwdPath,visited[m._goal]
 
 

##A* para encontrar el camino más corto tomando varios nodos y mirando el de menos peso###

def h(cell1, cell2):
    x1, y1 = cell1
    x2, y2 = cell2
    return (abs(x1 - x2) + abs(y1 - y2))
    
def aStar(m,start=None):
    if start is None:
        start=(m.rows,m.cols)
    open = PriorityQueue()
    open.put((h(start, m._goal), h(start, m._goal), start))
    aPath = {}
    g_score = {row: float("inf") for row in m.grid}
    g_score[start] = 0
    f_score = {row: float("inf") for row in m.grid}
    f_score[start] = h(start, m._goal)
    searchPath=[start]
    while not open.empty():
        currCell = open.get()[2]
        searchPath.append(currCell)
        if currCell == m._goal:
            break        
        for d in 'ESNW':
            if m.maze_map[currCell][d]==True:
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                elif d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                elif d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                elif d=='S':
                    childCell=(currCell[0]+1,currCell[1])

                temp_g_score = g_score[currCell] + 1
                temp_f_score = temp_g_score + h(childCell, m._goal)

                if temp_f_score < f_score[childCell]:   
                    aPath[childCell] = currCell
                    g_score[childCell] = temp_g_score
                    f_score[childCell] = temp_g_score + h(childCell, m._goal)
                    open.put((f_score[childCell], h(childCell, m._goal), childCell))


    fwdPath={}
    cell=m._goal
    while cell!=start:
        fwdPath[aPath[cell]]=cell
        cell=aPath[cell]
    return searchPath,aPath,fwdPath      

##BFS##

def BFS(m,start=None):
    if start is None:
        start=(m.rows,m.cols)
    frontier = deque()
    frontier.append(start)
    bfsPath = {}
    explored = [start]
    bSearch=[]

    while len(frontier)>0:
        currCell=frontier.popleft()
        if currCell==m._goal:
            break
        for d in 'ESNW':
            if m.maze_map[currCell][d]==True:
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                elif d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                elif d=='S':
                    childCell=(currCell[0]+1,currCell[1])
                elif d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                if childCell in explored:
                    continue
                frontier.append(childCell)
                explored.append(childCell)
                bfsPath[childCell] = currCell
                bSearch.append(childCell)
    # print(f'{bfsPath}')
    fwdPath={}
    cell=m._goal
    while cell!=(rowPstart,colPstart):
        fwdPath[bfsPath[cell]]=cell
        cell=bfsPath[cell]
    return bSearch,bfsPath,fwdPath     


if __name__=='__main__':
    
    rowPstart = int(input("Ingrese la posición de la FILA donde está el pasajero: "))
    colPstart = int(input("Ingrese el número de COLUMNA: "))
    
    rowPEnd = int(input("Ingrese la FILA destino del pasajero: "))
    colPEnd= int(input("Ingrese el número de COLUMNA: "))
    
    costSemaforo= int(input("Ingrese el costo de pasar por un semaforo: "))
    
    option = 0
        
    while(option!=6):
        option = int(input("ingresa la option y presiona Enter:"
                        +"\n1. TourTrip"
                        +"\n2. Camino más corto (sin considerar semaforización)"
                        +"\n3. Mejor opcion para el pasajero (A*)"
                        +"\n4. Camino más rápido con semaforización"
                        +"\n5. Ruta con menos consumo de combustible"
                        +"\n5. Salir"))

        ###tourTrip (debe pasar por todos los nodos marcados)###
        ###bfs iterativo###
        if(option==1):
            myMaze=maze(15,20)
            ##filas y columnas de la meta
            myMaze.CreateMaze(rowPEnd,colPEnd,loopPercent=100)
            #myMaze.CreateMaze(loadMaze='dijkMaze.csv')

            #azul punto turístico
            
            h1=agent(myMaze,4,4,color=COLOR.blue)
            h2=agent(myMaze,12,6,color=COLOR.blue)
            h3=agent(myMaze,8,5,color=COLOR.blue)
            
            #rojo los semaforos
            h4=agent(myMaze,7,2,color=COLOR.red)
            h5=agent(myMaze,10,11,color=COLOR.red)
            h6=agent(myMaze,14,5,color=COLOR.red)
            h7=agent(myMaze,14,6,color=COLOR.red)
            h8=agent(myMaze,7,7,color=COLOR.red)
            
            h1.cost=-50
            h2.cost=-50
            h3.cost=-50
            #h4.cost=-5
            #h5.cost=-5

            path,c=TourTrip(myMaze,h1,h2,h3,start=(rowPstart,colPstart))
            textLabel(myMaze,'Total Costo de TourTrip',str(abs(c)))
            #print(path, "El consumo de combustible es: " +str(abs(c-397)))

            #a=agent(myMaze,color=COLOR.cyan,filled=True,footprints=True)
            a=agent(myMaze,rowPstart,colPstart,color=COLOR.cyan,filled=True,footprints=True)
            myMaze.tracePath({a:path})
        
        ##camino más corto sin considerar semaforización###
        if(option==2): 
            
            myMaze=maze(15,20)
            #creación el mapa con meta
            myMaze.CreateMaze(rowPEnd,colPEnd,loopPercent=100)
            #la meta esta en la esquina superior izquierda por default (1,1)
            #m.CreateMaze(loopPercent=10,theme='dark')
            bSearch,bfsPath,fwdPath=BFS(myMaze, start=(rowPstart,colPstart))
            #camino de la busqueda
            a=agent(myMaze,rowPstart,colPstart,footprints=True,color=COLOR.yellow,shape='square',filled=True)
            #camino de ida más corto
            b=agent(myMaze,rowPEnd,colPEnd,footprints=True,color=COLOR.red,shape='square',filled=False,goal=(rowPstart,colPstart))
            
            h4=agent(myMaze,7,2,color=COLOR.red)
            h5=agent(myMaze,10,11,color=COLOR.red)
            h6=agent(myMaze,14,5,color=COLOR.red)
            h7=agent(myMaze,14,6,color=COLOR.red)
            h8=agent(myMaze,7,7,color=COLOR.red)
            
            #agente de la meta
            c=agent(myMaze,rowPstart,colPstart,footprints=True,color=COLOR.cyan,shape='square',filled=True,goal=(rowPEnd,colPEnd))
            #camino de vuelta más corto
            #c=agent(m,1,1,footprints=True,color=COLOR.cyan,shape='square',filled=True,goal=(m.rows,m.cols))
            
            myMaze.tracePath({a:bSearch},delay=100)
            myMaze.tracePath({b:bfsPath},delay=100)
            myMaze.tracePath({c:fwdPath},delay=100)
            
            
        ##A* para encontrar el camino más corto tomando varios nodos y mirando el de menos peso###
        if(option==3):
            myMaze=maze(15,20)
            #meta
            myMaze.CreateMaze(rowPEnd,colPEnd,loopPercent=100)
            #myMaze=maze(4,4)
            #myMaze.CreateMaze(loadMaze='aStardemo.csv')

            searchPath,aPath,fwdPath=aStar(myMaze,start=(rowPstart,colPstart) )
            a=agent(myMaze,rowPstart,colPstart, footprints=True,color=COLOR.blue,filled=True)
            #agente de la meta
            b=agent(myMaze,rowPEnd,colPEnd,footprints=True,color=COLOR.yellow,filled=True,goal=(rowPstart,colPstart))
            c=agent(myMaze,rowPstart,colPstart, footprints=True,color=COLOR.red,goal=(rowPEnd,colPEnd))

            myMaze.tracePath({a:searchPath},delay=300)
            myMaze.tracePath({b:aPath},delay=300)
            myMaze.tracePath({c:fwdPath},delay=300)

            l=textLabel(myMaze,'Costo al Pasajero',len(fwdPath)+1)
            l=textLabel(myMaze,'Total Recorrido de la búsqueda',len(searchPath))
            
        ##camino más corto con semaforización###
        if(option==4):
            myMaze=maze(15,20)
            ##filas y columnas de la meta
            myMaze.CreateMaze(rowPEnd,colPEnd,loopPercent=100)
            #myMaze.CreateMaze(loadMaze='dijkMaze.csv')

            #amarillo los taxis
            #rojo los semaforos
            #azul punto turístico
            #verde el pasajero
            h1=agent(myMaze,4,4,color=COLOR.red)
            h2=agent(myMaze,7,6,color=COLOR.red)
            h3=agent(myMaze,8,1,color=COLOR.red)
            
            #h4=agent(myMaze,7,2,color=COLOR.red)
            #h5=agent(myMaze,12,3,color=COLOR.red)
            #h6=agent(myMaze,9,5,color=COLOR.red)
            #h7=agent(myMaze,4,6,color=COLOR.red)
            #h8=agent(myMaze,8,7,color=COLOR.red)
            
            h1.cost=100
            h2.cost=100
            h3.cost=100
            #h4.cost=-5
            #h5.cost=-5

            
            path,c=AConSemaforizacion(myMaze,h1,h2,h3,start=(rowPstart,colPstart))
            textLabel(myMaze,'Total recorrido del viaje',str(abs(c)))
            #print(path, "El consumo de combustible es: " +str(abs(c-397)))

            # a=agent(myMaze,color=COLOR.cyan,filled=True,footprints=True)
            a=agent(myMaze,rowPstart,colPstart,color=COLOR.cyan,filled=True,footprints=True)
            myMaze.tracePath({a:path})
        
        ###Ruta con menos consumo de combustible##
        if(option==5):
            myMaze=maze(15,20)
            #meta
            myMaze.CreateMaze(rowPEnd,colPEnd,loopPercent=100)


            searchPath,aPath,fwdPath=aStar(myMaze,start=(rowPstart,colPstart) )
            a=agent(myMaze,rowPstart,colPstart, footprints=True,color=COLOR.blue,filled=True)
            #agente de la meta
            b=agent(myMaze,rowPEnd,colPEnd,footprints=True,color=COLOR.yellow,filled=True,goal=(rowPstart,colPstart))
            c=agent(myMaze,rowPstart,colPstart, footprints=True,color=COLOR.red,goal=(rowPEnd,colPEnd))

            myMaze.tracePath({a:searchPath},delay=300)
            myMaze.tracePath({b:aPath},delay=300)
            myMaze.tracePath({c:fwdPath},delay=300)

            l=textLabel(myMaze,'Consumo de combustible',len(fwdPath)+1)
            l=textLabel(myMaze,'Total Búsqueda',len(searchPath))
            
        
        ##salir del programa### 
        if(option==6):
            print("Hasta luego")
            break
        else:
            print("Opción no válida")


    ##tourTrip (debe pasar por todos los que pueda)
"""        

myMaze=maze(15,20)
            #creación el mapa con meta
            myMaze.CreateMaze(rowPEnd,colPEnd,loopPercent=100)
            #la meta esta en la esquina superior izquierda por default (1,1)
            #m.CreateMaze(loopPercent=10,theme='dark')
            bSearch,bfsPath,fwdPath=BFS(myMaze, start=(rowPstart,colPstart))
            #camino de la busqueda
            a=agent(myMaze,footprints=True,color=COLOR.yellow,shape='square',filled=True)
            #camino de ida más corto
            b=agent(myMaze,footprints=True,color=COLOR.red,shape='square',filled=False)
            
            h4=agent(myMaze,7,2,color=COLOR.red)
            h5=agent(myMaze,10,11,color=COLOR.red)
            h6=agent(myMaze,14,5,color=COLOR.red)
            h7=agent(myMaze,14,6,color=COLOR.red)
            h8=agent(myMaze,7,7,color=COLOR.red)
            
            #agente de la meta
            c=agent(myMaze,rowPEnd,colPEnd,footprints=True,color=COLOR.cyan,shape='square',filled=True,goal=(rowPstart,colPstart))
            #camino de vuelta más corto
            #c=agent(m,1,1,footprints=True,color=COLOR.cyan,shape='square',filled=True,goal=(m.rows,m.cols))
            
            myMaze.tracePath({a:bSearch},delay=100)
            myMaze.tracePath({c:bfsPath},delay=100)
            myMaze.tracePath({b:fwdPath},delay=100)








    if(option==1):
        myMaze=maze(15,20)
        ##filas y columnas de la meta
        myMaze.CreateMaze(10,4,loopPercent=100)
        #myMaze.CreateMaze(loadMaze='dijkMaze.csv')

        #amarillo los taxis
        #rojo los semaforos
        #azul punto turístico
        #verde el pasajero
        h1=agent(myMaze,4,4,color=COLOR.blue)
        h2=agent(myMaze,7,6,color=COLOR.blue)
        h3=agent(myMaze,8,1,color=COLOR.blue)
        
        h4=agent(myMaze,4,2,color=COLOR.red)
        h5=agent(myMaze,4,3,color=COLOR.red)
        h6=agent(myMaze,4,5,color=COLOR.red)
        h7=agent(myMaze,4,6,color=COLOR.red)
        h8=agent(myMaze,4,7,color=COLOR.red)
        
        h1.cost=-100
        h2.cost=-200
        h3.cost=-200
        #h4.cost=-5
        #h5.cost=-5

        
        # path,c=dijstra(myMaze,h1,h2,h2,h3,h4,h5)
        path,c=dijkstraTourTrip(myMaze,h1,h2,h3,start=(rowPstart,colPstart))
        textLabel(myMaze,'Total Costo de TourTrip',str(abs(c)))
        print(path, "El consumo de combustible es: " +str(abs(c-397)))

        # a=agent(myMaze,color=COLOR.cyan,filled=True,footprints=True)
        a=agent(myMaze,rowPstart,colPstart,color=COLOR.cyan,filled=True,footprints=True)
        myMaze.tracePath({a:path})
        
    ##camino más corto sin considerar semaforización   
    elif(option == 2):
        myMaze=maze(10,15)
        myMaze.CreateMaze(5,6,loopPercent=100)
        # myMaze.CreateMaze(loadMaze='dijkMaze.csv')

        h1=agent(myMaze,1,1,color=COLOR.green)
        h2=agent(myMaze,3,6,color=COLOR.green)
        h3=agent(myMaze,8,1,color=COLOR.green)
        #h4=agent(myMaze,4,2,color=COLOR.red)
        #h5=agent(myMaze,4,3,color=COLOR.red)

        h1.cost=0
        h2.cost=0
        h3.cost=0
        #h4.cost=-5
        #h5.cost=-5

        # path,c=dijstra(myMaze,h1,h2,h2,h3,h4,h5)
        path,c=dijkstra(myMaze,start=(rowPstart,colPstart))
        textLabel(myMaze,'Costo sin considerar semaforización',str(c*2))
        print(path, f"El consumo de combustible es: "+str(c))

        # a=agent(myMaze,color=COLOR.cyan,filled=True,footprints=True)
        a=agent(myMaze,rowPstart,colPstart,color=COLOR.cyan,filled=True,footprints=True)
        myMaze.tracePath({a:path})
        
    ##mejor opcion (A*) ruta más economica para el pasajero
    elif(option == 3):
        myMaze=maze(10,15)
        #meta
        myMaze.CreateMaze(1,1,loopPercent=100)
        #myMaze=maze(4,4)
        #myMaze.CreateMaze(loadMaze='aStardemo.csv')

        searchPath,aPath,fwdPath=aStar(myMaze)
        a=agent(myMaze,footprints=True,color=COLOR.blue,filled=True)
        #agente de la
        b=agent(myMaze,1,1,footprints=True,color=COLOR.yellow,filled=True,goal=(myMaze.rows,myMaze.cols))
        c=agent(myMaze,footprints=True,color=COLOR.red)

        myMaze.tracePath({a:searchPath},delay=300)
        myMaze.tracePath({b:aPath},delay=300)
        myMaze.tracePath({c:fwdPath},delay=300)

        l=textLabel(myMaze,'A Star Path Length',len(fwdPath)+1)
        l=textLabel(myMaze,'A Star Search Length',len(searchPath))
    
    myMaze.run()
    """
myMaze.run()