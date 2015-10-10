import math
#Static definitions:
#Order of triangle to draw:
iterations=5
#Static SVG file name for now:
svgfilename="/home/david/Pictures/Sieve/SierpinskiOutput.svg"
# Open svg file for writing:
outfile=open(svgfilename,'w')
#Diagram size in SVG units:
diagsz=800.0
#Half the length of a segment (radius of a circle centered on a vertex):
spotsize=1.0/(2**(iterations+2))*diagsz
##Need half of sin(pi/3) for hexagon corner:
hsp3=0.5*math.sin(math.pi/3)
#Order 1 triangle as reference points:
refpoints=[
  [  0.0 , 0.0 ],
  [  0.25, hsp3],
  [  0.75, hsp3],
  [  1.0 , 0.0 ]
]
#Create a vector to hold the developing curve:
points=list(refpoints)
#Interpolate new points:
#At each step, do a linear transformation from refpoints (starts at 0,0; ends at 1,0) to a segment of the curve.
#If we call the segment's start and endpoints ax,ay and bx,by, the transformation matrix is:
#[bx-ax  ay-by  ax] 
#[by-ay  bx-ax  ay] 
#[  0      0    1 ] 
for n in range(iterations):
  for i in range(len(points)-1):
    #Set up target segment coords before starting to insert into points vector:
    ax=points[3*i  ][0]
    ay=points[3*i  ][1]
    bx=points[3*i+1][0]
    by=points[3*i+1][1]
    for j in range(len(refpoints)-2):
      x=(bx-ax)*refpoints[j+1][0]+(ay-by)*refpoints[j+1][1]*(-(1-2*((i+n)%2)))+ax
      y=(by-ay)*refpoints[j+1][0]+(bx-ax)*refpoints[j+1][1]*(-(1-2*((i+n)%2)))+ay
      points.insert(3*i+j+1,[x,y])

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
outfile.write('"\n style="fill:none;stroke:red;stroke-width:%.4f" />\n' % (spotsize/3.0))

#End SVG:
outfile.write('</svg>\n')
#Close the file
outfile.close()
