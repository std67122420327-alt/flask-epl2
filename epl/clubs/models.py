from epl import db
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship , Mapped , mapped_column
from typing import List

class Club(db.Model):
    __tablename__ = 'club'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False , unique=True)
    stadium: Mapped[str] = mapped_column(String(100), nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    logo: Mapped[str] = mapped_column(String(256), nullable=False)

    players: Mapped[List['Player']] = relationship(back_populates="club")

    def __repr__(self) -> str:
        return f"Clubs({self.name})"

    
class Player(db.Model):
    __tablename__ = 'player'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False , unique=True)
    position: Mapped[str] = mapped_column(String(20), nullable=False)
    nationality: Mapped[str] = mapped_column(String(25), nullable=False)
    goal: Mapped[int] = mapped_column(Integer, nullable=True, default=0)
    squad_no: Mapped[int] = mapped_column(Integer, nullable=True)
    img: Mapped[str] = mapped_column(String(256), nullable=False)
    clean_sheet: Mapped[int] = mapped_column(Integer, nullable=True, default=0)
    club_id: Mapped[int] = mapped_column(Integer, ForeignKey('club.id'))

    club: Mapped['Club'] = relationship(back_populates='players')
    def __repr__(self):
        return f"<Players {self.name}>"


