from elasticsearch import Elasticsearch
from datetime import datetime

from typing import Dict, Any


class Indexer(object):
    def __init__(self, url: str):
        self.url = url
        self.es = Elasticsearch(url)
        self.index_value = None
        self.date_value = None
        self.create_current_index()

    def index(self, document) -> Dict[str, Any]:
        if self.index_value is None or self.check_day_change():
            self.create_current_index()
        res = self.es.index(index=self.index_value, document=document, doc_type='job')
        return res

    def check_index_exist(self, index) -> bool:
        return self.es.indices.exists(index=index)

    def create_current_index(self) -> None:
        current_date = datetime.utcnow().date()
        current_index = f"job-{current_date.strftime('%Y-%m-%d')}"
        if not self.check_index_exist(current_index):
            self.es.indices.create(index=current_index)
        self.index_value, self.date_value = current_index, current_date

    def check_day_change(self) -> bool:
        return self.date_value < datetime.utcnow().date()
