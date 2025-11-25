from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .operators_to_sources import OperatorsToSources
    from .appeal import Appeal


class Operator(Base):
    is_active: Mapped[bool]
    req_limit: Mapped[int] = mapped_column(default=10)

    appeals: Mapped[list["Appeal"]] = relationship(back_populates="operator")
    sources_association: Mapped[list["OperatorsToSources"]] = relationship(
        back_populates="operator",
    )
