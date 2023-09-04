from collections import defaultdict

def min_window(s, t):
    # Initialize dictionaries to store character frequencies
    target_freq = defaultdict(int)
    window_freq = defaultdict(int)

    # Count the frequencies of characters in t
    for char in t:
        target_freq[char] += 1

    # Initialize variables to track the minimum window
    min_window_size = 0
    min_window_start = 0
    min_window_end = 0

    # Initialize variables to track the current window
    window_start = 0
    window_end = 0
    chars_matched = 0

    # Iterate over the string s using the sliding window technique
    while window_end < len(s):
        # Expand the window by including the next character
        if s[window_end] in target_freq:
            window_freq[s[window_end]] += 1
            if window_freq[s[window_end]] == target_freq[s[window_end]]:
                chars_matched += 1

        # Shrink the window if all characters in t are matched
        while chars_matched == len(target_freq):
            # Update the minimum window if a smaller window is found
            if window_end - window_start + 1 < min_window_size:
                min_window_size = window_end - window_start + 1
                min_window_start = window_start
                min_window_end = window_end

            # Shrink the window by removing the leftmost character
            if s[window_start] in target_freq:
                window_freq[s[window_start]] -= 1
                if window_freq[s[window_start]] < target_freq[s[window_start]]:
                    chars_matched -= 1
            window_start += 1

        window_end += 1

    # Return the minimum window substring or an empty string if not found
    if min_window_size != float('inf'):
        return s[min_window_start:min_window_end + 1]
    else:
        return ""

print(min_window("ADOBECODEBANC", "ABC"))
        