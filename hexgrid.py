import math, operator
#Static defs
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

#Create the spiral:
#Start in the middle
points=[[0,0]]
#Now add points while spiraling outward.
for i in range(rings):
  #move right one step to go to next ring:
  points.append(map(operator.add, points[-1], moves[-1]))
  #First side is short:
  for k in range(i):
    points.append(map(operator.add, points[-1], moves[0]))
  #Do the rest of the sides at full length:
  for j in range(1,len(moves)):
    for k in range(i+1):
      points.append(map(operator.add, points[-1], moves[j]))
