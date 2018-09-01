'''
Created on Aug 29, 2018

@author: cdleong

TODO: OO it to PyFantasyYahooInterface
'''
import YahooSports as ysp
import math



class PyfantasyYahooSportsInterface(object):
    # CLASS CONSTANTS
    NFL_PLAYERS_PER_TEAM = 53
    NUMBER_OF_NFL_TEAMS = 32
    NUMBER_OF_DEFENSES = NUMBER_OF_NFL_TEAMS
    
    # experimentally determined that there's 2789 "players" in the Yahoo DB, actually
    # TODO: fix calculation method
    MAX_NFL_PLAYERS = (NFL_PLAYERS_PER_TEAM*NUMBER_OF_NFL_TEAMS) + NUMBER_OF_DEFENSES
    MAX_RETURNED_PER_QUERY = 25  # determined experimentally
    MAX_QUERY = math.ceil(MAX_NFL_PLAYERS/MAX_RETURNED_PER_QUERY)*2 
    POSSIBLE_POSITIONS = ["QB", "WR", "RB", "TE", "K" , "DEF"]

    
    def __init__(self, auth_filename):
        '''
        Constructor        
        '''
        print(f"Initializing {self}")
        self.connect(auth_filename)

    def connect(self, auth_filename):
        
        # Try connecting with saved session
        session = ysp.YahooConnection(auth_filename)
        
        # Oh no it's not live
        if not session.is_live_session():
            url = session.auth_url()
            print("Go to URL:")
            print(url)
            pin = input('Enter PIN from browser: ')
            session.enter_pin(pin)
        
        self.session = session    
    
    
    def query_yahoo(self, query):    
        return self.session.get(query)
    
    def get_xml_from_yahoo_result(self, result):        
        return result.clean_text
    
    
    def get_players_data(self, position=""):
        xml_results = []
        count = PyfantasyYahooSportsInterface.MAX_RETURNED_PER_QUERY
        start = 0
        count_string = "players count"
        i = 0
        more_players_to_retrieve = True
        
        
        while i < PyfantasyYahooSportsInterface.MAX_QUERY and more_players_to_retrieve:
            start = i * count
            i += 1
            
            print(f"i: {i}, start:{start}")
            
            # base query
            query = "game/nfl/players;out=draft_analysis,percent_owned"
            
            # Just one position?
            if position:
                print(f"adding position {position} to query")
                query = query + ";position=" + position
                    
            query = query+";count=" + str(count)             
            query = query + ";start=" + str(start)
            
            print(f"Final query: {query}")
            
            result = self.query_yahoo(query)
            xml = self.get_xml_from_yahoo_result(result)
            xml_results.append(xml)
            if count_string not in xml:
                print("count is zero, breaking out of loop")
                more_players_to_retrieve = False
            else:
                matched_lines = [line for line in xml.split('\n') if count_string in line]
                print("COUNT: {}".format(matched_lines))
        
        return xml_results
    
        
    def query_league(self, subquery="", league_number=None,):
        if not league_number:
            league_number = input("League number is: ")
        query = "league/nfl.l."+str(league_number) +subquery # get league info    
        
        return self.query_yahoo(query)
            
    #     brett_favre_xml = session.get("game/223/players;player_keys=223.p.1025/draft_analysis")
    #     print(brett_favre_xml)
    #     print(brett_favre_xml.clean_text)
        
        #http://fantasysports.yahooapis.com/fantasy/v2/game/nfl
    #     nfl_games_xml = session.get("game/nfl")
    #     print(nfl_games_xml.clean_text) 
        
    #     players_xml = session.get("game/nfl/players")
    #     print(players_xml.clean_text)
         
    
    def clear_text_file_and_write(self, filename, contents_to_write):
        filename = filename + ".txt"
        
        #clear it first
        open(filename, 'w').close()
        
        #  add the text
        with open(filename, "a") as text_file:     
            print(f"{contents_to_write}", file=text_file)    
    
    
if __name__ == "__main__":

    auth_filename="auth_keys.txt"
    pyfsi = PyfantasyYahooSportsInterface(auth_filename)
        
    
    # experimentally determined that there's 2789 "players" in the Yahoo DB. 
    xml_results = pyfsi.get_players_data()
    filename = "all_players" + ".txt" 
    for result in xml_results:
        pyfsi.clear_text_file_and_write(filename, result)
    
#     
#     # get a result for each position
#     for position in POSSIBLE_POSITIONS:
#         xml_results = get_players_data(session, position)
#  
#         filename = position + ".txt"
#         for result in xml_results:
#             pyfsi.clear_text_file_and_write(filename, xml_result)
                
                
    print("done")