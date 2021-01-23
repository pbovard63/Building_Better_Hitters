import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests
import re
from IPython.core.display import display, HTML    # make sure Jupyter knows to display it as HTML
import time, os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def Baseball_Savant_Soup_Generator(url):
    '''
    Arguments: Takes in a url to a Baseball Savant leaderboard.
    Returns: Beautiful soup object that can be used to pull data.
    '''
    #Set up selenium:
    import time, os
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    
    chromedriver = "/Applications/chromedriver" # path to the chromedriver executable
    os.environ["webdriver.chrome.driver"] = chromedriver
    
    driver = webdriver.Chrome(chromedriver)
    driver.get(url)
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    #Close out driver:
    driver.close()
    
    return soup

def Savant_Stats_Puller(soup):
    '''
    Argument: takes in a URL to Baseball Savant leaderboard.
    Returns: a list of stats from the leaderboard.
    '''
    #Finding stats from the soup object:
    stat_lines = soup.find('div', id='sortable_stats').find_all('tr')
    compiled_stats = []
    for line_item in stat_lines:
        ind_stat_line = [item.get_text() for item in line_item.find_all('td')]
        compiled_stats.append(ind_stat_line)
        final_stats = compiled_stats[1:]
    return final_stats

def Savant_Link_Puller(soup):
    '''
    Arguments: takes in a url to Baseball Savant leaderboard.
    Returns: a list of player links from teh leaderboard, to each player's individual page.
    '''
    #Pulling the list of player links:
    player_links = soup.find('div', id='sortable_stats').find_all('tr')
    compiled_links = []
    for line_item in player_links:
        ind_link = [item.get("href") for item in line_item.find_all('a')]
        compiled_links.append(ind_link)
        final_link = compiled_links[1:]
    return final_link

def Savant_DataFrame_Builder(url):
    '''
    Arguments: takes in a url to Baseball Savant Leaderboard.
    Returns: a Pandas dataframe containing the data from the table.
    '''
    #utilizing helper functions for the soup list, player links, and stats:
    soup = Baseball_Savant_Soup_Generator(url)
    player_links = Savant_Link_Puller(soup)
    player_stats = Savant_Stats_Puller(soup)
    
    #Creating Column headers for the dataframe:
    headers = soup.find('div', id='sortable_stats').find_all('th')
    columns = [col.get_text() for col in headers]
    
    #Setting up dataframe:
    savant_df = pd.DataFrame(player_stats, columns=columns)
    
    savant_df.set_index(savant_df['Rk.'], inplace=True)
    savant_df.drop(columns='Rk.',inplace=True)
    savant_df['Player Link'] = player_links
    
    return savant_df