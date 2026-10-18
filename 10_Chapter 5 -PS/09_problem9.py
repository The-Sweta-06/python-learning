# Q9. Can you change the values inside a list which is contained in set S?


s = {8, 7, 12, "Sweta", [1,2]}

# No, you cannot change the values inside a list contained in a set in python,
# In fact, you cannot even have a list as an element in a set because sets in python require all their elements to be immutable and hashable.
# Lists are mutable and not hashable, so they cannot be added to a set.