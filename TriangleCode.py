#!/usr/bin/python
import math, random
#Static SVG file name for now:
svgfilename="/home/david/Pictures/Sieve/TriangleOutput.svg"
#Static number of rows:
rows=20
# Open svg file for writing:
outfile=open(svgfilename,'w')
#Write svg header:
outfile.write('<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n')
outfile.write('<svg xmlns:svg="http://www.w3.org/2000/svg"\n')
outfile.write('xmlns="http://www.w3.org/2000/svg" version="1.1"\n')
#Make 350 px wide, 175 px high diagram with a 5 px blank border
outfile.write('width="'+str(rows*10)+'" height="'+str(rows*10)+'">\n')
#Create list of spots. The list contains:
# Count: the number of the spot
# x: the x coordinate of the spot's center
# y: the y coordinate of the spot's center
# color animation vector containing a list of:
#  [start time in seconds,
#   duration in seconds,
#   end color vector [r,g,b]
#   ]
poslist=[]
#Which spot are we at?
count=1
#Vertical spacing between rows is sqrt(3/4)
vspace=(3.0/4)**0.5
for i in range(0,rows):
  #The leftmost spot in row i is at x=-i/2
  x=-i/2.0
  #Each row in a triangle has i+1 spots.
  for j in range(i+1):
    poslist.append([count,x,vspace*i,[]])
    x+=1
    count+=1
#Mark the multiples for animation:
for k in range(2,count): #Don't want multiples of 1!
  if not len(poslist[k-1][3]): #Only mark multiples of primes
    tempcolour=[random.randint(0,255), random.randint(0,255), random.randint(0,255)] #Create a random colour - TODO: Structure this later.
    for i in range(2*k,len(poslist),k): #mark all multiples of k
      poslist[i-1][3].append([k,1,tempcolour])
for i in range(len(poslist)):
  tempstring='    <circle fill="rgb(255,0,0)" cx="%.4f" cy="%.4f" r="%.1f"><!--%d-->' % ((poslist[i][1]+rows/2.0)*10.0, (poslist[i][2]+1.0)*10.0, 5, poslist[i][0])
  outfile.write(tempstring+'\n')
  if len(poslist[i][3]):
    for j in range(len(poslist[i][3])):
      outfile.write('        <animate attributeName="fill" attributeType="CSS"\n')
      tempstring='        to="rgb(%d,%d,%d)" begin="%ds" dur="%ds" fill="freeze" />\n' % (poslist[i][3][j][2][0], poslist[i][3][j][2][1], poslist[i][3][j][2][2], poslist[i][3][j][0], poslist[i][3][j][1] )
      outfile.write(tempstring)
  outfile.write('    </circle>\n')
outfile.write('</svg>\n')
outfile.close()
#Pass the output filename to the calling page.
print svgfilename
