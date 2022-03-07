from TeamProjectMatcher import findTeam
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
                # DFS has to replace current findTeam code.
                # new field "day_started" in Project object, it will be used to later sort the completedProjects
                # list. It has to be set to the day the project started
                findTeam(contributors, projects)

        for index,project in enumerate(workingProjects):
            project.days -= 1
            
            if project.days == 0:
                # Make its contributors available again
                for worker in project.contributors:
                    worker.available = True
                # move from working to completed
                # !!!!!!!!! mut change to put completed with appropriate order
                completedProjects(workingProjects.pop(index))
                
        time += 1

        if workingProjects == []:
            break
    
    # sorts the completed projects by the day they started, so that they are correctly ordered in output file
    sorted_completedProjects = sorted(completedProjects, key= lambda x : x.day_started)
    return(completedProjects)