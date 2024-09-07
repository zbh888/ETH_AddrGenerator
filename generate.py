from eth_account import Account
import time
import sys

start_t = time.time()
now = time.time()
while (now - start_t < int(sys.argv[1])):
# 生成一个随机私钥
    private_key = Account.create().key.hex()

# 从私钥生成以太坊地址
    account = Account.from_key(private_key)
    address = account.address
    now = time.time()
    print(f"{address},{private_key}")
