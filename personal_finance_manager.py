import json 
from datetime import datetime

class Transaction:
    def __init__(self,tid,category,amount,description,date=None):
        self.tid = tid
        self.category = category
        self.amount = amount
        self.description = description
        self.date = date or datetime.now().strftime("%Y-%m-%d")
        
    def __str__(self):
        return f"[{self.date}] {self.category} | {self.description} | {self.amount}"


    def __repr__(self):
        return f"Transaction ({self.tid} , {self.category},{self.amount})"


    def to_dict(self):
        return{
            "tid": self.tid,
            "category": self.category,
            "amount": self.amount,
            "description": self.description,
            "date": self.date            
        }

    @classmethod 
    def from_dict(cls,data):
        return cls(
            data["tid"],
            data["category"],
            data["amount"],
            data["description"],
            data["date"]
        )


class Budget:
    def __init__(self,category,limit):
        self.category = category 
        self.limit = limit
        self.spent = 0

    @property
    def remaining(self):
        return self.limit - self.spent

    @property
    def is_exceeded(self):
        return  self.spent > self.limit

    def __str__(self):
        status = "EXCEEDED" if self.is_exceeded else "OK"
        return f"{self.category}: {self.spent}/{self.limit} [{status}]" 


class ExpenseManager:
    def __init__(self, filename="data.json"):
        self.filename = filename
        self.transactions = []
        self.categories = set()
        self._next_id = 1

        self._load()     
        self.budgets = {}   

    def _load(self):
        try :
            with open(self.filename,"r") as f :
                data = json.load(f)
                self.transactions = [
                    Transaction.from_dict(t)
                    for t in data.get("transactions",[])
                ]
                self._next_id = data.get ("next_id" , 1)
                for t in self.transactions:
                    self.categories.add(t.category)
        except FileNotFoundError :
            pass
        except json.JSONDecodeError :
            print("warning: corrupted file ")

    def _save(self) :
        try:
            with open(self.filename,"w") as f :
                json.dump({
                    "transactions" : [t.to_dict() for t in self.transactions],
                    "next_id": self._next_id
                },f,indent=2)
        except Exception as e :
            print(f"save failed: {e}")

    def add_transaction(self, category, amount, description):
        t = Transaction(
        tid=self._next_id,
        category=category,
        amount=amount,
        description=description
    )

        self.transactions.append(t)
        self.categories.add(category)

        self._next_id += 1
        self._save()

   
    def total_by_category(self, category):
        return sum(t.amount for t in self.transactions if t.category == category)



manager = ExpenseManager()

manager.add_transaction("food", 200, "Lunch")
manager.add_transaction("travel", 500, "Auto")

print(manager.total_by_category("food"))

for t in manager.transactions:
    print(t)

print("Food total:", manager.total_by_category("food"))




