#team details
teams = ["Liverpool", "Spurs", "Southampton", "Leicester", "Everton", "Man Utd", "Chelsea", "West Ham", "Man City", "Wolves", "Aston Villa", "Crystal Palace","Leeds", "Newcastle", "Arsenal", "Brighton", "Burnley", "Fulham", "West Brom", "Sheffield"]

scored = [36,25,25,24,23,22,26,21,18,13,21,19,22,16,11,15,6,12,10,7]

conceded = [19,12,18,17,18,19,14,16,12,17,13,25,24,21,16,21,18,22,26,24]

#method to calculate goal difference and put it into a list
def goalDifference(scored,conceded):
    
    goal_difference = []
    
    for i in range(20):
        
        name = teams[i]
        gs = scored[i]
        gc = conceded[i]
        #calculate difference
        gd = gs -gc
        #put details to list
        goal_difference.append([name, gd])
        
    return goal_difference
    
gsr = goalDifference(scored,conceded)
#sort goal difference method
def diffTable(gsr):
    
    table = []
    
    for x in gsr:
        
        name = x[0]
        difference = x[1]
        toadd = [name, difference]
        table.append(toadd)
    
    table = sorted(table, key=lambda x: x[1], reverse=True)
    return table
        
lineprint = diffTable(gsr)
#method that prints goal difference rank line by line
def linebyline(lineprint):
    
    for x in lineprint:
        
        print(x[0] + " " + str(x[1]))
        
        
linebyline(lineprint)






