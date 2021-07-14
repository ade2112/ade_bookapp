from dataclasses import dataclass
import uuid
from pydantic import BaseModel
import resource_query

@dataclass
class Resource(BaseModel):
    # id: uuid
    author: str
    title: str
    image_ulr: str
    link: str

    def create_resource(self) -> str:
        mes=resource_query.create_res(self)
        return mes

    def update_resource(self, id) -> str:
        mes=resource_query.update_res(self,id)
        return mes

    def delete_resource(id) -> str:
        mes=resource_query.delete_res(id)
        return mes

    def fetch_resources(self) -> str:
        rows=resource_query.fetch_res()
        return rows
    def search_resource(self,title) -> str:
        rows=resource_query.search(title)
        return rows
