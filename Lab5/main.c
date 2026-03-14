#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/wait.h>

int main(void) {
    int fd[2];

    pipe(fd);

    pid_t pid = fork();

    if (pid > 0) {
        close(fd[0]);

        printf("Type the message to search for in the current directory: ");
        char message[256];
        fgets(message, sizeof(message), stdin);
        message[strcspn(message, "\n")] = 0;

        write(fd[1], message, strlen(message) + 1);

        close(fd[1]);
        wait(NULL);

        printf("Search finished\n");
    }
    else {
        close(fd[1]);

        char content[256];
        read(fd[0], content, sizeof(content));
        close(fd[0]);

        char command[512];
        sprintf(command, "grep -ls '%s' *", content);

        execlp("sh", "sh", "-c", command, NULL);

        exit(1);
    }
}
