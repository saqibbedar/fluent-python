struct Context {
    int multiplier;
};

int multiply(struct Context *ctx, int x)
{
    return ctx->multiplier * x;
}