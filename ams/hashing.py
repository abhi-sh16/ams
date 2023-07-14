from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=['bcrypt'],deprecated='auto')


class Hash:
    @staticmethod
    def bcrypt(passw: str):
        return pwd_cxt.hash(passw)


    @staticmethod
    def verify(hashed_pass:str,plain_pass:str):
        return pwd_cxt.verify(plain_pass,hashed_pass)
