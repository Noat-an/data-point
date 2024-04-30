"""empty message

Revision ID: 6b64e47f655d
Revises: a92f7c4b4d1d
Create Date: 2024-04-30 05:41:18.759341

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6b64e47f655d'
down_revision: Union[str, None] = 'a92f7c4b4d1d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('parts', schema=None) as batch_op:
        batch_op.create_foreign_key(None, 'product', ['product_id'], ['id'], ondelete='CASCADE')

    with op.batch_alter_table('parts_quality', schema=None) as batch_op:
        batch_op.create_foreign_key(None, 'parts', ['part_id'], ['id'], ondelete='CASCADE')

    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.alter_column('owner_id',
               existing_type=sa.UUID(),
               nullable=True,
               comment='id владельца хранилища',
               existing_comment='Уникальный идентификатор владельца')
        batch_op.create_foreign_key(None, 'storage_owner', ['owner_id'], ['id'], ondelete='SET NULL')

    with op.batch_alter_table('storage', schema=None) as batch_op:
        batch_op.alter_column('url',
               existing_type=sa.VARCHAR(),
               comment='URL источника',
               existing_comment='часть URL источника',
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('storage', schema=None) as batch_op:
        batch_op.alter_column('url',
               existing_type=sa.VARCHAR(),
               comment='часть URL источника',
               existing_comment='URL источника',
               existing_nullable=False)

    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.alter_column('owner_id',
               existing_type=sa.UUID(),
               nullable=False,
               comment='Уникальный идентификатор владельца',
               existing_comment='id владельца хранилища')

    with op.batch_alter_table('parts_quality', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')

    with op.batch_alter_table('parts', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')

    # ### end Alembic commands ###
