'''
Created on Sep 3, 2018

TODO:

@author: cdleong
'''

# Example OrderedDict
''' 
OrderedDict(
    [
        ('player_key', '380.p.100011'), 
        ('player_id', '100011'), 
        ('name', 
            OrderedDict(
                    [
                        ('full', 'Indianapolis'), 
                        ('first', 'Indianapolis'), 
                        ('last', None), 
                        ('ascii_first', 'Indianapolis'), 
                        ('ascii_last', None)
                    ]
                )
        ), 
        (
            'editorial_player_key', 
            'nfl.p.100011'
        ), 
        ('editorial_team_key', 'nfl.t.11'), 
        ('editorial_team_full_name', 'Indianapolis Colts'), 
        ('editorial_team_abbr', 'Ind'), 
        ('bye_weeks', OrderedDict([('week', '9')])), 
        ('uniform_number', None), 
        ('display_position', 'DEF'), 
        ('headshot', OrderedDict([('url', 'https://s.yimg.com/lq/i/us/sp/v/nfl/teams/1/50x50w/ind.gif'), ('size', 'small')])), 
        ('image_url', 'https://s.yimg.com/lq/i/us/sp/v/nfl/teams/1/50x50w/ind.gif'), 
        ('is_undroppable', '0'), 
        ('position_type', 'DT'), 
        ('eligible_positions', OrderedDict([('position', 'DEF')])), 
        ('draft_analysis', 
        OrderedDict(
                        [
                            ('average_pick', '-'), 
                            ('average_round', '-'), 
                            ('average_cost', '-'), 
                            ('percent_drafted', '-')
                        ]
                    )
        ), 
        (
            'percent_owned', 
            OrderedDict([('coverage_type', 'week'), ('week', '1'), ('delta', '0')])
        )
    ]
)

'''
# 

class YahooNFLPlayer(object):
    _INVALID_DRAFT_POSITION = 1000000
    '''
    classdocs
    '''


    def __init__(self, yahoo_ordered_dict):
        self.yahoo_ordered_dict = yahoo_ordered_dict
        self.set_adpf()

    def get_player_key(self):
        return self.yahoo_ordered_dict['player_key']
        
    def get_position(self):
        return self.yahoo_ordered_dict['eligible_positions']['position']
        
    def get_full_name(self):
        return self.yahoo_ordered_dict['name']['full']
    
    def get_draft_analysis(self):
        return self.yahoo_ordered_dict['draft_analysis']
    
    def get_adp(self):
        return self.get_draft_analysis()['average_pick']

    def set_adpf(self):
        if self.get_draft_analysis()['average_pick'] is "-":
            self.adpf = YahooNFLPlayer._INVALID_DRAFT_POSITION
        else: 
            self.adpf = float(self.get_draft_analysis()['average_pick'])
 
    def get_adpf(self):
        return self.adpf
    
    