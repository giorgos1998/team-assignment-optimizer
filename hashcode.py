import os
import pathlib

path_results = os.path.join(pathlib.Path().absolute(), "input_data")
files = [f for f in os.listdir(path_results) if os.path.isfile(os.path.join(path_results, f))]

# Class for projects
class Project:
    def __init__(self):
        self.name = ""
        self.days = 0
        self.score = 0
        self.deadline = 0
        self.skills = []
        self.contributors_count = 0
        self.contributors = []
        self.working = False
    
    def get_score(self, w1, w2):
        return((w1*self.score + w2/self.deadline)/(w1+w2))
    
    def get_deadline(self, current_days):
        return(self.deadline - (current_days + self.days) >= self.score)
    
    def print(self):
        print("Project name: " + self.name +
        "\n Days: " + str(self.days) +
        "\n Score: " + str(self.score) +
        "\n Deadline: " + str(self.deadline) +
        "\n Skills: " + ", ".join([skill[0] + " " + str(skill[1]) for skill in self.skills]) +
        "\n No of contributors: " + str(self.contributors_count) +
        "\n Contributors: " + ", ".join([contributor.name for contributor in self.contributors]))

# class for contributors
class Contributor:
    def __init__(self):
        self.name = ""
        self.skills = {}
        self.available = True
        self.levelUp = False
    
    def upgrade_skill(self, skill):
        self.skills[skill] += 1
    
    def has_skill(self, skill):
        return(skill in self.skills)

# method to read file and get data for all contributors and projects
def read_file(file_name):
    # initialize empty lists of project and contributors
    projects = []
    contributors = []

    #open file of contributors and projects
    file1 = open("input_data/" + file_name, 'r')

    # get number of contributors and projects
    keys = file1.readline().strip().split(" ")
    contributors_num= int(keys[0])
    projects_num= int(keys[1])

    #get data for each contributor
    for i in range (0,contributors_num):
        # Get next line from file
        line = file1.readline().strip().split(" ")
        line[1]=int(line[1])
        # initialize new contributor and fill name and skills
        contributor = Contributor()
        contributor.name = line[0]
        for j in range(0,line[1]):
            subline = file1.readline().strip().split(" ")
            contributor.skills[subline[0]] = int(subline[1])
        # add new contributor to the list of contributors
        contributors.append(contributor)

    for k in range (0,projects_num):
        # Get next line from file
        line = file1.readline().strip().split(" ")
        line[-1]=int(line[-1])
        # initialize new project and fill with data
        project = Project()
        project.name = line[0]
        project.days = int(line[1])
        project.score = int(line[2])
        project.deadline = int(line[3])
        project.contributors_count = line[4]
        for l in range(0,(line[-1])):
            subline = file1.readline().strip().split(" ")
            project.skills.append([subline[0], int(subline[1]), False])
        # add new project to the list of projects
        projects.append(project)

    # we are done with the file, we free it from memory
    file1.close()

    return([contributors, projects])

# Returns project's score
def scoreFunc(project):
    return project.get_score()

# Sorts projects list based on score
def sortProjects(projects):
    projects.sort(key=scoreFunc)

def findTeams(contributors, projects):
    completed_projects = 0
    for project in projects:
        if project.working:
            continue
        curTeam = []

        for skillList in project.skills:
            for contributor in contributors:
                if contributor.available and contributor.has_skill(skillList[0]):
                    if contributor.skills[skillList[0]] == skillList[1]:
                        # Found suitable contributor
                        curTeam.append(contributor)
                        contributor.levelUp = True
                        break
                    elif contributor.skills[skillList[0]] > skillList[1]:
                        # Found suitable contributor
                        curTeam.append(contributor)
                        break
                
            else:
                #Cannot satisfy current project position
                for contributor in curTeam:
                    contributor.levelUp = False
                break
        
        
        if len(curTeam) == len(project.skills):
            project.contributors = curTeam
            completed_projects += 1
            project.working = True
            for worker in project.contributors:
                worker.available = False

    return (completed_projects)

def sim(contributors, projects):
    time = 0
    completedProjects = []
    workingProjectExists = True

    while workingProjectExists:
        findTeams(contributors, projects)
        workingProjectExists = False
        for index,project in enumerate(projects):
            if project.working:
                workingProjectExists = True
                project.days -= 1
                
                if project.days == 0:
                    completedProjects.append(projects.pop(index))
                    for worker in project.contributors:
                        worker.available = True
                
        time += 1
    
    return(completedProjects)

for file in files:
    results = read_file(file)
    completed = sim(results[0], results[1])

    output = open(file + "_result.txt", "w")

    output.write(str(len(completed)) + "\n")
    for project in completed:
        output.write(project.name + "\n")
        output.write(" ".join(contributor.name for contributor in project.contributors) + "\n")

    output.close()