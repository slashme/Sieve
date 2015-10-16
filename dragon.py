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
segments=[[None,None,1],[None,None,0]]
for j in range(iterations):
  tempdir=firstdir #Start with the saved first direction, will iterate.
  for i in range(2**(j+1)+1):
    if i%2:
      segments.insert(i,[None,None,(i/2+1)%2])
    if i:
      if segments[i-1][2] and segments[i][2]: tempdir=(tempdir-2)%8
      if not segments[i-1][2] and not segments[i][2]: tempdir=(tempdir+2)%8
    segments[i][0]=directions[tempdir]
    segments[i][1]=steplength
  print(str(segments))
  firstdir =(firstdir +1)%8
  firststep=(firststep+1)%8
  if j%2:
    steplength/=2
