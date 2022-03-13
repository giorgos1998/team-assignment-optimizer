

class SimulationData():
    
    def __init__(self):
        self.contributors = ContributorsData()
        self.projects = ProjectsData()
        self.skills = SkillsData()
        self.latest_possible_date = 0

        self.number_of_skills_per_project = {}
        self.number_of_skills_per_contributor = {}
        self.number_of_skills_occurence = {}
        self.skills_currently_needed = {}

    def change_latest_date(self, number):
        if number > self.latest_possible_date:
            self.latest_possible_date = number
    
    

class ContributorsData():
    
    def __init__(self):
        self.number = 0
        self.level_ups = 0
        # data about how many contributors were working during the simulation
        self.sum_working_daily = 0 # needed to calculate average
        self.min_contributors_working = float("inf")
        self.max_contributors_working = 0
        self.average_contributors_working = 0
        # data about contributors skills
        # self.start_skill_levels = 0
        # self.finish_skills_levels = 0
        # self.skills_gain = 0
        
    def increase_level_ups(self, number):
        self.level_ups += number

    def new_day_data(self, number):
        self.sum_working_daily += number
        if number < self.min_contributors_working:
            self.min_contributors_working = number
        if number > self.max_contributors_working:
            self.max_contributors_working = number
    
    def get_average_working(self, days):
        self.average_contributors_working = self.sum_working_daily / days
        return(self.average_contributors_working)

class ProjectsData():
    
    def __init__(self):
        self.number = 0
        self.completed = 0
        # data about the score
        self.min_score = float("inf")
        self.max_score = 0
        self.average_score = 0
        self.score_achieved = 0
        self.max_theoretical_score = 0
        # data about the required days
        self.sum_days = 0 # needed to calculate average
        self.min_days = float("inf")
        self.max_days = 0
        self.average_days = 0
        # data about required skills
        self.sum_skills = 0 # needed to calculate average
        self.min_skills = float("inf")
        self.max_skills = 0
        self.averages_skills = 0
    
    def add_new_project(self, line):
        self.new_days_data(int(line[1]))
        self.new_score_data(int(line[2]))
        self.new_skills_data(line[-1])

    def new_score_data(self, number):
        self.max_theoretical_score += number
        if number < self.min_score:
            self.min_score = number
        if number > self.max_score:
            self.max_score = number
    
    
    def increase_score(self, number):
        self.score_achieved += number
    
    def get_average_score(self):
        self.average_score = self.max_theoretical_score / self.number
        return(self.average_score)
    
    def new_days_data(self, number):
        self.sum_days += number
        if number < self.min_days:
            self.min_days = number
        if number > self.max_days:
            self.max_days = number
    
    def get_average_days(self):
        self.average_days = self.sum_days / self.number
        return(self.average_days)
    
    def new_skills_data(self, number):
        self.sum_skills += number
        if number < self.min_skills:
            self.min_skills = number
        if number > self.max_skills:
            self.max_skills = number
    
    def get_average_skills(self):
        self.averages_skills_required = self.sum_skills / self.number
        return(self.averages_skills_required)
    
    def normalize_days(self, days):
        return((days - self.min_days) / (self.max_days - self.min_days))

    def normalize_score(self, score):
        return((score - self.min_score) / (self.max_score - self.min_score))
    
    def normalize_skills(self, skills):
        return((skills - self.min_skills) / (self.max_skills - self.min_skills))

    def print_days_data(self):
        print("Min days: " + str(self.min_days) + "\nMax days: " + str(self.max_days) + "\nAverage days: " + str(self.get_average_days()))
    
    def print_score_data(self):
        print("Min score: " + str(self.min_score) + "\nMax score: " + str(self.max_score) + "\nAverage score: " + str(self.get_average_score()))
    
    def print_skills_data(self):
        print("Min skills: " + str(self.min_skills) + "\nMax skills: " + str(self.max_skills) + "\nAverage skills: " + str(self.get_average_skills()))

# for future development
class SkillsData():
    
    def __init__(self):
        self.skills = {}
    
    def add_contributor_skill(self, subline):
        skill = subline[0]
        level = int(subline[1])
        if skill not in self.skills:
                self.skills[skill] = {}
            
        if level not in self.skills[skill]:
            self.skills[skill][level] = 1
        else:
            self.skills[skill][level] += 1