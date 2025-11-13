#include <stdio.h>

void tower_of_hanoi(int n, char source, char auxiliary, char target) {
    if (n == 1) {
        printf("Move disk 1 from rod %c to rod %c\n", source, target);
        return;
    }

    // Move n-1 disks from source to auxiliary
    tower_of_hanoi(n - 1, source, target, auxiliary);

    // Move nth disk from source to target
    printf("Move disk %d from rod %c to rod %c\n", n, source, target);

    // Move n-1 disks from auxiliary to target
    tower_of_hanoi(n - 1, auxiliary, source, target);
}

int main() {
    int n = 10; // Number of disks
    tower_of_hanoi(n, 'A', 'B', 'C');
    return 0;
}