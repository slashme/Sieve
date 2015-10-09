import math
#Static definitions:
#Spotsize needs to be corrected, just testing...
spotsize=1
#Static SVG file name for now:
svgfilename="/home/david/Pictures/Sieve/SierpinskiOutput.svg"
#Diagram size in SVG units:
diagsz=800.0
#Order of triangle to draw:
iterations=5
##Need half of sin(pi/3) for hexagon corner:
hsp3=0.5*math.sin(math.pi/3)
#Order 1 triangle as reference points:
refpoints=[
  [  0.0 , 0.0 ],
  [  0.25, hsp3],
  [  0.75, hsp3],
  [  1.0 , 0.0 ]
]
points=list(refpoints)
#Interpolate new points:
for i in range(iterations):
  for i in range(len(points)-1):
    for j in range(len(refpoints)-2):
      x=refpoints[j+1][0]*(points[i+1][0]-points[i][0])+ refpoints[j+1][1]*(points[i  ][1]-points[i+1][1])+ refpoints[j][0]
      y=refpoints[j+1][0]*(points[i+1][1]-points[i][1])+ refpoints[j+1][1]*(points[i+1][0]-points[i  ][0])+ refpoints[j][1]
      points.insert(3*i+j+1,[x,y])

# Open svg file for writing:
outfile=open(svgfilename,'w')
#Write svg header:
outfile.write('<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n')
outfile.write('<svg xmlns:svg="http://www.w3.org/2000/svg"\n')
outfile.write('xmlns="http://www.w3.org/2000/svg" version="1.1"\n')
#Set svg size:
outfile.write('width="%.2f" height="%.2f">\n' % (diagsz, diagsz))
#Create a line to follow the curve:
outfile.write('<polyline points="')
for i in range(len(points)):
  outfile.write( '\n%.4f,%.4f ' % ((points[i][0])*diagsz, (points[i][1])*diagsz))
outfile.write('"\n style="fill:none;stroke:red;stroke-width:%.4f" />\n' % (spotsize/4.0))

#End SVG:
outfile.write('</svg>\n')
#Close the file
outfile.close()
