import math, operator
#Static defs
#Number of rings
rings=20
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
#Diagram size in SVG units:
diagsz=800.0
#Static spot size for now:
spotsize=diagsz/(rings+1)/2.0

#Static SVG file name for now:
svgfilename="/home/david/Pictures/Sieve/hexgridOutput.svg"
# Open svg file for writing:
outfile=open(svgfilename,'w')

#Write svg header:
outfile.write('<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n')
outfile.write('<svg xmlns:svg="http://www.w3.org/2000/svg"\n')
outfile.write('xmlns="http://www.w3.org/2000/svg" version="1.1"\n')
#Set svg size:
outfile.write('width="%.2f" height="%.2f">\n' % (diagsz, diagsz))

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

#Draw the spiral:
outfile.write('<polyline style="fill:none; stroke:red; stroke-width:%.4f"\n  points="' % (spotsize/10))
for i in range(len(points)):
  outfile.write( '\n%.4f,%.4f ' % ((points[i][0])*spotsize+diagsz/2.0, (points[i][1])*spotsize+diagsz/2.0))
outfile.write('" />')

#Draw even spots:
outfile.write('<g id="evenspots">')
for i in range(0,len(points),2):
  outfile.write(' <circle id="%d" fill="rgb(255,0,0)" opacity="1" cx="%.4f" cy="%.4f" r="%.4f" />\n' % (i, (points[i][0])*spotsize+diagsz/2, (points[i][1])*spotsize+diagsz/2, spotsize/2))
outfile.write('</g>')

#End SVG:
outfile.write('</svg>\n')
#Close the file
outfile.close()

