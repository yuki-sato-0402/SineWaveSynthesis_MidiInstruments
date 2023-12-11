import re, itertools

def pickup(v_or_p, i_sine, i_vel, i_line):
  path = f'S{i_sine}/S{i_sine}{v_or_p}{i_vel}.txt'
  with open(path, mode='r') as f: lines = f.readlines()
  return re.findall(r'(.+),\s(.+;)$', lines[i_line])[0][1]

p = itertools.product(('V', 'P'), range(1, 15 + 1), range(0, 8 + 1))
for v_or_p, i_sine, i_line in p:
  path = f'S{i_sine}/ordered/S{i_sine}{v_or_p}i{i_line}.txt'
  lines = [pickup(v_or_p, i_sine, i, i_line) for i in range(1, 9 + 1)]
  with open(path, mode='w') as f: f.writelines('\n'.join(lines))
  print(path, lines)