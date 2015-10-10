import math, operator
#Number of rings
rings=3
#Need sin(pi/3) for hexagon corner:
sp3=math.sin(math.pi/3)
#Direction list:
moves=[
    [ 0.5, sp3], #right up
    [-0.5, sp3], #left  up
    [-1.0, 0.0], #left
    [-0.5,-sp3], #left  down
    [ 0.5,-sp3], #right down
    [ 1.0, 0.0]  #right
    ]
#Start in the middle
points=[[0,0]]
print(str(points[-1])) #debug
for i in range(rings):
  #move right one step:
  points.append(map(operator.add, points[-1], moves[-1]))
  print("right ring %d" %i) #debug
  print("[%.3f,%.3f]" %(points[-1][0], points[-1][1])) #debug
  #First side is short:
  for k in range(i):
    print("right up ring %d cell %d" %(i,k)) #debug
    points.append(map(operator.add, points[-1], moves[0]))
    print("[%.3f,%.3f]" %(points[-1][0], points[-1][1])) #debug
  #Do the rest of the sides:
  for j in range(1,len(moves)):
    for k in range(i+1):
      print("ring %d side %d cell %d" %(i,j,k)) #debug
      points.append(map(operator.add, points[-1], moves[j]))
      print("[%.3f,%.3f]" %(points[-1][0], points[-1][1])) #debug
