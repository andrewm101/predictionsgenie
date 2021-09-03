from bs4 import BeautifulSoup
import requests
import math
from Point import Point
from My_Dictionary import My_Dictionary

class PredictionsGenie:
    def poisson(self, lambda_val, k):
        return math.pow(lambda_val, k) * math.exp(-1 * lambda_val) / math.factorial(k)
    
    def scraper(self, soup, home_away_classifier):
        table = soup.find("table", attrs={"id" : home_away_classifier})
        table_body = table.find("tbody")
        team_data = table_body.find_all("td")

        i = 0
        for index in team_data:
            del team_data[1 + 3 * i: 7 + 3 * i]
            team_data[i] = str(index)[4 : (len(team_data[i]) - 6)]
            i += 1
        return team_data    

    def calculations(self, avg_goals_home, avg_goals_away, avg_goals_home_team,\
    avg_conceded_away, avg_goals_away_team, avg_conceded_home_team):
        avg_conceded_by_home = avg_goals_away
        avg_conceded_by_away = avg_goals_home
        avg_goals_user_home = avg_goals_home_team
        home_attack_strength = avg_goals_user_home / avg_goals_home

        #Number of goals conceded away last season 
        #by the away team / number of away games played.
        avg_conceded_user_away = avg_conceded_away
        away_defensive_strength = avg_conceded_user_away / avg_conceded_by_away

        expected_home_goals = home_attack_strength * away_defensive_strength * avg_goals_home

        avg_goals_user_away= avg_goals_away_team
        away_attack_strength =  avg_goals_user_away/ avg_goals_away
        avg_conceded_user_home = avg_conceded_home_team
        home_defensive_strength = avg_conceded_user_home / avg_goals_away

        expected_away_goals = away_attack_strength * home_defensive_strength * avg_goals_away
                                            
        # using the Poisson now...
        probabilities_Manchester_United = []
        probabilities_Arsenal = []
        probabilities_Map = My_Dictionary()
        print("Format of score " + "(Home goals, Away goals)")
        for manchestergoals in range(5):
            poisson_manchester = self.poisson(expected_home_goals, manchestergoals)
            probabilities_Manchester_United.append(poisson_manchester)
            for arsenalgoals in range(5):
                poisson_arsenal = self.poisson(expected_away_goals, arsenalgoals)
                if(arsenalgoals == 0.0):
                    probabilities_Arsenal.append(poisson_arsenal)
                print("(" + str(manchestergoals) + ", " + str(arsenalgoals) + ")" + \
                str(poisson_manchester * poisson_arsenal * 100) + "%")
                probabilities_Map.add("(" + str(manchestergoals) + ", " + str(arsenalgoals) + ")", str(poisson_manchester * poisson_arsenal * 100))
        return probabilities_Map
    
    def dictionary_builder(self, team_data):
        data_mappings = My_Dictionary()
        total_goals_scored = 0
        for x in range(0, 57, 3):
            team_name = team_data[x]
            point_data = Point(team_data[x + 1], team_data[x + 2])
            total_goals_scored += int(team_data[x + 1])
            data_mappings.add(team_name, point_data)
        data_mappings.add("total", total_goals_scored)
        return data_mappings
    
    def getPredictions(self, home, away):
        url = 'http://1x2stats.com/en-us/ENG/2020/Premier-League/table-home-away/'
        req = requests.get(url)
        soup = BeautifulSoup(req.text, 'html.parser') 
        home_team_data = self.scraper(soup, "homeClassification")
        away_team_data = self.scraper(soup,"awayClassification")
        home_mappings = self.dictionary_builder(home_team_data)
        away_mappings = self.dictionary_builder(away_team_data)

        print(home_mappings)
        print(away_mappings)
        
        avg_goals_home = float(home_mappings["total"]) / 380.0
        avg_goals_away = float(away_mappings["total"]) /380.0        
        home_Point = home_mappings[home]
        avg_conceded_user_home = float(home_Point.avg_conceded_by_team) / 19
        avg_goals_user_home = float(home_Point.avg_goals_by_team) / 19

        away_Point = away_mappings[away]
        avg_conceded_user_away = float(away_Point.avg_conceded_by_team) / 19
        avg_goals_user_away = float(home_Point.avg_goals_by_team) / 19
    
        avg_goals_home = home_mappings["total"] / 380
        avg_goals_away = away_mappings["total"] / 380   
    
        return self.calculations(avg_goals_home, avg_goals_away, avg_goals_user_home,
        avg_conceded_user_away, avg_goals_user_away, avg_conceded_user_home) 
