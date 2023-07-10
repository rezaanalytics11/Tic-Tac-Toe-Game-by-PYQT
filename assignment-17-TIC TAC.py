import random
import time
import PySide6
from PySide6.QtUiTools import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from functools import partial

class TicTacToe(QMainWindow):
    def __init__(self):
        super(). __init__()

        loader=QUiLoader()
        self.ui=loader.load('ticgame.ui',None)
        self.ui.show()
        self.total_scorex = 0
        self.total_scoreo = 0


        self.game=[[self.ui.btn_1,self.ui.btn_2,self.ui.btn_3],[self.ui.btn_4,self.ui.btn_5,
                   self.ui.btn_6],[self.ui.btn_7,self.ui.btn_8,self.ui.btn_9]]

        self.ui.reset_game.clicked.connect(self.reset_game)
        self.ui.new_game.clicked.connect(self.new_game)
        self.ui.player_player.clicked.connect(self.player_player)
        self.ui.player_computer.clicked.connect(self.player_computer)
        self.ui.about.clicked.connect(self.about)


    def new_game(self):

         for i in range(3):

            for j in range(3):

                self.game[i][j].setText('')
                self.game[i][j].setStyleSheet("color: black; background-color: skyblue")
                self.game[i][j].clicked.connect(partial(self.play,i,j))




         self.player='X'
        #self.player=random.choice(['X','O'])
        #self.player = random.choice('X')

    def play(self,i,j):
      if self.player_computer() == True:
       if self.game[i][j].text() == "":
        if self.player=='X':
         self.game[i][j].setText('X')
         self.game[i][j].setStyleSheet("color: black; background-color: red")
         self.player='O'
        else:
         i = random.choice([0, 1, 2])
         j = random.choice([0, 1, 2])
         if self.game[i][j].text() == "":
          self.game[i][j].setText('0')
          self.game[i][j].setStyleSheet("color: black; background-color: yellow")
          self.player = 'X'

        self.win()

      elif self.player_player() == True:
        if self.game[i][j].text() == "":
         if self.player == 'X':
            self.game[i][j].setText('X')
            self.game[i][j].setStyleSheet("color: black; background-color: red")
            self.player = 'O'
         else:
          if self.game[i][j].text() == "":
             self.game[i][j].setText('0')
             self.game[i][j].setStyleSheet("color: black; background-color: yellow")
             self.player = 'X'

        self.win()


    def win(self):

        if self.game[0][0].text() =='X' and self.game[0][1].text()=='X' and self.game[0][2].text() =='X' :
            self.total_scorex = self.total_scorex + 1
            self.ui.textbox.setText(str('total score X : {}'.format(self.total_scorex)))

            msgBox=QMessageBox()
            msgBox.setText('Player Won!')
            msgBox.exec()

            time.sleep(5)
            self.reset_game()


        elif self.game[1][0].text() == 'X' and self.game[1][1].text() == 'X' and self.game[1][2].text() == 'X':
            self.total_scorex = self.total_scorex + 1
            self.ui.textbox.setText(str('total score X : {}'.format(self.total_scorex)))

            msgBox=QMessageBox()
            msgBox.setText('Player Won!')
            msgBox.exec()

            time.sleep(5.0)
            self.reset_game()


        elif self.game[2][0].text() == 'X' and self.game[2][1].text() == 'X' and self.game[2][2].text() == 'X':
            self.total_scorex = self.total_scorex + 1
            self.ui.textbox.setText(str('total score X : {}'.format(self.total_scorex)))

            msgBox=QMessageBox()
            msgBox.setText('Player Won!')
            msgBox.exec()

            time.sleep(5.0)
            self.reset_game()


        elif self.game[0][0].text() == 'X' and self.game[1][0].text() == 'X' and self.game[2][0].text() == 'X':
            self.total_scorex = self.total_scorex + 1
            self.ui.textbox.setText(str('total score X : {}'.format(self.total_scorex)))

            msgBox=QMessageBox()
            msgBox.setText('Player Won!')
            msgBox.exec()

            time.sleep(5.0)
            self.reset_game()


        elif self.game[0][1].text() == 'X' and self.game[1][1].text() == 'X' and self.game[2][1].text() == 'X':
            self.total_scorex = self.total_scorex + 1
            self.ui.textbox.setText(str('total score X : {}'.format(self.total_scorex)))

            msgBox=QMessageBox()
            msgBox.setText('Player Won!')
            msgBox.exec()

            time.sleep(5.0)
            self.reset_game()


        elif self.game[0][2].text() == 'X' and self.game[1][2].text() == 'X' and self.game[2][2].text() == 'X':
            self.total_scorex = self.total_scorex + 1
            self.ui.textbox.setText(str('total score X : {}'.format(self.total_scorex)))

            msgBox=QMessageBox()
            msgBox.setText('Player Won!')
            msgBox.exec()

            time.sleep(5.0)
            self.reset_game()


        elif self.game[0][0].text() == 'X' and self.game[1][1].text() == 'X' and self.game[2][2].text() == 'X':
            self.total_scorex = self.total_scorex + 1
            self.ui.textbox.setText(str('total score X : {}'.format(self.total_scorex)))

            msgBox=QMessageBox()
            msgBox.setText('Player Won!')
            msgBox.exec()

            time.sleep(5.0)
            self.reset_game()


        elif self.game[2][0].text() == 'X' and self.game[1][1].text() == 'X' and self.game[0][2].text() == 'X':
            self.total_scorex=self.total_scorex+1
            self.ui.textbox.setText(str('total score X :{}'.format(self.total_scorex)))

            msgBox=QMessageBox()
            msgBox.setText('Player Won!')
            msgBox.exec()

            time.sleep(5)
            self.reset_game()




        elif self.game[0][0].text() =='O' and self.game[0][1].text()=='O' and self.game[0][2].text() =='O' :
            self.total_scoreo = self.total_scoreo + 1
            self.ui.textbox.setText(str('total score O : {}'.format(self.total_scoreo)))

            msgBox=QMessageBox()
            msgBox.setText('Player Won!')
            msgBox.exec()

            time.sleep(5)
            self.reset_game()


        elif self.game[1][0].text() == 'O' and self.game[1][1].text() == 'O' and self.game[1][2].text() == 'O':
            self.total_scoreo = self.total_scoreo + 1
            self.ui.textbox.setText(str('total score O : {}'.format(self.total_scoreo)))

            msgBox=QMessageBox()
            msgBox.setText('Player Won!')
            msgBox.exec()

            time.sleep(5.0)
            self.reset_game()


        elif self.game[2][0].text() == 'O' and self.game[2][1].text() == 'O' and self.game[2][2].text() == 'O':
            self.total_scoreo = self.total_scoreo + 1
            self.ui.textbox.setText(str('total score O : {}'.format(self.total_scoreo)))

            msgBox=QMessageBox()
            msgBox.setText('Player Won!')
            msgBox.exec()

            time.sleep(5)
            self.reset_game()


        elif self.game[0][0].text() == 'O' and self.game[1][0].text() == 'O' and self.game[2][0].text() == 'O':
            self.total_scoreo = self.total_scoreo + 1
            self.ui.textbox.setText(str('total score O : {}'.format(self.total_scoreo)))

            msgBox=QMessageBox()
            msgBox.setText('Player Won!')
            msgBox.exec()

            time.sleep(5)
            self.reset_game()


        elif self.game[0][1].text() == 'O' and self.game[1][1].text() == 'O' and self.game[2][1].text() == 'O':
            self.scoreo = self.total_scoreo + 1
            self.ui.textbox.setText(str('total score O : {}'.format(self.total_scoreo)))

            msgBox=QMessageBox()
            msgBox.setText('Player Won!')
            msgBox.exec()

            time.sleep(5)
            self.reset_game()


        elif self.game[0][2].text() == 'O' and self.game[1][2].text() == 'O' and self.game[2][2].text() == 'O':
            self.total_scoreo = self.total_scoreo + 1
            self.ui.textbox.setText(str('total score O : {}'.format(self.total_scoreo)))

            msgBox=QMessageBox()
            msgBox.setText('Player Won!')
            msgBox.exec()

            time.sleep(5)
            self.reset_game()

        elif self.game[0][0].text() == 'O' and self.game[1][1].text() == 'O' and self.game[2][2].text() == 'O':
            self.total_scoreo = self.total_scoreo + 1
            self.ui.textbox.setText(str('total score O : {}'.format(self.total_scoreo)))

            msgBox=QMessageBox()
            msgBox.setText('Player Won!')
            msgBox.exec()

            time.sleep(5)
            self.reset_game()

        elif self.game[2][0].text() == 'O' and self.game[1][1].text() == 'O' and self.game[0][2].text() == 'O' :
            self.total_scoreo=self.total_scoreo+1
            self.ui.textbox.setText(str('total score O :{}'.format(self.total_scoreo)))

            msgBox=QMessageBox()
            msgBox.setText('Player Won!')
            msgBox.exec()

            time.sleep(5)
            self.reset_game()


    def reset_game(self):
        self.ui.textbox1.setText(str('total score O:{}'.format(self.total_scoreo)))
        self.ui.textbox2.setText(str('total score X:{}'.format(self.total_scorex)))
        self.ui.textbox.setText('')
        for i in range(3):
         for j in range(3):
          self.game[i][j].setText(' ')
          self.game[i][j].setStyleSheet("color: black; background-color: skyblue")


    def about(self):

            msgBox=QMessageBox()
            msgBox.setText('There is no information at this stage, We will include adequate data very soon!')
            msgBox.exec()


    def player_player(self):
            return True

    def player_computer(self):
            return True


app= QApplication([])
window=TicTacToe()


app.exec()