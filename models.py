# from numpy import number
from ast import List
from pydantic import BaseModel, EmailStr

class AgentCreate(BaseModel):
    # agent_id :str Pk
    full_name: str
    mobile: str
    email: EmailStr
    address: str
    upi_id: str
    aadhaar: str
    commtype: str
    commval: float
    status: int
# Add Customer
class CustomerCreate(BaseModel):
    # customer_id : str pk
    full_name: str
    mobile: str
    email: EmailStr
    address: str
    # News_name: str
    # Del_date: str
    agent_id: str
    status : int

# Master Newspaper
class AddNewspaper(BaseModel):
    # newspaper_id: str pk
    news_name: str
    price: float
    status : int
    
# Subs for Customer
class SubscriptionCostumerwise(BaseModel):
    # subscription_id: str pk
    customer_id: str #fk
    newspaper_name: str #fk
    agent_id: str #fk
    start_date: str
    price_type: str
    price: float
    status:int
    
    # newspapers: List[SubscriptionItem]