'''
Created on Aug 29, 2018

@author: cdleong
'''
import YahooSports as ysp
import math

nfl_players_per_team = 53
nfl_teams = 32
max_nfl_players = nfl_players_per_team*nfl_teams
max_count_yahoo_returns_per_query = 25  # determined experimentally
max_queries = math.ceil(max_nfl_players/max_count_yahoo_returns_per_query)


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
    
    xml_results = []
    count = max_count_yahoo_returns_per_query
    start = 0
    position = "QB"
    
   
   
    result = query_yahoo(session, query)
    xml = get_xml_from_yahoo_result(result)
    
    
 
    
    count_string = "players count"
    
    for i in range(0, max_queries):
        start = i*count
        
        query = "game/nfl/players;out=draft_analysis,percent_owned;position="+position+";count="+str(count)+";start="+str(start) 
        result = query_yahoo(session, query)
        xml = get_xml_from_yahoo_result(result)
        xml_results.append(xml)
        
        if count_string not in xml:
            print("count is zero, breaking out of loop")
            break
        else:
            matched_lines = [line for line in xml.split('\n') if count_string in line]
            print("COUNT: {}".format(matched_lines))
        
        

    filename = position + ".txt"
    with open(filename, "a") as text_file: 
        for result in xml_results:
            print(f"{result}", file=text_file)
    print("done")