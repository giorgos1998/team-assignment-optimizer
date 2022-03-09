# Class for projects
class Project:
    def __init__(self):
        self.name = ""
        self.days = 0
        self.day_started = -1
        self.score = 0
        self.deadline = 0
        # skills = [ [skill name, required level, mentored status], ... ]
        self.skills = []
        self.contributors_count = 0
        self.contributors = []
        self.importance = 0
        # Flag used by the simulation
        self.working = False
    
    def get_current_score(self, current_days):
        return(self.score + min(0, self.deadline - self.days - current_days))
    
    # To string method, use print(project) to print
    def __str__(self):
        return ("\n\nProject name: " + self.name +
        "\n Days: " + str(self.days) +
        "\n Score: " + str(self.score) +
        "\n Deadline: " + str(self.deadline) +
        "\n Skills: " + ", ".join([skill[0] + " " + str(skill[1]) for skill in self.skills]) +
        "\n No of contributors: " + str(self.contributors_count) +
        "\n Contributors: " + ", ".join([contributor.name for contributor in self.contributors]))

    # To string representer, used when print([project, ...]) or similar is called
    def __repr__(self):
        return str(self)
