'''
Created on Aug 29, 2018

@author: cdleong

'''
import xmltodict

OPENING_XML_STRING = '''<?xml version="1.0" ?>'''

class PyFantasyDataParser(object):
    '''
    reads data!
    '''

    def __init__(self):
        '''
        Constructor
        '''
        print(f"Initializing {self}")

    def parse_yahoo_xml_string_to_dict(self, xml_string):
        # remove the first line, with the "<?xml version="1.0" ?>"
        if OPENING_XML_STRING in xml_string:
            xml_string.replace(OPENING_XML_STRING, "")

        return xmltodict.parse(xml_string)

    def clear_text_file_and_write_multiple_xml_results(self, file_path, xml_results):
        # clear it first
        open(file_path, 'w').close()

        #  append
        with open(file_path, "a") as text_file:
            for result in xml_results:
                print(f"{result}", file=text_file)

    def game_parse(self, xml_string_to_parse):

            base_dict = self.parse_yahoo_xml_string_to_dict(xml_string_to_parse)
            fantasy_content_dict = base_dict['fantasy_content']
            game_dict = fantasy_content_dict['game']
            players_dict = game_dict['players']
            player_list = players_dict['player']
            return player_list

    def get_player_list_from_xml_string(self, xml_string_to_parse):
        '''
        :param xml_string_to_parse:
        '''
        player_list = []
        if "<players count" in xml_string_to_parse:
            base_dict = self.parse_yahoo_xml_string_to_dict(xml_string_to_parse)
            fantasy_content_dict = base_dict['fantasy_content']

            # TODO: more elegant conditional
            if "<game>" in xml_string_to_parse:
                game_dict = fantasy_content_dict['game']
                players_dict = game_dict['players']
                player_list = players_dict['player']
            elif "<league>" in xml_string_to_parse:
                league_dict = fantasy_content_dict['league']
                players_dict = league_dict['players']
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

        # split on OPENING_XML_STRING
        xml_strings = string_containing_multiple_xml_strings.split(OPENING_XML_STRING)

        combined_player_list = self.combine_xml_strings_to_one_big_list_of_players(xml_strings)
        print(f"Got {len(combined_player_list)} players")
        return combined_player_list

if __name__ == "__main__":
    bob = PyFantasyDataParser()

    data_file_path = "../data/all_league_players.txt"
    player_list = bob.get_player_list_from_data_file(data_file_path)
