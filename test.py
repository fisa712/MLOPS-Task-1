import numpy as np
from wallet import Wallet

def test_getAmount():
  asif = Wallet()
  asif.setAmount(1000)
  assert asif.getAmount()==np.array(1000)
