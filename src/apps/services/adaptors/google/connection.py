from typing import List

from google.oauth2 import service_account
from googleapiclient.discovery import build

from .config import Config


class GoogleClientConnection:

    def __init__(
            self,
            service_account_info
    ) -> None:
        self.service_account_info = service_account_info

    @property
    def credentials(self):

        credentials = service_account.Credentials.from_service_account_info(
            self.service_account_info, scopes=Config.SERVICE_SCOPES
        )
        return credentials

    @property
    def service(self):
        service = build(
            Config.SERVICE_NAME,
            Config.SERVICE_API_VERSION,
            credentials=self.credentials
        )
        return service

    def get_servise_file_list(self, page_size: int = 100) -> List[dict]:
        results: dict = self.service.files().list(
            pageSize=page_size,
            fields=f"files({', '.join(Config.SERVICE_FIELDS)})"
        ).execute()
        return results.get('files')
