from passlib.context import CryptContext

pwd_context=CryptContext(schemes=["argon2"],deprecated="auto")

#function to hash password
def hash_password(password:str)->str:
    return pwd_context.hash(password)

#function to verify password
def verify_password(plain_password:str,hashed_password:str)->bool:
    return pwd_context.verify(plain_password,hashed_password)


