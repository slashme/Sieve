#!/usr/bin/python
import math, random
#Static SVG file name for now:
svgfilename="/home/david/Pictures/Sieve/HilbertOutput.svg"
#Static number of iterations:
iterations=5
#Number of points in diagram:
npoints=2**(2*iterations)
#Diagram size in SVG units:
diagsz=800.0
#Spot size is diagram size divided in 2 for each iteration:
spotsize=diagsz/(2.0**(iterations+1))
#List of funky colors:
colorlist=[
  [  0,255,  0],
  [  0,  0,255],
  [255,255,  0],
  [255,  0,255],
  [  0,255,255],
  [  0,  0,  0],
  [  0,127,  0],
  [  0,  0,127],
  [127,127,  0],
  [127,  0,127],
  [  0,127,127],
  [127,127,127],
  [  0, 63,  0],
  [  0,  0, 63],
  [ 63, 63,  0],
  [ 63,  0, 63],
  [  0, 63, 63],
  [ 63, 63, 63],
  [127, 63,127],
  [127,127, 63],
  [ 63, 63,127],
  [ 63,127, 63],
  [127, 63, 63],
  [ 63, 63, 63],
  [255, 63,255],
  [255,255, 63],
  [ 63, 63,255],
  [ 63,255, 63],
  [255, 63, 63],
  [ 63, 63, 63]
]
# Open svg file for writing:
outfile=open(svgfilename,'w')
#Write svg header:
outfile.write('<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n')
outfile.write('<svg xmlns:svg="http://www.w3.org/2000/svg"\n')
outfile.write('xmlns="http://www.w3.org/2000/svg" version="1.1"\n')
#Make 350 px wide, 175 px high diagram with a 5 px blank border
outfile.write('width="%.2f" height="%.2f">\n' % (diagsz, diagsz))
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

#Hilbert curve algorithm; not optimal. Shouldn't really recurse this.
def hilbert(x0, y0, xr, xt, yr, yt, n):
    if n:
        hilbert(x0,               y0,               yr/2, yt/2, xr/2, xt/2, n - 1)
        hilbert(x0 + xr/2,        y0 + xt/2,        xr/2, xt/2, yr/2, yt/2, n - 1)
        hilbert(x0 + xr/2 + yr/2, y0 + xt/2 + yt/2, xr/2, xt/2, yr/2, yt/2, n - 1)
        hilbert(x0 + xr/2 + yr,   y0 + xt/2 + yt,  -yr/2,-yt/2,-xr/2,-xt/2, n - 1)
    else:
        xi = x0 + (xr + yr)/2
        yi = y0 + (xt + yt)/2
        poslist.append([xi, yi, []])

hilbert(0.0, 0.0, 1.0, 0.0, 0.0, 1.0, iterations)

countb=0 #new counter, so that we can mark the nth prime and count a sane number of seconds.
tempcolor=[255,255,255] #Fade all to white
#Mark the multiples for animation:
for k in range(2,len(poslist)): #Don't want multiples of 1!
  if not len(poslist[k-1][2]): #Only mark multiples of primes
    #tempcolor=colorlist[countb%len(colorlist)] #Select the next color from the list
    for i in range(2*k,len(poslist)+1,k): #mark all multiples of k. Because we're handling the i-1th item,go one further.
      poslist[i-1][2].append([countb+1,0.5,tempcolor])
    countb+=1
for i in range(len(poslist)):
  tempstring='    <circle fill="rgb(255,0,0)" cx="%.4f" cy="%.4f" r="%.1f"><!--%d-->\n' % ((poslist[i][0])*diagsz, (poslist[i][1])*diagsz, spotsize, i+1)
  outfile.write(tempstring)
  if len(poslist[i][2]):
    #for j in range(len(poslist[i][2])): #Commented out: Fading to white only, so no need to do different fades for different colours.
    for j in range(1): 
      outfile.write('        <animate attributeName="fill" attributeType="CSS"\n')
      tempstring='        to="rgb(%d,%d,%d)" begin="%ds" dur="%.4fs" fill="freeze" />\n' % (poslist[i][2][j][2][0], poslist[i][2][j][2][1], poslist[i][2][j][2][2], poslist[i][2][j][0], poslist[i][2][j][1] )
      outfile.write(tempstring)
  outfile.write('    </circle>\n')

#Create a line to follow the Hilbert curve
outfile.write('<polyline points="')
for i in range(len(poslist)):
  outfile.write( '\n%.4f,%.4f ' % ((poslist[i][0])*diagsz, (poslist[i][1])*diagsz))
outfile.write('"\n style="fill:none;stroke:red;stroke-width:%.4f" />\n' % (spotsize/4.0))

# Label the primes
for i in range(len(poslist)):
  if not len(poslist[i][2]):
    tempstring='    <text text-anchor="middle" opacity="0" fill="rgb(0,0,0)" x="%.4f" y="%.4f" font-size="%.2f">%d\n' % ((poslist[i][0])*diagsz, (poslist[i][1])*diagsz+spotsize/3.0, spotsize, i+1)
    outfile.write(tempstring)
    outfile.write('        <animate attributeName="opacity" attributeType="CSS"\n')
    #Rough prime counting function is n/ln(n)
    tempstring='        to="1" begin="%ds" dur="1s" fill="freeze" />\n' % (math.ceil(1.2*2**iterations/math.log(2**iterations)))
    outfile.write(tempstring)
    outfile.write('    </text>\n')


outfile.write('</svg>\n')
outfile.close()
#Pass the output filename to the calling page.
print svgfilename
