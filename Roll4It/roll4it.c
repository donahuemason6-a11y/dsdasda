/*
 * COP 3223 - Introduction to Programming in C
 * Assignment 1 - Roll4It
 *
 * Simulates the opening screens of the game "Roll For It":
 * prints the game logo, a sample row of six dice, and a
 * sample card holding four dice, then waits for the user
 * to press Enter before exiting.
 */

/* Preprocessor commands to include C library header files */
#include <stdio.h>
#include <stdlib.h>

/* Function declarations (prototypes) */
void logo(void);
void sampleDice(void);
void sampleCard(void);

/* main - program entry point */
int main(void)
{
    /* Display the game logo */
    logo();

    /* Display a sample row of six dice */
    sampleDice();

    /* Display a sample card with four dice */
    sampleCard();

    /* Pause the command prompt until the user presses Enter */
    printf("Press Enter to continue...");
    getchar();

    /* Return 0 to indicate successful operation of the program */
    return 0;
}

/*
 * logo - prints the name of the game in ASCII art
 */
void logo(void)
{
    printf(" _____    ____   _       _       _  _    _____  _______ \n");
    printf("|  __ \\  / __ \\ | |     | |     | || |  |_   _||__   __|\n");
    printf("| |__) || |  | || |     | |     | || |_   | |     | |   \n");
    printf("|  _  / | |  | || |     | |     |__   _|  | |     | |   \n");
    printf("| | \\ \\ | |__| || |____ | |____    | |   _| |_    | |   \n");
    printf("|_|  \\_\\ \\____/ |______||______|   |_|  |_____|   |_|   \n");
    printf("\n");
}

/*
 * sampleDice - prints a sample row of six dice
 */
void sampleDice(void)
{
    printf(" .-----.  .-----.  .-----.  .-----.  .-----.  .-----. \n");
    printf(" |  1  |  |  2  |  |  3  |  |  4  |  |  5  |  |  6  | \n");
    printf(" '-----'  '-----'  '-----'  '-----'  '-----'  '-----' \n");
    printf("\n");
}

/*
 * sampleCard - prints a sample card holding four dice
 */
void sampleCard(void)
{
    printf(" .-----------------------. \n");
    printf(" |   .-----.   .-----.   | \n");
    printf(" |   |  1  |   |  2  |   | \n");
    printf(" |   '-----'   '-----'   | \n");
    printf(" |                       | \n");
    printf(" |   .-----.   .-----.   | \n");
    printf(" |   |  3  |   |  4  |   | \n");
    printf(" |   '-----'   '-----'   | \n");
    printf(" '-----------------------' \n");
    printf("\n");
}
