import math
#Static definitions:
#Order of triangle to draw:
iterations=5
##Need half of sin(pi/3) for hexagon corner:
hsp3=0.5*math.sin(math.pi/3)
#Order 1 triangle as reference points:
refpoints=[
  [  0.0 , 0.0 ],
  [  0.25, hsp3],
  [  0.75, hsp3],
  [  0.0 , 1.0 ]
]
points=list(refpoints)
#Interpolate new points:
for i in range(len(points)-1):
  for j in range(len(refpoints)-2):
    x=refpoints[j+1][0]*(points[i+1][0]-points[i][0])+ refpoints[j+1][1]*(points[i  ][1]-points[i+1][1])+ refpoints[j][0]
    y=refpoints[j+1][0]*(points[i+1][1]-points[i][1])+ refpoints[j+1][1]*(points[i+1][0]-points[i  ][0])+ refpoints[j][1]
    points.insert(3*i+j+1,[x,y])


