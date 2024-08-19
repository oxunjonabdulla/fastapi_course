from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hash():
    @staticmethod
    def bcrypt(password: str) -> bool:
        hash_password = pwd_context.hash(password)
        return hash_password

    @staticmethod
    def verify(plain_password: str, hashed_password: str) -> bool:
        correct_password = pwd_context.verify(plain_password, hashed_password)
        return correct_password
