import uuid
from datetime import datetime

from sqlalchemy import (
    Integer,
    String,
    DateTime,
    Boolean
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from sqlalchemy.dialects.postgresql import UUID

from ..base import Base


class EventCalendar(Base):
    __tablename__ = 'event_calendar'

    record_id: Mapped[uuid.UUID] = (
        mapped_column(UUID(as_uuid=True),
                      primary_key=True,
                      default=uuid.uuid7()
                      )
        )
    schedule_year: Mapped[int] = mapped_column(Integer, nullable=False)
    round_number: Mapped[int] = mapped_column(Integer, nullable=False)
    round_country: Mapped[str] = mapped_column(String, nullable=True)
    round_location: Mapped[str] = mapped_column(String, nullable=True)
    round_offical_name: Mapped[str] = mapped_column(String, nullable=True)
    round_event_date: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    round_event_name: Mapped[str] = mapped_column(String, nullable=True)
    round_event_fmt: Mapped[str] = mapped_column(String, nullable=True)
    round_type_session_1: Mapped[str] = mapped_column(String, nullable=True)
    round_date_session_1: Mapped[DateTime] = mapped_column(DateTime(timezone=True), nullable=True)
    round_date_utc_session_1: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    round_type_session_2: Mapped[str] = mapped_column(String, nullable=True)
    round_date_session_2: Mapped[DateTime] = mapped_column(DateTime(timezone=True), nullable=True)
    round_date_utc_session_2: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    round_type_session_3: Mapped[str] = mapped_column(String, nullable=True)
    round_date_session_3: Mapped[DateTime] = mapped_column(DateTime(timezone=True), nullable=True)
    round_date_utc_session_3: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    round_type_session_4: Mapped[str] = mapped_column(String, nullable=True)
    round_date_session_4: Mapped[DateTime] = mapped_column(DateTime(timezone=True), nullable=True)
    round_date_utc_session_4: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    round_type_session_5: Mapped[str] = mapped_column(String, nullable=True)
    round_date_session_5: Mapped[DateTime] = mapped_column(DateTime(timezone=True), nullable=True)
    round_date_utc_session_5: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    fone_api_support: Mapped[bool] = mapped_column(Boolean, nullable=False)


if __name__ == '__main__':
    raise SystemExit()
