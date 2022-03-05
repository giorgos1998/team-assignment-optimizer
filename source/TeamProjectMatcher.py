# Helper function that returns project's score
def scoreFunc(project):
    return project.get_score()

# Helper function that sorts projects list based on score
def sortProjects(projects):
    projects.sort(key=scoreFunc)

# Matches contributors to projects that fulfill required skills
def findTeams(contributors, projects):

    completed_projects = 0

    for project in projects:
        # if current project has already a team, skip it
        if project.working:
            continue

        curTeam = []

        for skillList in project.skills:
            for contributor in contributors:
                # Check if selected contributor is suitable for the selected position
                if contributor.available and contributor.has_skill(skillList[0]):
                    if contributor.skills[skillList[0]] == skillList[1]:
                        # Found suitable contributor
                        curTeam.append(contributor)
                        # Contributors of the same level as the given task will level up
                        contributor.levelUp = True
                        break
                    elif contributor.skills[skillList[0]] > skillList[1]:
                        # Found suitable contributor
                        curTeam.append(contributor)
                        break
                
            else:
                # Cannot satisfy current project position
                # Reset level ups for the unfinished team
                for contributor in curTeam:
                    contributor.levelUp = False
                break
        
        # Check that all positions of the current project are filled
        if len(curTeam) == len(project.skills):
            # Assign team to current project
            project.contributors = curTeam
            # Project will be finished, add it to the count
            completed_projects += 1
            # Mark project as ongoing
            project.working = True
            # Mark workers as unavailable
            for worker in project.contributors:
                worker.available = False

    return (completed_projects)