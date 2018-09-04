'''
UI for yahoo draft advisor
Created on Sep 3, 2018

@author: cdleong
'''
from PyQt5.QtWidgets import (QWidget, QLabel, 
    QComboBox, QApplication)
import sys
import yahoo_draft_advisor as yda

class PyFantasyGUI(QWidget):
    
    def __init__(self, draft_advisor):
        super().__init__()
        
        self.draft_advisor = draft_advisor
        self.initUI()
        
        
    def initUI(self):      

        
        
        draftable_players = self.draft_advisor.get_top_draftable_players(10)
        self.lbl = QLabel(str(draftable_players[0]), self)
         
        
        combo = QComboBox(self)
        
        for item in draftable_players:
            combo.addItem(str(item))

        combo.move(50, 50)
        self.lbl.move(50, 150)

        combo.activated[str].connect(self.onActivated)        
         
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('PyFantasyGUI')
        self.show()
        
        
    def onActivated(self, text):
      
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
    