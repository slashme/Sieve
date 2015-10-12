#Six directions of movement to enumerate points on stretched hex grid
directions=[
[[ 1,-1],[ 1, 1]]
[[ 0, 2],[ 1, 1]]
[[ 0, 2],[-1, 1]]
[[-1,-1],[-1, 1]]
[[-1,-1],[ 0,-2]]
[[ 1,-1],[ 0,-2]]
]
#Base repeat counts of movement directions to enumerate points for Ulam spiral on triangular tiling.
#For each additional ring, do each movement one extra time.
baserepeat=[0,0,1,0,1,1]
