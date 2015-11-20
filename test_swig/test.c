int fact(int n) {
    if (n < 0)
        return 0;
    int res = 1;
    while (n > 1)
        res *= n--;
    return res;
}
