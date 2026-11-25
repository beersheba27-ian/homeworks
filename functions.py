from typing import Callable, Sequence

def my_sorted[T, K](items: Sequence[T],/,*, key:Callable[[T], T|K]|None=None) -> list[T]:
    """
    returns sorted by key list
    implementation according the following algorithm:
    1. Creating list of already sorted by key parts from "items"
      (no additional sorting is required)
    2. Merge of all parts from the created above list  
     
    """

         