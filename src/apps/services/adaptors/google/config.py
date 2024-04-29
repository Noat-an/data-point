

class Config:
    SERVICE_NAME = 'drive'
    SERVICE_API_VERSION = 'v3'
    SERVICE_SCOPES = ['https://www.googleapis.com/auth/drive']
    SERVICE_FIELDS = [
        'id',
        'name',
        'mimeType',
        'parents',
        'createdTime',
        'modifiedTime',
        'quotaBytesUsed',
        'size',
        'fileExtension',
        'owners',
        'lastModifyingUser',
        'md5Checksum',
        'thumbnailLink',
        'webContentLink',
        'webViewLink',
        'permissions'
    ]
