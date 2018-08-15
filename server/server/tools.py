import random

def random_string(num):
  candicate_chars = "0123456789abcdefghijklmnopqr" \
                    "stuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
  rtn_string = ''
  max_len = len(candicate_chars)
  for i in range(num):
    my_random = random.randint(0, max_len - 1)
    rtn_string += candicate_chars[my_random]
  return rtn_string
