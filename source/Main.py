import os
import logging
from FileParser import read_file
from Simulation import sim
from OutputGenerator import writeToFile

logging.basicConfig(level=logging.DEBUG, filename="log.txt", format='%(asctime)s- %(levelname)s- %(message)s')
input_dir = "input_data"

if __name__ == "__main__":
    # check if the directory input_data exists, else exit
    if not (os.path.exists(input_dir) and os.path.isdir(input_dir)):
        logging.error("Directory \'input_data\' not found. Exiting...")
        exit(-1)

    # get all file names in input_directory
    files = [f for f in os.listdir("input_data") if os.path.isfile(os.path.join("input_data", f))]

    # check if the directory input_data exists, else create it
    if not (os.path.exists("output_data") and os.path.isdir("output_data")):
        logging.info("Directory \'output_data\' not found, attempting to create it...")
        try:
            os.mkdir("output_data")
        except Exception :
            logging.error("Could not create \'output_data\' directory. Exiting...")
            exit(-2)

    # run the simulation for each input file and save the results in the appropriate output file
    for file in files:
        contributors, projects, data = read_file(file)
        completedProjects = sim(contributors, projects, data)
        writeToFile(file, completedProjects)