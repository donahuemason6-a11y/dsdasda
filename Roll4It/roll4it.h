// user defined header file for Roll4It
#ifndef ROLL4IT_H
#define ROLL4IT_H

// constants
// size of player's name array
#define NAME 20
// total number of player dice
#define DICE 6
// array column with the value
#define DIE_VALUE 0
// array column to track if die is used
#define DIE_STATUS 1
// committed states
#define NO_COMMIT -1
#define CARD1_COMMIT 1
#define CARD2_COMMIT 2
#define CARD3_COMMIT 3
// play options
#define PLAY 1
#define QUIT 0
// number of cards displayed
#define CARDS 3
// number of dice on a card
#define CARD_DICE 4
// points for card
#define CARD_POINTS 10
// card requirements options
#define REQ_NOT_MET 0
#define REQ_MET 1
// die used flag
#define DIE_USED 1
// success flag
#define SUCCESS 1
// true / false
#define TRUE 1
#define FALSE 0
// player numbers
#define PLAYER1 1
#define PLAYER2 2
// score to win game
#define WIN 40
// menu options
#define RULES 2
#define LEAD 3
#define EXIT 4
// data file values
#define LINE 100
#define FIELDS 3
#define DATA 30
#define ZERO 0

// function prototypes
void readLeaderboardFile();
char *trim(char *str);

#endif
