#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

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
// success flage
#define SUCCESS 1

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
int checkDice(int playerDice[DICE][2]);
void reclaimDice(int playerDice[DICE][2], int cardNum);
void pickUpDice(int playerDice[DICE][2]);
int checkCardStatus(int cardOne[CARD_DICE], int cardTwo[CARD_DICE], int cardThree[CARD_DICE], int playerDice[DICE][2]);
int getDieStatus(int dieNum, int playerDice[DICE][2]);
int selectDie();
int selectCard();
int rollAgain();

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

    // call play function
    play();

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
    char player[NAME];
    int score = 0;
    
    // loop control variables
    int roll = PLAY;
    int turn = PLAY;

    // array of six dice, second column tracks if the die is committed to a card
    int dice[DICE][2];
    
    // array of values on a card
    int cardOne[CARD_DICE];
    int cardTwo[CARD_DICE];
    int cardThree[CARD_DICE];

    // used to store the player's selected die 
    int dieNumber = 0;

    // used to store the player's selected card
    int cardNumber = 0;

    // stores which card was completed
    int cardResult = REQ_NOT_MET;

    // initialize the arrays to all -1 
    memset(dice, NO_COMMIT, sizeof(dice));
    memset(cardOne, NO_COMMIT, sizeof(cardOne));
    memset(cardTwo, NO_COMMIT, sizeof(cardTwo));
    memset(cardThree, NO_COMMIT, sizeof(cardThree));

    // store the player's name
    printf("Enter the player's name\n");
    scanf("%s", player);
    
    // generate three random cards
    populateCard(cardOne);
    populateCard(cardTwo);
    populateCard(cardThree);

    // for each roll, need to roll the dice, print the card, print the status, print the dice
    while(roll) {
        // Roll the dice
        rollDice(dice);

        // print the cards and status
        printCards(cardOne, cardTwo, cardThree);
        printCardStatus(cardOne, cardTwo, cardThree, dice);

        // print the dice
        printDice(dice);

        while(turn) {
            // all six dice are committed, player has to pick them all up
            if (checkDice(dice) == DICE) {
                printf("No dice left to select, pick up all dice\n");
                pickUpDice(dice);
                break;
            }
            else {
                // prompt player to select die and store
                dieNumber = selectDie();

                // end turn
                if (dieNumber == QUIT) {
                    break;
                }

                cardNumber = selectCard();

                // commit the die to the selected card
                commitDie(dieNumber, cardNumber, dice);

                // print cards and status 
                printCards(cardOne, cardTwo, cardThree);
                printCardStatus(cardOne, cardTwo, cardThree, dice);

                // print dice 
                printDice(dice);

                // check if a card was completed
                cardResult = checkCardStatus(cardOne, cardTwo, cardThree, dice);

                // card completed, add the points
                if (cardResult != REQ_NOT_MET) {
                    score = score + CARD_POINTS;
                    printf("%s, your score is now %d\n", player, score);
                }

                // replace the completed card and reclaim its dice
                if (cardResult == CARD1_COMMIT) {
                    populateCard(cardOne);
                    reclaimDice(dice, CARD1_COMMIT);
                    break;
                }
                else if (cardResult == CARD2_COMMIT) {
                    populateCard(cardTwo);
                    reclaimDice(dice, CARD2_COMMIT);
                    break;
                }
                else if (cardResult == CARD3_COMMIT) {
                    populateCard(cardThree);
                    reclaimDice(dice, CARD3_COMMIT);
                    break;
                }
            }
        }   
    
        roll = rollAgain();
    }
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
void rollDice(int dice[DICE][2]) {
    // all dice are committed, nothing to roll so pick them all up
    if (checkDice(dice) == DICE) {
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
    // nothing to print when every die is committed
    if (checkDice(dice) == DICE) {
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
    // check if the die is already on a card
    int result = getDieStatus(dieNum, playerDice);

    if (result == NO_COMMIT) {
        playerDice[dieNum - 1][DIE_STATUS] = cardNum;
    }
}

// display which committed die is satisfying each card requirement 
void printCardStatus (int cardOne[CARD_DICE], int cardTwo[CARD_DICE], int cardThree[CARD_DICE], int playerDice[DICE][2]) { 
    // flags if all of a card's requirements are met
    int completeOne = REQ_MET;
    int completeTwo = REQ_MET;
    int completeThree = REQ_MET;

    // keeps track of the used dice
    int usedDiceOne[DICE] = {0}; 
    int usedDiceTwo[DICE] = {0}; 
    int usedDiceThree[DICE] = {0}; 

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

    // overall status for card one
    if (completeOne) {
        printf("CARD COMPLETE!\t\t");
    }
    else {
        printf("Card not complete.\t");
    }

    // overall status for card two
    if (completeTwo) {
        printf("CARD COMPLETE!\t\t");
    }
    else {
        printf("Card not complete.\t");
    }

    // overall status for card three
    if (completeThree) {
        printf("CARD COMPLETE!\n");
    }
    else {
        printf("Card not complete.\n");
    }
    
    printf("=================================\n"); 
}

// count how many dice are committed to cards
int checkDice(int playerDice[DICE][2]) {
    int count = 0;

    for(int d = 0; d < DICE; d++) {
        if (playerDice[d][DIE_STATUS] != NO_COMMIT) {
            count++;
        }
    }

    return count;
}

// take back the dice from a completed card
void reclaimDice(int playerDice[DICE][2], int cardNum) {
    for(int d = 0; d < DICE; d++) {
        if (playerDice[d][DIE_STATUS] == cardNum) {
            playerDice[d][DIE_STATUS] = NO_COMMIT;
        }
    }
}

// pick up every die no matter what card it is on
void pickUpDice(int playerDice[DICE][2]) {
    for(int d = 0; d < DICE; d++) {
        playerDice[d][DIE_STATUS] = NO_COMMIT;
    }
}

// check if a card is complete and return which one
int checkCardStatus(int cardOne[CARD_DICE], int cardTwo[CARD_DICE], int cardThree[CARD_DICE], int playerDice[DICE][2]) {
    // return value for a completed card
    int requirementMet = REQ_NOT_MET;

    // keeps track of the used dice
    int usedDiceOne[DICE] = {0}; 
    int usedDiceTwo[DICE] = {0}; 
    int usedDiceThree[DICE] = {0}; 

    // flags if all of a card's requirements are met
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
            if (playerDice[die][DIE_STATUS] == CARD1_COMMIT && !usedDiceOne[die] && playerDice[die][DIE_VALUE] == requiredValOne) { 
                usedDiceOne[die] = DIE_USED; 
                foundOne = REQ_MET; 
                break; 
            } 
        }

        if (!foundOne) {
            completeOne = REQ_NOT_MET;
        }

        // check card two
        for (int die = 0; die < DICE; die++) { 
            if (playerDice[die][DIE_STATUS] == CARD2_COMMIT && !usedDiceTwo[die] && playerDice[die][DIE_VALUE] == requiredValTwo) { 
                usedDiceTwo[die] = DIE_USED; 
                foundTwo = REQ_MET; 
                break; 
            } 
        }

        if (!foundTwo) {
            completeTwo = REQ_NOT_MET;
        }

        // check card three
        for (int die = 0; die < DICE; die++) { 
            if (playerDice[die][DIE_STATUS] == CARD3_COMMIT && !usedDiceThree[die] && playerDice[die][DIE_VALUE] == requiredValThree) { 
                usedDiceThree[die] = DIE_USED; 
                foundThree = REQ_MET; 
                break; 
            } 
        }

        if (!foundThree) {
            completeThree = REQ_NOT_MET;
        }
    } 

    // report which card is done
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

// check if a die is already committed to a card
int getDieStatus(int dieNum, int playerDice[DICE][2]) {
    if (playerDice[dieNum - 1][DIE_STATUS] != NO_COMMIT) {
        printf("Die %d is already committed to Card %d.\n", dieNum, playerDice[dieNum - 1][DIE_STATUS]);
        return playerDice[dieNum - 1][DIE_STATUS];
    }

    return NO_COMMIT;
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
