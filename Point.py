class Point:
    def __init__(self,user_passed_conceded, user_passed_goals):
        self.avg_conceded_by_team = user_passed_conceded
        self.avg_goals_by_team = user_passed_goals
    def __str__(self):
        return ("(" + str(self.avg_conceded_by_team) + \
        ", " + str(self.avg_goals_by_team) + ")")