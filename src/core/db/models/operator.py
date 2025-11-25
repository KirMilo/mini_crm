from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .source import Source


class Operator(Base):
    is_active: Mapped[bool]
    req_limit: Mapped[int] = mapped_column(default=10)

    sources: Mapped[list[Mapped["Source"]]] = relationship(
        secondary="operators_to_sources",
        back_populates="operators",
    )
