from typing import List

from googleapiclient.http import MediaIoBaseDownload, MediaFileUpload

from ..base._base import RemoveStorage
from .connection import GoogleClientConnection
from .schemas import GoogleFileSchema


class GoogleDriveStorage(RemoveStorage):
    def __init__(self, service_account_info) -> None:
        self.service_account_info = service_account_info

    @property
    def serviceMetadata(self) -> List[GoogleFileSchema]:
        connection = GoogleClientConnection(
            self.service_account_info
        )
        return connection.get_servise_file_list

    def getFileParams(self, file_name):
        pass

    def uploadFile(self):
        pass

    def downloadFile(self):
        pass
