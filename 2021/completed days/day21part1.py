position1 = 5
position2 = 6
pointsplayer1 = 0
pointsplayer2 = 0

dr = [1,2,3]
totalrolls = 0
winner = False
roll = 0

while winner is False:
    # Check that every position is existant 
    dr[0] = dr[0] % 100
    dr[1] = dr[1] % 100
    dr[2] = dr[2] % 100
    if dr[0] == 0:
        dr[0] = 100
    if dr[1] == 0:
        dr[1] = 100
    if dr[2] == 0: 
        dr[2] = 100
    # Calculate roll total
    roll = dr[0] + dr[1] + dr[2]
    # Move three positions along for next roll 
    dr[0] += 3
    dr[1] += 3
    dr[2] += 3
    # Add three to total amount of rolls 
    totalrolls += 3    
    position1 = position1 + roll 
    position1 = position1 % 10
    if position1 == 0 : position1 = 10
    pointsplayer1 += position1
    # Check to see if there's a winner 
    if pointsplayer1 >= 1000:
        print(pointsplayer2 * totalrolls)
        winner = True
        break
    dr[0] = dr[0] % 100
    dr[1] = dr[1] % 100
    dr[2] = dr[2] % 100
    if dr[0] == 0:
        dr[0] = 100
    if dr[1] == 0:
        dr[1] = 100
    if dr[2] == 0: 
        dr[2] = 100
    roll = dr[0] + dr[1] + dr[2]
    dr[1] += 3
    dr[2] += 3
    dr[0] += 3
    totalrolls += 3
    position2 = position2 + roll
    position2 = position2 % 10
    if position2 == 0 : position2 = 10
    pointsplayer2 += position2
    if pointsplayer2 >= 1000:
        print(pointsplayer1 * totalrolls)
        winner = True