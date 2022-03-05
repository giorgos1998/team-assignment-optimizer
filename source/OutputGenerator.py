import os

# Creates a file that contains the team assignment for each completed project
def writeToFile(file, completedProjects):
    file_path = os.path.join("output_data", file[0:-7] + "_result.txt")
    output = open(file_path, "w")
    # First line contains the number of completed projects
    output.write(str(len(completedProjects)) + "\n")

    # The rest of the lines contain the project name and its contributors
    for project in completedProjects:
        output.write(project.name + "\n")
        output.write(" ".join(contributor.name for contributor in project.contributors) + "\n")

    output.close()