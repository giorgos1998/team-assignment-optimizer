import copy

# Helper function that returns project's score
def scoreFunc(project):
    return project.get_score()

# Helper function that sorts projects list based on score
def sortProjects(projects):
    projects.sort(key=scoreFunc)

# Matches contributors to projects that fulfill required skills
def findTeam(contributors, projects):

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
    
# Finds all possible teams for one project and their scores    
def findTeamDFS(contributors, project):
    # initially no solutions
    solutions = []

    # make initial search front, contains all contributor-skill pair we have in contributors
    front = []
    for contributor in contributors:
        for skill in contributor.skills:
            front.append((contributor,skill))
    
    # run initial iteration of DFS, fills solutions list
    dfs(front, [], project.skills, solutions, contributors)
    
    # sort the solutions
    solutions.sort(key=lambda x:x[-1])
    
    #print(solutions)
    
    # return teams
    return solutions

# Recursive DFS will add every possible team it finds in solutions
def dfs(neibors, solution, needed, solutions, contributors):

    # if we reached a leaf max depth
    if (len(solution)==len(needed)):
        # keep a copy of needed because we are going to modify it
        temp_needed = copy.deepcopy(needed)
        # initialize score
        score=0
        # inadequate skill level(s) flag 
        error = False
        # for every contributor-skill pair in our solution
        for i,contr in enumerate(solution):
            # for every other skill of this solution and it's not mentored
            for j,skill in enumerate(temp_needed):
                if(i!=j and not skill[2]):
                    # if the contributor can mentor this skill
                    if skill in list(contr[0].skills.keys()):
                        if(contr.skills[skill]>skill[1]):
                            # mentor it
                            temp_needed[j][1] -= 1
                            temp_needed[j][2] = True
        
        # check that contributors in solution meet the skill requirements
        # this happebs here, after other contributors have mentored what they can
        for contr,skill in zip(solution,temp_needed):
            # if the skill level of contributor is lower than the skill level
            # then solution is invalid, can't work here even if mentored
            if(contr[0].skills[contr[1]] < skill[1]):
                error = True
                score = -1
                break
            # else they can
            else:
                score += 1
            # if they level up increase score
            if(contr[0].skills[contr[1]] <= skill[1]+1):
                score += 1
        
        # more bias ?
        if not error:
            score+=1
        
        # add this to possible solutions if valid
        if(score>0):
            solutions.append(solution+[score])
        
        return
    
    # not reached a leaf yet
    for n in neibors:
        childs = []
        
        # skip next contributor if skill is incompatible
        # we don't check skill level here because we don't know what will be mentored
        # we can only check skill compatibility 
        if(n[1]!=needed[len(solution)][0]):
            continue
        # else add them to the solution
        solution.append(n)
        # find the children of this node, for every contributor
        for contributor in contributors:
            flag = False
            # if they are already in the solution don't add them
            for contr in solution:
                if contributor.name==contr[0]:
                    flag = True
                    break
            if flag:
                continue
            # else add all their skills as childern to this node
            for skill in contributor.skills:
                childs.append((contributor,skill))
        # run dfs recursively
        dfs(childs, solution, needed, solutions, contributors)
        # once returned remove current node from solution
        solution.pop()

    return