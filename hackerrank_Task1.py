# Hackerrank.Task1.ATABEK
# Complete the twoStrings function below.
def twoStrings(s1, s2):
    if set(s1) & set(s2):
        return 'YES'
    else:
        return 'NO'