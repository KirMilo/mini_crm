from datetime import datetime, timezone
from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .lead import Lead
    from .source import Source
    from .operator import Operator


class Appeal(Base):
    lead_id: Mapped[int] = mapped_column(ForeignKey('leads.id'))
    source_id: Mapped[int] = mapped_column(ForeignKey('sources.id'))
    operator_id: Mapped[int] = mapped_column(ForeignKey('operators.id'))
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc)
    )

    lead: Mapped["Lead"] = relationship(back_populates="appeals")
    source: Mapped["Source"] = relationship(back_populates="appeals")
    operator: Mapped["Operator"] = relationship(back_populates="appeals")
