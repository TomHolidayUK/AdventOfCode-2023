# because the galaxies and distance grow linearly we can exptrapolate:
# ((galaxy expansion factor - a previous galaxy expansion factor) * number of intersections between pairs) + value with a previous galaxy expansion factor
# (999999 * n) + 9521550
# or
# (999999 * 298924) + 9222626

# need to find sum of all the number of expansion rows and columns between each pair

# boundary_total = distance_total with galaxies doubled (9521550) - distance_total with normal galaxies doubled (9222626)
# boundary_total = 298924
# therefore answer =
print((999998 * 298924) + 9521550)
# or
print((999999 * 298924) + 9222626)




