'''
Created on Aug 29, 2018

@author: cdleong


'''
import YahooSports as ysp
import math

# CONSTANTS
NFL_PLAYERS_PER_TEAM = 53
NUMBER_OF_NFL_TEAMS = 32
NUMBER_OF_DEFENSES = NUMBER_OF_NFL_TEAMS
MAX_NFL_PLAYERS = (NFL_PLAYERS_PER_TEAM*NUMBER_OF_NFL_TEAMS) + NUMBER_OF_DEFENSES
MAX_RETURNED_PER_QUERY = 25  # determined experimentally
MAX_QUERY = math.ceil(MAX_NFL_PLAYERS/MAX_RETURNED_PER_QUERY)
POSSIBLE_POSITIONS = ["QB", "WR", "RB", "TE", "K" , "DEF"]


def make_saved_session(auth_filename):
    session = ysp.YahooConnection(auth_filename)
    if not session.is_live_session():
        url = session.auth_url()
        print("Go to URL:")
        print(url)
        pin = input('Enter PIN from browser: ')
        session.enter_pin(pin)
        
def use_saved_session(auth_filename):
    session = ysp.YahooConnection(auth_filename)
    return session

def query_yahoo(session, query):    
    return session.get(query)

def get_xml_from_yahoo_result(result):
    
    return result.clean_text


def get_players_for_position(session, position):
    xml_results = []
    count = MAX_RETURNED_PER_QUERY
    start = 0
    count_string = "players count"
    i = 0
    more_players_to_retrieve = True
    while i < MAX_QUERY and more_players_to_retrieve:
        start = i * count
        i += 1
        query = "game/nfl/players;out=draft_analysis,percent_owned;position=" + position + ";count=" + str(count) + ";start=" + str(start)
        result = query_yahoo(session, query)
        xml = get_xml_from_yahoo_result(result)
        xml_results.append(xml)
        if count_string not in xml:
            print("count is zero, breaking out of loop")
            more_players_to_retrieve = False
        else:
            matched_lines = [line for line in xml.split('\n') if count_string in line]
            print("COUNT: {}".format(matched_lines))
    
    return xml_results

    
def query_league(session, subquery="", league_number=None,):
    if not league_number:
        league_number = input("League number is: ")
    query = "league/nfl.l."+str(league_number) +subquery # get league info    
    
    return query_yahoo(session, query)
        
#     brett_favre_xml = session.get("game/223/players;player_keys=223.p.1025/draft_analysis")
#     print(brett_favre_xml)
#     print(brett_favre_xml.clean_text)
    
    #http://fantasysports.yahooapis.com/fantasy/v2/game/nfl
#     nfl_games_xml = session.get("game/nfl")
#     print(nfl_games_xml.clean_text) 
    
#     players_xml = session.get("game/nfl/players")
#     print(players_xml.clean_text)
     
    
if __name__ == "__main__":

    auth_filename="auth_keys.txt"
    session = make_saved_session(auth_filename)
    session = use_saved_session(auth_filename)
        
    query = "game/nfl/players" # get all the players
    query = "game/nfl/players/draft_analysis" # get all the players, with draft analysis
    query = "game/nfl/players/percent_owned" # get all the players, with percent_owned
    query = "game/nfl/players;out=draft_analysis,percent_owned" # get all the players, with percent_owned
    query = "game/nfl/players;out=draft_analysis,percent_owned;position=QB;count=25"
    
    
    for position in POSSIBLE_POSITIONS:
        xml_results = get_players_for_position(session, position)

        filename = position + ".txt"
        with open(filename, "a") as text_file: 
            for result in xml_results:
                print(f"{result}", file=text_file)
    print("done")