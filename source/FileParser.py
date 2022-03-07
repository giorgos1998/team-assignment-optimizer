from dataclasses import dataclass
from ContributorModule import Contributor
from ProjectModule import Project
from DataModule import SimulationData
import os

# Method that reads input file and gets data for all contributors and projects
def read_file(file_name):
    print("reading", file_name)
    dataCollection = SimulationData()
    # Initialize empty lists of project and contributors
    projects = []
    contributors = []

    # Open file of contributors and projects
    file = open(os.path.join("input_data", file_name), 'r')

    # Get number of contributors and projects
    keys = file.readline().strip().split(" ")
    contributors_num= int(keys[0])
    projects_num= int(keys[1])
    dataCollection.contributors.number = contributors_num
    dataCollection.projects.number = projects_num

    # Get data for each contributor
    for i in range (0,contributors_num):

        line = file.readline().strip().split(" ")
        line[1]=int(line[1])

        # Initialize new contributor and fill name and skills
        contributor = Contributor()
        contributor.name = line[0]
        for j in range(0,line[1]):
            subline = file.readline().strip().split(" ")
            contributor.skills[subline[0]] = int(subline[1])

        # Add new contributor to the list of contributors
        contributors.append(contributor)

    # Get data for each project
    for i in range (0,projects_num):

        line = file.readline().strip().split(" ")
        line[-1]=int(line[-1])

        # Initialize new project and fill it with data
        project = Project()
        project.name = line[0]
        project.days = int(line[1])
        project.score = int(line[2])
        project.deadline = int(line[3])
        project.contributors_count = line[4]

        dataCollection.projects.new_days_data(project.days)
        dataCollection.projects.new_score_data(project.score)
        dataCollection.projects.new_skills_data(line[-1])
        dataCollection.change_latest_date(project.deadline + project.days)
        for j in range(0,(line[-1])):
            subline = file.readline().strip().split(" ")
            project.skills.append([subline[0], int(subline[1]), False])
        
        # Add new project to the list of projects
        projects.append(project)
    print("Latest possible day reachable: " + str(dataCollection.latest_possible_date))
    dataCollection.projects.print_days_data()
    print("Max theoretica score: " + str(dataCollection.projects.max_theoretical_score))
    dataCollection.projects.print_score_data()
    dataCollection.projects.print_skills_data()
    file.close()

    return([contributors, projects, dataCollection])