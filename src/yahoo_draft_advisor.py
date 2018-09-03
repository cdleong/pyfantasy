'''
Created on Sep 3, 2018

@author: cdleong
'''
import yahoo_sports_interface as ysi
import yahoo_nfl_player as ynp
import random
import operator
from operator import attrgetter




class PyFantasyYahooDraftAdvisor(object):
    _TOP_N = 15
    '''
    classdocs
    '''
    
    


    def __init__(self, players_list):
        '''
        Constructor
        '''        
        self.players_list = self.pre_process(players_list)
        
        
        
        
        for i in range(0, PyFantasyYahooDraftAdvisor._TOP_N):
            
            

            player = self.players_list[i]
            print(f"player {i}: {player.get_last_name()}, adp: {player.get_adp()}")
            
                
        
    def pre_process(self, players_list):
        '''
        Filters out players with adp of '-'
        Sorts by ADP
        
        :param players_list:
        '''
        processed_list = []
        for player_dict in players_list:
            player = ynp.YahooNFLPlayer(player_dict)
            if player.get_adp() is not "-":
                processed_list.append(player)
                
        # https://stackoverflow.com/questions/403421/how-to-sort-a-list-of-objects-based-on-an-attribute-of-the-objects
        # https://stackoverflow.com/questions/4010322/sort-a-list-of-class-instances-python
        
        print(f"First item: {processed_list[0]}")
        print(f"First item: {processed_list[0].get_adp()}")
        
        print(f"sorting. size: {len(processed_list)}")
        processed_list.sort(key=operator.attrgetter('adpf'))
        print(f"sorting. size: {len(processed_list)}")
        return processed_list

            
    
        

def main():
    
    auth_filename="auth_keys.txt"
    data_file_path = "../data/all_players.txt"
    
    #get data    
    my_pyfsi = ysi.PyFantasyYahooSportsInterface(auth_filename)
    players_list = my_pyfsi.get_player_list_from_data_file(data_file_path)
    
    
    
    # Process/parse the data
    
    my_draft_advisor = PyFantasyYahooDraftAdvisor(players_list)
    

if __name__ == '__main__':
    main()