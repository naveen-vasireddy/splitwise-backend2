from pydantic import BaseModel
from typing import List

class ExpenseUser(BaseModel):
    userId: str
    amountPaid: float
    amountOwed: float

class Expense(BaseModel):
    expenseId: str
    groupId: str
    description: str
    totalAmount: float
    users: List[ExpenseUser]