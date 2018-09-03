'''
Created on Aug 29, 2018

@author: cdleong
'''
import YahooSports as ysp
import math
import xmltodict
from distutils import text_file
import random



OPENING_XML_STRING = '''<?xml version="1.0" ?>'''    

class PyFantasyYahooSportsInterface(object):
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
        self.auth_filename = auth_filename
        self.session = None


    def connect(self):
        
        # Try connecting with saved session
        session = ysp.YahooConnection(self.auth_filename)
        
        # Oh no it's not live
        if not session.is_live_session():
            url = session.auth_url()
            print("Go to URL:")
            print(url)
            pin = input('Enter PIN from browser: ')
            session.enter_pin(pin)
        
        self.session = session    
    
    
    def query_yahoo(self, query):
        if self.session is None:
            self.connect()
        else:
            if not self.session.is_live_session():
                self.connect()                
                
        return self.session.get(query)   
    
    def get_xml_from_yahoo_result(self, result):        
        return result.clean_text
    
        

    def download_players_data_list_of_dicts(self, position=""):
        xml_results = self.download_players_data_xml_strings(position)
        one_big_list_of_players = self.combine_xml_strings_to_one_big_list_of_players(xml_results)
        return one_big_list_of_players
        
        
    
    def download_players_data_xml_strings(self, position=""):
        '''
        Returns a list of XML strings.
        :param position:
        '''
        
        
        xml_results = []
        count = PyFantasyYahooSportsInterface.MAX_RETURNED_PER_QUERY
        start = 0
        count_string = "players count"
        i = 0
        more_players_to_retrieve = True
        
        
        while i < PyFantasyYahooSportsInterface.MAX_QUERY and more_players_to_retrieve:
            start = i * count
            i += 1
            
            print(f"i: {i}, start:{start}")
            
            # base query
            query = "game/nfl/players;out=draft_analysis,percent_owned"
            
            # Just one position?
            if position:
                print(f"adding position {position} to query")
                query = query + ";position=" + position

            # Continue building query so we can loop through and get them all                    
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
    
        
    def league_specific_query(self, subquery="", league_number=None,):
        '''
        Returns an XML string
        :param subquery:
        :param league_number:
        '''
        if not league_number:
            league_number = input("League number is: ")
        query = "league/nfl.l."+str(league_number) +subquery # get league info    
        
        return self.query_yahoo(query)        
         
    
    def clear_text_file_and_write(self, base_filename, contents_to_write):
        base_filename = base_filename + ".txt"
        
        #clear it first
        open(base_filename, 'w').close()
        
        #  add the text
        with open(base_filename, "a") as text_file:     
            print(f"{contents_to_write}", file=text_file)    

    
    def parse_yahoo_xml_string_to_dict(self, xml_string):
        #remove the first line, with the "<?xml version="1.0" ?>"    
        if OPENING_XML_STRING in xml_string:
            xml_string.replace(OPENING_XML_STRING, "")
            
        return xmltodict.parse(xml_string)


    def get_player_list_from_xml_string(self, xml_string_to_parse):
        '''    
        :param xml_string_to_parse:
        '''
        player_list = []
        if "<players count" in xml_string_to_parse:
            base_dict = self.parse_yahoo_xml_string_to_dict(xml_string_to_parse)
            fantasy_content_dict = base_dict['fantasy_content']
            game_dict = fantasy_content_dict['game']
            players_dict = game_dict['players']    
            player_list = players_dict['player']
            
        return player_list    


    def combine_xml_strings_to_one_big_list_of_players(self, xml_strings):
        
        combined_player_list = []
        
       
        for xml_string in xml_strings:
            if xml_string:
                combined_player_list += self.get_player_list_from_xml_string(xml_string)
        
        return combined_player_list


    def get_player_list_from_data_file(self, data_file_path):
        print(f"Getting data from {data_file_path}")
        
        with open(data_file_path, "r") as text_file:
            string_containing_multiple_xml_strings = text_file.read()
        
        #split on OPENING_XML_STRING
        xml_strings = string_containing_multiple_xml_strings.split(OPENING_XML_STRING)
        
        combined_player_list = self.combine_xml_strings_to_one_big_list_of_players(xml_strings)
        return combined_player_list






def download_all_player_data_from_yahoo_and_write_to_files(pyfsi):
    '''
    Download all the data to text files.
    :param pyfsi: PyFantasyYahooSportsInterface
    '''    
    # experimentally determined that there's 2789 "players" in the Yahoo DB. 
    xml_results = pyfsi.download_players_data_xml_strings()
    base_filename = "all_players"
    for result in xml_results:
        pyfsi.clear_text_file_and_write(base_filename, result)
    

def download_player_data_for_each_positon_from_yahoo_and_write_to_files(pyfsi):
    # get a result for each position
    for position in PyFantasyYahooSportsInterface.POSSIBLE_POSITIONS:
        xml_results = pyfsi.download_players_data_xml_strings(position=position)
  
        base_filename = position + ".txt"
        for result in xml_results:
            pyfsi.clear_text_file_and_write(base_filename, result)
                
    print("done")    



    





    




def main():
    auth_filename="auth_keys.txt"
    pyfsi = PyFantasyYahooSportsInterface(auth_filename)
    
#     download_all_player_data_from_yahoo_and_write_to_files(pyfsi)
#     download_player_data_for_each_positon_from_yahoo_and_write_to_files(pyfsi)

    data_file_path = "../data/all_players.txt"
    player_list = pyfsi.get_player_list_from_data_file(data_file_path)
    
    print(random.choice(player_list))
    
    

    
if __name__ == "__main__":
    main()

