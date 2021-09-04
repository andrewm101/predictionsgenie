# PredictionsGenie

Check it out at : https://predictionsgenie.herokuapp.com/

  # Usage
    Buttons:
      Reset Page: Resets team selection and reverts page back to original dislpay
      Calculate Probabilities: Returns a table of results, button only respons only when
      a home and away team are selected
      
      Example: For an upcoming match between Leeds (Home) and Arsenal (Away), the goal of this 
      program is to provide the user with data representing the probability of a final score
      (i.e whats the probability that the final score is (2, 1)? )
      
      1) Hover over desired team and then drag and drop each team into their respective boxes
![image](https://user-images.githubusercontent.com/71049168/132085282-a2848aac-9faa-4ffe-a3b6-6d03ab78019d.png)

      2) Drag each team above the corresponding box, doing so will prompt either box to display
         a red border around its edges to communicate that the current selection is in the drop zone 
![Screenshot (16)](https://user-images.githubusercontent.com/71049168/132085340-a8f52456-fdcb-4c4b-879a-81bc3ab3c6db.png)
      3) When both teams have been dragged and dropped, click "calculate probabilities". 
         A green table will then appear displaying probabilities of a final score being achieved.
         (i.e the match in our example, has the a 9.25% chance of having a final score of (1 vs 0) or (0 vs 1)).
![image](https://user-images.githubusercontent.com/71049168/132085552-b567d1e5-c6c8-4999-ac78-20af11f8727b.png)

# About

**Front End** - Bootstrap | HTML | CSS | JavaScript
**Back End**  - Python | Beautiful Soup 4 | Flask
Hosting service: Heroku/Salesforce

Math behind the calculations uses the Possion Distribution to estimate the probabilites by using data from the
2020/2021 Premier League season. For more information on the Poission Distribution follow the links below
* https://www.itl.nist.gov/div898/handbook/eda/section3/eda366j.htm
* https://www.investopedia.com/terms/p/poisson-distribution.asp
* A step-by-step walk through of the math https://help.smarkets.com/hc/en-gb/articles/115001457989-How-to-calculate-Poisson-distribution-for-football-betting



