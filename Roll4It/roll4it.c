// COP 3223 Assignment 1 - Roll4It
// This program prints the game logo, six dice, and a card with 4 dice.

// include the C libraries
#include <stdio.h>
#include <stdlib.h>

// function prototypes
void logo();
void sampleDice();
void sampleCard();

int main()
{
    // call the three functions to print everything
    logo();
    sampleDice();
    sampleCard();

    // pause so the window doesn't close right away
    printf("Press Enter to continue...");
    getchar();

    // return 0 means the program worked
    return 0;
}

// prints the name of the game in big letters
void logo()
{
    printf("RRRR    OOO   L      L      4   4  III  TTTTT\n");
    printf("R   R  O   O  L      L      4   4   I     T\n");
    printf("RRRR   O   O  L      L      44444   I     T\n");
    printf("R  R   O   O  L      L          4   I     T\n");
    printf("R   R   OOO   LLLLL  LLLLL      4  III    T\n");
    printf("\n");
}

// prints six dice numbered 1 to 6
void sampleDice()
{
    printf(" _____   _____   _____   _____   _____   _____\n");
    printf("|     | |     | |     | |     | |     | |     |\n");
    printf("|  1  | |  2  | |  3  | |  4  | |  5  | |  6  |\n");
    printf("|_____| |_____| |_____| |_____| |_____| |_____|\n");
    printf("\n");
}

// prints one card with dice 1 2 3 4 on it
void sampleCard()
{
    printf(" _____________________\n");
    printf("|   _____     _____   |\n");
    printf("|  |     |   |     |  |\n");
    printf("|  |  1  |   |  2  |  |\n");
    printf("|  |_____|   |_____|  |\n");
    printf("|   _____     _____   |\n");
    printf("|  |     |   |     |  |\n");
    printf("|  |  3  |   |  4  |  |\n");
    printf("|  |_____|   |_____|  |\n");
    printf("|_____________________|\n");
    printf("\n");
}
