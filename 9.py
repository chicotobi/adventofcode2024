d = open('9').read().splitlines()[0]

forward_idx = 0
forward_id = 0
forward_length = int(d[forward_idx])

backward_idx = len(d)-1
backward_id = len(d)//2
backward_length = int(d[backward_idx])

global_idx = 0

within = 'forward'
counter = d[forward_idx]

checksum = 0
n_space = 0
while True:
  if within == 'forward':
    
    # Walk forward
    for i in range(forward_length):
      checksum += global_idx * forward_id
      print("add global_idx * forward_id:", global_idx, "*", forward_id)
      global_idx += 1
    forward_idx += 1
    
    # Get free space
    n_space += int(d[forward_idx])
    forward_idx += 1
    forward_id += 1
    
    # Get forward length
    forward_length = int(d[forward_idx])
    
    # Change to filling
    within = 'backward'
    
  # Check some kind of break condition?!
  if forward_id == backward_id:
    for i in range(backward_length):
      checksum += global_idx * forward_id
      print("add global_idx * forward_id:", global_idx, "*", forward_id)
      global_idx += 1
    break
  
  # Fill the free space from backwards
  if within == 'backward':
    # If there is more free space than we need
    if n_space > backward_length:
      for i in range(backward_length):
        checksum += global_idx * backward_id
        print("add global_idx * backward_id:", global_idx, "*", backward_id)
        global_idx += 1
        n_space -= 1
      backward_id -= 1
      backward_idx -= 2
      backward_length = int(d[backward_idx])
      print("backward_length",backward_length)
    elif n_space == backward_length:
      for i in range(n_space):
        checksum += global_idx * backward_id
        print("add global_idx * backward_id:", global_idx, "*", backward_id)
        global_idx += 1
        n_space -= 1
      backward_id -= 1
      backward_idx -= 2
      backward_length = int(d[backward_idx])
      print("backward_length",backward_length)
      within = 'forward'
    elif n_space < backward_length:
      for i in range(n_space):
        checksum += global_idx * backward_id
        print("add global_idx * backward_id:", global_idx, "*", backward_id)
        global_idx += 1
      backward_length -= n_space
      n_space = 0
      print("backward_length",backward_length)
      within = 'forward'
      
  # Check some kind of break condition?!
  if forward_id == backward_id:
    for i in range(backward_length):
      checksum += global_idx * forward_id
      print("add global_idx * forward_id:", global_idx, "*", forward_id)
      global_idx += 1
    break
  
print("checksum",checksum)
        
  
      