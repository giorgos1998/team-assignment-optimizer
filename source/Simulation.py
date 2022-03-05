from TeamProjectMatcher import findTeams

# Simulates the contributors working on projects
def sim(contributors, projects):
    time = 0
    completedProjects = []
    workingProjectExists = True

    # Sim will run until the projects that can be completed run out
    while workingProjectExists:
        # At the start of the day, fill as many projects as possible.
        # Note that ongoing projects will not be affected by this
        findTeams(contributors, projects)
        workingProjectExists = False

        for index,project in enumerate(projects):

            if project.working:
                workingProjectExists = True
                # If a project is been worked today, remove 1 of its required days
                project.days -= 1
                
                if project.days == 0:
                    # When a project is completed, add it to the completed list
                    completedProjects.append(projects.pop(index))
                    # Make its contributors available again
                    for worker in project.contributors:
                        worker.available = True
                
        time += 1
    
    return(completedProjects)