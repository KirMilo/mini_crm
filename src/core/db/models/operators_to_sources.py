from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, UniqueConstraint
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

    __table_args__ = (
        UniqueConstraint("operator_id", "source_id", name="uq_operator_source"),
    )

    operator: Mapped["Operator"] = relationship(back_populates="sources_association")
    source: Mapped["Source"] = relationship(back_populates="operators_association")

