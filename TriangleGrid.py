import math, operator, gmpy2
#Static defs
#Number of rings
rings=10

#Amount by which to squish the diagram:
squish=1/(3-math.sqrt(2))

#Generator function from primes using gmpy2:
def primes():
  n = 2
  while True:
    yield n
    n = gmpy2.next_prime(n)
#Create a new instance of the generator:
primegen=primes()

#Six directions of movement to enumerate points on stretched hex grid
directions=[
[[ 1,-1],[ 1, 1]],
[[ 0, 2],[ 1, 1]],
[[ 0, 2],[-1, 1]],
[[-1,-1],[-1, 1]],
[[-1,-1],[ 0,-2]],
[[ 1,-1],[ 0,-2]]
]
#Base repeat counts of movement directions to enumerate points for Ulam spiral on triangular tiling.
#For each additional ring, do each movement one extra time.
baserepeat=[0,0,1,0,1,1]

#Diagram size in SVG units:
diagsz=800.0

#Static SVG file name for now:
svgfilename="/home/david/Pictures/Sieve/TriangleGridOutput.svg"
# Open svg file for writing:
outfile=open(svgfilename,'w')

#Create the spiral:
#Start with (0,0) in the middle of the innermost hexagon:
points=[[1,-1]]
#Now add points while spiraling outward.
for i in range(rings):
  #add the number of points determined by the base repetition plus the ring count:
  for k in range(len(baserepeat)):
    for l in range(baserepeat[k]+i):
      points.append(map(operator.add, points[-1], directions[k][0]))
      points.append(map(operator.add, points[-1], directions[k][1]))
#Last point in the spiral is the start of the next ring; remove.
del points[-1]

#What the spot size will be after squishing and before scaling:
spotsize=2.0*(1/(3.0-math.sqrt(2)))
#Find the maximum coordinate in the points list. The diagram is symmetrical, so the y coordinate will be the max, and there's no need to get abs. values.
#Then add the spot size in squished units, so that we can include the edge spots, not just their centers.
maxcoord=max(map(max, points))/squish+spotsize
#Scale factor to transform to SVG coordinates:
scalefactor=diagsz/maxcoord

#Scaling:
#Scale the spot size up:
spotsize *= scalefactor
#Now squish the spiral by the right factor to make the hexagons regular, scale up to SVG size, and shift into the center of the diagram:
points[:]=[[x[0]*scalefactor+diagsz/2,x[1]*squish*scalefactor+diagsz/2] for x in points]

#Create list of primes:
primelist=[int(next(primegen))]
while primelist[-1]<=len(points):
  primelist.append(int(next(primegen)))
#Truncate if needed:
while primelist[-1]>=len(points):
  del primelist[-1]

#Write svg header:
outfile.write('<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n')
outfile.write('<svg xmlns:svg="http://www.w3.org/2000/svg"\n')
outfile.write('xmlns="http://www.w3.org/2000/svg" version="1.1"\n')
#Set svg size:
outfile.write('width="%.2f" height="%.2f">\n' % (diagsz, diagsz))

#Draw and animate spots at multiples of prime numbers:
#How many primes to animate:
#nprimes=min(max(len(primelist)/2, 10), len(primelist))
#for p in range(nprimes):
for p in range(len(primelist)):
  outfile.write('<g id="mod%dspots">\n' %(primelist[p]))
  for i in range(0,len(points),primelist[p]):
    outfile.write(' <circle id="%dx%d" fill="rgb(0,0,255)" stroke="none" opacity="0.2" cx="%.4f" cy="%.4f" r="%.4f" >\n' % (primelist[p], i, (points[i][0]), (points[i][1]), spotsize/2))
    outfile.write('  <animate attributeName="opacity" begin="%ds" dur="2s" fill="freeze" from="0.2"          to="1"            /> \n' % (2*p))
    outfile.write('  <animate attributeName="fill"    begin="%ds" dur="2s" fill="freeze" from="rgb(0,0,255)" to="rgb(255,0,0)" /> \n' % (2*p))
    outfile.write('  <animate attributeName="opacity" begin="%ds" dur="2s" fill="freeze" from="1"            to="0.2"          /> \n' % (2*(p+1)))
    outfile.write('  <animate attributeName="fill"    begin="%ds" dur="2s" fill="freeze" from="rgb(255,0,0)" to="rgb(0,0,255)" /> \n' % (2*(p+1)))
    outfile.write(' </circle>\n')
  outfile.write('</g>')

#Draw and animate spots at prime numbers:
for p in range(len(primelist)):
  outfile.write(' <circle id="prime%d" fill="rgb(0,255,0)" stroke="none" opacity="0" cx="%.4f" cy="%.4f" r="%.4f" >\n' % (primelist[p], (points[primelist[p]][0]), (points[primelist[p]][1]), spotsize/2))
  outfile.write('  <animate attributeName="opacity" begin="%ds" dur="2s" fill="freeze" from="0.0"          to="1"            /> \n' % (2*p+1))
  outfile.write(' </circle>\n')

#End SVG:
outfile.write('</svg>\n')
#Close the file
outfile.close()

