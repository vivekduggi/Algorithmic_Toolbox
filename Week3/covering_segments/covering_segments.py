# Uses python3




## ==================================================================================================================== ##






# Greedy function to calculate minimum number of points to cover all segments
def optimal_points(segments):
    points = []
    
    # sorting segments list by its end point in ascending order

    segments = sorted(segments, key = lambda x:x[1])

 
    count = 0
    i = 0
  
    
    while(i < len(segments)):
        points.append(segments[i][1])
        pos = segments[i][1]        
        i += 1
        count += 1
        print(points)         
   
        while (i < len(segments) and (pos >= segments[i][0] and pos <= segments[i][1])):
            i += 1

 
            
    return(points)
    

n, *data = map(int, input().split(" "))
segments = list(zip(data[::2],data[1::2]))
points = optimal_points(segments)
print(len(points))
for p in points:
    print(p, end=' ')
