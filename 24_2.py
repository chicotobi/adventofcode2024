d = open('24').read().splitlines()

idx = [i for i,x in enumerate(d) if x == ''][0]
 
rules = [i.split(" -> ") for i in d[idx+1:]]
rules = [i.split(" ")+ [j] for i,j in rules]

#Apply swaps
keys = [out for in1, op, in2, out in rules]
swaps = {k:k for k in keys}
swaps["kmb"] = "z10"
swaps["z10"] = "kmb"
swaps["tvp"] = "z15"
swaps["z15"] = "tvp"
swaps["dpg"] = "z25"
swaps["z25"] = "dpg"
swaps["vdk"] = "mmf"
swaps["mmf"] = "vdk"
rules = [(in1, op, in2, swaps[out]) for in1, op, in2, out in rules]

# Solution is therefore dpg,kmb,mmf,tvp,vdk,z10,z15,z25

rename_dct = {}

def ren(x):
  if x in rename_dct.keys():
    return rename_dct[x]
  else:
    return x

tidy_rules = []

def check(i, in1, check_in1, op, check_op, in2, check_in2, new_out_name):
  if in1 == check_in1 and op == check_op and in2 == check_in2:
    if in1[-2:] != in2[-2:]:
      raise
    if out != new_out_name:
      rename_dct[out] = new_out_name
    if (in1, op, in2, new_out_name) not in tidy_rules:
      new_rule = (in1, op, in2, new_out_name)
      print(new_rule)
      tidy_rules.append(new_rule)
      rules[i] = new_rule
  if in2 == check_in1 and op == check_op and in1 == check_in2:
    if in1[-2:] != in2[-2:]:
      raise
    if out != new_out_name:
      rename_dct[out] = new_out_name
    if (in2, op, in1, new_out_name) not in tidy_rules:
      new_rule = (in2, op, in1, new_out_name)
      print(new_rule)
      tidy_rules.append(new_rule)
      rules[i] = new_rule

# Just ... reverse engineer the adder logic
global_idx = 0
A    = f"x{global_idx:02}"
B    = f"y{global_idx:02}"
xor1 = xor2 = 'xor2_00' 
and1 = or1 = 'or1_01'

while True:  
  for i, (in1, op, in2, out) in enumerate(rules):
    in1 = ren(in1)
    in2 = ren(in2)
    out = ren(out)
    rules[i] = (in1, op, in2, out)
  
    check(i, in1, A, op, 'XOR', in2, B, xor1)
    check(i, in1, A, op, 'AND', in2, B, and1)
    if global_idx > 0:
      check(i, in1, xor1, op, 'XOR', in2, or1_old, xor2)
      check(i, in1, xor1, op, 'AND', in2, or1_old, and2)
      check(i, in1, and2, op, 'OR', in2, and1, or1)
    # Check if the adder is fully computed for location at global_idx
    if xor2 in rename_dct.values() and or1 in rename_dct.values():
      global_idx += 1
      print("increase global_idx to",global_idx)
          
      A    = f"x{global_idx:02}"
      B    = f"y{global_idx:02}"
      xor1 = f"xor1_{global_idx:02}"
      and1 = f"and1_{global_idx:02}"
      or1_old = f"or1_{global_idx:02}"
      xor2 = f"xor2_{global_idx:02}"
      and2 = f"and2_{global_idx:02}"
      or1 = f"or1_{global_idx+1:02}"