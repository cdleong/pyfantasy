from YahooSports import YahooConnection

def make_saved_session(auth_filename):
    session = YahooConnection(auth_filename)
    if not session.is_live_session():
        url = session.auth_url()
        print("Go to URL:")
        print(url)
        pin = input('Enter PIN from browser: ')
        session.enter_pin(pin)
        
def use_saved_session(auth_filename):
    session = YahooConnection(auth_filename)
    return session

def query_yahoo(session, query):    
    return session.get(query)

def print_yahoo_result(result):    
    print(result.clean_text)
    
def query_league(session, league_number=None):
    if not league_number:
        league_number = input("League number is: ")
    query = "league/nfl.l."+str(league_number) # get league info    
    
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
    session = use_saved_session(auth_filename)
    query = "game/nfl/players" # get all the players
    query = "game/nfl/players/draft_analysis" # get all the players, with draft analysis
    

    result = query_yahoo(session, query)
    print(result)
    print_yahoo_result(result)