from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Deck
from app.schemas import DeckCreate, DeckRead

router = APIRouter(prefix="/decks", tags=["decks"])


@router.post("", response_model=DeckRead, status_code=status.HTTP_201_CREATED)
def create_deck(data: DeckCreate, db: Session = Depends(get_db)):
    deck = Deck(title=data.title)
    db.add(deck)
    db.commit()
    db.refresh(deck)
    return deck


@router.get("", response_model=list[DeckRead])
def list_decks(db: Session = Depends(get_db)):
    return db.scalars(select(Deck).order_by(Deck.id)).all()


@router.get("/{deck_id}", response_model=DeckRead)
def get_deck(deck_id: int, db: Session = Depends(get_db)):
    deck = db.get(Deck, deck_id)
    if deck is None:
        raise HTTPException(status_code=404, detail="Deck not found")
    return deck


@router.delete("/{deck_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_deck(deck_id: int, db: Session = Depends(get_db)):
    deck = db.get(Deck, deck_id)
    if deck is None:
        raise HTTPException(status_code=404, detail="Deck not found")
    db.delete(deck)
    db.commit()