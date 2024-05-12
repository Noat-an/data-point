import sqlalchemy as sa

from src.apps.api.storage import model
from src.db.common._repository import BaseRepository


class ProductRepository(BaseRepository):

    async def get_product_list(self) -> list[model.Product]:
        result = await self.session.execute(
            sa.select(
                model.Product.name,
                model.Product.parts,
                model.Product.size
            )
        )
        return result.all()

    async def get_file_list(self, product_name: str):
        result = await self.session.execute(
            sa.select(
                model.ProductParts.part_num,
                model.ProductParts.row,
                model.ProductParts.size
            )
        )
        return result.all()

    async def add_product(self, obj: model.ProductParts) -> None:
        return await super().add(obj)
