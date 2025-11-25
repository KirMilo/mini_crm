from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .operators_to_sources import OperatorsToSources
    from .appeal import Appeal


class Source(Base):
    name: Mapped[str] = mapped_column(unique=True)

    appeals: Mapped[list["Appeal"]] = relationship(back_populates="source")
    operators_association: Mapped[list["OperatorsToSources"]] = relationship(
        back_populates="source",
    )
