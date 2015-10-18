import math, copy
#Offset to get curve into middle of page:
offset=[0.33,0.23]
#Diagram size
diagsz=1000.0
#How many iterations of the curve to draw:
iterations=9

#Static SVG file name for now:
svgfilename="/home/david/Pictures/Sieve/dragonOutput.svg"
# Open svg file for writing:
outfile=open(svgfilename,'w')
#Write svg header:
outfile.write('<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n')
outfile.write('<svg xmlns:svg="http://www.w3.org/2000/svg"\n')
outfile.write('xmlns="http://www.w3.org/2000/svg" version="1.1"\n')
outfile.write('width="%.2f" height="%.2f" >\n' % (diagsz, diagsz))

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
#Curve radius
radius=0
#Direction to move from origin for starting point:
firststep=5
oldfirststep=firststep
#Direction to move in for first step along the curve:
firstdir=0
steplength=0.5
oldsteplength=steplength
#Create initial segments list: [[x,y],length, curve dir.] 
segments=[[[0,0],0,0],[[0,0],0,1]]
#start the path statement outside the loop:
outfile.write('<path style="fill:none;stroke:black;stroke-width:0.5">\n')
for j in range(iterations):
  tempdir=firstdir #Start with the saved first direction, will iterate.
  for i in range(2**(j+1)+1):
    if i%2: #if i is odd
      segments.insert(i,[[0,0],0,(i/2)%2])
  oldsegments=copy.deepcopy(segments)#Copying a list containing objects by a=b[:] doesn't work!
  for i in range(2**(j+1)+1):
    if i:
      if not segments[i-1][2] and not segments[i][2]: tempdir=(tempdir-2)%8
      if segments[i-1][2] and segments[i][2]: tempdir=(tempdir+2)%8
    segments[i][0]=directions[tempdir]
    segments[i][1]=steplength
  oldradius=radius
  radius=1/(2**(j*0.5+1))
  outfile.write('  <animate attributeName="d"\n  begin="%ds" dur="1s" fill="freeze"\n  from=\n' % j)
  outfile.write('"M %.4f,%.4f\n' % tuple([y+x*oldradius/math.sqrt(sum([x**2 for x in directions[oldfirststep]]))*diagsz/2 for x,y in zip(directions[oldfirststep],[w*diagsz for w in offset])]))
  for i in range(len(segments)):
    outfile.write('   a %.4f,%.4f 0 0,%d %.4f,%.4f\n' % (oldradius*diagsz/2, oldradius*diagsz/2, oldsegments[i][2], oldsegments[i][0][0]*oldsteplength*diagsz/2, oldsegments[i][0][1]*oldsteplength*diagsz/2))
  outfile.write('"\n')
  outfile.write('to="M %.4f,%.4f\n' % tuple([y+x*radius/math.sqrt(sum([x**2 for x in directions[firststep]]))*diagsz/2 for x,y in zip(directions[firststep],[w*diagsz for w in offset])]))
  for i in range(len(segments)):
    outfile.write('   a %.4f,%.4f 0 0,%d %.4f,%.4f\n' % (radius*diagsz/2, radius*diagsz/2, segments[i][2], segments[i][0][0]*steplength*diagsz/2, segments[i][0][1]*steplength*diagsz/2))
  outfile.write('"\n')
  outfile.write('/>\n')
  oldfirstdir=firstdir
  oldfirststep=firststep
  firstdir =(firstdir +1)%8
  firststep=(firststep+1)%8
  oldsteplength=steplength
  if (j)%2:
    steplength/=2
#Finish the path:
outfile.write('</path>\n')
outfile.write('</svg>')
