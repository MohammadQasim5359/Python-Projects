import math
def get_next_point(thestep):

    x_coord = int(input("Input x%d coord "%thestep))
    y_coord = int(input("Input y%d coord "%thestep))
    coordinate = (x_coord,y_coord)
    
    return coordinate
    
def cal_distance(coordinate1,coordinate2):
    distance = math.sqrt((coordinate2[0]-coordinate1[0])**2 + (coordinate2[1]-coordinate1[1])**2)

    return distance
    
def main():
    oldcoordinate = (0,0)
    theswitch = 0
    stepcount = 1
    distancelist = []
    oldcoordinatelist = []
    newcoordinatelist = []
    distanceliststep = 1
    coordinatestep = 0
    while theswitch == 0:
        
         newcoordinate = get_next_point(stepcount)
         if newcoordinate == (999,999):
             theswitch = 1
             continue
         oldcoordinatelist.append(str(oldcoordinate))
         newcoordinatelist.append(str(newcoordinate))
         thedistance = cal_distance(oldcoordinate, newcoordinate)
         distancelist.append(thedistance)
         
         
         oldcoordinate = newcoordinate
         
         stepcount = stepcount + 1
         
    total = sum(distancelist)
    print("-"*70)
    
    for thedistance in distancelist:
        print("Step {0}: Traveled from {1:^13} to {2:^13} {3:>6.2f} units".format(distanceliststep,oldcoordinatelist[coordinatestep], newcoordinatelist[coordinatestep] ,thedistance))
        distanceliststep = distanceliststep + 1
        coordinatestep = coordinatestep + 1
        
    print("-"*70)
          
    print("Total distance traveled by the robot is: {:.2f} Units.".format(total))
    

if __name__ == "__main__":
    print("Enter 999 in both x and y to end program")
    main()

    