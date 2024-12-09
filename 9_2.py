d = open('9').read().splitlines()[0]

# Build the "string"
s = []
cur_id = 0
i = 0
id_range = []
while i < len(d):
  idx0 = len(s)
  for j in range(int(d[i])):
    s.append(cur_id)
  idx1 = len(s)
  id_range.append([idx0, idx1])
  cur_id += 1
  i += 1
  if i == len(d):
    break
  for j in range(int(d[i])):
    s.append(-1)
  i += 1
  
# Create a marked
s2 = ''.join('.' if i == -1 else 'X' for i in s )

# Fill backwards
import tqdm
for cur_id in tqdm.tqdm(list(reversed(range(cur_id)))):
  cur_id_range = id_range[cur_id]
  cur_len = cur_id_range[1] - cur_id_range[0]
  
  s2 = ''.join('.' if i == -1 else 'X' for i in s )

  # Find space
  idx0 = s2.find('.' * cur_len)
  if idx0 != -1 and idx0 < cur_id_range[0]:
    #print('move',cur_id)
    for i in range(cur_len):
      s[idx0 + i] = cur_id
      s[cur_id_range[0] + i] = -1
    s2 = ''.join('.' if i == -1 else 'X' for i in s )
    #print('new string is',s2)
      
  cur_id -= 1
  
# Calc checksum
print(sum(i*v for i, v in enumerate(s) if v != -1))