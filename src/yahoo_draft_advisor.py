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
    
    
    


    def __init__(self, players_list):
        '''
        Constructor
        '''        
        self.draftable_players_list = self.pre_process(players_list)
        self.drafted_by_others = []
        self.drafted_by_me = []
        
        
        
        
            
                
        
    def pre_process(self, players_list):
        '''
        Filters out players with adp of '-'
        Sorts by ADP
        
        :param players_list:
        '''
        
        print(f"preprocessing for '-' adp: initial size: {len(players_list)}")
        processed_list = []
        for player_dict in players_list:
            player = ynp.YahooNFLPlayer(player_dict)
            if player.get_adp() is not "-":
                processed_list.append(player)
        
        
        print(f"New size: {len(processed_list)}")
        
                
        # https://stackoverflow.com/questions/403421/how-to-sort-a-list-of-objects-based-on-an-attribute-of-the-objects
        # https://stackoverflow.com/questions/4010322/sort-a-list-of-class-instances-python
        
        print("Sorting list.")
        processed_list.sort(key=operator.attrgetter('adpf'))
        
        return processed_list

            
    def get_top_draftable_players(self, num_players=15):
        self.draftable_players_list.sort(key=operator.attrgetter('adpf'))
        return self.draftable_players_list[0:num_players]
        
    
        

def main():
    
    auth_filename="auth_keys.txt"
    data_file_path = "../data/all_players.txt"
    
    #get data    
    my_pyfsi = ysi.PyFantasyYahooSportsInterface(auth_filename)
    players_list = my_pyfsi.get_player_list_from_data_file(data_file_path)
    
    
    
    # Process/parse the data
    
    my_draft_advisor = PyFantasyYahooDraftAdvisor(players_list)
    top_draftable_players = my_draft_advisor.get_top_draftable_players(12)
    print(f"top {len(top_draftable_players)} players:")
    for draftable in top_draftable_players:
        print(f"Name: {draftable.get_full_name()}, \n\tadp:{draftable.get_adp()}, \n\tplayer_key: {draftable.get_player_key()}")
    

if __name__ == '__main__':
    main()