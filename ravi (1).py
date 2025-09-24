def wordBreak(s: str, wordDict: list[str]) -> bool:
    word_set = set(wordDict)  # For O(1) lookup
    dp = [False] * (len(s) + 1)
    dp[0] = True  # Base case

    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break  # No need to check further once dp[i] is True

    return dp[len(s)]