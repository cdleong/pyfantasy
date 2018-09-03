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
    
    
    


    def __init__(self, players_list, league_roster_positions):
        '''
        Constructor
        '''        
        self.draftable_players_list = self.pre_process(players_list)
        self.original_draftable_players_list = self.draftable_players_list.copy()
        self.drafted_by_others = []
        self.drafted_by_me = []
        self.avg_adp_for_each_position = None
        self.roster_positions = league_roster_positions
        
        
                
        
    def pre_process(self, players_list):
        '''
        Filters out players with adp of '-'
        Sorts by ADP
        
        #TODO: handle duplicates
        
        :param players_list:
        '''
        orig_len = len(players_list)
        
        processed_list = []
        for player_dict in players_list:
            player = ynp.YahooNFLPlayer(player_dict)
            if player.get_adp() is not "-":
                processed_list.append(player)
        
        print(f"preprocessing for '-' adp: initial size: {orig_len}, processed size:{len(processed_list)}")
        
        
                
        # https://stackoverflow.com/questions/403421/how-to-sort-a-list-of-objects-based-on-an-attribute-of-the-objects
        # https://stackoverflow.com/questions/4010322/sort-a-list-of-class-instances-python
        
        print("Sorting list.")
        processed_list.sort(key=operator.attrgetter('adpf'))
        
        return processed_list


    
    def get_top_draftable_players(self, num_players=15, position=""):
        
        self.draftable_players_list.sort(key=operator.attrgetter('adpf'))
        
        players_to_return = []
        if position:
            print(f"getting top players for {position}")
            for player in self.draftable_players_list:
                if player.get_position() == position:
                    players_to_return.append(player)
                
        else: 
            players_to_return = self.draftable_players_list
        
        players_to_return = players_to_return[0:num_players]
        return players_to_return
            
    
    
    
    def draft_player(self, player_key, by_me=False):
        print(f"Draft player function. Draftable players: {len(self.draftable_players_list)}")
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

        print(f"After drafting a player, draftable players: {len(self.draftable_players_list)}")

    
    
    
    def get_all_players_for_position(self, position):
        players_for_position = []
        for player in self.original_draftable_players_list:
            if player.get_position() == position:
                players_for_position.append(player)
        return players_for_position
            
    
    def calculate_avg_adp_for_position(self, position):
        players_at_position = self.get_all_players_for_position(position)
        sum_adp = sum(player.get_adpf() for player in players_at_position)
        avg_adp = sum_adp/len(players_at_position)
        return avg_adp
    
    def _calulate_avg_adp_for_each_position(self):
        pos_avg_adp_dict = {}
        for position in ysi.PyFantasyYahooSportsInterface.POSSIBLE_POSITIONS:
            avg_adp = self.calculate_avg_adp_for_position(position)
#             print(f"average adp for position {position}: {avg_adp}")
            pos_avg_adp_dict[position]=avg_adp
            
        return pos_avg_adp_dict
    
    def get_avg_adp_for_each_position(self):
        if self.avg_adp_for_each_position is None:
            self.avg_adp_for_each_position = self._calulate_avg_adp_for_each_position()

        return self.avg_adp_for_each_position
    
    def sort_positions_based_on_avg_adp(self):
        position_adp_list = list(self.get_avg_adp_for_each_position().items())
        print(f"Items: {position_adp_list}")
        print(f"first item: {position_adp_list[0]}")
        # https://stackoverflow.com/questions/3121979/how-to-sort-list-tuple-of-lists-tuples
        position_adp_list.sort(key= lambda tup: tup[1])
        return position_adp_list

def main():
    
    auth_filename="auth_keys.txt"
    data_file_path = "../data/all_players.txt"
    
    # load data    
    my_pyfsi = ysi.PyFantasyYahooSportsInterface(auth_filename)
    
    get_updated_data = False
    if get_updated_data:
        my_pyfsi.download_all_player_data_from_yahoo_and_write_to_files(data_file_path)
    
    players_list = my_pyfsi.get_player_list_from_data_file(data_file_path)
    
    league_roster = "QB, WR, WR, RB, RB, TE, K, DEF, BN, BN, BN, BN, BN, IR".split()
    print(f"{league_roster}")
    my_draft_advisor = PyFantasyYahooDraftAdvisor(players_list, league_roster)
    
    print(f"OK, we've got {len(my_draft_advisor.original_draftable_players_list)} choices to start")
    for position in ysi.PyFantasyYahooSportsInterface.POSSIBLE_POSITIONS:
        all_for_pos = my_draft_advisor.get_all_players_for_position(position)
        print(f"# of existing players at {position}: {len(all_for_pos)}")    
    
    pos_avg_adp_dict = my_draft_advisor.get_avg_adp_for_each_position()
    print(f"Average adp for each position: {pos_avg_adp_dict}")
    
    position_based_draft_order_avg_adp = my_draft_advisor.sort_positions_based_on_avg_adp()
    print(f"Based on avg adp, the positional priority list is: {position_based_draft_order_avg_adp}")
    
    
    

    

    
    # Simulate other people drafting
    for i in range(0,10):
        top_draftable_players = my_draft_advisor.get_top_draftable_players(5)
        random_draftable = random.choice(top_draftable_players)    
        my_draft_advisor.draft_player(random_draftable.get_player_key(), by_me=False)

    
    
    # Simulate me drafting 
    top_draftable_players = my_draft_advisor.get_top_draftable_players(6)
    print(f"top {len(top_draftable_players)} draftable players:")
    for idx, draftable in enumerate(top_draftable_players):
        print(f"#{idx}: Name: {draftable.get_full_name()}, adp:{draftable.get_adp()}, position:{draftable.get_position()}, player_key: {draftable.get_player_key()}")

        
    random_draftable = random.choice(top_draftable_players)      
    my_draft_advisor.draft_player(random_draftable.get_player_key(), by_me=True)
    
    
    
    for position in ysi.PyFantasyYahooSportsInterface.POSSIBLE_POSITIONS:
        top_draftable_for_pos =  my_draft_advisor.get_top_draftable_players(3, position=position)
        
        print(f"TOP PLAYERS FOR POSITION: {position}")
        for idx, draftable in enumerate(top_draftable_for_pos):        
            print(f"#{idx}: Name: {draftable.get_full_name()}, adp:{draftable.get_adp()}, position:{draftable.get_position()}, player_key: {draftable.get_player_key()}")
    

    
    
if __name__ == '__main__':
    main()