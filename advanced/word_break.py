def word_break(s, word_dict):
    n = len(s)
    """
    - The dp array is used to track whether a valid word break can 
    be achieved for each substring of the input string
    -Setting all elements to False ensures that we start with
    a clean state where no valid word breaks are assumed. 
    - As we process the substrings and find valid word breaks,
    we will update the corresponding dp elements to True.
    - Initializing the dp array to False is a common practice in 
    dynamic programming solutions to ensure a consistent 
    starting point for the algorithm. It provides a clear base state 
    from which we can build the solution iteratively.
    """
    dp = [False] * (n + 1)

    """
    dp[i] represents whether a valid word break can
    be achieved for the substring s[:i].
    Set dp[0] to True since an empty string can 
    be considered a valid word break.
    """
    dp[0] = True

    """
    Iterate from i = 1 to n, representing the current substring.
    For each i, iterate from j = 0 to i, representing the split 
    position of the substring s[:i].
    """
    for i in range(1, n + 1):
        for j in range(i):
            """
            If dp[j] is True (indicating a valid word break for the substring s[:j])
            and the substring s[j:i] is present in the word dictionary,
            set dp[i] to True and break out of the inner loop.
            """
            if dp[j] and s[j:i] in word_dict:
                dp[i] = True
                break
    """
    After the iterations, return dp[n], which represents whether a 
    valid word break can be achieved for the entire string s.
    """
    return dp[n]


word_dict = {"apple", "pen", "applepen", "pine", "pineapple"}

s1 = "applepenpineapple"
print(word_break(s1, word_dict))  # Output: True,
# string can be broken into valid words
# it is possible to segment the string into words from the given dict.

s2 = "pineapplepenapple"
print(word_break(s2, word_dict))  # Output: True

s3 = "catsandog"
print(word_break(s3, word_dict))  # Output: False
