'''
Created on Aug 29, 2018

@author: cdleong
'''
import YahooSports as ysp
import math
import xmltodict
from distutils import text_file
import random


__test_string = '''<?xml version="1.0" ?><fantasy_content copyright="Data provided by Yahoo! and STATS, LLC" ns0:uri="http://fantasysports.yahooapis.com/fantasy/v2/game/nfl/players;count=25;out=draft_analysis,percent_owned;start=0" refresh_rate="60" time="191.02597236633ms" xml:lang="en-US" xmlns:ns0="http://www.yahooapis.com/v1/base.rng">  
   <game>    
      <game_key>380</game_key>    
      <game_id>380</game_id>    
      <name>Football</name>    
      <code>nfl</code>    
      <type>full</type>    
      <url>https://football.fantasysports.yahoo.com/f1</url>    
      <season>2018</season>    
      <is_registration_over>0</is_registration_over>    
      <is_game_over>0</is_game_over>    
      <is_offseason>0</is_offseason>    
      <players count="25">      
         <player>        
            <player_key>380.p.28398</player_key>        
            <player_id>28398</player_id>        
            <name>          
               <full>Todd Gurley II</full>          
               <first>Todd</first>          
               <last>Gurley II</last>          
               <ascii_first>Todd</ascii_first>          
               <ascii_last>Gurley II</ascii_last>          
            </name>        
            <editorial_player_key>nfl.p.28398</editorial_player_key>        
            <editorial_team_key>nfl.t.14</editorial_team_key>        
            <editorial_team_full_name>Los Angeles Rams</editorial_team_full_name>        
            <editorial_team_abbr>LAR</editorial_team_abbr>        
            <bye_weeks>          
               <week>12</week>          
            </bye_weeks>        
            <uniform_number>30</uniform_number>        
            <display_position>RB</display_position>        
            <headshot>          
               <url>https://s.yimg.com/iu/api/res/1.2/R0dS3WGRW9RFJadp.KihwQ--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08232018/28398.png</url>          
               <size>small</size>          
            </headshot>        
            <image_url>https://s.yimg.com/iu/api/res/1.2/R0dS3WGRW9RFJadp.KihwQ--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08232018/28398.png</image_url>        
            <is_undroppable>0</is_undroppable>        
            <position_type>O</position_type>        
            <eligible_positions>          
               <position>RB</position>          
            </eligible_positions>        
            <has_player_notes>1</has_player_notes>        
            <draft_analysis>          
               <average_pick>1.4</average_pick>          
               <average_round>1.0</average_round>          
               <average_cost>68.6</average_cost>          
               <percent_drafted>1.00</percent_drafted>          
            </draft_analysis>        
            <percent_owned>          
               <coverage_type>week</coverage_type>          
               <week>1</week>          
               <value>100</value>          
               <delta>0</delta>          
            </percent_owned>        
         </player>      
         <player>        
            <player_key>380.p.26671</player_key>        
            <player_id>26671</player_id>        
            <name>          
               <full>Le'Veon Bell</full>          
               <first>Le'Veon</first>          
               <last>Bell</last>          
               <ascii_first>Le'Veon</ascii_first>          
               <ascii_last>Bell</ascii_last>          
            </name>        
            <editorial_player_key>nfl.p.26671</editorial_player_key>        
            <editorial_team_key>nfl.t.23</editorial_team_key>        
            <editorial_team_full_name>Pittsburgh Steelers</editorial_team_full_name>        
            <editorial_team_abbr>Pit</editorial_team_abbr>        
            <bye_weeks>          
               <week>7</week>          
            </bye_weeks>        
            <uniform_number>26</uniform_number>        
            <display_position>RB</display_position>        
            <headshot>          
               <url>https://s.yimg.com/iu/api/res/1.2/7ctYzETVTHzBLMN5nPsZOg--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08212018/26671.png</url>          
               <size>small</size>          
            </headshot>        
            <image_url>https://s.yimg.com/iu/api/res/1.2/7ctYzETVTHzBLMN5nPsZOg--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08212018/26671.png</image_url>        
            <is_undroppable>0</is_undroppable>        
            <position_type>O</position_type>        
            <eligible_positions>          
               <position>RB</position>          
            </eligible_positions>        
            <has_player_notes>1</has_player_notes>        
            <draft_analysis>          
               <average_pick>2.1</average_pick>          
               <average_round>1.0</average_round>          
               <average_cost>66.6</average_cost>          
               <percent_drafted>1.00</percent_drafted>          
            </draft_analysis>        
            <percent_owned>          
               <coverage_type>week</coverage_type>          
               <week>1</week>          
               <value>100</value>          
               <delta>0</delta>          
            </percent_owned>        
         </player>      
         <player>        
            <player_key>380.p.28474</player_key>        
            <player_id>28474</player_id>        
            <name>          
               <full>David Johnson</full>          
               <first>David</first>          
               <last>Johnson</last>          
               <ascii_first>David</ascii_first>          
               <ascii_last>Johnson</ascii_last>          
            </name>        
            <editorial_player_key>nfl.p.28474</editorial_player_key>        
            <editorial_team_key>nfl.t.22</editorial_team_key>        
            <editorial_team_full_name>Arizona Cardinals</editorial_team_full_name>        
            <editorial_team_abbr>Ari</editorial_team_abbr>        
            <bye_weeks>          
               <week>9</week>          
            </bye_weeks>        
            <uniform_number>31</uniform_number>        
            <display_position>RB</display_position>        
            <headshot>          
               <url>https://s.yimg.com/iu/api/res/1.2/bVYbyRhr4G4DV0jCJ_W4DA--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08222018/28474.png</url>          
               <size>small</size>          
            </headshot>        
            <image_url>https://s.yimg.com/iu/api/res/1.2/bVYbyRhr4G4DV0jCJ_W4DA--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08222018/28474.png</image_url>        
            <is_undroppable>0</is_undroppable>        
            <position_type>O</position_type>        
            <eligible_positions>          
               <position>RB</position>          
            </eligible_positions>        
            <has_player_notes>1</has_player_notes>        
            <has_recent_player_notes>1</has_recent_player_notes>        
            <draft_analysis>          
               <average_pick>4.0</average_pick>          
               <average_round>1.0</average_round>          
               <average_cost>64.0</average_cost>          
               <percent_drafted>1.00</percent_drafted>          
            </draft_analysis>        
            <percent_owned>          
               <coverage_type>week</coverage_type>          
               <week>1</week>          
               <value>100</value>          
               <delta>0</delta>          
            </percent_owned>        
         </player>      
         <player>        
            <player_key>380.p.29238</player_key>        
            <player_id>29238</player_id>        
            <name>          
               <full>Ezekiel Elliott</full>          
               <first>Ezekiel</first>          
               <last>Elliott</last>          
               <ascii_first>Ezekiel</ascii_first>          
               <ascii_last>Elliott</ascii_last>          
            </name>        
            <editorial_player_key>nfl.p.29238</editorial_player_key>        
            <editorial_team_key>nfl.t.6</editorial_team_key>        
            <editorial_team_full_name>Dallas Cowboys</editorial_team_full_name>        
            <editorial_team_abbr>Dal</editorial_team_abbr>        
            <bye_weeks>          
               <week>8</week>          
            </bye_weeks>        
            <uniform_number>21</uniform_number>        
            <display_position>RB</display_position>        
            <headshot>          
               <url>https://s.yimg.com/iu/api/res/1.2/wy93YGddP62dCPtzgMCU3w--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08272018/29238.png</url>          
               <size>small</size>          
            </headshot>        
            <image_url>https://s.yimg.com/iu/api/res/1.2/wy93YGddP62dCPtzgMCU3w--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08272018/29238.png</image_url>        
            <is_undroppable>0</is_undroppable>        
            <position_type>O</position_type>        
            <eligible_positions>          
               <position>RB</position>          
            </eligible_positions>        
            <draft_analysis>          
               <average_pick>4.3</average_pick>          
               <average_round>1.0</average_round>          
               <average_cost>65.0</average_cost>          
               <percent_drafted>1.00</percent_drafted>          
            </draft_analysis>        
            <percent_owned>          
               <coverage_type>week</coverage_type>          
               <week>1</week>          
               <value>100</value>          
               <delta>0</delta>          
            </percent_owned>        
         </player>      
         <player>        
            <player_key>380.p.24171</player_key>        
            <player_id>24171</player_id>        
            <name>          
               <full>Antonio Brown</full>          
               <first>Antonio</first>          
               <last>Brown</last>          
               <ascii_first>Antonio</ascii_first>          
               <ascii_last>Brown</ascii_last>          
            </name>        
            <editorial_player_key>nfl.p.24171</editorial_player_key>        
            <editorial_team_key>nfl.t.23</editorial_team_key>        
            <editorial_team_full_name>Pittsburgh Steelers</editorial_team_full_name>        
            <editorial_team_abbr>Pit</editorial_team_abbr>        
            <bye_weeks>          
               <week>7</week>          
            </bye_weeks>        
            <uniform_number>84</uniform_number>        
            <display_position>WR</display_position>        
            <headshot>          
               <url>https://s.yimg.com/iu/api/res/1.2/ImJACC_rt5ql2NHxT40_gw--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08212018/24171.png</url>          
               <size>small</size>          
            </headshot>        
            <image_url>https://s.yimg.com/iu/api/res/1.2/ImJACC_rt5ql2NHxT40_gw--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08212018/24171.png</image_url>        
            <is_undroppable>0</is_undroppable>        
            <position_type>O</position_type>        
            <eligible_positions>          
               <position>WR</position>          
            </eligible_positions>        
            <draft_analysis>          
               <average_pick>5.0</average_pick>          
               <average_round>1.0</average_round>          
               <average_cost>61.4</average_cost>          
               <percent_drafted>1.00</percent_drafted>          
            </draft_analysis>        
            <percent_owned>          
               <coverage_type>week</coverage_type>          
               <week>1</week>          
               <value>100</value>          
               <delta>0</delta>          
            </percent_owned>        
         </player>      
         <player>        
            <player_key>380.p.30972</player_key>        
            <player_id>30972</player_id>        
            <name>          
               <full>Saquon Barkley</full>          
               <first>Saquon</first>          
               <last>Barkley</last>          
               <ascii_first>Saquon</ascii_first>          
               <ascii_last>Barkley</ascii_last>          
            </name>        
            <editorial_player_key>nfl.p.30972</editorial_player_key>        
            <editorial_team_key>nfl.t.19</editorial_team_key>        
            <editorial_team_full_name>New York Giants</editorial_team_full_name>        
            <editorial_team_abbr>NYG</editorial_team_abbr>        
            <bye_weeks>          
               <week>9</week>          
            </bye_weeks>        
            <uniform_number>26</uniform_number>        
            <display_position>RB</display_position>        
            <headshot>          
               <url>https://s.yimg.com/iu/api/res/1.2/QrLazFupWOTD6HuG7VZetg--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08232018/30972.png</url>          
               <size>small</size>          
            </headshot>        
            <image_url>https://s.yimg.com/iu/api/res/1.2/QrLazFupWOTD6HuG7VZetg--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08232018/30972.png</image_url>        
            <is_undroppable>0</is_undroppable>        
            <position_type>O</position_type>        
            <eligible_positions>          
               <position>RB</position>          
            </eligible_positions>        
            <has_player_notes>1</has_player_notes>        
            <draft_analysis>          
               <average_pick>7.5</average_pick>          
               <average_round>1.2</average_round>          
               <average_cost>57.1</average_cost>          
               <percent_drafted>1.00</percent_drafted>          
            </draft_analysis>        
            <percent_owned>          
               <coverage_type>week</coverage_type>          
               <week>1</week>          
               <value>100</value>          
               <delta>0</delta>          
            </percent_owned>        
         </player>      
         <player>        
            <player_key>380.p.30180</player_key>        
            <player_id>30180</player_id>        
            <name>          
               <full>Alvin Kamara</full>          
               <first>Alvin</first>          
               <last>Kamara</last>          
               <ascii_first>Alvin</ascii_first>          
               <ascii_last>Kamara</ascii_last>          
            </name>        
            <editorial_player_key>nfl.p.30180</editorial_player_key>        
            <editorial_team_key>nfl.t.18</editorial_team_key>        
            <editorial_team_full_name>New Orleans Saints</editorial_team_full_name>        
            <editorial_team_abbr>NO</editorial_team_abbr>        
            <bye_weeks>          
               <week>6</week>          
            </bye_weeks>        
            <uniform_number>41</uniform_number>        
            <display_position>RB</display_position>        
            <headshot>          
               <url>https://s.yimg.com/iu/api/res/1.2/7A96_Mp9YBaFvXY59Uipew--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08252018/30180.png</url>          
               <size>small</size>          
            </headshot>        
            <image_url>https://s.yimg.com/iu/api/res/1.2/7A96_Mp9YBaFvXY59Uipew--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08252018/30180.png</image_url>        
            <is_undroppable>0</is_undroppable>        
            <position_type>O</position_type>        
            <eligible_positions>          
               <position>RB</position>          
            </eligible_positions>        
            <has_player_notes>1</has_player_notes>        
            <draft_analysis>          
               <average_pick>6.8</average_pick>          
               <average_round>1.1</average_round>          
               <average_cost>60.2</average_cost>          
               <percent_drafted>1.00</percent_drafted>          
            </draft_analysis>        
            <percent_owned>          
               <coverage_type>week</coverage_type>          
               <week>1</week>          
               <value>100</value>          
               <delta>0</delta>          
            </percent_owned>        
         </player>      
         <player>        
            <player_key>380.p.26650</player_key>        
            <player_id>26650</player_id>        
            <name>          
               <full>DeAndre Hopkins</full>          
               <first>DeAndre</first>          
               <last>Hopkins</last>          
               <ascii_first>DeAndre</ascii_first>          
               <ascii_last>Hopkins</ascii_last>          
            </name>        
            <editorial_player_key>nfl.p.26650</editorial_player_key>        
            <editorial_team_key>nfl.t.34</editorial_team_key>        
            <editorial_team_full_name>Houston Texans</editorial_team_full_name>        
            <editorial_team_abbr>Hou</editorial_team_abbr>        
            <bye_weeks>          
               <week>10</week>          
            </bye_weeks>        
            <uniform_number>10</uniform_number>        
            <display_position>WR</display_position>        
            <headshot>          
               <url>https://s.yimg.com/iu/api/res/1.2/yZDrmUs3Sg2oIrO4x3Pf0Q--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08212018/26650.png</url>          
               <size>small</size>          
            </headshot>        
            <image_url>https://s.yimg.com/iu/api/res/1.2/yZDrmUs3Sg2oIrO4x3Pf0Q--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08212018/26650.png</image_url>        
            <is_undroppable>0</is_undroppable>        
            <position_type>O</position_type>        
            <eligible_positions>          
               <position>WR</position>          
            </eligible_positions>        
            <has_player_notes>1</has_player_notes>        
            <draft_analysis>          
               <average_pick>8.5</average_pick>          
               <average_round>1.2</average_round>          
               <average_cost>56.9</average_cost>          
               <percent_drafted>1.00</percent_drafted>          
            </draft_analysis>        
            <percent_owned>          
               <coverage_type>week</coverage_type>          
               <week>1</week>          
               <value>100</value>          
               <delta>0</delta>          
            </percent_owned>        
         </player>      
         <player>        
            <player_key>380.p.27540</player_key>        
            <player_id>27540</player_id>        
            <name>          
               <full>Odell Beckham Jr.</full>          
               <first>Odell</first>          
               <last>Beckham Jr.</last>          
               <ascii_first>Odell</ascii_first>          
               <ascii_last>Beckham Jr.</ascii_last>          
            </name>        
            <editorial_player_key>nfl.p.27540</editorial_player_key>        
            <editorial_team_key>nfl.t.19</editorial_team_key>        
            <editorial_team_full_name>New York Giants</editorial_team_full_name>        
            <editorial_team_abbr>NYG</editorial_team_abbr>        
            <bye_weeks>          
               <week>9</week>          
            </bye_weeks>        
            <uniform_number>13</uniform_number>        
            <display_position>WR</display_position>        
            <headshot>          
               <url>https://s.yimg.com/iu/api/res/1.2/_RGqQklqk4yOvHxwthf0AA--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08232018/27540.png</url>          
               <size>small</size>          
            </headshot>        
            <image_url>https://s.yimg.com/iu/api/res/1.2/_RGqQklqk4yOvHxwthf0AA--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08232018/27540.png</image_url>        
            <is_undroppable>0</is_undroppable>        
            <position_type>O</position_type>        
            <eligible_positions>          
               <position>WR</position>          
            </eligible_positions>        
            <has_player_notes>1</has_player_notes>        
            <draft_analysis>          
               <average_pick>9.9</average_pick>          
               <average_round>1.3</average_round>          
               <average_cost>54.5</average_cost>          
               <percent_drafted>1.00</percent_drafted>          
            </draft_analysis>        
            <percent_owned>          
               <coverage_type>week</coverage_type>          
               <week>1</week>          
               <value>100</value>          
               <delta>0</delta>          
            </percent_owned>        
         </player>      
         <player>        
            <player_key>380.p.28403</player_key>        
            <player_id>28403</player_id>        
            <name>          
               <full>Melvin Gordon</full>          
               <first>Melvin</first>          
               <last>Gordon</last>          
               <ascii_first>Melvin</ascii_first>          
               <ascii_last>Gordon</ascii_last>          
            </name>        
            <status>Q</status>        
            <status_full>Questionable</status_full>        
            <editorial_player_key>nfl.p.28403</editorial_player_key>        
            <editorial_team_key>nfl.t.24</editorial_team_key>        
            <editorial_team_full_name>Los Angeles Chargers</editorial_team_full_name>        
            <editorial_team_abbr>LAC</editorial_team_abbr>        
            <bye_weeks>          
               <week>8</week>          
            </bye_weeks>        
            <uniform_number>28</uniform_number>        
            <display_position>RB</display_position>        
            <headshot>          
               <url>https://s.yimg.com/iu/api/res/1.2/bMoDjDdF0xmJ3ChALe7dSg--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08262018/28403.png</url>          
               <size>small</size>          
            </headshot>        
            <image_url>https://s.yimg.com/iu/api/res/1.2/bMoDjDdF0xmJ3ChALe7dSg--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08262018/28403.png</image_url>        
            <is_undroppable>0</is_undroppable>        
            <position_type>O</position_type>        
            <eligible_positions>          
               <position>RB</position>          
            </eligible_positions>        
            <draft_analysis>          
               <average_pick>12.9</average_pick>          
               <average_round>1.9</average_round>          
               <average_cost>52.3</average_cost>          
               <percent_drafted>1.00</percent_drafted>          
            </draft_analysis>        
            <percent_owned>          
               <coverage_type>week</coverage_type>          
               <week>1</week>          
               <value>100</value>          
               <delta>0</delta>          
            </percent_owned>        
         </player>      
         <player>        
            <player_key>380.p.24793</player_key>        
            <player_id>24793</player_id>        
            <name>          
               <full>Julio Jones</full>          
               <first>Julio</first>          
               <last>Jones</last>          
               <ascii_first>Julio</ascii_first>          
               <ascii_last>Jones</ascii_last>          
            </name>        
            <editorial_player_key>nfl.p.24793</editorial_player_key>        
            <editorial_team_key>nfl.t.1</editorial_team_key>        
            <editorial_team_full_name>Atlanta Falcons</editorial_team_full_name>        
            <editorial_team_abbr>Atl</editorial_team_abbr>        
            <bye_weeks>          
               <week>8</week>          
            </bye_weeks>        
            <uniform_number>11</uniform_number>        
            <display_position>WR</display_position>        
            <headshot>          
               <url>https://s.yimg.com/iu/api/res/1.2/1dSy_kq454iOPS7WubUk3Q--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08222018/24793.png</url>          
               <size>small</size>          
            </headshot>        
            <image_url>https://s.yimg.com/iu/api/res/1.2/1dSy_kq454iOPS7WubUk3Q--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08222018/24793.png</image_url>        
            <is_undroppable>0</is_undroppable>        
            <position_type>O</position_type>        
            <eligible_positions>          
               <position>WR</position>          
            </eligible_positions>        
            <has_player_notes>1</has_player_notes>        
            <draft_analysis>          
               <average_pick>11.4</average_pick>          
               <average_round>1.7</average_round>          
               <average_cost>52.7</average_cost>          
               <percent_drafted>1.00</percent_drafted>          
            </draft_analysis>        
            <percent_owned>          
               <coverage_type>week</coverage_type>          
               <week>1</week>          
               <value>100</value>          
               <delta>0</delta>          
            </percent_owned>        
         </player>      
         <player>        
            <player_key>380.p.29281</player_key>        
            <player_id>29281</player_id>        
            <name>          
               <full>Michael Thomas</full>          
               <first>Michael</first>          
               <last>Thomas</last>          
               <ascii_first>Michael</ascii_first>          
               <ascii_last>Thomas</ascii_last>          
            </name>        
            <editorial_player_key>nfl.p.29281</editorial_player_key>        
            <editorial_team_key>nfl.t.18</editorial_team_key>        
            <editorial_team_full_name>New Orleans Saints</editorial_team_full_name>        
            <editorial_team_abbr>NO</editorial_team_abbr>        
            <bye_weeks>          
               <week>6</week>          
            </bye_weeks>        
            <uniform_number>13</uniform_number>        
            <display_position>WR</display_position>        
            <headshot>          
               <url>https://s.yimg.com/iu/api/res/1.2/FAlfbFaDH6cPfTBBL9cP6w--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08252018/29281.png</url>          
               <size>small</size>          
            </headshot>        
            <image_url>https://s.yimg.com/iu/api/res/1.2/FAlfbFaDH6cPfTBBL9cP6w--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08252018/29281.png</image_url>        
            <is_undroppable>0</is_undroppable>        
            <position_type>O</position_type>        
            <eligible_positions>          
               <position>WR</position>          
            </eligible_positions>        
            <draft_analysis>          
               <average_pick>14.3</average_pick>          
               <average_round>2.1</average_round>          
               <average_cost>46.9</average_cost>          
               <percent_drafted>1.00</percent_drafted>          
            </draft_analysis>        
            <percent_owned>          
               <coverage_type>week</coverage_type>          
               <week>1</week>          
               <value>100</value>          
               <delta>0</delta>          
            </percent_owned>        
         </player>      
         <player>        
            <player_key>380.p.30199</player_key>        
            <player_id>30199</player_id>        
            <name>          
               <full>Kareem Hunt</full>          
               <first>Kareem</first>          
               <last>Hunt</last>          
               <ascii_first>Kareem</ascii_first>          
               <ascii_last>Hunt</ascii_last>          
            </name>        
            <editorial_player_key>nfl.p.30199</editorial_player_key>        
            <editorial_team_key>nfl.t.12</editorial_team_key>        
            <editorial_team_full_name>Kansas City Chiefs</editorial_team_full_name>        
            <editorial_team_abbr>KC</editorial_team_abbr>        
            <bye_weeks>          
               <week>12</week>          
            </bye_weeks>        
            <uniform_number>27</uniform_number>        
            <display_position>RB</display_position>        
            <headshot>          
               <url>https://s.yimg.com/iu/api/res/1.2/yuO.eVIZo4KnBH63whFK2Q--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08282018/30199.png</url>          
               <size>small</size>          
            </headshot>        
            <image_url>https://s.yimg.com/iu/api/res/1.2/yuO.eVIZo4KnBH63whFK2Q--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08282018/30199.png</image_url>        
            <is_undroppable>0</is_undroppable>        
            <position_type>O</position_type>        
            <eligible_positions>          
               <position>RB</position>          
            </eligible_positions>        
            <has_player_notes>1</has_player_notes>        
            <draft_analysis>          
               <average_pick>11.1</average_pick>          
               <average_round>1.7</average_round>          
               <average_cost>54.7</average_cost>          
               <percent_drafted>1.00</percent_drafted>          
            </draft_analysis>        
            <percent_owned>          
               <coverage_type>week</coverage_type>          
               <week>1</week>          
               <value>100</value>          
               <delta>0</delta>          
            </percent_owned>        
         </player>      
         <player>        
            <player_key>380.p.26699</player_key>        
            <player_id>26699</player_id>        
            <name>          
               <full>Keenan Allen</full>          
               <first>Keenan</first>          
               <last>Allen</last>          
               <ascii_first>Keenan</ascii_first>          
               <ascii_last>Allen</ascii_last>          
            </name>        
            <editorial_player_key>nfl.p.26699</editorial_player_key>        
            <editorial_team_key>nfl.t.24</editorial_team_key>        
            <editorial_team_full_name>Los Angeles Chargers</editorial_team_full_name>        
            <editorial_team_abbr>LAC</editorial_team_abbr>        
            <bye_weeks>          
               <week>8</week>          
            </bye_weeks>        
            <uniform_number>13</uniform_number>        
            <display_position>WR</display_position>        
            <headshot>          
               <url>https://s.yimg.com/iu/api/res/1.2/UEud_xdjAangoqjW6GXluQ--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08262018/26699.png</url>          
               <size>small</size>          
            </headshot>        
            <image_url>https://s.yimg.com/iu/api/res/1.2/UEud_xdjAangoqjW6GXluQ--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08262018/26699.png</image_url>        
            <is_undroppable>0</is_undroppable>        
            <position_type>O</position_type>        
            <eligible_positions>          
               <position>WR</position>          
            </eligible_positions>        
            <draft_analysis>          
               <average_pick>16.8</average_pick>          
               <average_round>2.2</average_round>          
               <average_cost>44.1</average_cost>          
               <percent_drafted>1.00</percent_drafted>          
            </draft_analysis>        
            <percent_owned>          
               <coverage_type>week</coverage_type>          
               <week>1</week>          
               <value>100</value>          
               <delta>0</delta>          
            </percent_owned>        
         </player>      
         <player>        
            <player_key>380.p.27581</player_key>        
            <player_id>27581</player_id>        
            <name>          
               <full>Davante Adams</full>          
               <first>Davante</first>          
               <last>Adams</last>          
               <ascii_first>Davante</ascii_first>          
               <ascii_last>Adams</ascii_last>          
            </name>        
            <editorial_player_key>nfl.p.27581</editorial_player_key>        
            <editorial_team_key>nfl.t.9</editorial_team_key>        
            <editorial_team_full_name>Green Bay Packers</editorial_team_full_name>        
            <editorial_team_abbr>GB</editorial_team_abbr>        
            <bye_weeks>          
               <week>7</week>          
            </bye_weeks>        
            <uniform_number>17</uniform_number>        
            <display_position>WR</display_position>        
            <headshot>          
               <url>https://s.yimg.com/iu/api/res/1.2/FsSM1k8ol7XaTLtkHVrA1A--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08212018/27581.png</url>          
               <size>small</size>          
            </headshot>        
            <image_url>https://s.yimg.com/iu/api/res/1.2/FsSM1k8ol7XaTLtkHVrA1A--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08212018/27581.png</image_url>        
            <is_undroppable>0</is_undroppable>        
            <position_type>O</position_type>        
            <eligible_positions>          
               <position>WR</position>          
            </eligible_positions>        
            <draft_analysis>          
               <average_pick>17.8</average_pick>          
               <average_round>2.3</average_round>          
               <average_cost>42.8</average_cost>          
               <percent_drafted>1.00</percent_drafted>          
            </draft_analysis>        
            <percent_owned>          
               <coverage_type>week</coverage_type>          
               <week>1</week>          
               <value>100</value>          
               <delta>0</delta>          
            </percent_owned>        
         </player>      
         <player>        
            <player_key>380.p.30117</player_key>        
            <player_id>30117</player_id>        
            <name>          
               <full>Leonard Fournette</full>          
               <first>Leonard</first>          
               <last>Fournette</last>          
               <ascii_first>Leonard</ascii_first>          
               <ascii_last>Fournette</ascii_last>          
            </name>        
            <editorial_player_key>nfl.p.30117</editorial_player_key>        
            <editorial_team_key>nfl.t.30</editorial_team_key>        
            <editorial_team_full_name>Jacksonville Jaguars</editorial_team_full_name>        
            <editorial_team_abbr>Jax</editorial_team_abbr>        
            <bye_weeks>          
               <week>9</week>          
            </bye_weeks>        
            <uniform_number>27</uniform_number>        
            <display_position>RB</display_position>        
            <headshot>          
               <url>https://s.yimg.com/iu/api/res/1.2/PxIVNC6zaw20NDHFH5duAQ--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08232018/30117.png</url>          
               <size>small</size>          
            </headshot>        
            <image_url>https://s.yimg.com/iu/api/res/1.2/PxIVNC6zaw20NDHFH5duAQ--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08232018/30117.png</image_url>        
            <is_undroppable>0</is_undroppable>        
            <position_type>O</position_type>        
            <eligible_positions>          
               <position>RB</position>          
            </eligible_positions>        
            <has_player_notes>1</has_player_notes>        
            <draft_analysis>          
               <average_pick>15.4</average_pick>          
               <average_round>2.1</average_round>          
               <average_cost>47.3</average_cost>          
               <percent_drafted>1.00</percent_drafted>          
            </draft_analysis>        
            <percent_owned>          
               <coverage_type>week</coverage_type>          
               <week>1</week>          
               <value>100</value>          
               <delta>0</delta>          
            </percent_owned>        
         </player>      
         <player>        
            <player_key>380.p.24791</player_key>        
            <player_id>24791</player_id>        
            <name>          
               <full>A.J. Green</full>          
               <first>A.J.</first>          
               <last>Green</last>          
               <ascii_first>A.J.</ascii_first>          
               <ascii_last>Green</ascii_last>          
            </name>        
            <editorial_player_key>nfl.p.24791</editorial_player_key>        
            <editorial_team_key>nfl.t.4</editorial_team_key>        
            <editorial_team_full_name>Cincinnati Bengals</editorial_team_full_name>        
            <editorial_team_abbr>Cin</editorial_team_abbr>        
            <bye_weeks>          
               <week>9</week>          
            </bye_weeks>        
            <uniform_number>18</uniform_number>        
            <display_position>WR</display_position>        
            <headshot>          
               <url>https://s.yimg.com/iu/api/res/1.2/IM8_hBPAyznTCwHbfqLptw--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08222018/24791.png</url>          
               <size>small</size>          
            </headshot>        
            <image_url>https://s.yimg.com/iu/api/res/1.2/IM8_hBPAyznTCwHbfqLptw--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08222018/24791.png</image_url>        
            <is_undroppable>0</is_undroppable>        
            <position_type>O</position_type>        
            <eligible_positions>          
               <position>WR</position>          
            </eligible_positions>        
            <has_player_notes>1</has_player_notes>        
            <draft_analysis>          
               <average_pick>18.7</average_pick>          
               <average_round>2.3</average_round>          
               <average_cost>39.5</average_cost>          
               <percent_drafted>1.00</percent_drafted>          
            </draft_analysis>        
            <percent_owned>          
               <coverage_type>week</coverage_type>          
               <week>1</week>          
               <value>100</value>          
               <delta>0</delta>          
            </percent_owned>        
         </player>      
         <player>        
            <player_key>380.p.30154</player_key>        
            <player_id>30154</player_id>        
            <name>          
               <full>Dalvin Cook</full>          
               <first>Dalvin</first>          
               <last>Cook</last>          
               <ascii_first>Dalvin</ascii_first>          
               <ascii_last>Cook</ascii_last>          
            </name>        
            <editorial_player_key>nfl.p.30154</editorial_player_key>        
            <editorial_team_key>nfl.t.16</editorial_team_key>        
            <editorial_team_full_name>Minnesota Vikings</editorial_team_full_name>        
            <editorial_team_abbr>Min</editorial_team_abbr>        
            <bye_weeks>          
               <week>10</week>          
            </bye_weeks>        
            <uniform_number>33</uniform_number>        
            <display_position>RB</display_position>        
            <headshot>          
               <url>https://s.yimg.com/iu/api/res/1.2/Q.RrjEoZWmMgYj.FbT6z0Q--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08222018/30154.png</url>          
               <size>small</size>          
            </headshot>        
            <image_url>https://s.yimg.com/iu/api/res/1.2/Q.RrjEoZWmMgYj.FbT6z0Q--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08222018/30154.png</image_url>        
            <is_undroppable>0</is_undroppable>        
            <position_type>O</position_type>        
            <eligible_positions>          
               <position>RB</position>          
            </eligible_positions>        
            <has_player_notes>1</has_player_notes>        
            <draft_analysis>          
               <average_pick>17.7</average_pick>          
               <average_round>2.3</average_round>          
               <average_cost>45.0</average_cost>          
               <percent_drafted>1.00</percent_drafted>          
            </draft_analysis>        
            <percent_owned>          
               <coverage_type>week</coverage_type>          
               <week>1</week>          
               <value>100</value>          
               <delta>0</delta>          
            </percent_owned>        
         </player>      
         <player>        
            <player_key>380.p.27535</player_key>        
            <player_id>27535</player_id>        
            <name>          
               <full>Mike Evans</full>          
               <first>Mike</first>          
               <last>Evans</last>          
               <ascii_first>Mike</ascii_first>          
               <ascii_last>Evans</ascii_last>          
            </name>        
            <editorial_player_key>nfl.p.27535</editorial_player_key>        
            <editorial_team_key>nfl.t.27</editorial_team_key>        
            <editorial_team_full_name>Tampa Bay Buccaneers</editorial_team_full_name>        
            <editorial_team_abbr>TB</editorial_team_abbr>        
            <bye_weeks>          
               <week>5</week>          
            </bye_weeks>        
            <uniform_number>13</uniform_number>        
            <display_position>WR</display_position>        
            <headshot>          
               <url>https://s.yimg.com/iu/api/res/1.2/y5nlfg.OhA29vgI4ILVl6g--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08272018/27535.png</url>          
               <size>small</size>          
            </headshot>        
            <image_url>https://s.yimg.com/iu/api/res/1.2/y5nlfg.OhA29vgI4ILVl6g--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08272018/27535.png</image_url>        
            <is_undroppable>0</is_undroppable>        
            <position_type>O</position_type>        
            <eligible_positions>          
               <position>WR</position>          
            </eligible_positions>        
            <has_player_notes>1</has_player_notes>        
            <draft_analysis>          
               <average_pick>22.7</average_pick>          
               <average_round>2.8</average_round>          
               <average_cost>34.6</average_cost>          
               <percent_drafted>1.00</percent_drafted>          
            </draft_analysis>        
            <percent_owned>          
               <coverage_type>week</coverage_type>          
               <week>1</week>          
               <value>100</value>          
               <delta>0</delta>          
            </percent_owned>        
         </player>      
         <player>        
            <player_key>380.p.24017</player_key>        
            <player_id>24017</player_id>        
            <name>          
               <full>Rob Gronkowski</full>          
               <first>Rob</first>          
               <last>Gronkowski</last>          
               <ascii_first>Rob</ascii_first>          
               <ascii_last>Gronkowski</ascii_last>          
            </name>        
            <editorial_player_key>nfl.p.24017</editorial_player_key>        
            <editorial_team_key>nfl.t.17</editorial_team_key>        
            <editorial_team_full_name>New England Patriots</editorial_team_full_name>        
            <editorial_team_abbr>NE</editorial_team_abbr>        
            <bye_weeks>          
               <week>11</week>          
            </bye_weeks>        
            <uniform_number>87</uniform_number>        
            <display_position>TE</display_position>        
            <headshot>          
               <url>https://s.yimg.com/iu/api/res/1.2/Qnkswpez0N.a_H.RgWkN6Q--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08212018/24017.png</url>          
               <size>small</size>          
            </headshot>        
            <image_url>https://s.yimg.com/iu/api/res/1.2/Qnkswpez0N.a_H.RgWkN6Q--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08212018/24017.png</image_url>        
            <is_undroppable>0</is_undroppable>        
            <position_type>O</position_type>        
            <eligible_positions>          
               <position>TE</position>          
            </eligible_positions>        
            <has_player_notes>1</has_player_notes>        
            <draft_analysis>          
               <average_pick>19.6</average_pick>          
               <average_round>2.5</average_round>          
               <average_cost>39.2</average_cost>          
               <percent_drafted>1.00</percent_drafted>          
            </draft_analysis>        
            <percent_owned>          
               <coverage_type>week</coverage_type>          
               <week>1</week>          
               <value>100</value>          
               <delta>0</delta>          
            </percent_owned>        
         </player>      
         <player>        
            <player_key>380.p.28534</player_key>        
            <player_id>28534</player_id>        
            <name>          
               <full>Stefon Diggs</full>          
               <first>Stefon</first>          
               <last>Diggs</last>          
               <ascii_first>Stefon</ascii_first>          
               <ascii_last>Diggs</ascii_last>          
            </name>        
            <editorial_player_key>nfl.p.28534</editorial_player_key>        
            <editorial_team_key>nfl.t.16</editorial_team_key>        
            <editorial_team_full_name>Minnesota Vikings</editorial_team_full_name>        
            <editorial_team_abbr>Min</editorial_team_abbr>        
            <bye_weeks>          
               <week>10</week>          
            </bye_weeks>        
            <uniform_number>14</uniform_number>        
            <display_position>WR</display_position>        
            <headshot>          
               <url>https://s.yimg.com/iu/api/res/1.2/63b0CbC.WRpNNvGa74BpXw--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08222018/28534.png</url>          
               <size>small</size>          
            </headshot>        
            <image_url>https://s.yimg.com/iu/api/res/1.2/63b0CbC.WRpNNvGa74BpXw--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08222018/28534.png</image_url>        
            <is_undroppable>0</is_undroppable>        
            <position_type>O</position_type>        
            <eligible_positions>          
               <position>WR</position>          
            </eligible_positions>        
            <has_player_notes>1</has_player_notes>        
            <draft_analysis>          
               <average_pick>29.1</average_pick>          
               <average_round>3.5</average_round>          
               <average_cost>24.1</average_cost>          
               <percent_drafted>1.00</percent_drafted>          
            </draft_analysis>        
            <percent_owned>          
               <coverage_type>week</coverage_type>          
               <week>1</week>          
               <value>100</value>          
               <delta>0</delta>          
            </percent_owned>        
         </player>      
         <player>        
            <player_key>380.p.26686</player_key>        
            <player_id>26686</player_id>        
            <name>          
               <full>Travis Kelce</full>          
               <first>Travis</first>          
               <last>Kelce</last>          
               <ascii_first>Travis</ascii_first>          
               <ascii_last>Kelce</ascii_last>          
            </name>        
            <editorial_player_key>nfl.p.26686</editorial_player_key>        
            <editorial_team_key>nfl.t.12</editorial_team_key>        
            <editorial_team_full_name>Kansas City Chiefs</editorial_team_full_name>        
            <editorial_team_abbr>KC</editorial_team_abbr>        
            <bye_weeks>          
               <week>12</week>          
            </bye_weeks>        
            <uniform_number>87</uniform_number>        
            <display_position>TE</display_position>        
            <headshot>          
               <url>https://s.yimg.com/iu/api/res/1.2/8a3tQ7GFVmjz5yFqGa6OWQ--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08282018/26686.png</url>          
               <size>small</size>          
            </headshot>        
            <image_url>https://s.yimg.com/iu/api/res/1.2/8a3tQ7GFVmjz5yFqGa6OWQ--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08282018/26686.png</image_url>        
            <is_undroppable>0</is_undroppable>        
            <position_type>O</position_type>        
            <eligible_positions>          
               <position>TE</position>          
            </eligible_positions>        
            <has_player_notes>1</has_player_notes>        
            <draft_analysis>          
               <average_pick>24.8</average_pick>          
               <average_round>3.1</average_round>          
               <average_cost>31.5</average_cost>          
               <percent_drafted>1.00</percent_drafted>          
            </draft_analysis>        
            <percent_owned>          
               <coverage_type>week</coverage_type>          
               <week>1</week>          
               <value>100</value>          
               <delta>0</delta>          
            </percent_owned>        
         </player>      
         <player>        
            <player_key>380.p.30121</player_key>        
            <player_id>30121</player_id>        
            <name>          
               <full>Christian McCaffrey</full>          
               <first>Christian</first>          
               <last>McCaffrey</last>          
               <ascii_first>Christian</ascii_first>          
               <ascii_last>McCaffrey</ascii_last>          
            </name>        
            <editorial_player_key>nfl.p.30121</editorial_player_key>        
            <editorial_team_key>nfl.t.29</editorial_team_key>        
            <editorial_team_full_name>Carolina Panthers</editorial_team_full_name>        
            <editorial_team_abbr>Car</editorial_team_abbr>        
            <bye_weeks>          
               <week>4</week>          
            </bye_weeks>        
            <uniform_number>22</uniform_number>        
            <display_position>RB</display_position>        
            <headshot>          
               <url>https://s.yimg.com/iu/api/res/1.2/I2Nua3.SXdJraKJ8Sbz4hQ--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08212018/30121.png</url>          
               <size>small</size>          
            </headshot>        
            <image_url>https://s.yimg.com/iu/api/res/1.2/I2Nua3.SXdJraKJ8Sbz4hQ--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08212018/30121.png</image_url>        
            <is_undroppable>0</is_undroppable>        
            <position_type>O</position_type>        
            <eligible_positions>          
               <position>RB</position>          
            </eligible_positions>        
            <has_player_notes>1</has_player_notes>        
            <draft_analysis>          
               <average_pick>25.7</average_pick>          
               <average_round>3.2</average_round>          
               <average_cost>34.6</average_cost>          
               <percent_drafted>1.00</percent_drafted>          
            </draft_analysis>        
            <percent_owned>          
               <coverage_type>week</coverage_type>          
               <week>1</week>          
               <value>100</value>          
               <delta>0</delta>          
            </percent_owned>        
         </player>      
         <player>        
            <player_key>380.p.27631</player_key>        
            <player_id>27631</player_id>        
            <name>          
               <full>Devonta Freeman</full>          
               <first>Devonta</first>          
               <last>Freeman</last>          
               <ascii_first>Devonta</ascii_first>          
               <ascii_last>Freeman</ascii_last>          
            </name>        
            <editorial_player_key>nfl.p.27631</editorial_player_key>        
            <editorial_team_key>nfl.t.1</editorial_team_key>        
            <editorial_team_full_name>Atlanta Falcons</editorial_team_full_name>        
            <editorial_team_abbr>Atl</editorial_team_abbr>        
            <bye_weeks>          
               <week>8</week>          
            </bye_weeks>        
            <uniform_number>24</uniform_number>        
            <display_position>RB</display_position>        
            <headshot>          
               <url>https://s.yimg.com/iu/api/res/1.2/._fMTmSt9DNlW5CuBXUrpw--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08222018/27631.png</url>          
               <size>small</size>          
            </headshot>        
            <image_url>https://s.yimg.com/iu/api/res/1.2/._fMTmSt9DNlW5CuBXUrpw--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08222018/27631.png</image_url>        
            <is_undroppable>0</is_undroppable>        
            <position_type>O</position_type>        
            <eligible_positions>          
               <position>RB</position>          
            </eligible_positions>        
            <has_player_notes>1</has_player_notes>        
            <draft_analysis>          
               <average_pick>23.6</average_pick>          
               <average_round>2.9</average_round>          
               <average_cost>36.1</average_cost>          
               <percent_drafted>1.00</percent_drafted>          
            </draft_analysis>        
            <percent_owned>          
               <coverage_type>week</coverage_type>          
               <week>1</week>          
               <value>100</value>          
               <delta>0</delta>          
            </percent_owned>        
         </player>      
         <player>        
            <player_key>380.p.27277</player_key>        
            <player_id>27277</player_id>        
            <name>          
               <full>Adam Thielen</full>          
               <first>Adam</first>          
               <last>Thielen</last>          
               <ascii_first>Adam</ascii_first>          
               <ascii_last>Thielen</ascii_last>          
            </name>        
            <status>Q</status>        
            <status_full>Questionable</status_full>        
            <editorial_player_key>nfl.p.27277</editorial_player_key>        
            <editorial_team_key>nfl.t.16</editorial_team_key>        
            <editorial_team_full_name>Minnesota Vikings</editorial_team_full_name>        
            <editorial_team_abbr>Min</editorial_team_abbr>        
            <bye_weeks>          
               <week>10</week>          
            </bye_weeks>        
            <uniform_number>19</uniform_number>        
            <display_position>WR</display_position>        
            <headshot>          
               <url>https://s.yimg.com/iu/api/res/1.2/_f7LGTo99FmWZBLzGRMQTA--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08222018/27277.png</url>          
               <size>small</size>          
            </headshot>        
            <image_url>https://s.yimg.com/iu/api/res/1.2/_f7LGTo99FmWZBLzGRMQTA--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08222018/27277.png</image_url>        
            <is_undroppable>0</is_undroppable>        
            <position_type>O</position_type>        
            <eligible_positions>          
               <position>WR</position>          
            </eligible_positions>        
            <has_player_notes>1</has_player_notes>        
            <draft_analysis>          
               <average_pick>26.2</average_pick>          
               <average_round>3.2</average_round>          
               <average_cost>27.5</average_cost>          
               <percent_drafted>1.00</percent_drafted>          
            </draft_analysis>        
            <percent_owned>          
               <coverage_type>week</coverage_type>          
               <week>1</week>          
               <value>100</value>          
               <delta>0</delta>          
            </percent_owned>        
         </player>      
      </players>    
   </game>  
</fantasy_content>
'''
__test_string_2 = '''<?xml version="1.0" ?><fantasy_content copyright="Data provided by Yahoo! and STATS, LLC" ns0:uri="http://fantasysports.yahooapis.com/fantasy/v2/game/nfl/players;count=25;out=draft_analysis,percent_owned;start=25" refresh_rate="60" time="189.26286697388ms" xml:lang="en-US" xmlns:ns0="http://www.yahooapis.com/v1/base.rng">  
   <game>    
      <game_key>380</game_key>    
      <game_id>380</game_id>    
      <name>Football</name>    
      <code>nfl</code>    
      <type>full</type>    
      <url>https://football.fantasysports.yahoo.com/f1</url>    
      <season>2018</season>    
      <is_registration_over>0</is_registration_over>    
      <is_game_over>0</is_game_over>    
      <is_offseason>0</is_offseason>    
      <players count="25">      
         <player>        
            <player_key>380.p.6762</player_key>        
            <player_id>6762</player_id>        
            <name>          
               <full>Larry Fitzgerald</full>          
               <first>Larry</first>          
               <last>Fitzgerald</last>          
               <ascii_first>Larry</ascii_first>          
               <ascii_last>Fitzgerald</ascii_last>          
            </name>        
            <editorial_player_key>nfl.p.6762</editorial_player_key>        
            <editorial_team_key>nfl.t.22</editorial_team_key>        
            <editorial_team_full_name>Arizona Cardinals</editorial_team_full_name>        
            <editorial_team_abbr>Ari</editorial_team_abbr>        
            <bye_weeks>          
               <week>9</week>          
            </bye_weeks>        
            <uniform_number>11</uniform_number>        
            <display_position>WR</display_position>        
            <headshot>          
               <url>https://s.yimg.com/iu/api/res/1.2/cHJ8jAKIKK9NEyridutGhw--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08222018/6762.png</url>          
               <size>small</size>          
            </headshot>        
            <image_url>https://s.yimg.com/iu/api/res/1.2/cHJ8jAKIKK9NEyridutGhw--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08222018/6762.png</image_url>        
            <is_undroppable>0</is_undroppable>        
            <position_type>O</position_type>        
            <eligible_positions>          
               <position>WR</position>          
            </eligible_positions>        
            <draft_analysis>          
               <average_pick>34.9</average_pick>          
               <average_round>4.0</average_round>          
               <average_cost>20.8</average_cost>          
               <percent_drafted>1.00</percent_drafted>          
            </draft_analysis>        
            <percent_owned>          
               <coverage_type>week</coverage_type>          
               <week>1</week>          
               <value>99</value>          
               <delta>0</delta>          
            </percent_owned>        
         </player>      
         <player>        
            <player_key>380.p.29399</player_key>        
            <player_id>29399</player_id>        
            <name>          
               <full>Tyreek Hill</full>          
               <first>Tyreek</first>          
               <last>Hill</last>          
               <ascii_first>Tyreek</ascii_first>          
               <ascii_last>Hill</ascii_last>          
            </name>        
            <editorial_player_key>nfl.p.29399</editorial_player_key>        
            <editorial_team_key>nfl.t.12</editorial_team_key>        
            <editorial_team_full_name>Kansas City Chiefs</editorial_team_full_name>        
            <editorial_team_abbr>KC</editorial_team_abbr>        
            <bye_weeks>          
               <week>12</week>          
            </bye_weeks>        
            <uniform_number>10</uniform_number>        
            <display_position>WR</display_position>        
            <headshot>          
               <url>https://s.yimg.com/iu/api/res/1.2/KGaqzv0n1HLlWNPV2NEetw--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08282018/29399.png</url>          
               <size>small</size>          
            </headshot>        
            <image_url>https://s.yimg.com/iu/api/res/1.2/KGaqzv0n1HLlWNPV2NEetw--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08282018/29399.png</image_url>        
            <is_undroppable>0</is_undroppable>        
            <position_type>O</position_type>        
            <eligible_positions>          
               <position>WR</position>          
            </eligible_positions>        
            <has_player_notes>1</has_player_notes>        
            <draft_analysis>          
               <average_pick>28.2</average_pick>          
               <average_round>3.4</average_round>          
               <average_cost>27.9</average_cost>          
               <percent_drafted>1.00</percent_drafted>          
            </draft_analysis>        
            <percent_owned>          
               <coverage_type>week</coverage_type>          
               <week>1</week>          
               <value>100</value>          
               <delta>0</delta>          
            </percent_owned>        
         </player>      
         <player>        
            <player_key>380.p.25105</player_key>        
            <player_id>25105</player_id>        
            <name>          
               <full>Doug Baldwin</full>          
               <first>Doug</first>          
               <last>Baldwin</last>          
               <ascii_first>Doug</ascii_first>          
               <ascii_last>Baldwin</ascii_last>          
            </name>        
            <status>Q</status>        
            <status_full>Questionable</status_full>        
            <editorial_player_key>nfl.p.25105</editorial_player_key>        
            <editorial_team_key>nfl.t.26</editorial_team_key>        
            <editorial_team_full_name>Seattle Seahawks</editorial_team_full_name>        
            <editorial_team_abbr>Sea</editorial_team_abbr>        
            <bye_weeks>          
               <week>7</week>          
            </bye_weeks>        
            <uniform_number>89</uniform_number>        
            <display_position>WR</display_position>        
            <headshot>          
               <url>https://s.yimg.com/iu/api/res/1.2/pcslXEt6lWz8Bg86Xf0Isw--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08212018/25105.png</url>          
               <size>small</size>          
            </headshot>        
            <image_url>https://s.yimg.com/iu/api/res/1.2/pcslXEt6lWz8Bg86Xf0Isw--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08212018/25105.png</image_url>        
            <is_undroppable>0</is_undroppable>        
            <position_type>O</position_type>        
            <eligible_positions>          
               <position>WR</position>          
            </eligible_positions>        
            <has_player_notes>1</has_player_notes>        
            <draft_analysis>          
               <average_pick>32.6</average_pick>          
               <average_round>3.8</average_round>          
               <average_cost>23.2</average_cost>          
               <percent_drafted>1.00</percent_drafted>          
            </draft_analysis>        
            <percent_owned>          
               <coverage_type>week</coverage_type>          
               <week>1</week>          
               <value>99</value>          
               <delta>0</delta>          
            </percent_owned>        
         </player>      
         <player>        
            <player_key>380.p.29384</player_key>        
            <player_id>29384</player_id>        
            <name>          
               <full>Jordan Howard</full>          
               <first>Jordan</first>          
               <last>Howard</last>          
               <ascii_first>Jordan</ascii_first>          
               <ascii_last>Howard</ascii_last>          
            </name>        
            <editorial_player_key>nfl.p.29384</editorial_player_key>        
            <editorial_team_key>nfl.t.3</editorial_team_key>        
            <editorial_team_full_name>Chicago Bears</editorial_team_full_name>        
            <editorial_team_abbr>Chi</editorial_team_abbr>        
            <bye_weeks>          
               <week>5</week>          
            </bye_weeks>        
            <uniform_number>24</uniform_number>        
            <display_position>RB</display_position>        
            <headshot>          
               <url>https://s.yimg.com/iu/api/res/1.2/DX64asZBlHmihxe55uM14A--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08282018/29384.png</url>          
               <size>small</size>          
            </headshot>        
            <image_url>https://s.yimg.com/iu/api/res/1.2/DX64asZBlHmihxe55uM14A--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08282018/29384.png</image_url>        
            <is_undroppable>0</is_undroppable>        
            <position_type>O</position_type>        
            <eligible_positions>          
               <position>RB</position>          
            </eligible_positions>        
            <has_player_notes>1</has_player_notes>        
            <draft_analysis>          
               <average_pick>28.9</average_pick>          
               <average_round>3.5</average_round>          
               <average_cost>30.6</average_cost>          
               <percent_drafted>1.00</percent_drafted>          
            </draft_analysis>        
            <percent_owned>          
               <coverage_type>week</coverage_type>          
               <week>1</week>          
               <value>99</value>          
               <delta>0</delta>          
            </percent_owned>        
         </player>      
         <player>        
            <player_key>380.p.25802</player_key>        
            <player_id>25802</player_id>        
            <name>          
               <full>T.Y. Hilton</full>          
               <first>T.Y.</first>          
               <last>Hilton</last>          
               <ascii_first>T.Y.</ascii_first>          
               <ascii_last>Hilton</ascii_last>          
            </name>        
            <editorial_player_key>nfl.p.25802</editorial_player_key>        
            <editorial_team_key>nfl.t.11</editorial_team_key>        
            <editorial_team_full_name>Indianapolis Colts</editorial_team_full_name>        
            <editorial_team_abbr>Ind</editorial_team_abbr>        
            <bye_weeks>          
               <week>9</week>          
            </bye_weeks>        
            <uniform_number>13</uniform_number>        
            <display_position>WR</display_position>        
            <headshot>          
               <url>https://s.yimg.com/iu/api/res/1.2/iuHT43oYRDVSYGn_LYGCyw--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08282018/25802.png</url>          
               <size>small</size>          
            </headshot>        
            <image_url>https://s.yimg.com/iu/api/res/1.2/iuHT43oYRDVSYGn_LYGCyw--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08282018/25802.png</image_url>        
            <is_undroppable>0</is_undroppable>        
            <position_type>O</position_type>        
            <eligible_positions>          
               <position>WR</position>          
            </eligible_positions>        
            <has_player_notes>1</has_player_notes>        
            <draft_analysis>          
               <average_pick>35.8</average_pick>          
               <average_round>4.2</average_round>          
               <average_cost>21.5</average_cost>          
               <percent_drafted>1.00</percent_drafted>          
            </draft_analysis>        
            <percent_owned>          
               <coverage_type>week</coverage_type>          
               <week>1</week>          
               <value>99</value>          
               <delta>0</delta>          
            </percent_owned>        
         </player>      
         <player>        
            <player_key>380.p.26658</player_key>        
            <player_id>26658</player_id>        
            <name>          
               <full>Zach Ertz</full>          
               <first>Zach</first>          
               <last>Ertz</last>          
               <ascii_first>Zach</ascii_first>          
               <ascii_last>Ertz</ascii_last>          
            </name>        
            <editorial_player_key>nfl.p.26658</editorial_player_key>        
            <editorial_team_key>nfl.t.21</editorial_team_key>        
            <editorial_team_full_name>Philadelphia Eagles</editorial_team_full_name>        
            <editorial_team_abbr>Phi</editorial_team_abbr>        
            <bye_weeks>          
               <week>9</week>          
            </bye_weeks>        
            <uniform_number>86</uniform_number>        
            <display_position>TE</display_position>        
            <headshot>          
               <url>https://s.yimg.com/iu/api/res/1.2/BjwWIvaNttNHkFS78HSWXQ--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08282018/26658.png</url>          
               <size>small</size>          
            </headshot>        
            <image_url>https://s.yimg.com/iu/api/res/1.2/BjwWIvaNttNHkFS78HSWXQ--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08282018/26658.png</image_url>        
            <is_undroppable>0</is_undroppable>        
            <position_type>O</position_type>        
            <eligible_positions>          
               <position>TE</position>          
            </eligible_positions>        
            <has_player_notes>1</has_player_notes>        
            <draft_analysis>          
               <average_pick>32.4</average_pick>          
               <average_round>3.8</average_round>          
               <average_cost>23.3</average_cost>          
               <percent_drafted>1.00</percent_drafted>          
            </draft_analysis>        
            <percent_owned>          
               <coverage_type>week</coverage_type>          
               <week>1</week>          
               <value>100</value>          
               <delta>0</delta>          
            </percent_owned>        
         </player>      
         <player>        
            <player_key>380.p.30161</player_key>        
            <player_id>30161</player_id>        
            <name>          
               <full>Joe Mixon</full>          
               <first>Joe</first>          
               <last>Mixon</last>          
               <ascii_first>Joe</ascii_first>          
               <ascii_last>Mixon</ascii_last>          
            </name>        
            <editorial_player_key>nfl.p.30161</editorial_player_key>        
            <editorial_team_key>nfl.t.4</editorial_team_key>        
            <editorial_team_full_name>Cincinnati Bengals</editorial_team_full_name>        
            <editorial_team_abbr>Cin</editorial_team_abbr>        
            <bye_weeks>          
               <week>9</week>          
            </bye_weeks>        
            <uniform_number>28</uniform_number>        
            <display_position>RB</display_position>        
            <headshot>          
               <url>https://s.yimg.com/iu/api/res/1.2/rzubkS7PamCIBHasank8lw--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08222018/30161.png</url>          
               <size>small</size>          
            </headshot>        
            <image_url>https://s.yimg.com/iu/api/res/1.2/rzubkS7PamCIBHasank8lw--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08222018/30161.png</image_url>        
            <is_undroppable>0</is_undroppable>        
            <position_type>O</position_type>        
            <eligible_positions>          
               <position>RB</position>          
            </eligible_positions>        
            <has_player_notes>1</has_player_notes>        
            <draft_analysis>          
               <average_pick>36.7</average_pick>          
               <average_round>4.3</average_round>          
               <average_cost>22.3</average_cost>          
               <percent_drafted>1.00</percent_drafted>          
            </draft_analysis>        
            <percent_owned>          
               <coverage_type>week</coverage_type>          
               <week>1</week>          
               <value>99</value>          
               <delta>0</delta>          
            </percent_owned>        
         </player>      
         <player>        
            <player_key>380.p.28392</player_key>        
            <player_id>28392</player_id>        
            <name>          
               <full>Amari Cooper</full>          
               <first>Amari</first>          
               <last>Cooper</last>          
               <ascii_first>Amari</ascii_first>          
               <ascii_last>Cooper</ascii_last>          
            </name>        
            <editorial_player_key>nfl.p.28392</editorial_player_key>        
            <editorial_team_key>nfl.t.13</editorial_team_key>        
            <editorial_team_full_name>Oakland Raiders</editorial_team_full_name>        
            <editorial_team_abbr>Oak</editorial_team_abbr>        
            <bye_weeks>          
               <week>7</week>          
            </bye_weeks>        
            <uniform_number>89</uniform_number>        
            <display_position>WR</display_position>        
            <headshot>          
               <url>https://s.yimg.com/iu/api/res/1.2/t7KktSAoBwL4Trr71unm7A--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08242018/28392.png</url>          
               <size>small</size>          
            </headshot>        
            <image_url>https://s.yimg.com/iu/api/res/1.2/t7KktSAoBwL4Trr71unm7A--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08242018/28392.png</image_url>        
            <is_undroppable>0</is_undroppable>        
            <position_type>O</position_type>        
            <eligible_positions>          
               <position>WR</position>          
            </eligible_positions>        
            <has_player_notes>1</has_player_notes>        
            <draft_analysis>          
               <average_pick>37.0</average_pick>          
               <average_round>4.3</average_round>          
               <average_cost>18.9</average_cost>          
               <percent_drafted>1.00</percent_drafted>          
            </draft_analysis>        
            <percent_owned>          
               <coverage_type>week</coverage_type>          
               <week>1</week>          
               <value>99</value>          
               <delta>0</delta>          
            </percent_owned>        
         </player>      
         <player>        
            <player_key>380.p.30175</player_key>        
            <player_id>30175</player_id>        
            <name>          
               <full>JuJu Smith-Schuster</full>          
               <first>JuJu</first>          
               <last>Smith-Schuster</last>          
               <ascii_first>JuJu</ascii_first>          
               <ascii_last>Smith-Schuster</ascii_last>          
            </name>        
            <editorial_player_key>nfl.p.30175</editorial_player_key>        
            <editorial_team_key>nfl.t.23</editorial_team_key>        
            <editorial_team_full_name>Pittsburgh Steelers</editorial_team_full_name>        
            <editorial_team_abbr>Pit</editorial_team_abbr>        
            <bye_weeks>          
               <week>7</week>          
            </bye_weeks>        
            <uniform_number>19</uniform_number>        
            <display_position>WR</display_position>        
            <headshot>          
               <url>https://s.yimg.com/iu/api/res/1.2/SKIoTgzo1RWhPiL8JkuStg--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08212018/30175.png</url>          
               <size>small</size>          
            </headshot>        
            <image_url>https://s.yimg.com/iu/api/res/1.2/SKIoTgzo1RWhPiL8JkuStg--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08212018/30175.png</image_url>        
            <is_undroppable>0</is_undroppable>        
            <position_type>O</position_type>        
            <eligible_positions>          
               <position>WR</position>          
            </eligible_positions>        
            <has_player_notes>1</has_player_notes>        
            <draft_analysis>          
               <average_pick>40.3</average_pick>          
               <average_round>4.6</average_round>          
               <average_cost>14.3</average_cost>          
               <percent_drafted>1.00</percent_drafted>          
            </draft_analysis>        
            <percent_owned>          
               <coverage_type>week</coverage_type>          
               <week>1</week>          
               <value>99</value>          
               <delta>0</delta>          
            </percent_owned>        
         </player>      
         <player>        
            <player_key>380.p.27624</player_key>        
            <player_id>27624</player_id>        
            <name>          
               <full>Jerick McKinnon</full>          
               <first>Jerick</first>          
               <last>McKinnon</last>          
               <ascii_first>Jerick</ascii_first>          
               <ascii_last>McKinnon</ascii_last>          
            </name>        
            <status>Q</status>        
            <status_full>Questionable</status_full>        
            <editorial_player_key>nfl.p.27624</editorial_player_key>        
            <editorial_team_key>nfl.t.25</editorial_team_key>        
            <editorial_team_full_name>San Francisco 49ers</editorial_team_full_name>        
            <editorial_team_abbr>SF</editorial_team_abbr>        
            <bye_weeks>          
               <week>11</week>          
            </bye_weeks>        
            <uniform_number>28</uniform_number>        
            <display_position>RB</display_position>        
            <headshot>          
               <url>https://s.yimg.com/iu/api/res/1.2/pNvJv736xkZPXGG3x2u7Rg--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08202018/27624.png</url>          
               <size>small</size>          
            </headshot>        
            <image_url>https://s.yimg.com/iu/api/res/1.2/pNvJv736xkZPXGG3x2u7Rg--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08202018/27624.png</image_url>        
            <is_undroppable>0</is_undroppable>        
            <position_type>O</position_type>        
            <eligible_positions>          
               <position>RB</position>          
            </eligible_positions>        
            <has_player_notes>1</has_player_notes>        
            <draft_analysis>          
               <average_pick>32.8</average_pick>          
               <average_round>3.8</average_round>          
               <average_cost>28.3</average_cost>          
               <percent_drafted>1.00</percent_drafted>          
            </draft_analysis>        
            <percent_owned>          
               <coverage_type>week</coverage_type>          
               <week>1</week>          
               <value>99</value>          
               <delta>0</delta>          
            </percent_owned>        
         </player>      
         <player>        
            <player_key>380.p.24035</player_key>        
            <player_id>24035</player_id>        
            <name>          
               <full>Golden Tate</full>          
               <first>Golden</first>          
               <last>Tate</last>          
               <ascii_first>Golden</ascii_first>          
               <ascii_last>Tate</ascii_last>          
            </name>        
            <editorial_player_key>nfl.p.24035</editorial_player_key>        
            <editorial_team_key>nfl.t.8</editorial_team_key>        
            <editorial_team_full_name>Detroit Lions</editorial_team_full_name>        
            <editorial_team_abbr>Det</editorial_team_abbr>        
            <bye_weeks>          
               <week>6</week>          
            </bye_weeks>        
            <uniform_number>15</uniform_number>        
            <display_position>WR</display_position>        
            <headshot>          
               <url>https://s.yimg.com/iu/api/res/1.2/3R_u166V5sj6bjZcmDiKPA--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08272018/24035.png</url>          
               <size>small</size>          
            </headshot>        
            <image_url>https://s.yimg.com/iu/api/res/1.2/3R_u166V5sj6bjZcmDiKPA--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08272018/24035.png</image_url>        
            <is_undroppable>0</is_undroppable>        
            <position_type>O</position_type>        
            <eligible_positions>          
               <position>WR</position>          
            </eligible_positions>        
            <has_player_notes>1</has_player_notes>        
            <draft_analysis>          
               <average_pick>48.3</average_pick>          
               <average_round>5.4</average_round>          
               <average_cost>12.8</average_cost>          
               <percent_drafted>1.00</percent_drafted>          
            </draft_analysis>        
            <percent_owned>          
               <coverage_type>week</coverage_type>          
               <week>1</week>          
               <value>98</value>          
               <delta>0</delta>          
            </percent_owned>        
         </player>      
         <player>        
            <player_key>380.p.7200</player_key>        
            <player_id>7200</player_id>        
            <name>          
               <full>Aaron Rodgers</full>          
               <first>Aaron</first>          
               <last>Rodgers</last>          
               <ascii_first>Aaron</ascii_first>          
               <ascii_last>Rodgers</ascii_last>          
            </name>        
            <editorial_player_key>nfl.p.7200</editorial_player_key>        
            <editorial_team_key>nfl.t.9</editorial_team_key>        
            <editorial_team_full_name>Green Bay Packers</editorial_team_full_name>        
            <editorial_team_abbr>GB</editorial_team_abbr>        
            <bye_weeks>          
               <week>7</week>          
            </bye_weeks>        
            <uniform_number>12</uniform_number>        
            <display_position>QB</display_position>        
            <headshot>          
               <url>https://s.yimg.com/iu/api/res/1.2/KAybTAwhxN0pAbtPslho1A--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08212018/7200.png</url>          
               <size>small</size>          
            </headshot>        
            <image_url>https://s.yimg.com/iu/api/res/1.2/KAybTAwhxN0pAbtPslho1A--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08212018/7200.png</image_url>        
            <is_undroppable>0</is_undroppable>        
            <position_type>O</position_type>        
            <eligible_positions>          
               <position>QB</position>          
            </eligible_positions>        
            <has_player_notes>1</has_player_notes>        
            <draft_analysis>          
               <average_pick>23.2</average_pick>          
               <average_round>2.9</average_round>          
               <average_cost>26.4</average_cost>          
               <percent_drafted>1.00</percent_drafted>          
            </draft_analysis>        
            <percent_owned>          
               <coverage_type>week</coverage_type>          
               <week>1</week>          
               <value>100</value>          
               <delta>0</delta>          
            </percent_owned>        
         </player>      
         <player>        
            <player_key>380.p.23997</player_key>        
            <player_id>23997</player_id>        
            <name>          
               <full>Demaryius Thomas</full>          
               <first>Demaryius</first>          
               <last>Thomas</last>          
               <ascii_first>Demaryius</ascii_first>          
               <ascii_last>Thomas</ascii_last>          
            </name>        
            <editorial_player_key>nfl.p.23997</editorial_player_key>        
            <editorial_team_key>nfl.t.7</editorial_team_key>        
            <editorial_team_full_name>Denver Broncos</editorial_team_full_name>        
            <editorial_team_abbr>Den</editorial_team_abbr>        
            <bye_weeks>          
               <week>10</week>          
            </bye_weeks>        
            <uniform_number>88</uniform_number>        
            <display_position>WR</display_position>        
            <headshot>          
               <url>https://s.yimg.com/iu/api/res/1.2/x0bYG2c5Zz0ERJJbFiUAdQ--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08222018/23997.png</url>          
               <size>small</size>          
            </headshot>        
            <image_url>https://s.yimg.com/iu/api/res/1.2/x0bYG2c5Zz0ERJJbFiUAdQ--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08222018/23997.png</image_url>        
            <is_undroppable>0</is_undroppable>        
            <position_type>O</position_type>        
            <eligible_positions>          
               <position>WR</position>          
            </eligible_positions>        
            <has_player_notes>1</has_player_notes>        
            <draft_analysis>          
               <average_pick>43.3</average_pick>          
               <average_round>4.9</average_round>          
               <average_cost>15.4</average_cost>          
               <percent_drafted>1.00</percent_drafted>          
            </draft_analysis>        
            <percent_owned>          
               <coverage_type>week</coverage_type>          
               <week>1</week>          
               <value>99</value>          
               <delta>0</delta>          
            </percent_owned>        
         </player>      
         <player>        
            <player_key>380.p.24788</player_key>        
            <player_id>24788</player_id>        
            <name>          
               <full>Cam Newton</full>          
               <first>Cam</first>          
               <last>Newton</last>          
               <ascii_first>Cam</ascii_first>          
               <ascii_last>Newton</ascii_last>          
            </name>        
            <editorial_player_key>nfl.p.24788</editorial_player_key>        
            <editorial_team_key>nfl.t.29</editorial_team_key>        
            <editorial_team_full_name>Carolina Panthers</editorial_team_full_name>        
            <editorial_team_abbr>Car</editorial_team_abbr>        
            <bye_weeks>          
               <week>4</week>          
            </bye_weeks>        
            <uniform_number>1</uniform_number>        
            <display_position>QB</display_position>        
            <headshot>          
               <url>https://s.yimg.com/iu/api/res/1.2/Q1ziSQG6UAf7iID63Nj9YQ--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08212018/24788.png</url>          
               <size>small</size>          
            </headshot>        
            <image_url>https://s.yimg.com/iu/api/res/1.2/Q1ziSQG6UAf7iID63Nj9YQ--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08212018/24788.png</image_url>        
            <is_undroppable>0</is_undroppable>        
            <position_type>O</position_type>        
            <eligible_positions>          
               <position>QB</position>          
            </eligible_positions>        
            <has_player_notes>1</has_player_notes>        
            <draft_analysis>          
               <average_pick>47.0</average_pick>          
               <average_round>5.3</average_round>          
               <average_cost>10.0</average_cost>          
               <percent_drafted>1.00</percent_drafted>          
            </draft_analysis>        
            <percent_owned>          
               <coverage_type>week</coverage_type>          
               <week>1</week>          
               <value>100</value>          
               <delta>0</delta>          
            </percent_owned>        
         </player>      
         <player>        
            <player_key>380.p.29405</player_key>        
            <player_id>29405</player_id>        
            <name>          
               <full>Alex Collins</full>          
               <first>Alex</first>          
               <last>Collins</last>          
               <ascii_first>Alex</ascii_first>          
               <ascii_last>Collins</ascii_last>          
            </name>        
            <editorial_player_key>nfl.p.29405</editorial_player_key>        
            <editorial_team_key>nfl.t.33</editorial_team_key>        
            <editorial_team_full_name>Baltimore Ravens</editorial_team_full_name>        
            <editorial_team_abbr>Bal</editorial_team_abbr>        
            <bye_weeks>          
               <week>10</week>          
            </bye_weeks>        
            <uniform_number>34</uniform_number>        
            <display_position>RB</display_position>        
            <headshot>          
               <url>https://s.yimg.com/iu/api/res/1.2/tDUuvXiiEdRXFbQlbEcUnQ--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08222018/29405.png</url>          
               <size>small</size>          
            </headshot>        
            <image_url>https://s.yimg.com/iu/api/res/1.2/tDUuvXiiEdRXFbQlbEcUnQ--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08222018/29405.png</image_url>        
            <is_undroppable>0</is_undroppable>        
            <position_type>O</position_type>        
            <eligible_positions>          
               <position>RB</position>          
            </eligible_positions>        
            <has_player_notes>1</has_player_notes>        
            <draft_analysis>          
               <average_pick>47.0</average_pick>          
               <average_round>5.3</average_round>          
               <average_cost>12.8</average_cost>          
               <percent_drafted>1.00</percent_drafted>          
            </draft_analysis>        
            <percent_owned>          
               <coverage_type>week</coverage_type>          
               <week>1</week>          
               <value>98</value>          
               <delta>0</delta>          
            </percent_owned>        
         </player>      
         <player>        
            <player_key>380.p.27591</player_key>        
            <player_id>27591</player_id>        
            <name>          
               <full>Jarvis Landry</full>          
               <first>Jarvis</first>          
               <last>Landry</last>          
               <ascii_first>Jarvis</ascii_first>          
               <ascii_last>Landry</ascii_last>          
            </name>        
            <editorial_player_key>nfl.p.27591</editorial_player_key>        
            <editorial_team_key>nfl.t.5</editorial_team_key>        
            <editorial_team_full_name>Cleveland Browns</editorial_team_full_name>        
            <editorial_team_abbr>Cle</editorial_team_abbr>        
            <bye_weeks>          
               <week>11</week>          
            </bye_weeks>        
            <uniform_number>80</uniform_number>        
            <display_position>WR</display_position>        
            <headshot>          
               <url>https://s.yimg.com/iu/api/res/1.2/s87DuNVwFQzJaplHjLXT_Q--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08272018/27591.png</url>          
               <size>small</size>          
            </headshot>        
            <image_url>https://s.yimg.com/iu/api/res/1.2/s87DuNVwFQzJaplHjLXT_Q--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08272018/27591.png</image_url>        
            <is_undroppable>0</is_undroppable>        
            <position_type>O</position_type>        
            <eligible_positions>          
               <position>WR</position>          
            </eligible_positions>        
            <has_player_notes>1</has_player_notes>        
            <draft_analysis>          
               <average_pick>50.5</average_pick>          
               <average_round>5.7</average_round>          
               <average_cost>9.3</average_cost>          
               <percent_drafted>1.00</percent_drafted>          
            </draft_analysis>        
            <percent_owned>          
               <coverage_type>week</coverage_type>          
               <week>1</week>          
               <value>98</value>          
               <delta>0</delta>          
            </percent_owned>        
         </player>      
         <player>        
            <player_key>380.p.29307</player_key>        
            <player_id>29307</player_id>        
            <name>          
               <full>Kenyan Drake</full>          
               <first>Kenyan</first>          
               <last>Drake</last>          
               <ascii_first>Kenyan</ascii_first>          
               <ascii_last>Drake</ascii_last>          
            </name>        
            <editorial_player_key>nfl.p.29307</editorial_player_key>        
            <editorial_team_key>nfl.t.15</editorial_team_key>        
            <editorial_team_full_name>Miami Dolphins</editorial_team_full_name>        
            <editorial_team_abbr>Mia</editorial_team_abbr>        
            <bye_weeks>          
               <week>11</week>          
            </bye_weeks>        
            <uniform_number>32</uniform_number>        
            <display_position>RB</display_position>        
            <headshot>          
               <url>https://s.yimg.com/iu/api/res/1.2/mPf_mdNY5XcDbsLCQO5v2A--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08232018/29307.png</url>          
               <size>small</size>          
            </headshot>        
            <image_url>https://s.yimg.com/iu/api/res/1.2/mPf_mdNY5XcDbsLCQO5v2A--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08232018/29307.png</image_url>        
            <is_undroppable>0</is_undroppable>        
            <position_type>O</position_type>        
            <eligible_positions>          
               <position>RB</position>          
            </eligible_positions>        
            <has_player_notes>1</has_player_notes>        
            <draft_analysis>          
               <average_pick>40.5</average_pick>          
               <average_round>4.7</average_round>          
               <average_cost>17.5</average_cost>          
               <percent_drafted>1.00</percent_drafted>          
            </draft_analysis>        
            <percent_owned>          
               <coverage_type>week</coverage_type>          
               <week>1</week>          
               <value>98</value>          
               <delta>0</delta>          
            </percent_owned>        
         </player>      
         <player>        
            <player_key>380.p.29279</player_key>        
            <player_id>29279</player_id>        
            <name>          
               <full>Derrick Henry</full>          
               <first>Derrick</first>          
               <last>Henry</last>          
               <ascii_first>Derrick</ascii_first>          
               <ascii_last>Henry</ascii_last>          
            </name>        
            <editorial_player_key>nfl.p.29279</editorial_player_key>        
            <editorial_team_key>nfl.t.10</editorial_team_key>        
            <editorial_team_full_name>Tennessee Titans</editorial_team_full_name>        
            <editorial_team_abbr>Ten</editorial_team_abbr>        
            <bye_weeks>          
               <week>8</week>          
            </bye_weeks>        
            <uniform_number>22</uniform_number>        
            <display_position>RB</display_position>        
            <headshot>          
               <url>https://s.yimg.com/iu/api/res/1.2/BsK3qj71MxrCBdeBCCiGHw--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08232018/29279.png</url>          
               <size>small</size>          
            </headshot>        
            <image_url>https://s.yimg.com/iu/api/res/1.2/BsK3qj71MxrCBdeBCCiGHw--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08232018/29279.png</image_url>        
            <is_undroppable>0</is_undroppable>        
            <position_type>O</position_type>        
            <eligible_positions>          
               <position>RB</position>          
            </eligible_positions>        
            <has_player_notes>1</has_player_notes>        
            <draft_analysis>          
               <average_pick>50.7</average_pick>          
               <average_round>5.7</average_round>          
               <average_cost>15.2</average_cost>          
               <percent_drafted>1.00</percent_drafted>          
            </draft_analysis>        
            <percent_owned>          
               <coverage_type>week</coverage_type>          
               <week>1</week>          
               <value>97</value>          
               <delta>0</delta>          
            </percent_owned>        
         </player>      
         <player>        
            <player_key>380.p.5228</player_key>        
            <player_id>5228</player_id>        
            <name>          
               <full>Tom Brady</full>          
               <first>Tom</first>          
               <last>Brady</last>          
               <ascii_first>Tom</ascii_first>          
               <ascii_last>Brady</ascii_last>          
            </name>        
            <editorial_player_key>nfl.p.5228</editorial_player_key>        
            <editorial_team_key>nfl.t.17</editorial_team_key>        
            <editorial_team_full_name>New England Patriots</editorial_team_full_name>        
            <editorial_team_abbr>NE</editorial_team_abbr>        
            <bye_weeks>          
               <week>11</week>          
            </bye_weeks>        
            <uniform_number>12</uniform_number>        
            <display_position>QB</display_position>        
            <headshot>          
               <url>https://s.yimg.com/iu/api/res/1.2/K4TGf.cQSCiks4HMIB82Lg--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08272018/5228.png</url>          
               <size>small</size>          
            </headshot>        
            <image_url>https://s.yimg.com/iu/api/res/1.2/K4TGf.cQSCiks4HMIB82Lg--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08272018/5228.png</image_url>        
            <is_undroppable>0</is_undroppable>        
            <position_type>O</position_type>        
            <eligible_positions>          
               <position>QB</position>          
            </eligible_positions>        
            <has_player_notes>1</has_player_notes>        
            <draft_analysis>          
               <average_pick>35.0</average_pick>          
               <average_round>4.1</average_round>          
               <average_cost>15.2</average_cost>          
               <percent_drafted>1.00</percent_drafted>          
            </draft_analysis>        
            <percent_owned>          
               <coverage_type>week</coverage_type>          
               <week>1</week>          
               <value>100</value>          
               <delta>0</delta>          
            </percent_owned>        
         </player>      
         <player>        
            <player_key>380.p.26561</player_key>        
            <player_id>26561</player_id>        
            <name>          
               <full>Josh Gordon</full>          
               <first>Josh</first>          
               <last>Gordon</last>          
               <ascii_first>Josh</ascii_first>          
               <ascii_last>Gordon</ascii_last>          
            </name>        
            <status>Q</status>        
            <status_full>Questionable</status_full>        
            <editorial_player_key>nfl.p.26561</editorial_player_key>        
            <editorial_team_key>nfl.t.5</editorial_team_key>        
            <editorial_team_full_name>Cleveland Browns</editorial_team_full_name>        
            <editorial_team_abbr>Cle</editorial_team_abbr>        
            <bye_weeks>          
               <week>11</week>          
            </bye_weeks>        
            <uniform_number>12</uniform_number>        
            <display_position>WR</display_position>        
            <headshot>          
               <url>https://s.yimg.com/iu/api/res/1.2/B7oGCmKZfwDP5CwuosBZzQ--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08272018/26561.png</url>          
               <size>small</size>          
            </headshot>        
            <image_url>https://s.yimg.com/iu/api/res/1.2/B7oGCmKZfwDP5CwuosBZzQ--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08272018/26561.png</image_url>        
            <is_undroppable>0</is_undroppable>        
            <position_type>O</position_type>        
            <eligible_positions>          
               <position>WR</position>          
            </eligible_positions>        
            <has_player_notes>1</has_player_notes>        
            <has_recent_player_notes>1</has_recent_player_notes>        
            <draft_analysis>          
               <average_pick>51.4</average_pick>          
               <average_round>5.7</average_round>          
               <average_cost>15.8</average_cost>          
               <percent_drafted>1.00</percent_drafted>          
            </draft_analysis>        
            <percent_owned>          
               <coverage_type>week</coverage_type>          
               <week>1</week>          
               <value>97</value>          
               <delta>0</delta>          
            </percent_owned>        
         </player>      
         <player>        
            <player_key>380.p.25178</player_key>        
            <player_id>25178</player_id>        
            <name>          
               <full>Chris Hogan</full>          
               <first>Chris</first>          
               <last>Hogan</last>          
               <ascii_first>Chris</ascii_first>          
               <ascii_last>Hogan</ascii_last>          
            </name>        
            <editorial_player_key>nfl.p.25178</editorial_player_key>        
            <editorial_team_key>nfl.t.17</editorial_team_key>        
            <editorial_team_full_name>New England Patriots</editorial_team_full_name>        
            <editorial_team_abbr>NE</editorial_team_abbr>        
            <bye_weeks>          
               <week>11</week>          
            </bye_weeks>        
            <uniform_number>15</uniform_number>        
            <display_position>WR</display_position>        
            <headshot>          
               <url>https://s.yimg.com/iu/api/res/1.2/pM_Y4drjgQzGXyhOefVNEQ--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08212018/25178.png</url>          
               <size>small</size>          
            </headshot>        
            <image_url>https://s.yimg.com/iu/api/res/1.2/pM_Y4drjgQzGXyhOefVNEQ--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08212018/25178.png</image_url>        
            <is_undroppable>0</is_undroppable>        
            <position_type>O</position_type>        
            <eligible_positions>          
               <position>WR</position>          
            </eligible_positions>        
            <has_player_notes>1</has_player_notes>        
            <draft_analysis>          
               <average_pick>72.9</average_pick>          
               <average_round>8.0</average_round>          
               <average_cost>5.5</average_cost>          
               <percent_drafted>1.00</percent_drafted>          
            </draft_analysis>        
            <percent_owned>          
               <coverage_type>week</coverage_type>          
               <week>1</week>          
               <value>97</value>          
               <delta>0</delta>          
            </percent_owned>        
         </player>      
         <player>        
            <player_key>380.p.28537</player_key>        
            <player_id>28537</player_id>        
            <name>          
               <full>Jay Ajayi</full>          
               <first>Jay</first>          
               <last>Ajayi</last>          
               <ascii_first>Jay</ascii_first>          
               <ascii_last>Ajayi</ascii_last>          
            </name>        
            <status>Q</status>        
            <status_full>Questionable</status_full>        
            <editorial_player_key>nfl.p.28537</editorial_player_key>        
            <editorial_team_key>nfl.t.21</editorial_team_key>        
            <editorial_team_full_name>Philadelphia Eagles</editorial_team_full_name>        
            <editorial_team_abbr>Phi</editorial_team_abbr>        
            <bye_weeks>          
               <week>9</week>          
            </bye_weeks>        
            <uniform_number>26</uniform_number>        
            <display_position>RB</display_position>        
            <headshot>          
               <url>https://s.yimg.com/iu/api/res/1.2/8_wBYAWL1yFaypSAH51Miw--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08212018/28537.png</url>          
               <size>small</size>          
            </headshot>        
            <image_url>https://s.yimg.com/iu/api/res/1.2/8_wBYAWL1yFaypSAH51Miw--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08212018/28537.png</image_url>        
            <is_undroppable>0</is_undroppable>        
            <position_type>O</position_type>        
            <eligible_positions>          
               <position>RB</position>          
            </eligible_positions>        
            <has_player_notes>1</has_player_notes>        
            <draft_analysis>          
               <average_pick>48.9</average_pick>          
               <average_round>5.5</average_round>          
               <average_cost>11.4</average_cost>          
               <percent_drafted>1.00</percent_drafted>          
            </draft_analysis>        
            <percent_owned>          
               <coverage_type>week</coverage_type>          
               <week>1</week>          
               <value>98</value>          
               <delta>0</delta>          
            </percent_owned>        
         </player>      
         <player>        
            <player_key>380.p.25785</player_key>        
            <player_id>25785</player_id>        
            <name>          
               <full>Russell Wilson</full>          
               <first>Russell</first>          
               <last>Wilson</last>          
               <ascii_first>Russell</ascii_first>          
               <ascii_last>Wilson</ascii_last>          
            </name>        
            <editorial_player_key>nfl.p.25785</editorial_player_key>        
            <editorial_team_key>nfl.t.26</editorial_team_key>        
            <editorial_team_full_name>Seattle Seahawks</editorial_team_full_name>        
            <editorial_team_abbr>Sea</editorial_team_abbr>        
            <bye_weeks>          
               <week>7</week>          
            </bye_weeks>        
            <uniform_number>3</uniform_number>        
            <display_position>QB</display_position>        
            <headshot>          
               <url>https://s.yimg.com/iu/api/res/1.2/OxOjQVJkvUee70.hiV8ULg--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08212018/25785.png</url>          
               <size>small</size>          
            </headshot>        
            <image_url>https://s.yimg.com/iu/api/res/1.2/OxOjQVJkvUee70.hiV8ULg--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08212018/25785.png</image_url>        
            <is_undroppable>0</is_undroppable>        
            <position_type>O</position_type>        
            <eligible_positions>          
               <position>QB</position>          
            </eligible_positions>        
            <has_player_notes>1</has_player_notes>        
            <draft_analysis>          
               <average_pick>43.1</average_pick>          
               <average_round>4.9</average_round>          
               <average_cost>13.9</average_cost>          
               <percent_drafted>1.00</percent_drafted>          
            </draft_analysis>        
            <percent_owned>          
               <coverage_type>week</coverage_type>          
               <week>1</week>          
               <value>100</value>          
               <delta>0</delta>          
            </percent_owned>        
         </player>      
         <player>        
            <player_key>380.p.31041</player_key>        
            <player_id>31041</player_id>        
            <name>          
               <full>Royce Freeman</full>          
               <first>Royce</first>          
               <last>Freeman</last>          
               <ascii_first>Royce</ascii_first>          
               <ascii_last>Freeman</ascii_last>          
            </name>        
            <editorial_player_key>nfl.p.31041</editorial_player_key>        
            <editorial_team_key>nfl.t.7</editorial_team_key>        
            <editorial_team_full_name>Denver Broncos</editorial_team_full_name>        
            <editorial_team_abbr>Den</editorial_team_abbr>        
            <bye_weeks>          
               <week>10</week>          
            </bye_weeks>        
            <uniform_number>37</uniform_number>        
            <display_position>RB</display_position>        
            <headshot>          
               <url>https://s.yimg.com/iu/api/res/1.2/T3dV2I_d9.8UrssEPihUZw--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08222018/31041.png</url>          
               <size>small</size>          
            </headshot>        
            <image_url>https://s.yimg.com/iu/api/res/1.2/T3dV2I_d9.8UrssEPihUZw--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08222018/31041.png</image_url>        
            <is_undroppable>0</is_undroppable>        
            <position_type>O</position_type>        
            <eligible_positions>          
               <position>RB</position>          
            </eligible_positions>        
            <has_player_notes>1</has_player_notes>        
            <draft_analysis>          
               <average_pick>70.6</average_pick>          
               <average_round>7.7</average_round>          
               <average_cost>7.7</average_cost>          
               <percent_drafted>0.99</percent_drafted>          
            </draft_analysis>        
            <percent_owned>          
               <coverage_type>week</coverage_type>          
               <week>1</week>          
               <value>95</value>          
               <delta>0</delta>          
            </percent_owned>        
         </player>      
         <player>        
            <player_key>380.p.9317</player_key>        
            <player_id>9317</player_id>        
            <name>          
               <full>LeSean McCoy</full>          
               <first>LeSean</first>          
               <last>McCoy</last>          
               <ascii_first>LeSean</ascii_first>          
               <ascii_last>McCoy</ascii_last>          
            </name>        
            <status>Q</status>        
            <status_full>Questionable</status_full>        
            <editorial_player_key>nfl.p.9317</editorial_player_key>        
            <editorial_team_key>nfl.t.2</editorial_team_key>        
            <editorial_team_full_name>Buffalo Bills</editorial_team_full_name>        
            <editorial_team_abbr>Buf</editorial_team_abbr>        
            <bye_weeks>          
               <week>11</week>          
            </bye_weeks>        
            <uniform_number>25</uniform_number>        
            <display_position>RB</display_position>        
            <headshot>          
               <url>https://s.yimg.com/iu/api/res/1.2/mdG7t5jI1vLr7ce71pRWmg--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08232018/9317.png</url>          
               <size>small</size>          
            </headshot>        
            <image_url>https://s.yimg.com/iu/api/res/1.2/mdG7t5jI1vLr7ce71pRWmg--~B/YXBwaWQ9c2hhcmVkO2NoPTIzMzY7Y3I9MTtjdz0xNzkwO2R4PTg1NztkeT0wO2ZpPXVsY3JvcDtoPTYwO3E9MTAwO3c9NDY-/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08232018/9317.png</image_url>        
            <is_undroppable>0</is_undroppable>        
            <position_type>O</position_type>        
            <eligible_positions>          
               <position>RB</position>          
            </eligible_positions>        
            <has_player_notes>1</has_player_notes>        
            <draft_analysis>          
               <average_pick>39.4</average_pick>          
               <average_round>4.5</average_round>          
               <average_cost>21.2</average_cost>          
               <percent_drafted>1.00</percent_drafted>          
            </draft_analysis>        
            <percent_owned>          
               <coverage_type>week</coverage_type>          
               <week>1</week>          
               <value>98</value>          
               <delta>0</delta>          
            </percent_owned>        
         </player>      
      </players>    
   </game>  
</fantasy_content>
'''

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
    
    def get_players_data_combined(self, position=""):
        xml_results = self.get_players_data_xml_strings(self, position)
        for xml_result in xml_results:
            xmltodict.parse(xml_result)
        
        
    
    def get_players_data_xml_strings(self, position=""):
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
         
    
    def clear_text_file_and_write(self, base_filename, contents_to_write):
        base_filename = base_filename + ".txt"
        
        #clear it first
        open(base_filename, 'w').close()
        
        #  add the text
        with open(base_filename, "a") as text_file:     
            print(f"{contents_to_write}", file=text_file)    
    



def download_player_data_from_yahoo(pyfsi):
    '''
    Download all the data to text files.
    :param pyfsi: PyFantasyYahooSportsInterface
    '''

    # experimentally determined that there's 2789 "players" in the Yahoo DB. 
    xml_results = pyfsi.get_players_data_xml_strings()
    base_filename = "all_players"
    for result in xml_results:
        pyfsi.clear_text_file_and_write(base_filename, result)
    
     
    # get a result for each position
    for position in PyFantasyYahooSportsInterface.POSSIBLE_POSITIONS:
        xml_results = pyfsi.get_players_data_xml_strings(position=position)
  
        base_filename = position + ".txt"
        for result in xml_results:
            pyfsi.clear_text_file_and_write(base_filename, result)
                
    print("done")    


def parse_yahoo_xml_string_to_dict(xml_string):
    #remove the first line, with the "<?xml version="1.0" ?>"
    
    if OPENING_XML_STRING in xml_string:
        xml_string.replace(OPENING_XML_STRING, "")
        
    return xmltodict.parse(xml_string)
    


def get_player_list_from_xml_string(xml_string_to_parse):
    '''    
    :param xml_string_to_parse:
    '''
    player_list = []
    if "<players count" in xml_string_to_parse:
        base_dict = parse_yahoo_xml_string_to_dict(xml_string_to_parse)
        fantasy_content_dict = base_dict['fantasy_content']
        game_dict = fantasy_content_dict['game']
        players_dict = game_dict['players']    
        player_list = players_dict['player']
        
        #
    return player_list

def combine_xml_strings_to_one_big_list_of_players(xml_strings):
    
    combined_player_list = []
    
   
    for xml_string in xml_strings:
        if xml_string:
            combined_player_list += get_player_list_from_xml_string(xml_string)
    
    return combined_player_list
    


def get_player_list_from_data_file(data_file_path):
    string_containing_multiple_xml_strings = ""
    with open(data_file_path, "r") as text_file:
        string_containing_multiple_xml_strings = text_file.read()
    print("{len(string_containing_multiple_xml_strings)}")
#split on OPENING_XML_STRING
    xml_strings = string_containing_multiple_xml_strings.split(OPENING_XML_STRING)
    combined_player_list = combine_xml_strings_to_one_big_list_of_players(xml_strings)
    return combined_player_list

def main():
#     auth_filename="auth_keys.txt"
#     pyfsi = PyFantasyYahooSportsInterface(auth_filename)
#     download_player_data_from_yahoo(pyfsi)

    data_file_path = "../data/all_players.txt"

    player_list = get_player_list_from_data_file(data_file_path)
    
    print(random.choice(player_list))
    
    

    
if __name__ == "__main__":
    main()

