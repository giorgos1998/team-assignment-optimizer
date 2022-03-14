from TeamProjectMatcher import findTeam, findTeamDFS
from ProjectManagement import scoreProjects

# Simulates the contributors working on projects
def sim(contributors, projects, data):
    time = 0
    completedProjects = []
    workingProjects = []

    # Sim will run until the projects that can be completed run out
    while True:
        if projects != []:
            projects = scoreProjects(projects, data, time)
            
            for project in projects:
            
                # if current project has already a team, skip it
                if(project.working):
                    continue
                    
                # DFS 
                teams = findTeamDFS(contributors, project)
                #print(project.name,"teams :",teams)
                
                # if we found any teams pick the best
                solution = []
                if(len(teams)>0):
                    for contributor,skill in zip(teams[-1][:-1],project.skills):
                        solution.append(contributor[0])
                        if(skill[1] >= contributor[0].skills[skill[0]]):
                            contributor[0].skills[skill[0]] += 1
                    #print("solution :", solution)
                    # also set the project fields to working status
                    project.contributors = solution
                    project.working = True
                    for contributor in project.contributors:
                        contributor.available = False                        
                    workingProjects.append(project)
        
        for index,project in enumerate(workingProjects):
            project.days -= 1
            
            if project.days == 0:
                # Make its contributors available again
                for contributor in project.contributors:
                    contributor.available = True
                # move from working to completed
                # !!!!!!!!! mut change to put completed with appropriate order
                completedProjects.append(workingProjects.pop(index))
                
        time += 1
        
        #print("time ",time,"##############################33\n")
        if time>data.latest_possible_date:
            print("out of time")
            break
    
    # sorts the completed projects by the day they started, so that they are correctly ordered in output file
    sorted_completedProjects = sorted(completedProjects, key= lambda x : x.day_started)
    return(completedProjects)
