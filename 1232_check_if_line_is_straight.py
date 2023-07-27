
def checkSlope(coords):
    slope = (coords[0][1] - coords[1][1]) / (coords[0][0] - coords[1][0]) 
    
    # Now compare the rest 
    for coord in coords[2:]:
        if slope != (coords[0][1] - coord[1]) / (coords[0][0] - coord[0]): 
            return False
    return True 


print(checkSlope([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]))  
print(checkSlope([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]))  