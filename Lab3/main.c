#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int main() {
    char url[512];

    while (1) {
        printf("Paste link to the file (ex. https://www.gutenberg.org/cache/epub/84/pg84.txt):\n> ");

        scanf("%s", url);

        pid_t pid = fork();

        if (pid < 0) {
            return 1;
        }
        if (pid == 0) {
            execlp("curl", "curl", "-s", url, NULL);

            exit(1);
        }
        else {
            int status;

            wait(&status);

            int finishCode = WEXITSTATUS(status);
            if (finishCode != 0)
                printf("There was an unexpected error!");
        }

        printf("Do you want to check the content of another file? Y/N ");
        char answer;
        scanf(" %c%*[^\n]", &answer);

        while (answer != 'y' && answer != 'Y' && answer != 'n' && answer != 'N')
            scanf(" %c%*[^\n]", &answer);

        if (answer == 'n' || answer == 'N')
            break;
    }
    return 0;
}