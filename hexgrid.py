import math, operator, gmpy2
#Static defs
#Number of rings
rings=10
#Need sin(pi/3) for hexagon corner:
sp3=math.sin(math.pi/3)

#Generator function from primes using gmpy2:
def primes():
  n = 2
  while True:
    yield n
    n = gmpy2.next_prime(n)
#Create a new instance of the generator:
primegen=primes()

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

#Create list of primes:
primelist=[int(next(primegen))]
while primelist[-1]<=len(points):
  primelist.append(int(next(primegen)))
#Truncate if needed:
if primelist[-1]>len(points):
  del primelist[-1]

#Write svg header:
outfile.write('<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n')
outfile.write('<svg xmlns:svg="http://www.w3.org/2000/svg"\n')
outfile.write('xmlns="http://www.w3.org/2000/svg" version="1.1"\n')
#Set svg size:
outfile.write('width="%.2f" height="%.2f">\n' % (diagsz, diagsz))

#Draw the spiral:
#outfile.write('<polyline style="fill:none; stroke:red; stroke-width:%.4f"\n  points="' % (spotsize/10))
#for i in range(len(points)):
#  outfile.write( '\n%.4f,%.4f ' % ((points[i][0])*spotsize+diagsz/2.0, (points[i][1])*spotsize+diagsz/2.0))
#outfile.write('" />')

#Draw prime spots:
for p in range(len(primelist)):
  outfile.write('<g id="mod%dspots">\n' %(primelist[p]))
  for i in range(0,len(points),primelist[p]):
    outfile.write(' <circle id="%dx%d" fill="rgb(0,0,255)" stroke="none" opacity="0.2" stroke-width="%.4f" cx="%.4f" cy="%.4f" r="%.4f" >\n' % (primelist[p], i, spotsize/10, (points[i][0])*spotsize+diagsz/2, (points[i][1])*spotsize+diagsz/2, spotsize/2))
    outfile.write('  <animate attributeName="opacity" begin="%ds" dur="2s" fill="freeze" from="0.2"          to="1"            /> \n' % (2*p))
    outfile.write('  <animate attributeName="fill"    begin="%ds" dur="2s" fill="freeze" from="rgb(0,0,255)" to="rgb(255,0,0)" /> \n' % (2*p))
    outfile.write('  <animate attributeName="opacity" begin="%ds" dur="2s" fill="freeze" from="1"            to="0.3"          /> \n' % (2*(p+1)))
    outfile.write('  <animate attributeName="fill"    begin="%ds" dur="2s" fill="freeze" from="rgb(255,0,0)" to="rgb(0,0,255)" /> \n' % (2*(p+1)))
    outfile.write(' </circle>\n')
  outfile.write('</g>')

#End SVG:
outfile.write('</svg>\n')
#Close the file
outfile.close()

