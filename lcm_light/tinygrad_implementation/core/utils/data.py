import tinygrad as nn
from typing import (runtime_checkable, Protocol, Sized)
from abc import abstractmethod


class Batched(Sized, Protocol):
    """ abstract base class for describing the characterstics of the batch data
    """
    @abstractmethod
    def __getitem__(self, idx: int) -> Any: ...
    ## TODO: add also the datatypes of the standardised sets (i.e huggingface, data file formats etc )