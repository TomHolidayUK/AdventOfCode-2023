// Plan
// 1 - Extract data from .txt file
// 2 - Line by line find max of each colour and compare to limits
// 3 - If all are within limits, add 1 to the total

#include <stdio.h>
#include <string.h>
#include <ctype.h>

void removeFirstXCharacters(char *str, size_t x)
{
    size_t len = strlen(str);

    if (x >= len)
    {
        str[0] = '\0'; // If string is empty
    }
    else
    {
        // Move the string content x characters to the left with memmove()
        memmove(str, str + x, len - x + 1); // +1 to include the null terminator
    }
}

#define MAX_LINES 100
#define MAX_LENGTH 200

int main()
{

    FILE *file; // Create file pointer
    char filename[] = "data2.txt";

    // Open the file for reading
    file = fopen(filename, "r");

    char line[MAX_LENGTH];
    char *lines[MAX_LINES];
    int lineCount = 0;
    int total = 0;
    int total2 = 0;

    // Check if the file was opened successfully
    if (file != NULL)
    {
        printf("File Open Successful\n");
        while (fgets(line, sizeof(line), file) != NULL && lineCount < MAX_LINES)
        {
            // Print the line
            printf("%s\n", line);
            char *token;

            size_t removeCount = 8;

            removeFirstXCharacters(line, removeCount);

            printf("Cropped String: %s\n", line);

            int max_blue = 0;
            int max_red = 0;
            int max_green = 0;

            token = strtok(line, ";"); // strtok splits the string at the chosen delimeter by creating tokens
            while (token != NULL)
            {
                printf("Token: %s\n", token);

                // Iterate over each character in the token
                for (size_t i = 0; i < strlen(token); i++)
                {
                    if (isdigit(token[i]) && token[i + 2] == 'r' && token[i] - '0' > max_red && isspace(token[i + 1]))
                    {
                        // printf("Number: %c at index: %zu has colour: %c\n", token[i], i, token[i + 2]);
                        max_red = token[i] - '0';
                    }
                    else if (isdigit(token[i]) && token[i + 2] == 'b' && token[i] - '0' > max_blue && isspace(token[i + 1]))
                    {
                        // printf("Number: %c at index: %zu has colour: %c\n", token[i], i, token[i + 2]);
                        max_blue = token[i] - '0';
                    }
                    else if (isdigit(token[i]) && token[i + 2] == 'g' && token[i] - '0' > max_green && isspace(token[i + 1]))
                    {
                        // printf("Number: %c at index: %zu has colour: %c\n", token[i], i, token[i + 2]);
                        max_green = token[i] - '0';
                    }
                    else if (isdigit(token[i]) && token[i + 3] == 'g' && ((token[i] - '0') * 10) + (token[i + 1] - '0') > max_green && isdigit(token[i + 1]))
                    {
                        // printf("Number: %d at index: %zu has colour: %c\n", ((token[i] - '0') * 10) + (token[i + 1] - '0'), i, token[i + 2]);
                        max_green = ((token[i] - '0') * 10) + (token[i + 1] - '0');
                    }
                    else if (isdigit(token[i]) && token[i + 3] == 'b' && ((token[i] - '0') * 10) + (token[i + 1] - '0') > max_blue && isdigit(token[i + 1]))
                    {
                        // printf("Number: %d at index: %zu has colour: %c\n", ((token[i] - '0') * 10) + (token[i + 1] - '0'), i, token[i + 2]);
                        max_blue = ((token[i] - '0') * 10) + (token[i + 1] - '0');
                    }
                    else if (isdigit(token[i]) && token[i + 3] == 'r' && ((token[i] - '0') * 10) + (token[i + 1] - '0') > max_red && isdigit(token[i + 1]))
                    {
                        // printf("Number: %d at index: %zu has colour: %c\n", ((token[i] - '0') * 10) + (token[i + 1] - '0'), i, token[i + 2]);
                        max_red = ((token[i] - '0') * 10) + (token[i + 1] - '0');
                    }
                }

                // Get the next token
                token = strtok(NULL, ";");
            }

            printf("Max Red: %d\n", max_red);
            printf("Max Blue: %d\n", max_blue);
            printf("Max Green: %d\n", max_green);

            if (max_red <= 12 && max_blue <= 14 && max_green <= 13)
            {
                total += lineCount + 1;
            }

            total2 += max_red * max_blue * max_green;

            lineCount++;

            printf("%s\n", "---------");
        }
    }
    else
    {
        fprintf(stderr, "Could not open file %s for reading\n", filename);
        return 1; // Return an error code
    }
    printf("Part 1 Total: %d\n", total);
    printf("Part 2 Total: %d\n", total2);

    return 0;
}