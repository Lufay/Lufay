#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(int c, char **v) {
    while(--c > 1 && !fork());
    sleep(c = atoi(v[c]));
    printf("%d\n", c);
    wait(NULL);
}
