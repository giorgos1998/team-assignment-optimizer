
# calculates the importance of each projects and returns a sorted list by importance
def scoreProjects(projects, data, time):
    for index,project in enumerate(projects):
        score = project.get_current_score(time)
        # if the project's score is <= 0, then it is useless to us, so we delete the project to save time from future permutations
        if score <= 0:
            projects.pop(index)
            continue
        norm_score = data.projects.normalize_score(project.score)
        norm_days = data.projects.normalize_days(project.days)
        norm_skills = data.projects.normalize_skills(len(project.skills))
        # In later versions, the significance of the required skills will also be taken into account
        project.importance = norm_score * 0.5 + (1 - norm_days) * 0.3 + (1 - norm_skills) * 0.2
    
    # Untested
    sorted_projects = sorted(projects, key= lambda x: x.importance)
    return(sorted_projects)