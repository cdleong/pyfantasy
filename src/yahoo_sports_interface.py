'''
Created on Aug 29, 2018

@author: cdleong
'''
import YahooSports as ysp
import math
import xmltodict
import pandas as pd
import random
import data_parser
secure_random = random.SystemRandom()

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
    POSSIBLE_POSITIONS = ["QB", "WR", "RB", "TE", "K", "DEF"]

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

    def download_stat_categories(self):
        '''
        https://developer.yahoo.com/fantasysports/guide/game-resource.html
        http://fantasysports.yahooapis.com/fantasy/v2/game/nfl/stat_categories
        '''
        query = "game/nfl/stat_categories"
        result = self.query_yahoo(query)
        xml = self.get_xml_from_yahoo_result(result)
        file_path = "../data/stat_categories.txt"
        with open(file_path, "a") as text_file:
            print(f"{xml}", file=text_file)

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
            query = "game/nfl/players;out=draft_analysis,percent_owned,stats"

#            league_num = 0  # TODO: ask user for league_num arg, use this if
#            they provided one.
#            league_query = f"league/nfl.l.{league_num}/players;out=draft_analysis,percent_owned,stats"

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

        see also https://developer.yahoo.com/fantasysports/guide/players-collection.html
        and https://developer.yahoo.com/fantasysports/guide/league-resource.html#league-resource-key_format
        'league/{league_key}/players'
        so for example "league/nfl.l.42"
        '''
        if not league_number:
            league_number = input("League number is: ")
        query = "league/nfl.l." + str(league_number) + subquery  # get league info

        return self.query_yahoo(query)



    def download_all_player_data_from_yahoo_and_write_to_files(self, download_path="../data/all_players.txt"):
        '''
        Download all the data to text files.
        :param pyfsi: PyFantasyYahooSportsInterface
        '''
        # experimentally determined that there's 2789 "players" in the Yahoo DB.
        xml_results = self.download_players_data_xml_strings()

        self.clear_text_file_and_write_multiple_xml_results(download_path, xml_results)

    def download_player_data_for_each_position_from_yahoo_and_write_to_files(self):
        # get a result for each position
        for position in PyFantasyYahooSportsInterface.POSSIBLE_POSITIONS:
            xml_results = self.download_players_data_xml_strings(position=position)

            # TODO: arg?
            base_filename = "../data/" + position + ".txt"
            for result in xml_results:
                self.clear_text_file_and_write_multiple_xml_results(base_filename, result)

        print("done")


def player_list_as_dataframe(player_ordereddict):
    return pd.DataFrame.from_dict(player_ordereddict)


def main():
    # TODO: argparse - download or read?
    auth_filename = "auth_keys.txt"
    pyfsi = PyFantasyYahooSportsInterface(auth_filename)

    pyfsi.download_stat_categories()
    pyfsi.download_all_player_data_from_yahoo_and_write_to_files("../data/all_league_players.txt")
#    pyfsi.download_player_data_for_each_position_from_yahoo_and_write_to_files(pyfsi)

    data_file_path = "../data/all_players.txt"
    player_list = pyfsi.get_player_list_from_data_file(data_file_path)

#    random_player = secure_random.choice(player_list)
#    pprint.pprint(random_player)

#    player_df = player_list_as_dataframe(player_list)
#    print(player_df.info())
#    print(player_df.describe())


if __name__ == "__main__":
    main()
