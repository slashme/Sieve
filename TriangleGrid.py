import math, operator, gmpy2
#Static defs
#Number of rings
rings=2

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
#Calculate spot size based on diagram size: Probably wrong at the moment.
spotsize=diagsz/(rings+1)/2.0

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
#Now squish the spiral by the right factor to make the hexagons regular:
points[:]=[[x[0],x[1]*squish] for x in points]
