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
                # DFS goes here
                findTeam(contributors, projects)

        for index,project in enumerate(workingProjects):
            project.days -= 1
            
            if project.days == 0:
                # Make its contributors available again
                for worker in project.contributors:
                    worker.available = True
                # move from working to completed
                completedProjects(workingProjects.pop(index))
                
        time += 1

        if workingProjects == []:
            break
    
    return(completedProjects)