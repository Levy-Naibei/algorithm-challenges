def string_permutaions(s):
  permutations = []
  if len(s) == 0:
      return []
  if len(s) == 1:
      return [s]

  for i in range(len(s)):
    current_char = s[i]
    """remaining chars obtained by slicing the string 
      before and after the current character """
    rem_chars = s[:i] + s[i + 1 :]

    """The function string_permutations is recursively called 
    with the remaining_chars to generate all permutations 
    of the remaining characters."""
    for perm in string_permutaions(rem_chars):
      """
      Each permutation of the remaining characters is
      concatenated with the current_char to form a new permutation,
      which is then added to the permutations list.
      """
      permutations.append(current_char + perm)
  return permutations


print(string_permutaions("abc"))
