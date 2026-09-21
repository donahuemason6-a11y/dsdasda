#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// size of the player name array
#define NAME 20

// function prototypes
void logo();
void sampleDice();
void sampleCard();
void play();
void randomCard();
void randomDice();
int rollDie();

// main function
int main() {

    // seed the random number generator with the current time
    srand(time(NULL));

    // call function logo
    logo();

    // call sample dice function
    //sampleDice();

    // call sample card function
    //sampleCard();

    // call function play to start the game
    play();

    // clear the input buffer
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

// asks for the player's name then deals the cards and rolls the dice
void play() {

    // stores the player's name
    char player[NAME];

    // prompt the player for their name and read it in
    printf("Enter the player's name\n");
    scanf("%s", player);

    // deal three random playing cards
    randomCard();
    randomCard();
    randomCard();

    // roll the player's six dice
    randomDice();
}

// prints one card with four random die values on it
void randomCard() {

    // roll four dice for the card
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

// prints the player's six dice with random values
void randomDice() {

    // roll the six dice
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

// returns a random number from 1 to 6 like rolling one die
int rollDie() {
    return rand() % 6 + 1;
}
