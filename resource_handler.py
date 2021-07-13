from dataclasses import dataclass
import uuid
from pydantic import BaseModel

@dataclass
class Resource(BaseModel):
    id: uuid
    author: str
    title: str
    image_ulr: str
    link: str

    def create_resource(self, ) -> str:
        return "resource Created"

    def update_resource(self, id) -> str:
        return "resource Updated"

    def delete_resource(self, id) -> str:
        return "resource Deleted"

    def fetch_resources(self, id) -> str:
        return "resources Fetched Successfully"

    def search_resource(self, search_key) -> str:
        return "resource Found"
