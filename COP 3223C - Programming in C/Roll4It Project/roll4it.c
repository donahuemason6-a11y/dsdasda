#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

// constants
#define NAME 20
#define DICE 6
#define DIE_VALUE 0
#define DIE_STATUS 1
#define NO_COMMIT -1
#define CARD1_COMMIT 1
#define CARD2_COMMIT 2
#define CARD3_COMMIT 3
#define PLAY 1
#define QUIT 0
#define CARDS 3
#define CARD_DICE 4
#define CARD_POINTS 10
#define REQ_NOT_MET 0
#define REQ_MET 1
#define DIE_USED 1
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
int printCardStatus(int cardOne[CARD_DICE], int cardTwo[CARD_DICE], int cardThree[CARD_DICE], int playerDice[DICE][2]);
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
    // game variables
    int score = 0;
    int roll = PLAY;
    int turn = PLAY;
    int dice[DICE][2];
    int cardOne[CARD_DICE];
    int cardTwo[CARD_DICE];
    int cardThree[CARD_DICE];
    int dieNumber = 0;
    int cardNumber = 0;
    char player[NAME];

    // initialize the arrays to -1
    memset(dice, -1, sizeof(dice));
    memset(cardOne, -1, sizeof(cardOne));
    memset(cardTwo, -1, sizeof(cardTwo));
    memset(cardThree, -1, sizeof(cardThree));

    printf("Enter the player's name\n");
    scanf("%s", player);

    // populate the three playing cards
    populateCard(cardOne);
    populateCard(cardTwo);
    populateCard(cardThree);

    // keep playing until the player quits
    while (roll == PLAY) {
        rollDice(dice);
        printCards(cardOne, cardTwo, cardThree);
        printCardStatus(cardOne, cardTwo, cardThree, dice);
        printDice(dice);

        // player commits dice until they end their turn
        while (turn == PLAY) {
            dieNumber = selectDie();

            if (dieNumber == QUIT) {
                break;
            }

            cardNumber = selectCard();
            commitDie(dieNumber, cardNumber, dice);
            printCards(cardOne, cardTwo, cardThree);
            printCardStatus(cardOne, cardTwo, cardThree, dice);
            printDice(dice);
        }

        roll = rollAgain();
    }
}

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

int rollDie() {
    int value = (rand() % 6) + 1;
    return value;
}

// fills one card with four random die values
void populateCard(int card[CARD_DICE]) {
    int i;

    for (i = 0; i < CARD_DICE; i++) {
        card[i] = rollDie();
    }
}

// displays the three cards side by side
void printCards(int cardOne[CARD_DICE], int cardTwo[CARD_DICE], int cardThree[CARD_DICE]) {
    printf("\n============================ CARDS ============================\n\n");
    printf("===== CARD 1 =====     ===== CARD 2 =====     ===== CARD 3 =====\n");
    printf(".-----------------.    .-----------------.    .-----------------.\n");
    printf("| .-----. .-----. |    | .-----. .-----. |    | .-----. .-----. |\n");
    printf("| |  %d  | |  %d  | |    | |  %d  | |  %d  | |    | |  %d  | |  %d  | |\n", cardOne[0], cardOne[1], cardTwo[0], cardTwo[1], cardThree[0], cardThree[1]);
    printf("| '-----' '-----' |    | '-----' '-----' |    | '-----' '-----' |\n");
    printf("| .-----. .-----. |    | .-----. .-----. |    | .-----. .-----. |\n");
    printf("| |  %d  | |  %d  | |    | |  %d  | |  %d  | |    | |  %d  | |  %d  | |\n", cardOne[2], cardOne[3], cardTwo[2], cardTwo[3], cardThree[2], cardThree[3]);
    printf("| '-----' '-----' |    | '-----' '-----' |    | '-----' '-----' |\n");
    printf("'-----------------'    '-----------------'    '-----------------'\n\n");
}

// rolls only the dice that are not committed to a card
void rollDice(int dice[DICE][2]) {
    int i;

    for (i = 0; i < DICE; i++) {
        if (dice[i][DIE_STATUS] == NO_COMMIT) {
            dice[i][DIE_VALUE] = rollDie();
        }
    }
}

// displays only the dice that are not committed to a card
void printDice(int dice[DICE][2]) {
    int i;

    // top border
    for (i = 0; i < DICE; i++) {
        if (dice[i][DIE_STATUS] == NO_COMMIT) {
            printf(".-----. ");
        }
    }
    printf("\n");

    // die values
    for (i = 0; i < DICE; i++) {
        if (dice[i][DIE_STATUS] == NO_COMMIT) {
            printf("|  %d  | ", dice[i][DIE_VALUE]);
        }
    }
    printf("\n");

    // bottom border
    for (i = 0; i < DICE; i++) {
        if (dice[i][DIE_STATUS] == NO_COMMIT) {
            printf("'-----' ");
        }
    }
    printf("\n");

    // die numbers for the player to select
    for (i = 0; i < DICE; i++) {
        if (dice[i][DIE_STATUS] == NO_COMMIT) {
            printf(" -(%d)-  ", i + 1);
        }
    }
    printf("\n");
}

// marks the selected die as committed to the selected card
void commitDie(int dieNum, int cardNum, int playerDice[DICE][2]) {
    playerDice[dieNum - 1][DIE_STATUS] = cardNum;
}

// shows which card requirements have been matched by committed dice
int printCardStatus(int cardOne[CARD_DICE], int cardTwo[CARD_DICE], int cardThree[CARD_DICE], int playerDice[DICE][2]) {
    int requirementMet = REQ_NOT_MET;
    int usedDiceOne[DICE] = {0};
    int usedDiceTwo[DICE] = {0};
    int usedDiceThree[DICE] = {0};
    int i;
    int j;

    // status header
    printf("== CARD 1 STATUS ==     == CARD 2 STATUS ==     == CARD 3 STATUS ==\n");

    // check each of the four requirements on the cards
    for (i = 0; i < CARD_DICE; i++) {
        int requiredValOne = cardOne[i];
        int requiredValTwo = cardTwo[i];
        int requiredValThree = cardThree[i];
        int foundOne = REQ_NOT_MET;
        int foundTwo = REQ_NOT_MET;
        int foundThree = REQ_NOT_MET;

        // card one
        for (j = 0; j < DICE; j++) {
            if (playerDice[j][DIE_STATUS] == CARD1_COMMIT && usedDiceOne[j] != DIE_USED && playerDice[j][DIE_VALUE] == requiredValOne) {
                usedDiceOne[j] = DIE_USED;
                printf("[%d] <-- Die %d           ", requiredValOne, j + 1);
                foundOne = REQ_MET;
                break;
            }
        }
        if (foundOne == REQ_NOT_MET) {
            printf("[%d] <-- Not matched     ", requiredValOne);
        }

        // card two
        for (j = 0; j < DICE; j++) {
            if (playerDice[j][DIE_STATUS] == CARD2_COMMIT && usedDiceTwo[j] != DIE_USED && playerDice[j][DIE_VALUE] == requiredValTwo) {
                usedDiceTwo[j] = DIE_USED;
                printf("[%d] <-- Die %d           ", requiredValTwo, j + 1);
                foundTwo = REQ_MET;
                break;
            }
        }
        if (foundTwo == REQ_NOT_MET) {
            printf("[%d] <-- Not matched     ", requiredValTwo);
        }

        // card three
        for (j = 0; j < DICE; j++) {
            if (playerDice[j][DIE_STATUS] == CARD3_COMMIT && usedDiceThree[j] != DIE_USED && playerDice[j][DIE_VALUE] == requiredValThree) {
                usedDiceThree[j] = DIE_USED;
                printf("[%d] <-- Die %d\n", requiredValThree, j + 1);
                foundThree = REQ_MET;
                break;
            }
        }
        if (foundThree == REQ_NOT_MET) {
            printf("[%d] <-- Not matched\n", requiredValThree);
        }
    }

    // bottom border
    printf("=====================================================\n");

    return requirementMet;
}

// asks the player for a die number with validation
int selectDie() {
    int dieNumber = -1;

    do {
        printf("\nEnter die number to commit (1 - 6, 0 to end turn): ");

        // data type validation
        if (scanf("%d", &dieNumber) != SUCCESS) {
            while (getchar() != '\n');
            dieNumber = -1;
        }

        // data input validation
        if (dieNumber != QUIT && (dieNumber < 1 || dieNumber > DICE)) {
            printf("Invalid die number\n");
        }
    } while (dieNumber != QUIT && (dieNumber < 1 || dieNumber > DICE));

    return dieNumber;
}

// asks the player for a card number with validation
int selectCard() {
    int cardNumber = -1;

    do {
        printf("Enter card number (1 - 3): ");

        // data type validation
        if (scanf("%d", &cardNumber) != SUCCESS) {
            while (getchar() != '\n');
            cardNumber = -1;
        }

        // data input validation
        if (cardNumber < 1 || cardNumber > CARDS) {
            printf("Invalid card number\n");
        }
    } while (cardNumber < 1 || cardNumber > CARDS);

    return cardNumber;
}

// asks the player if they want to roll again with validation
int rollAgain() {
    int choice = -1;

    do {
        printf("Roll again? (0 = No, 1 = Yes): ");

        // data type validation
        if (scanf("%d", &choice) != SUCCESS) {
            while (getchar() != '\n');
            choice = -1;
        }

        // data input validation
        if (choice != QUIT && choice != PLAY) {
            printf("Invalid entry\n");
        }
    } while (choice != QUIT && choice != PLAY);

    return choice;
}
