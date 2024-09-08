from pydantic import BaseModel,EmailStr,field_validator
from dataclasses import dataclass

class User(BaseModel):
    name:str
    email:EmailStr
    account_id:int

@dataclass
class Fuser:
    name:str
    email:str
    account_id:int

@field_validator("account_id")
def validator_account_id(cls,value):
    if value<=0:
        raise ValueError(f"account_id must be positive: {value}")
    return value

# user= User(name="Jack",email="jack",account_id=1234) # The email will throw an error
user= User(name="Jack",email="jack@pixegami.io",account_id=1234)
# fuser = Fuser(name:"Rome",email:"rome@john.com",account_id=222)
user_json_str = user.model_dump_json()
user_dict_str = user.model_dump()
# user_dict_data =asdict(fuser)
print(user)
print(user.email)
print(user.account_id)
print(user_json_str)