import enum
from src.database import Base
 
 
class TransactionType(str, enum.Enum):
    DEPOSIT = "deposito"
    WITHDRAWAL = "saque"
 
 
class User(Base):
    __tablename__ = "users"
 
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
 
    accounts = relationship("Account", back_populates="owner")
 
 

 
class Transaction(Base):
    __tablename__ = "transactions"
 
    id = Column(Integer, primary_key=True, index=True)
    account_id = Column(Integer, ForeignKey("accounts.id"), nullable=False)
    type = Column(Enum(TransactionType), nullable=False)
    amount = Column(Float, nullable=False)
    description = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
 
    account = relationship("Account", back_populates="transactions")
