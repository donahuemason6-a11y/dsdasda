#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include <ctype.h>

// user defined header file with the constants and new prototypes
#include "roll4it.h"

// define the Player struct 
typedef struct
{
    char player[NAME];
    int num;
    int score;
    int dice[DICE][2];
} Player;

// function prototypes
void logo();
void sampleDice();
void sampleCard();
void play();
void randomCard();
void randomDice();
int rollDie();
void populateCard(int card[CARD_DICE]);
void printCards(int cardOne[CARD_DICE], int cardTwo[CARD_DICE], int cardThree[CARD_DICE]);
void rollDice(int dice[DICE][2]);
void printDice(int dice[DICE][2]);
void commitDie(int dieNum, int cardNum, int playerDice[DICE][2]);
void printCardStatus(int cardOne[CARD_DICE], int cardTwo[CARD_DICE], int cardThree[CARD_DICE], int playerDice[DICE][2]);
int selectDie();
int selectCard();
int rollAgain();
void reclaimDice(int playerDice[DICE][2], int cardNum);
int checkDice(int playerDice[DICE][2]);
void pickUpDice(int playerDice[DICE][2]);
int checkCardStatus(int cardOne[CARD_DICE], int cardTwo[CARD_DICE], int cardThree[CARD_DICE], int playerDice[DICE][2]);
int getDieStatus(int dieNum, int playerDice[DICE][2]);
int isGameOver(Player playerOne, Player playerTwo);
void printGameResults(Player playerOne, Player playerTwo);
int printMenu();
void printRules();

// main function 
int main() {
    // seed the random function 
    srand((unsigned int)time(NULL));

    // call function logo
    logo();

    // call sample dice function
    // sampleDice();

    // call sample card function
    // sampleCard();

    int select = printMenu();

    while(select != EXIT)
    {
        switch (select) {
            case PLAY:
                // call play function
                play();
                break;
            case RULES:
                // call printRules function
                printRules();
                break;
            case LEAD:
                // read and display the leaderboard file
                readLeaderboardFile();
                break;
            case EXIT:
                // break out of the loop
                break;
            default:
                break;
        }

        // redisplay the menu for options 1, 2, and 3
        select = printMenu();
    }

    // clear the input buffer so pause remains on screen
    while((getchar()) != '\n');

    // temporary pause to allow screen to stay visible
    printf("\nPress any key to continue...\n");
    getchar();

    return 0;
}

// logo function
void logo() {
    printf(".--------------. .--------------. .--------------. .--------------. .--------------. .--------------. .--------------.\n");
    printf("|  _______     | |     ____     | |   _____      | |   _____      | |   _    _     | |     _____    | |  _________   |\n");
    printf("| |_   __ \\    | |   .'    `.   | |  |_   _|     | |  |_   _|     | |  | |  | |    | |    |_   _|   | | |  _   _  |  |\n");
    printf("|   | |__) |   | |  /  .--.  \\  | |    | |       | |    | |       | |  | |__| |_   | |      | |     | | |_/ | | \\_|  |\n");
    printf("|   |  __ /    | |  | |    | |  | |    | |   _   | |    | |   _   | |  |____   _|  | |      | |     | |     | |      |\n");
    printf("|  _| |  \\ \\_  | |  \\  `--'  /  | |   _| |__/ |  | |   _| |__/ |  | |      _| |_   | |     _| |_    | |    _| |_     |\n");
    printf("| |____| |___| | |   `.____.'   | |  |________|  | |  |________|  | |     |_____|  | |    |_____|   | |   |_____|    |\n");
    printf("'--------------' '--------------' '--------------' '--------------' '--------------' '--------------' '--------------'\n");
}

void sampleDice() {
    printf(".-----. .-----. .-----. .-----. .-----. .-----.\n");
    printf("|  1  | |  2  | |  3  | |  4  | |  5  | |  6  |\n");
    printf("'-----' '-----' '-----' '-----' '-----' '-----'\n");
}

void sampleCard() {
    printf(".-----------------.\n");
    printf("| .-----. .-----. |\n");
    printf("| |  1  | |  2  | |\n");
    printf("| '-----' '-----' |\n");
    printf("| .-----. .-----. |\n");
    printf("| |  3  | |  4  | |\n");
    printf("| '-----' '-----' |\n");
    printf("'-----------------'\n");
}

void play() {
    // player related variables
    Player playerOne;
    playerOne.num = PLAYER1;
    playerOne.score = 0;

    // store the player's name
    printf("Player one, enter the player's name\n");
    scanf("%s", playerOne.player);
    
    Player playerTwo;
    playerTwo.num = PLAYER2;
    playerTwo.score = 0;

    // store the player's name
    printf("Player two, enter the player's name\n");
    scanf("%s", playerTwo.player);   

    // char player[NAME];
    // int score = 0;
    
    // loop control variables
    int roll = PLAY;
    int turn = PLAY;

    // array of six dice, second column tracks if the die is committed to a card
    // int dice[DICE][2];

    // array of values on a card
    int cardOne[CARD_DICE];
    int cardTwo[CARD_DICE];
    int cardThree[CARD_DICE];

    // used to store the player's selected die 
    int dieNumber = 0;

    // used to store the player's selected card
    int cardNumber = 0;

    // used to track result of displayCardStatus
    int cardResult = REQ_NOT_MET;

    // initialize the arrays to all -1 
    memset(playerOne.dice, NO_COMMIT, sizeof(playerOne.dice));
    memset(playerTwo.dice, NO_COMMIT, sizeof(playerTwo.dice));
    memset(cardOne, NO_COMMIT, sizeof(cardOne));
    memset(cardTwo, NO_COMMIT, sizeof(cardTwo));
    memset(cardThree, NO_COMMIT, sizeof(cardThree));

    // generate three random cards
    populateCard(cardOne);
    populateCard(cardTwo);
    populateCard(cardThree);

    // initialize currentPlayer with playerOne
    Player currentPlayer = playerOne;

    // for each roll, need to roll the dice, print the card, print the status, print the dice
    while(!isGameOver(playerOne, playerTwo)){
        printf("\n===============================\n"); 
        printf("%s, it is your turn to roll\n", currentPlayer.player);
        printf("%s, your score is: %d\n", currentPlayer.player, currentPlayer.score);
        printf("===============================\n"); 
        // Roll the dice
        rollDice(currentPlayer.dice);

        // print the cards and status
        printCards(cardOne, cardTwo, cardThree);
        printCardStatus(cardOne, cardTwo, cardThree, currentPlayer.dice);

        // print the dice
        printDice(currentPlayer.dice);

        while(turn) {
            // check if all the dice are committed to cards, no dice to select
            // pick up all the dice and break out of the loop 
            if(checkDice(currentPlayer.dice) == DICE) {
                printf("No dice left to select, pick up all dice\n");
                pickUpDice(currentPlayer.dice);
                break;
            } else {
                // prompt player to select die and store
                dieNumber = selectDie();
            
                // end turn
                if (dieNumber == QUIT) {
                    break;
                }

                cardNumber = selectCard();

                // commit the die to the selected card
                commitDie(dieNumber, cardNumber, currentPlayer.dice);
        
                // print cards and status 
                printCards(cardOne, cardTwo, cardThree);
                printCardStatus(cardOne, cardTwo, cardThree, currentPlayer.dice);

                // print dice 
                printDice(currentPlayer.dice);
    
                // check the results
                cardResult = checkCardStatus(cardOne, cardTwo, cardThree, currentPlayer.dice);
                
                // if card requirements met, add to the player's score
                if(cardResult != REQ_NOT_MET) {
                    currentPlayer.score += CARD_POINTS;
                    printf("%s, your score is now %d\n", currentPlayer.player, currentPlayer.score);
                } 

                // player completed a card 
                // give the dice back from the completed card 
                // generate a new card
                // both players have to pick up their dice
                if (cardResult == CARD1_COMMIT) {
                    populateCard(cardOne);
                    reclaimDice(currentPlayer.dice, CARD1_COMMIT);
                    reclaimDice(playerOne.dice, CARD1_COMMIT);
                    reclaimDice(playerTwo.dice, CARD1_COMMIT);
                    break;
                } else if(cardResult == CARD2_COMMIT) {
                    populateCard(cardTwo);
                    reclaimDice(currentPlayer.dice, CARD2_COMMIT);
                    reclaimDice(playerOne.dice, CARD2_COMMIT);
                    reclaimDice(playerTwo.dice, CARD2_COMMIT);
                    break;
                } else if(cardResult == CARD3_COMMIT) {
                    populateCard(cardThree);
                    reclaimDice(currentPlayer.dice, CARD3_COMMIT);
                    reclaimDice(playerOne.dice, CARD3_COMMIT);
                    reclaimDice(playerTwo.dice, CARD3_COMMIT);
                    break;
                }
            }
        }

        // at the end of the turn, switch players
        if(currentPlayer.num == PLAYER1) {
            // copy the changes back to playerOne
            playerOne = currentPlayer;

            // update currentPlayer
            currentPlayer = playerTwo;
        } else if (currentPlayer.num == PLAYER2) {
            // copy the changes back to playerTwo
            playerTwo = currentPlayer;

            // update currentPlayer
            currentPlayer = playerOne;
        }
    }

    // call printGameResults to display the stats
    printGameResults(playerOne, playerTwo);
}

// card with four random dice printed
void randomCard() {
    int die1 = rollDie();
    int die2 = rollDie();
    int die3 = rollDie();
    int die4 = rollDie();

    printf(".-----------------.\n");
    printf("| .-----. .-----. |\n");
    printf("| |  %d  | |  %d  | |\n", die1, die2);
    printf("| '-----' '-----' |\n");
    printf("| .-----. .-----. |\n");
    printf("| |  %d  | |  %d  | |\n", die3, die4);
    printf("| '-----' '-----' |\n");
    printf("'-----------------'\n");
}

// six random dice printed
void randomDice() {
    int die1 = rollDie();
    int die2 = rollDie();
    int die3 = rollDie();
    int die4 = rollDie();
    int die5 = rollDie();
    int die6 = rollDie();

    printf(".-----. .-----. .-----. .-----. .-----. .-----.\n");
    printf("|  %d  | |  %d  | |  %d  | |  %d  | |  %d  | |  %d  |\n", die1, die2, die3, die4, die5, die6);
    printf("'-----' '-----' '-----' '-----' '-----' '-----'\n");
}

// randomly roll a die
int rollDie() {
    int value = (rand() % DICE) + 1;
    return value;
}

// populate the card with random dice
void populateCard(int card[CARD_DICE]) {
    for(int v = 0; v < CARD_DICE; v++) {
        card[v] = rollDie();
    }
}

// print the cards
void printCards(int cardOne[CARD_DICE], int cardTwo[CARD_DICE], int cardThree[CARD_DICE]) {

    printf("\n============================== CARDS ==============================\n\n");

    printf("===== CARD %d ======\t===== CARD %d ======\t===== CARD %d ======\n", CARD1_COMMIT, CARD2_COMMIT, CARD3_COMMIT); 
    printf(".-----------------.\t.-----------------.\t.-----------------.\n");
    printf("| .-----. .-----. |\t| .-----. .-----. |\t| .-----. .-----. |\n");
    printf("| |  %d  | |  %d  | |\t| |  %d  | |  %d  | |\t| |  %d  | |  %d  | |\n", 
        cardOne[0], cardOne[1], cardTwo[0], cardTwo[1], cardThree[0], cardThree[1]);
    printf("| '-----' '-----' |\t| '-----' '-----' |\t| '-----' '-----' |\n");
    printf("| .-----. .-----. |\t| .-----. .-----. |\t| .-----. .-----. |\t\n");
    printf("| |  %d  | |  %d  | |\t| |  %d  | |  %d  | |\t| |  %d  | |  %d  | |\n", 
        cardOne[2], cardOne[3], cardTwo[2], cardTwo[3], cardThree[2], cardThree[3]);
    printf("| '-----' '-----' |\t| '-----' '-----' |\t| '-----' '-----' |\n");
    printf("'-----------------'\t'-----------------'\t'-----------------'\n");
}

// roll the dice that are not committed to a card
// if there are no dice left to roll, player must pick up all the dice
void rollDice(int dice[DICE][2]) {
    if(checkDice(dice) == DICE) {
        printf("No dice left to roll, pick up all dice\n");
        pickUpDice(dice);
        return;
    }

    for(int d = 0; d < DICE; d++) {
        if(dice[d][DIE_STATUS] == NO_COMMIT) {
            dice[d][DIE_VALUE] = rollDie();
        }
    }
}

// print the dice that are not committed to a card
void printDice(int dice[DICE][2]) {
    // if all dice are committed to cards, there is nothing to display
    if(checkDice(dice) == DICE) {
        return;
    }

    // top border
    for(int d = 0; d < DICE; d++) {
        if(dice[d][DIE_STATUS] == NO_COMMIT)
        {
            printf(".-----. ");
        }
    }

    printf("\n");

    // die value
    for(int d = 0; d < DICE; d++) {
        if(dice[d][DIE_STATUS] == NO_COMMIT)
        {
            printf("|  %d  | ", dice[d][DIE_VALUE]);
        }
    }

    printf("\n");

    // bottom border
    for(int d = 0; d < DICE; d++) {
        if(dice[d][DIE_STATUS] == NO_COMMIT)
        {
            printf("'-----' ");
        }
    }

    printf("\n");

    // indexes
    for(int d = 0; d < DICE; d++) {
        if(dice[d][DIE_STATUS] == NO_COMMIT)
        {
            printf(" -(%d)-  ", d + 1);
        }
    }
    printf("\n");
}

// commit the selected die to the selected card 
void commitDie(int dieNum, int cardNum, int playerDice[DICE][2]) {
    // check if the die is already committed, can't move it to another card
    int result = getDieStatus(dieNum, playerDice);

    if(result == NO_COMMIT) {
        // commit the die to the selected card
        playerDice[dieNum - 1][DIE_STATUS] = cardNum;
    }
}

// display which committed die is satisfying each card requirement 
void printCardStatus (int cardOne[CARD_DICE], int cardTwo[CARD_DICE], int cardThree[CARD_DICE], int playerDice[DICE][2]) { 
    // keeps track of the used dice
    int usedDiceOne[DICE] = {0}; 
    int usedDiceTwo[DICE] = {0}; 
    int usedDiceThree[DICE] = {0}; 

    // flags if the cards are complete
    int completeOne = REQ_MET; 
    int completeTwo = REQ_MET; 
    int completeThree = REQ_MET; 

    // print header
    printf("\n== CARD %d STATUS ==\t== CARD %d STATUS ==\t== CARD %d STATUS ==\n", CARD1_COMMIT, CARD2_COMMIT, CARD3_COMMIT); 
    
    // check each requirement individually
    for (int requirement = 0; requirement < CARD_DICE; requirement++) { 
        int requiredValOne = cardOne[requirement]; 
        int requiredValTwo = cardTwo[requirement]; 
        int requiredValThree = cardThree[requirement]; 

        // flags if a matching die was found
        int foundOne = REQ_NOT_MET; 
        int foundTwo = REQ_NOT_MET; 
        int foundThree = REQ_NOT_MET; 
    
        // check card one
        for (int die = 0; die < DICE; die++) { 
            if (playerDice[die][DIE_STATUS] == CARD1_COMMIT && !usedDiceOne[die] && playerDice[die][DIE_VALUE] == requiredValOne) { 
                usedDiceOne[die] = DIE_USED; 
                printf("[%d] <-- Die %d\t\t", requiredValOne, die + 1); 
                foundOne = REQ_MET; 
                break; 
            } 
        }

        // no matching committed die found for card one
        if (!foundOne) {
            printf("[%d] <-- Not matched\t", requiredValOne); 
            completeOne = REQ_NOT_MET; 
        }

        // check card two
        for (int die = 0; die < DICE; die++) { 
            if (playerDice[die][DIE_STATUS] == CARD2_COMMIT && !usedDiceTwo[die] && playerDice[die][DIE_VALUE] == requiredValTwo) { 
                usedDiceTwo[die] = DIE_USED; 
                printf("[%d] <-- Die %d\t\t", requiredValTwo, die + 1); 
                foundTwo = REQ_MET; 
                break; 
            } 
        }

        // no matching committed die found for card two
        if (!foundTwo) {
            printf("[%d] <-- Not matched\t", requiredValTwo); 
            completeTwo = REQ_NOT_MET; 
        }

        // check card three
        for (int die = 0; die < DICE; die++) { 
            if (playerDice[die][DIE_STATUS] == CARD3_COMMIT && !usedDiceThree[die] && playerDice[die][DIE_VALUE] == requiredValThree) { 
                usedDiceThree[die] = DIE_USED; 
                printf("[%d] <-- Die %d\n", requiredValThree, die + 1); 
                foundThree = REQ_MET; 
                break; 
            } 
        }

        // no matching committed die found for card three 
        if (!foundThree) {
            printf("[%d] <-- Not matched\n", requiredValThree); 
            completeThree = REQ_NOT_MET; 
        }
    } 
    
    printf("\n"); 
    
    if (completeOne) { 
        printf("CARD COMPLETE!\t\t"); 
    } else { 
        printf("Card not complete.\t"); 
    } 

    if (completeTwo) { 
        printf("CARD COMPLETE!\t\t"); 
    } else { 
        printf("Card not complete.\t"); 
    } 

    if (completeThree) { 
        printf("CARD COMPLETE!\n"); 
    } else { 
        printf("Card not complete.\n"); 
    } 

    printf("===================================================================\n"); 
}

// prompt player to select a die
int selectDie() {
    int dieNumber = -1;

    do {
        printf("\nEnter die number to commit (1 - 6, 0 to end turn): ");

        // data type validation
        if (scanf("%d", &dieNumber) != SUCCESS) {
            // invalid input such as "abc"
            while (getchar() != '\n');
            dieNumber = -1;
        }

         // data validation
        if (dieNumber != QUIT && (dieNumber < 1 || dieNumber > DICE)) {
            printf("Invalid die number, try again\n");
        }

    } while (dieNumber != QUIT && (dieNumber < 1 || dieNumber > DICE));

    return dieNumber;
}

// prompt player to select a card
int selectCard() {
    int cardNumber = -1;

    do {
        printf("Enter card number (1 - 3): ");

        // data type validation
        if (scanf("%d", &cardNumber) != SUCCESS) {
            // invalid input such as "abc"
            while (getchar() != '\n');
            cardNumber = -1;
        }

        // data validation
        if (cardNumber < 1 || cardNumber > CARDS) {
            printf("Invalid card number, try again\n");
        }

    } while (cardNumber < 1 || cardNumber > CARDS);

    return cardNumber;
}

// prompt player if they want to roll again
int rollAgain() {
    int choice = -1;

    do {
        printf("Roll again? (0 = No, 1 = Yes): ");

        // data type validation
        if (scanf("%d", &choice) != SUCCESS) {
            // invalid input such as "abc"
            while (getchar() != '\n');
            choice = -1;
        }

        // data validation
        if (choice != QUIT && choice != PLAY) {
            printf("Invalid choice, try again\n");
        }

    } while (choice != QUIT && choice != PLAY);

    return choice;
}

// check if all dice are committed
int checkDice(int playerDice[DICE][2]) {
    int count = 0;

    for(int d = 0; d < DICE; d++) {
        if(playerDice[d][DIE_STATUS] != NO_COMMIT) {
            count++;
        }
    }

    return count;
}

// reclaim the dice from a committed card to roll again 
void reclaimDice(int playerDice[DICE][2], int cardNum) {
    for(int d = 0; d < DICE; d++) {
        if (playerDice[d][DIE_STATUS] == cardNum) {
            playerDice[d][DIE_STATUS] = NO_COMMIT;
        }
    }
}

// pick up all committed dice to 
void pickUpDice(int playerDice[DICE][2]) {
    for(int d = 0; d < DICE; d++) {
            playerDice[d][DIE_STATUS] = NO_COMMIT;
    }
}

// check if card requirements have been met
int checkCardStatus(int cardOne[CARD_DICE], int cardTwo[CARD_DICE], int cardThree[CARD_DICE], int playerDice[DICE][2]) {
    // return value for a completed card
    int requirementMet = REQ_NOT_MET;

    // keeps track of the used dice
    int usedDiceOne[DICE] = {0};
    int usedDiceTwo[DICE] = {0};
    int usedDiceThree[DICE] = {0};

    // flags if the cards are complete
    int completeOne = REQ_MET;
    int completeTwo = REQ_MET;
    int completeThree = REQ_MET;

    // check each requirement individually
    for (int requirement = 0; requirement < CARD_DICE; requirement++) {

        int requiredValOne = cardOne[requirement];
        int requiredValTwo = cardTwo[requirement];
        int requiredValThree = cardThree[requirement];

        // flags if a matching die was found
        int foundOne = REQ_NOT_MET;
        int foundTwo = REQ_NOT_MET;
        int foundThree = REQ_NOT_MET;

        // check card one
        for (int die = 0; die < DICE; die++) {
            if (playerDice[die][DIE_STATUS] == CARD1_COMMIT &&
                !usedDiceOne[die] &&
                playerDice[die][DIE_VALUE] == requiredValOne) {

                usedDiceOne[die] = DIE_USED;
                foundOne = REQ_MET;
                break;
            }
        }

        // no matching committed die found for card one
        if (!foundOne) {
            completeOne = REQ_NOT_MET;
        }

        // check card two
        for (int die = 0; die < DICE; die++) {
            if (playerDice[die][DIE_STATUS] == CARD2_COMMIT &&
                !usedDiceTwo[die] &&
                playerDice[die][DIE_VALUE] == requiredValTwo) {

                usedDiceTwo[die] = DIE_USED;
                foundTwo = REQ_MET;
                break;
            }
        }

        // no matching committed die found for card two
        if (!foundTwo) {
            completeTwo = REQ_NOT_MET;
        }

        // check card three
        for (int die = 0; die < DICE; die++) {
            if (playerDice[die][DIE_STATUS] == CARD3_COMMIT &&
                !usedDiceThree[die] &&
                playerDice[die][DIE_VALUE] == requiredValThree) {

                usedDiceThree[die] = DIE_USED;
                foundThree = REQ_MET;
                break;
            }
        }

        // no matching committed die found for card three
        if (!foundThree) {
            completeThree = REQ_NOT_MET;
        }
    }

    // determine which card was completed
    if (completeOne) {
        requirementMet = CARD1_COMMIT;
    }

    if (completeTwo) {
        requirementMet = CARD2_COMMIT;
    }

    if (completeThree) {
        requirementMet = CARD3_COMMIT;
    }

    return requirementMet;
}

// check if the selected die is already committed to a dice card
int getDieStatus(int dieNum, int playerDice[DICE][2]) {  
    if (playerDice[dieNum - 1][DIE_STATUS] != NO_COMMIT) { 
        printf("Die %d is already committed to Card %d.\n", dieNum, playerDice[dieNum - 1][DIE_STATUS]); 
        return playerDice[dieNum - 1][DIE_STATUS]; 
    } 
    
    return NO_COMMIT;
}

// check if the game is over
int isGameOver(Player playerOne, Player playerTwo) {
    int gameOver = FALSE;

    if(playerOne.score >= WIN || playerTwo.score >= WIN) {
        gameOver = TRUE;
    }
    
    return gameOver;
}

// display the results after the game is over
void printGameResults(Player playerOne, Player playerTwo) {
    printf("\n==========================\n"); 
    
    if(playerOne.score >= WIN) {
        printf("%s", playerOne.player );
    } else {
        printf("%s", playerTwo.player );
    }

    printf(" WON THE GAME!\n\n");
    printf("%s's score: %d\n", playerOne.player, playerOne.score);
    printf("%s's score: %d\n", playerTwo.player, playerTwo.score);
    printf("==========================\n"); 
}

// function displayMenu provides players with their options
int printMenu() {
    int choice = 0;

    // continue looping until player selects a valid option
    do {
        printf("\nSelect a menu option:\n");
        printf("1. Play Roll 4 It\n");
        printf("2. View game rules\n");
        printf("3. View leaderboard\n");
        printf("4. Exit game\n");

        // data type validation
        if (scanf("%d", &choice) != SUCCESS) {
            // invalid input such as "abc"
            while (getchar() != '\n');
            choice = 0;
        }

        // data validation
        if (choice < PLAY || choice > EXIT) {
            printf("Invalid choice, try again\n");
        }
    } while (choice < PLAY || choice > EXIT);

    return choice;
}

void printRules() {
    printf(".------------------ ROLL 4 IT - GAME RULES --------------------.\n");
    printf("| OBJECTIVE:                                                   |\n");
    printf("| Be the first player to reach 40 points.                      |\n");
    printf("|                                                              |\n");
    printf("| GAME SETUP:                                                  |\n");
    printf("| - Each player receives six dice.                             |\n");
    printf("| - Three scoring cards are placed face up.                    |\n");
    printf("| - Each scoring card has a combination of four dice that      |\n");
    printf("|   must be rolled to claim it.                                |\n");
    printf("| - Each scoring card is worth 10 points                       |\n");
    printf("|                                                              |\n");
    printf("| PLAYER TURN:                                                 |\n");
    printf("| - Roll all of the available dice.                            |\n");
    printf("| - Place dice on the scoring cards where they match the       |\n");
    printf("|    numbers shown on the cards.                               |\n");
    printf("| - May place multiple dice on the same card or use dice       |\n");
    printf("|    on different cards.                                       |\n");
    printf("| - If the required combination on a card is completed,        |\n");
    printf("|    claim that card and receive 10 points.                    |\n");
    printf("|                                                              |\n");
    printf("| UNCLAIMED CARDS:                                             |\n");
    printf("| - Dice placed on an incomplete card remain there for the     |\n");
    printf("|   next roll.                                                 |\n");
    printf("| - May NOT move the dice between cards unless all dice        |\n");
    printf("|   are picked up.                                             |\n");
    printf("|                                                              |\n");
    printf("| WINNING THE GAME:                                            |\n");
    printf("| - Continue taking turns until a player reaches 40 points.    |\n");
    printf("| - The first player to reach 40 points wins the game.         |\n");
    printf("|                                                              |\n");
    printf("| IMPORTANT:                                                   |\n");
    printf("| - Each die can only be used on one scoring card at a time.   |\n");
    printf("| - Players must decide how to use their dice after each roll. |\n");
    printf("| - Dice placement and strategy are important to winning!      |\n");
    printf("'--------------------------------------------------------------'\n");
}
// read the leaderboard file and display the contents
void readLeaderboardFile() {
    // stores one line at a time from the data file
    char line[LINE];

    // tracks which element of array data to store in
    int fieldIdx = ZERO;

    // array of strings holding every data element from the file
    char *data[DATA];

    // open the data file for reading
    FILE *fp = fopen("leaderboard.txt", "r");

    // file could not be found
    if (fp == NULL) {
        perror("Error opening file");
        return;
    }

    // read the file one line at a time
    while (fgets(line, LINE, fp) != NULL) {
        // split the line at the commas
        char *field = strtok(line, ",");

        // remove leading and trailing white space
        field = trim(field);

        // walk through each field on the line
        while (field != NULL) {
            // allocate memory for the field plus the null terminator
            data[fieldIdx] = malloc(strlen(field) + 1);

            // copy the field into the data array
            strcpy(data[fieldIdx], field);

            // next field on the same line
            field = strtok(NULL, ",");
            field = trim(field);

            fieldIdx++;
        }
    }

    // close the file
    fclose(fp);

    // leaderboard header
    printf("\n.---------------- ROLL 4 IT - Leaderboard ----------------.\n");
    printf("|                                                         |\n");
    printf("|     %-16s%-16s%-20s|\n", "Position", "Player", "Wins");
    printf("|                                                         |\n");

    // each line of the file is position, player, wins
    for (int i = ZERO; i < fieldIdx; i += FIELDS) {
        printf("|     %-16s%-16s%-20s|\n", data[i], data[i + 1], data[i + 2]);
    }

    // leaderboard footer
    printf("|                                                         |\n");
    printf("'_________________________________________________________'\n");
}

// trim the leading and trailing white space from a string
char *trim(char *str) {
    // nothing to trim
    if (str == NULL || *str == '\0') {
        return str;
    }

    // move past any leading white space
    char *start = str;

    while (isspace((unsigned char)*start)) {
        start++;
    }

    // find the end of the string
    char *end = str + strlen(str) - 1;

    // move back past any trailing white space
    while (end > start && isspace((unsigned char)*end)) {
        end--;
    }

    // close off the string after the last real character
    end[1] = '\0';

    return start;
}
