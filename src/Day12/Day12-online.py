def read_input(file_name): # read data
  with open(file_name, 'r') as f:
    ret = f.readlines()
  return ret


def parse_line(line): # parse a line of data into config and numbers (split numbers and turn to integers)
  config, numbers = line.split()
  return config, [int(g) for g in numbers.split(',')]


def get_clusters(config): # split into smaller clusters
  return [s for s in config.split('.') if s]


def count_placements(numbers, clusters, cache={}): #  recursive function that calculates the number of valid placements of numbers within clusters, subject to certain constraints. The function uses memoization (caching) to store and reuse previously computed results to optimize performance.
  key = "|".join(map(str, numbers))
  key += "#" + ":".join(clusters)
  if key in cache:
    return cache[key]

  if not numbers:
    for cluster in clusters:
      if "#" in cluster:
        return 0
    return 1
  if not clusters:
    return 0
  ret = 0
  group = numbers[0]
  cluster = clusters[0]
  len_cluster = len(cluster)
  if group > len_cluster and "#" in cluster:
    return 0
  for i in range(len_cluster - group + 1):
    left = cluster[:i]
    if "#" in left:
      continue
    right = cluster[i + group:]
    if right.startswith("#"):
      continue
    new_clusters = clusters[1:]
    if len(right) > 1:
      new_clusters.insert(0, right[1:])
    ret += count_placements(numbers[1:], new_clusters, cache)

  if "#" not in cluster:
    ret += count_placements(numbers, clusters[1:], cache)

  cache[key] = ret

  return ret


def calculate_total(filename, expand):
  total = 0
  for line in read_input(filename):
    config, numbers = parse_line(line)
    if expand: # for part 2 unfold the data
      config = "?".join(5 * [config])
      numbers = 5 * numbers
    clusters = get_clusters(config)
    print(clusters)
    delta = count_placements(numbers, clusters)
    total += delta
  return total


def part1():
  print(calculate_total('./src/Day12/Data12-test.txt', False))

# def part2():
#   print(calculate_total('./src/Day12/Data12-test.txt', True))


if __name__ == '__main__': # check whether the script is being run as the main program
  part1()
#   part2()