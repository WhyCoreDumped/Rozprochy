#include <stdio.h>
#include <Windows.h>

int main() {
    char url[512];
    char commandLine[1024];

    while (1) {
        printf("Paste link to the file (ex. https://www.gutenberg.org/cache/epub/84/pg84.txt):\n> ");
        if (scanf("%511s", url) != 1) break;

        snprintf(commandLine, sizeof(commandLine), "child_process.exe %s", url);

        STARTUPINFO si;
        PROCESS_INFORMATION pi;
        ZeroMemory(&si, sizeof(si));
        si.cb = sizeof(si);
        ZeroMemory(&pi, sizeof(pi));

        if (!CreateProcess(NULL, commandLine, NULL, NULL, FALSE, 0, NULL, NULL, &si, &pi)) {
            printf("CreateProcess Error: %lu\n", GetLastError());
        } else {
            WaitForSingleObject(pi.hProcess, INFINITE);
            CloseHandle(pi.hProcess);
            CloseHandle(pi.hThread);
        }

        printf("\nDo you want to check the content of another file? Y/N");
        char answer;
        scanf(" %c", &answer);

        if (answer == 'n' || answer == 'N')
            break;
    }

    return 0;
}