from __future__ import annotations

from CNB_application import create_app
from CNB_application.core import db
from rq.worker import Worker


class AdvancedWorker(Worker):
    def __init__(self, *args, **kwargs):
        self.app = create_app(api=False)
        super().__init__(*args, **kwargs)

    def work(self, *args, **kwargs):
        with self.app.app_context():
            return super().work(*args, **kwargs)

    @db.connection_context()
    def execute_job(self, *args, **kwargs):
        return super().execute_job(*args, **kwargs)
