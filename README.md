# Metis_Project_2
### *Metis Data Science Bootcamp Winter 2021 Project 2*  
### By: Patrick Bovard 

**Project Title:**    
**Predicting Player Production Using Statcast Data :baseball:**    

**Description:**    
The goal of this project is to use MLB Statcast data to predict MLB player offensive value, in terms of wRC+.  

**Features and Target Variables:**   
- Possible Features: Age, Avg. Exit Velocity, Avg. Launch Angle, Barrel Rate, Solid Contact Rate, Hard Hit Rate,  
  Zone Swing Rate, Out of Zone Swing Rate, Pull Rate, Straight Away Rate, Opposite Field Rate, Batted Ball Profile  
  (Groundball Rate, Flyball Rate, Line Drive Rate), Position, and Sprint Speed.  
- Target Variable: Weighted Runs Created Plus (wRC+)  

**Data Used (e.g., NYC Open Data):**   
- wRC+ Data from [Fangraphs](https://www.fangraphs.com/).   
- Statcast Data (Features) from [Baseball Savant](https://baseballsavant.mlb.com/).   
- Player Statistical Data from [Baseball Reference](https://www.baseball-reference.com/).^  

**Tools Used (e.g., Scrapy, Seaborn, etc.):**   
Selenium, BeautifulSoup, Python, Pandas, Numpy, Seaborn, SciPy Kit  

**Possible impacts of your project:**   
Possible impacts of this project are on the player development and scouting side of baseball.  There are two major  
sides that I see being impacts:
  - Identifying players with traits that correlate with offensive success (i.e. scouting, trading, or signing those  
    players as free agents).
  - Identifying areas of improvements that could lead to greater offensive impact on underperforming players on the  
    current roster (i.e. player development).  
    
**General Workflow of the Repo**:  
  1. Code to Pull Data from Individual Sites:  
    - Fangraphs: Fangraphs_code_notebook.ipynb  
    - Baseball Savant: Project_2_Savant_code.ipynb  
    - Baseball Reference: Baseball Reference Code.ipynb^  
  2. Build functions to use in effectively pulling/merging the data:  
    - Fangraphs: fangraphs_wrc_code.py  
    - Baseball Savant: baseball_savant_code.py  
  3. Merge Feature and Target Data into a single dataframe:  
    - Code to merge: savant_fangraphs_merge.ipynb  
    - Pickled Merged Data: stats.pkl  
  4. Initial Cleaning/Modeling of Data:  
    - first_model_notebook.ipynb  
    - second_model_notebook.ipynb  
    
*^Note: data from baseball-reference was not used in the final model, as I couldn't effectively merge with the Baseball Savant Data.*  
