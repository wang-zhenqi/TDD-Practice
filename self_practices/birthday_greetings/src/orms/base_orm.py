from pydantic import BaseModel


class BaseORM(BaseModel):
    def connect(self):
        pass

    def close(self):
        pass
