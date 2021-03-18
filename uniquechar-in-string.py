def has_unique_chars(string):
  return len(set(string)) == len(string)

print(has_unique_chars("abcdef"))
print(has_unique_chars("  nAa"))