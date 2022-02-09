from types import MappingProxyType
from typing import Iterator, Mapping, NamedTuple, Optional, Type
import astroid


# https://docs.python.org/3/library/warnings.html
CODES: Mapping[Type[Warning], int] = MappingProxyType({
    Warning: 1,
    UserWarning: 2,
    DeprecationWarning: 3,
    SyntaxWarning: 4,
    RuntimeWarning: 5,
    FutureWarning: 6,
    PendingDeprecationWarning: 7,
    ImportWarning: 8,
    UnicodeWarning: 9,
    BytesWarning: 10,
    ResourceWarning: 11,
})


class WarningInfo(NamedTuple):
    message: str
    category: Type[Warning]
    argument: Optional[str] = None

    @property
    def code(self) -> int:
        return CODES.get(self.category, 1)

    def __str__(self) -> str:
        return f'{self.category.__name__}: {self.message}'


class Extractor:
    def extract(self, node: astroid.NodeNG) -> Iterator[WarningInfo]:
        raise NotImplementedError
