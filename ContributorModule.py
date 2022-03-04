# Class for contributors
class Contributor:
    def __init__(self):
        self.name = ""
        self.skills = {}
        # Flags used by the simulation
        self.available = True
        self.levelUp = False
    
    # Levels up specified skill by 1 point
    def upgrade_skill(self, skill):
        self.skills[skill] += 1
    
    # Checks if this contributor has the specified skill
    def has_skill(self, skill):
        return(skill in self.skills)