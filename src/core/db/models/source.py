from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .operator import Operator


class Source(Base):
    name: Mapped[str] = mapped_column(unique=True)

    operators: Mapped[list["Operator"]] = relationship(
        secondary="operators_to_sources",
        back_populates="sources",
    )
