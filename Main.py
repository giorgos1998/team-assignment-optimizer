import os
import pathlib
from FileParser import read_file
from Simulation import sim
from OutputGenerator import writeToFile

path_results = os.path.join(pathlib.Path().absolute(), "input_data")
files = [f for f in os.listdir(path_results) if os.path.isfile(os.path.join(path_results, f))]

for file in files:
    contributors, projects = read_file(file)
    completedProjects = sim(contributors, projects)
    writeToFile(file, completedProjects)
