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
        
        #TODO: handle duplicates
        
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
            
    
    
    
    def draft_player(self, player_key, by_me=False):
        player_index = None
        for idx, draftable in enumerate(self.draftable_players_list):
            if draftable.get_player_key() == player_key:
                player_index=idx
                break
                
            
        
        
        
        if player_index is not None:
            player = self.draftable_players_list.pop(player_index)
            if by_me:
                print(f"Adding {player.get_full_name()} to your team")
                self.drafted_by_me.append(player)
            else:
                print(f"Adding {player.get_full_name()} to other teams")
                self.drafted_by_others.append(player)
        else:
            print(f"Can't draft {player_key}. Not found in draftable players")

#     def __repr__(self):
#         #TODO:
#         return f""

def main():
    
    auth_filename="auth_keys.txt"
    data_file_path = "../data/all_players.txt"
    
    #get data    
    my_pyfsi = ysi.PyFantasyYahooSportsInterface(auth_filename)
    players_list = my_pyfsi.get_player_list_from_data_file(data_file_path)
    
    
    
    # Process/parse the data
    
    my_draft_advisor = PyFantasyYahooDraftAdvisor(players_list)
    top_draftable_players = my_draft_advisor.get_top_draftable_players(6)
    print(f"top {len(top_draftable_players)} players:")
    for idx, draftable in enumerate(top_draftable_players):
        print(f"#{idx}: Name: {draftable.get_full_name()}, adp:{draftable.get_adp()}, position:{draftable.get_position()} player_key: {draftable.get_player_key()}")
    

    #draft test

    
    
    random_draftable = random.choice(top_draftable_players)    
    print(type(random_draftable))
    my_draft_advisor.draft_player(random_draftable.get_player_key(), by_me=False)
    my_draft_advisor.draft_player(random_draftable.get_player_key(), by_me=True)
    
    
    
    top_draftable_players = my_draft_advisor.get_top_draftable_players(6)
    print(f"top {len(top_draftable_players)} players:")
    for idx, draftable in enumerate(top_draftable_players):
        print(f"#{idx}: Name: {draftable.get_full_name()}, adp:{draftable.get_adp()}, position:{draftable.get_position()}, player_key: {draftable.get_player_key()}")

if __name__ == '__main__':
    main()