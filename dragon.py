import math
#Diagram size
diagsz=500.0
#Static SVG file name for now:
svgfilename="/home/david/Pictures/Sieve/dragonOutput.svg"
# Open svg file for writing:
outfile=open(svgfilename,'w')
#Write svg header:
outfile.write('<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n')
outfile.write('<svg xmlns:svg="http://www.w3.org/2000/svg"\n')
outfile.write('xmlns="http://www.w3.org/2000/svg" version="1.1"\n')
outfile.write('width="%.2f" height="%.2f" >\n' % (diagsz, diagsz))

#How many iterations of the curve to draw:
iterations=4
#Initialise set of directions:
directions=[
    [-1, 1],
    [-1, 0],
    [-1,-1],
    [ 0,-1],
    [ 1,-1],
    [ 1, 0],
    [ 1, 1],
    [ 0, 1]
    ]
#Direction to move from origin for starting point:
firststep=5
#Direction to move in for first step along the curve:
firstdir=0
steplength=0.5
#Create initial segments list: [[x,y],length, curve dir.] 
#Start with stuff that gets set in the main loop set to "None" to expose any bugs.
segments=[[None,None,0],[None,None,1]]
for j in range(iterations):
  tempdir=firstdir #Start with the saved first direction, will iterate.
  for i in range(2**(j+1)+1):
    if i%2: #if i is odd
      segments.insert(i,[None,None,(i/2)%2])
    if i:
      if not segments[i-1][2] and not segments[i][2]: tempdir=(tempdir-2)%8
      if segments[i-1][2] and segments[i][2]: tempdir=(tempdir+2)%8
    segments[i][0]=directions[tempdir]
    segments[i][1]=steplength
  radius=1/(2**(j*0.5+1))
  print("radius " + str(radius))
  outfile.write('<path style="fill:none;stroke:black;stroke-width:0.5" \n')
  outfile.write('d="M %.4f,%.4f\n' % tuple([x*steplength*diagsz for x in directions[firststep]]))
  for i in range(len(segments)):
    outfile.write('   a %.4f,%.4f 0 0,%d %.4f,%.4f\n' % (radius*diagsz, radius*diagsz, segments[i][2], segments[i][0][0]*steplength*diagsz, segments[i][0][1]*steplength*diagsz))
  outfile.write('"\n/>\n')
  firstdir =(firstdir +1)%8
  firststep=(firststep+1)%8
  if (j)%2:
    steplength/=2
  print("steplength "+str(steplength))
  print("iteration "+str(j))
outfile.write('</svg>')
