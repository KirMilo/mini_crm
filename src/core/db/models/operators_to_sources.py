from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .operator import Operator
    from .source import Source


class OperatorsToSources(Base):
    __tablename__ = "operators_to_sources"

    operator_id: Mapped[int] = mapped_column(ForeignKey("operators.id"))
    source_id: Mapped[int] = mapped_column(ForeignKey("sources.id"))
    weight: Mapped[int]

    operator: Mapped["Operator"] = relationship(back_populates="sources")
    source: Mapped["Source"] = relationship(back_populates="operators")
