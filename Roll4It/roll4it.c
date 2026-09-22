// COP 3223 Assignment 2 - Roll4It

// libraries
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// size of the name array
#define NAME 20

void logo();
void sampleDice();
void sampleCard();
void play();
void randomCard();
void randomDice();
int rollDie();

int main(){
    // seed the random numbers
    srand(time(NULL));

    logo();
    //sampleDice();
    //sampleCard();
    play();

    // clear the input buffer
    while((getchar()) != '\n');

    // pause
    printf("Press Enter to continue...");
    getchar();
    return 0;
}

// prints logo
void logo()
{
    printf(" _______       _______       _______       _______       _______       _______       __________\n");
    printf("|       |     |       |     |       |     |       |     |       |     |       |     |          |\n");
    printf("| RRRR  |     |  OOO  |     | L     |     | L     |     | 4   4 |     | IIIII |     | TTTTT    |\n");
    printf("| R   R |     | O   O |     | L     |     | L     |     | 4   4 |     |   I   |     |   T      |\n");
    printf("| RRRR  |     | O   O |     | L     |     | L     |     | 44444 |     |   I   |     |   T      |\n");
    printf("| R  R  |     | O   O |     | L     |     | L     |     |     4 |     |   I   |     |   T      |\n");
    printf("| R   R |     |  OOO  |     | LLLLL |     | LLLLL |     |     4 |     | IIIII |     |   T      |\n");
    printf("|_______|     |_______|     |_______|     |_______|     |_______|     |_______|     |_______|\n");
    printf("\n");
}

// prints dice
void sampleDice()
{
    printf(" _____       _____       _____       _____       _____       _____\n");
    printf("|     |     |     |     |     |     |     |     |     |     |     |\n");
    printf("|  1  |     |  2  |     |  3  |     |  4  |     |  5  |     |  6  |\n");
    printf("|_____|     |_____|     |_____|     |_____|     |_____|     |_____|\n");
    printf("\n");
}

// prints card with numbered dice
void sampleCard()
{
    printf(" _____________________\n");
    printf("|   _____       _____   |\n");
    printf("|  |     |     |     |  |\n");
    printf("|  |  1  |     |  2  |  |\n");
    printf("|  |_____|     |_____|  |\n");
    printf("|   _____       _____   |\n");
    printf("|  |     |     |     |  |\n");
    printf("|  |  3  |     |  4  |  |\n");
    printf("|  |_____|     |_____|  |\n");
    printf("|_____________________|\n");
    printf("\n");
}

// asks the player name then deals 3 cards and rolls the dice
void play()
{
    char player[NAME];

    printf("Enter the player's name\n");
    scanf("%s", player);

    randomCard();
    randomCard();
    randomCard();
    randomDice();
}

// prints a card with 4 random dice
void randomCard()
{
    int die1 = rollDie();
    int die2 = rollDie();
    int die3 = rollDie();
    int die4 = rollDie();

    printf(" _____________________\n");
    printf("|   _____       _____   |\n");
    printf("|  |     |     |     |  |\n");
    printf("|  |  %d  |     |  %d  |  |\n", die1, die2);
    printf("|  |_____|     |_____|  |\n");
    printf("|   _____       _____   |\n");
    printf("|  |     |     |     |  |\n");
    printf("|  |  %d  |     |  %d  |  |\n", die3, die4);
    printf("|  |_____|     |_____|  |\n");
    printf("|_____________________|\n");
    printf("\n");
}

// rolls the 6 dice
void randomDice()
{
    int die1 = rollDie();
    int die2 = rollDie();
    int die3 = rollDie();
    int die4 = rollDie();
    int die5 = rollDie();
    int die6 = rollDie();

    printf(" _____       _____       _____       _____       _____       _____\n");
    printf("|     |     |     |     |     |     |     |     |     |     |     |\n");
    printf("|  %d  |     |  %d  |     |  %d  |     |  %d  |     |  %d  |     |  %d  |\n", die1, die2, die3, die4, die5, die6);
    printf("|_____|     |_____|     |_____|     |_____|     |_____|     |_____|\n");
    printf("\n");
}

// random number 1 to 6
int rollDie()
{
    return rand() % 6 + 1;
}
