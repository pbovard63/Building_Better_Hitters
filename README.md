# Building Better Hitters:
## Predicting Baseball Player Offensive Success
## By: Patrick Bovard 
### *Metis Data Science Bootcamp Winter 2021 Project 2* 

**Description:**    
The goal of this project is to use MLB Statcast data to predict MLB player offensive value, via the statistic weighted runs created plus (wRC+).  This will be done by building a linear regression model, using Statcast data as features and wRC+ as the target.  

**Features and Target Variables:**   
- Final Features: 
    - Individual Terms:  
      - General Player Data: Player Age, Sprint Speed    
      - Quality of Contact:  Average Exit Velocity (Avg EV (MPH)), Average Launch Angle (Avg LA (°)), Barrel %, Solid Contact %, Flare/Burner %, Under %, Topped          %, Poor/Weak %  
      - Plate Discipline: Walk Rate (BB%), Zone Swing %, Out of Zone Swing 5, In Zone Contact %, Whiff %, First Strike %  
      - Batted Ball Direction: Pull %, Straight Away %, Opposite Field (Oppo) %
    - Interaction Terms: BB%*OutOfZone%, Barrel%*Topped%, Avg EV (MPH)*Sprint Speed, Barrel%*In Zone Contact %, Under %*Topped %, In Zone Contact % * Whiff %,          Whiff %**2  
- Target Variable: Weighted Runs Created Plus (wRC+)    

**FINAL PRESENTATION:** 
- PDF File: Project_2_Presentation.pdf (Powerpoint in "Presenatation" Folder)  

**Data Used:**   
- wRC+ Data from [Fangraphs](https://www.fangraphs.com/).   
- Statcast Data (Features) from [Baseball Savant](https://baseballsavant.mlb.com/).   
- Player Statistical Data from [Baseball Reference](https://www.baseball-reference.com/).^  

**Tools Used:**   
- Web-Scraping: Selenium, BeautifulSoup  
- Data Analysis and Model Building: Python, Pandas, Numpy, Scikit-learn  
- Visualization: Matplotlib, Seaborn  

**Possible impacts of your project:**   
Possible impacts of this project are on the player development and scouting side of baseball.  There are two major  
sides that I see being impacts:
  - Identifying players with traits that correlate with offensive success (i.e. scouting, trading, or signing those  
    players as free agents).
  - Identifying areas of improvements that could lead to greater offensive impact on underperforming players on the  
    current roster (i.e. player development).  
    
### NAVIGATING THE REPOSITORY:
    
**General Workflow of the Repo**:  
  1. Code to Pull Data from Individual Sites:  
    - Webscraping_code Folder:  
      - Fangraphs: Fangraphs_code_notebook.ipynb  
      - Baseball Savant: savant_code_notebook.ipynb  
      - Baseball Reference: Baseball Reference Code.ipynb^  
  2. Build functions to use in effectively pulling/merging the data:  
    - Webscraping_code Folder:  
      - Fangraphs: fangraphs_wrc_code.py  
      - Baseball Savant: baseball_savant_code.py  
  3. Merge Feature and Target Data into a single dataframe:  
    - Code to merge: savant_fangraphs_merge.ipynb  
    - Initial Pickled Merged Data: stats.pkl  
  4. Early Modeling:  
    - Folder: Early_Models  
  5. Final Model Iterations - in main area of repo:  
    1. new_savant_stats.ipynb: added in additioanl quality of contact stats, in zone contact rate, and first strike rate  
      - Led to creation of stats_2.pkl, new_stats.pkl  
    2. new_stats_modeling:  used new stats, modeling and residual analysis in this code led to me making the following changes to the final model:  
      - Removed Hard Hit %, GB%, FB%, LD%  
      - Added: Walk Rate, Whiff Rate  
    3. **Final Modeling and Testing: Final_Model_notebook**    
      - Uses function lr_validation_train.py (Linear Regression - Simple, Simple with KFOLD Cross Validation, Lasso, Ridge, Elastic Net)  
      - Uses function lasso_polynomial.py (LASSO Regression with Polynomial terms, to identify interaction terms)  
*^Note: data from baseball-reference was not used in the final model, as I couldn't effectively merge with the Baseball Savant Data.*  
