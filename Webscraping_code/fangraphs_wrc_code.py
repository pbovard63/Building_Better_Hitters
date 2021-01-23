import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests
import re
from IPython.core.display import display, HTML    # make sure Jupyter knows to display it as HTML
import time, os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def Fangraphs_wRC_Soup_Generator(url):
    '''
    Arguments: Takes in a url to Fangraphs.
    Returns: A beautiful soup object that can be used to parse through the data.
    '''
    import time, os
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys

    chromedriver = "/Applications/chromedriver" # path to the chromedriver executable
    os.environ["webdriver.chrome.driver"] = chromedriver
    
    driver = webdriver.Chrome(chromedriver)
    driver.get(url)
    
    players_dropdown = driver.find_element_by_xpath('//*[@id="root-season-grid"]/div/div[3]/div[3]/div[1]/select')
    players_dropdown.send_keys("Infinity")
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    driver.close()
    
    return soup

def Fangraphs_wRC_Puller(url):
    '''
    Arguments: a URL to Fangraphs.
    Returns: a table with wRC+ data from 2015-2020 for all players.
    '''
    #Using the Soup_Generator_Function first:
    soup = Fangraphs_wRC_Soup_Generator(url)
    
    #Creating the column headers:
    headers = soup.find('div', class_='table-scroll').find_all('th')
    columns = [col.get_text() for col in headers]
    
    #Now, pulling the stats:
    stat_lines = soup.find('div', class_='table-scroll').find_all('tr')
    compiled_stats = []
    for line_item in stat_lines:
        ind_stat_line = [item.get_text() for item in line_item.find_all('td')]
        compiled_stats.append(ind_stat_line)
        final_stats = compiled_stats[1:]
    
    #Finally, the dataframe:
    wrc_df = pd.DataFrame(final_stats, columns=columns)
    wrc_df.set_index(wrc_df['#'], inplace=True)
    wrc_df.drop(columns='#',inplace=True)
    wrc_df.replace("", '0', inplace=True)
    
    return(wrc_df)

def wRC_DataFrame_Shifter(url):
    '''
    Arguments: Takes in a url to fangraphs.
    Returns: a formatted pandas dataframe with each player's wRC+ by year.
    '''
  
    #Using the initial dataframe builder:
    initial_df = Fangraphs_wRC_Puller(url)
    
    wrc_pivot_df = initial_df.T
    wrc_pivot_df.columns = wrc_pivot_df.iloc[0]
    final_wrc_pivot_df = wrc_pivot_df[1:]
    
    names = final_wrc_pivot_df.columns.to_list()
    years = final_wrc_pivot_df.index.to_list()
    
    new_df_rows = []
    for name in names:
        for year in years:
            new_row = name + "-" + year
            new_df_rows.append(new_row)
            
    final_wrc_df = pd.DataFrame(new_df_rows, columns=['Name-Year'])
    final_wrc_df['wRC+'] = ''
    
    wrc_2015 = final_wrc_pivot_df.iloc[0].to_list()
    wrc_2016 = final_wrc_pivot_df.iloc[1].to_list()
    wrc_2017 = final_wrc_pivot_df.iloc[2].to_list()
    wrc_2018 = final_wrc_pivot_df.iloc[3].to_list()
    wrc_2019 = final_wrc_pivot_df.iloc[4].to_list()
    wrc_2020 = final_wrc_pivot_df.iloc[5].to_list()
    
    final_wrc_df['wRC+'].iloc[0::6] = wrc_2015
    final_wrc_df['wRC+'].iloc[1::6] = wrc_2016
    final_wrc_df['wRC+'].iloc[2::6] = wrc_2017
    final_wrc_df['wRC+'].iloc[3::6] = wrc_2018
    final_wrc_df['wRC+'].iloc[4::6] = wrc_2019
    final_wrc_df['wRC+'].iloc[5::6] = wrc_2020
    
    return final_wrc_df