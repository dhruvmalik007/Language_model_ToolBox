## this package follows the same endpoints  as lcm reference implementation, but with added functions
## to adopt the datasets across the format, also allowing parallelization in data loading and better shuffling mechniamss 

import logging
import tinygrad as nn
from typing import TypeVar

BatchT_co = TypeVar("BatchT_co",bound=[Dict, any] covariant=True)



class DataLoader(ABC, )