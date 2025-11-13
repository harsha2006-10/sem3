int precedence(char op) {
    if (op == '^') return 3;
    if (op == '*' || op == '/') return 2;
    if (op == '+' || op == '-') return 1;
    return 0;
}stack;
void infixToPostfix(char* infix, char* postfix) {
    Stack s; init(&s);
    int i = 0, j = 0;
    char c;

    while ((c = infix[i++]) != '\0') {
        if (isalnum(c)) {
            postfix[j++] = c;
        } else if (c == '(') {
            push(&s, c);
        } else if (c == ')') {
            while (!is_empty(&s) && peek(&s) != '(')
                postfix[j++] = pop(&s);
            pop(&s); // Remove '('
        } else {
            while (!is_empty(&s) && precedence(peek(&s)) >= precedence(c))
                postfix[j++] = pop(&s);
            push(&s, c);
        }
    }
    while (!is_empty(&s))
        postfix[j++] = pop(&s);
    postfix[j] = '\0';
}
