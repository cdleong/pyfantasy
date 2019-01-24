'''


@author: cdleong
'''
import pandas as pd
import pprint
import random
from data_parser import PyFantasyDataParser
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

secure_random = random.SystemRandom()
if __name__ == "__main__":
    # Read in the XML
    bob = PyFantasyDataParser()
    data_file_path = "../data/all_league_players.txt"
    player_list = bob.get_player_list_from_data_file(data_file_path)

    random_player = secure_random.choice(player_list)
    pprint.pprint(random_player)

    player_dicts_list = []
    for player in player_list:
        fullname = player['name']['full']
        position = player['eligible_positions']['position']
        fixed_position = position
        if isinstance(position, list):
            fixed_position = position[0]
        points = float(player['player_points']['total'])

        player_dict = {"fullname": fullname, "position": fixed_position, "points": points}
        player_dicts_list.append(player_dict)

    player_df = pd.DataFrame(player_dicts_list)
    player_df.to_csv("../data/player_points.csv")
#    print(player_df)
#    print(player_df.dtypes)

    print(player_df['position'].unique())
    for position in player_df['position'].unique():
        plt.figure()
        pos_df = player_df[player_df["position"] == position]
        pos_df = pos_df.sort_values(by=["points"])
        print(pos_df)
        print(position)
        g = sns.distplot(pos_df['points'],
                         kde_kws={"cut": 0},
                         rug=True)
        plt.title(position)
        fig = g.get_figure()
        fig.savefig(position+".png")

        top_n = 14
        plt.figure()
        top_df = pos_df.tail(top_n)
        g = sns.distplot(top_df['points'],
                         kde=False,
                         rug=True)
        plt.title(position+f"_top_{top_n}")
        fig = g.get_figure()
        fig.savefig(position+f"_top_{top_n}.png")
