from hashlib import md5
from itertools import count


# Part 1

def get_min_md5_hash_with_n_zero_prefix(secret_key: str, n: int) -> str:
    for i in count(1):
        if md5((secret_key + str(i)).encode()).hexdigest()[:n] == "0"*n:
            return i

assert get_min_md5_hash_with_n_zero_prefix("abcdef", n=5) == 609043
assert get_min_md5_hash_with_n_zero_prefix("pqrstuv", n=5) == 1048970
print(get_min_md5_hash_with_n_zero_prefix("ckczppom", n=5))
print(get_min_md5_hash_with_n_zero_prefix("ckczppom", n=6))
