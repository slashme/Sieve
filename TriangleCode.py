#!/usr/bin/python
import math
#Static SVG file name for now:
svgfilename="/home/david/Pictures/Sieve/TriangleOutput.svg"
#Static number of rows:
rows=10
# Open svg file for writing:
outfile=open(svgfilename,'w')
#Write svg header:
outfile.write('<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n')
outfile.write('<svg xmlns:svg="http://www.w3.org/2000/svg"\n')
outfile.write('xmlns="http://www.w3.org/2000/svg" version="1.1"\n')
#Make 350 px wide, 175 px high diagram with a 5 px blank border
outfile.write('width="'+str(rows)+'" height="'+str(rows)+'">\n')
#Create list of spots
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
    poslist.append([count,x,vspace*i])
    x+=1
    count+=1
for i in range(len(poslist)):
  tempstring='    <circle cx="%.4f" cy="%.4f" r="%.1f"/><!--%d-->' % (poslist[i][1], poslist[i][2], 0.5, poslist[i][0])
  outfile.write(tempstring+'\n')
outfile.write('</svg>\n')
outfile.close()
#Pass the output filename to the calling page.
print svgfilename
