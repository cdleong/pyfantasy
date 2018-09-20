'''
UI for yahoo draft advisor
Created on Sep 3, 2018

@author: cdleong
'''
from PyQt5.QtWidgets import (QWidget, QLabel, 
    QComboBox, QApplication, QPushButton, QHBoxLayout, QVBoxLayout)
import sys
import yahoo_draft_advisor as yda

class PyFantasyGUI(QWidget):
    
    def __init__(self, draft_advisor):
        super().__init__()
        
        self.draft_advisor = draft_advisor
        self.initUI()
        
    
        
            
    def initUI(self):      

        

        self.draftable_players = self.draft_advisor.get_top_draftable_players(10)
        self.lbl = QLabel(str(self.draftable_players[0]), self)
        self.current_key = self.find_key(str(self.draftable_players[0]))
         
        
        self.combo = QComboBox(self)
        
        for item in self.draftable_players:
            self.combo.addItem(str(item))

#         self.combo.move(50, 50)
#         self.lbl.move(50, 150)

        self.combo.activated[str].connect(self.onActivated)       
         
         
         
        #QUIT BUTTON
        qbtn = QPushButton('Quit', self)
#         qbtn.move(50, 50)
        qbtn.clicked.connect(QApplication.instance().quit)
        
        draft_player_btn = QPushButton('Draft Him', self)
        draft_player_btn.clicked.connect(self.draft_for_me)
        
        player_taken_btn = QPushButton("He is taken", self)
        player_taken_btn.clicked.connect(self.draft_for_others)
        
        
        
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        
        
        hbox.addWidget(qbtn)
        hbox.addWidget(draft_player_btn)
        hbox.addWidget(player_taken_btn)
        hbox.addWidget(self.combo)
        hbox.addWidget(self.lbl)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        
        
        self.setLayout(vbox)  
        
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('PyFantasyGUI')
        self.show()

    
    def regenerate_combo(self):
        print("regenerating combo box")
        self.draftable_players = self.draft_advisor.get_top_draftable_players()
        self.combo.clear()
        for draftable_player in self.draftable_players:
            self.combo.addItem(str(draftable_player))
        self.onActivated(str(self.draftable_players[0]))
        
    
    def draft_and_regenerate(self, by_me=False):
        
        currently_selected_guy_key = self.current_key
        print(f"Drafting key {currently_selected_guy_key}. By me = {by_me}")
        self.draft_advisor.draft_player(currently_selected_guy_key, by_me=by_me)
        self.regenerate_combo()
            
    
    def draft_for_others(self):
        self.draft_and_regenerate()
        
    def draft_for_me(self):
        
        self.draft_and_regenerate(by_me=True)
                
        
    def find_key(self, text):    
        
        for player in self.draftable_players:
            if str(player) == text:
                player_key = player.get_player_key()
                print(f"found key: {player_key}")
                return player_key
                
        
    def onActivated(self, text):
        self.current_key = self.find_key(text)
        self.lbl.setText(text)
        self.lbl.adjustSize()  
        

def run(draft_advisor):
    app = QApplication(sys.argv)
    ex = PyFantasyGUI(draft_advisor)
    sys.exit(app.exec_())
            
if __name__ == '__main__':
    league_roster = "QB,WR,WR,RB,RB,TE,K,DEF,BN,BN,BN,BN,BN,IR".split(",")
    print(f"{league_roster}")
    
    players_list = yda.load_data()    
    my_draft_advisor = yda.PyFantasyYahooDraftAdvisor(players_list, league_roster)
    
    
    

    
    run(my_draft_advisor)
    