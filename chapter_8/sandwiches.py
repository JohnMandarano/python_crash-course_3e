def make_sandwich(*args):
    print("\nI am making your sandwich with the following ingredients:")
    for arg in args:
        print(f" - {arg}")

make_sandwich('peanut butter', 'jelly')
make_sandwich('egg salad')
make_sandwich('ham', 'cheese', 'mustard', 'codfish roe')