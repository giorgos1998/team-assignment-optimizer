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
        # Flag used by the simulation
        self.working = False
    
    # Calculates how beneficial completing this project will be.
    # Method uses the points earned by completing the project and the days it
    # needs to be completed.
    def get_score(self, w1, w2):
        return((w1*self.score + w2/self.deadline)/(w1+w2))
    
    # Calculates if the project will award points if it starts in a specific day
    def get_time_score(self, current_days):
        return(max(0, self.deadline - current_days - self.days))
    
    # To string method, use print(project) to print
    def __str__(self):
        return ("Project name: " + self.name +
        "\n Days: " + str(self.days) +
        "\n Score: " + str(self.score) +
        "\n Deadline: " + str(self.deadline) +
        "\n Skills: " + ", ".join([skill[0] + " " + str(skill[1]) for skill in self.skills]) +
        "\n No of contributors: " + str(self.contributors_count) +
        "\n Contributors: " + ", ".join([contributor.name for contributor in self.contributors]))

    # To string representer, used when print([project, ...]) or similar is called
    def __repr__(self):
        return str(self)
