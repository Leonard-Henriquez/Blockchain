from Blockchain import *


bc = Blockchain()
print(bc.last_block)
bc.mine(1)
bc.transfer(1, 2, 150)
bc.transfer(2, 1, 150)
bc.mine(1)
bc.transfer(1, 2, 700)
bc.mine(1)
bc.mine(1)
bc.mine(1)
bc.mine(1)