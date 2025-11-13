#include <stdio.h>
#define MAX 100

typedef struct {
    int items[MAX];
    int top;
} Stack;
void init(Stack *s) {
    s->top = -1;
}
int is_empty(Stack *s) {
    return s->top == -1;
}

// Push an element onto the stack
void push(Stack *s, int item) {
    if (s->top == MAX - 1) {
        printf("Stack overflow\n");
        return;
    }
    s->items[++(s->top)] = item;
}

// Pop an element from the stack
int pop(Stack *s) {
    if (is_empty(s)) {
        printf("Stack underflow\n");
        return -1; // Return -1 to indicate error in this example
    }
    return s->items[(s->top)--];
}

// Peek the top element without removing it
int peek(Stack *s) {
    if (is_empty(s)) {
        printf("Stack is empty\n");
        return -1; // Return -1 to indicate empty stack
    }
    return s->items[s->top];
}

int main() {
    Stack stack;
    init(&stack);

    push(&stack,10);
    push(&stack,20);
    push(&stack,30);

    printf("Top element (peek): %d\n", peek(&stack));
    printf("popped element: %d\n",pop(&stack));
    printf("Top element after peek (peek): %d\n", peek(&stack));



    if (is_empty(&stack)) {
        printf("Stack is empty\n");
    } else {
        printf("Stack is not empty\n");
    }

    return 0;
}
            