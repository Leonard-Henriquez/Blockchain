from Blockchain import *


bc = Blockchain()
print(bc.last_block)
bc.transfer(1, 2, 5000)
bc.mine(1)
print(bc.last_block)
bc.transfer(1, 2, 1000)
bc.transfer(1, 2, 700)
bc.mine(1)
print(bc.last_block)
print (bc.check_balance(1))