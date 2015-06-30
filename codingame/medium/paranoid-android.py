# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# nbFloors: number of floors
# width: width of the area
# nbRounds: maximum number of rounds
# exitFloor: floor on which the exit is found
# exitPos: position of the exit on its floor
# nbTotalClones: number of generated clones
# nbAdditionalElevators: ignore (always zero)
# nbElevators: number of elevators
nbFloors, width, nbRounds, exitFloor, exitPos, nbTotalClones, nbAdditionalElevators, nbElevators = [int(i) for i in input().split()]
posOfElevator = {exitFloor: exitPos}
floorsDone = set()
for i in range(nbElevators):
    # elevatorFloor: floor on which this elevator is found
    # elevatorPos: position of the elevator on its floor
    elevatorFloor, elevatorPos = [int(i) for i in input().split()]
    posOfElevator[elevatorFloor] = elevatorPos

while 1:
    cloneFloor, clonePos, direction = input().split()
    cloneFloor = int(cloneFloor)
    clonePos = int(clonePos)

    if direction == 'NONE' or cloneFloor in floorsDone:
        print("WAIT")
        continue

    pos = posOfElevator[cloneFloor]
    if direction == 'RIGHT' and pos < clonePos:
        floorsDone.add(cloneFloor)
        print("BLOCK")
    elif direction == 'LEFT' and pos > clonePos:
        floorsDone.add(cloneFloor)
        print("BLOCK")
    else:
        print("WAIT")
