def count_unique_treasures(treasures):
    unique_treasures_count = 0
    treasures_chest = {}

    # Write ur code here
    for treasure in treasures:
      if treasure not in treasures_chest:
        treasures_chest[treasure] = True
        unique_treasures_count += 1

    return unique_treasures_count

print(count_unique_treasures([1, 2, 3, 3, 4, 4, 5]))  # ?
print(count_unique_treasures([3, 3, 3, 3, 3]))        # ?
print(count_unique_treasures([1, 2, 3, 4, 5]))        # ?