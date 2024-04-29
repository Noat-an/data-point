from __future__ import annotations

from typing import List

from pydantic import BaseModel


class LastModifyingUser(BaseModel):
    displayName: str
    kind: str
    me: bool
    permissionId: str
    emailAddress: str
    photoLink: str


class Owner(BaseModel):
    displayName: str
    kind: str
    me: bool
    permissionId: str
    emailAddress: str
    photoLink: str


class Permission(BaseModel):
    id: str
    displayName: str
    type: str
    kind: str
    photoLink: str
    emailAddress: str
    role: str
    deleted: bool
    pendingOwner: bool


class GoogleFileSchema(BaseModel):
    fileExtension: str
    md5Checksum: str
    mimeType: str
    parents: List[str]
    thumbnailLink: str
    lastModifyingUser: LastModifyingUser
    owners: List[Owner]
    webViewLink: str
    webContentLink: str
    size: str
    permissions: List[Permission]
    id: str
    name: str
    createdTime: str
    modifiedTime: str
    quotaBytesUsed: str
