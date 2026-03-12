#include <stdio.h>
#include <Windows.h>
#include <wininet.h>

int main(int argc, char *argv[]) {
    if (argc < 2) {
        return 1;
    }

    char *url = argv[1];
    HINTERNET hInternet, hConnect;
    char buffer[1024];
    DWORD bytesRead;

    hInternet = InternetOpen("MinimalCurl", INTERNET_OPEN_TYPE_DIRECT, NULL, NULL, 0);
    if (!hInternet) return 1;

    hConnect = InternetOpenUrl(hInternet, url, NULL, 0, INTERNET_FLAG_RELOAD, 0);
    if (!hConnect) {
        InternetCloseHandle(hInternet);
        return 1;
    }

    while (InternetReadFile(hConnect, buffer, sizeof(buffer) - 1, &bytesRead) && bytesRead > 0) {
        buffer[bytesRead] = '\0';
        printf("%s", buffer);
    }

    InternetCloseHandle(hConnect);
    InternetCloseHandle(hInternet);

    return 0;
}