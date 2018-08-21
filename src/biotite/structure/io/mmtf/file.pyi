# This source code is part of the Biotite package and is distributed
# under the 3-Clause BSD License. Please see 'LICENSE.rst' for further
# information.

from typing import Union, BinaryIO, Optional, Any, Iterator
import numpy as np
from ....file import File


class MMTFFile(File[BinaryIO]):
    def __init__(self) -> None: ...
    def read(self, file: Union[str, BinaryIO]) -> None: ...
    def write(self, file: Union[str, BinaryIO]) -> None: ...
    def get_codec(self, key: str) -> Optional[int]: ...
    def get_length(self, key: str) -> Optional[int]: ...
    def get_param(self, key: str) -> Optional[int]: ...
    def __getitem__(self, key: str) -> Any: ...
    def __setitem__(self, key: str, item: Any) -> None: ...
    def __delitem__(self, key: str) -> None: ...
    def set_array(
        self, key: str, array: np.ndarray, codec: int, param: int = 0
    ) -> None: ...
    def __iter__(self) -> Iterator[Any]: ...
    def __len__(self) -> int: ...