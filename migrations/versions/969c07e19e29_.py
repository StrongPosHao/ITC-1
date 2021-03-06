"""empty message

Revision ID: 969c07e19e29
Revises: 
Create Date: 2018-06-14 09:44:42.694306

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '969c07e19e29'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Admin',
    sa.Column('adminId', sa.BigInteger(), nullable=False),
    sa.Column('adminName', sa.Unicode(length=20), nullable=False),
    sa.Column('email', sa.Unicode(length=64), nullable=False),
    sa.Column('phone', sa.CHAR(length=11), nullable=False),
    sa.Column('password', sa.Unicode(length=100), nullable=False),
    sa.Column('headImage', sa.Unicode(length=256), nullable=False),
    sa.Column('authority', sa.CHAR(length=1), nullable=False),
    sa.PrimaryKeyConstraint('adminId')
    )
    op.create_table('Question',
    sa.Column('questionId', sa.BigInteger(), nullable=False),
    sa.Column('title', sa.Unicode(length=100), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('publicTime', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('questionId')
    )
    op.create_table('Tag',
    sa.Column('tagId', sa.BigInteger(), nullable=False),
    sa.Column('name', sa.Unicode(length=30), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('popularity', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('tagId')
    )
    op.create_table('User',
    sa.Column('userId', sa.BigInteger(), nullable=False),
    sa.Column('userName', sa.Unicode(length=20), nullable=False),
    sa.Column('email', sa.Unicode(length=64), nullable=False),
    sa.Column('phone', sa.CHAR(length=11), nullable=False),
    sa.Column('password', sa.Unicode(length=100), nullable=False),
    sa.Column('headImage', sa.Unicode(length=256), nullable=False),
    sa.Column('authority', sa.CHAR(length=1), nullable=False),
    sa.PrimaryKeyConstraint('userId')
    )
    op.create_table('Answer',
    sa.Column('answerId', sa.BigInteger(), nullable=False),
    sa.Column('userId', sa.BigInteger(), nullable=False),
    sa.Column('questionId', sa.BigInteger(), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('answerTime', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['questionId'], ['Question.questionId'], ),
    sa.ForeignKeyConstraint(['userId'], ['User.userId'], ),
    sa.PrimaryKeyConstraint('answerId')
    )
    op.create_table('AnswerComment',
    sa.Column('commentId', sa.BigInteger(), nullable=False),
    sa.Column('parentId', sa.BigInteger(), nullable=True),
    sa.Column('userId', sa.BigInteger(), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('commentTime', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['parentId'], ['AnswerComment.commentId'], ),
    sa.ForeignKeyConstraint(['userId'], ['User.userId'], ),
    sa.PrimaryKeyConstraint('commentId')
    )
    op.create_table('Article',
    sa.Column('articleId', sa.BigInteger(), nullable=False),
    sa.Column('userId', sa.BigInteger(), nullable=False),
    sa.Column('title', sa.Unicode(length=100), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('publicTime', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['userId'], ['User.userId'], ),
    sa.PrimaryKeyConstraint('articleId')
    )
    op.create_table('Draft',
    sa.Column('draftId', sa.BigInteger(), nullable=False),
    sa.Column('userId', sa.BigInteger(), nullable=False),
    sa.Column('title', sa.Unicode(length=100), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('saveTime', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['userId'], ['User.userId'], ),
    sa.PrimaryKeyConstraint('draftId')
    )
    op.create_table('FavoriteQuestion',
    sa.Column('questionId', sa.BigInteger(), nullable=False),
    sa.Column('userId', sa.BigInteger(), nullable=False),
    sa.Column('time', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['questionId'], ['Question.questionId'], ),
    sa.ForeignKeyConstraint(['userId'], ['User.userId'], ),
    sa.PrimaryKeyConstraint('questionId', 'userId')
    )
    op.create_table('Follow',
    sa.Column('followerId', sa.BigInteger(), nullable=False),
    sa.Column('followedId', sa.BigInteger(), nullable=False),
    sa.Column('followTime', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['followedId'], ['User.userId'], ),
    sa.ForeignKeyConstraint(['followerId'], ['User.userId'], ),
    sa.PrimaryKeyConstraint('followerId', 'followedId')
    )
    op.create_table('QuestionTag',
    sa.Column('questionId', sa.BigInteger(), nullable=False),
    sa.Column('tagId', sa.BigInteger(), nullable=False),
    sa.Column('time', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['questionId'], ['Question.questionId'], ),
    sa.ForeignKeyConstraint(['tagId'], ['Tag.tagId'], ),
    sa.PrimaryKeyConstraint('questionId', 'tagId')
    )
    op.create_table('UserTag',
    sa.Column('userId', sa.BigInteger(), nullable=False),
    sa.Column('tagId', sa.BigInteger(), nullable=False),
    sa.Column('time', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['tagId'], ['Tag.tagId'], ),
    sa.ForeignKeyConstraint(['userId'], ['User.userId'], ),
    sa.PrimaryKeyConstraint('userId', 'tagId')
    )
    op.create_table('ArticleComment',
    sa.Column('commentId', sa.BigInteger(), nullable=False),
    sa.Column('parentId', sa.BigInteger(), nullable=True),
    sa.Column('articleId', sa.BigInteger(), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('commentTime', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['articleId'], ['Article.articleId'], ),
    sa.ForeignKeyConstraint(['parentId'], ['ArticleComment.commentId'], ),
    sa.PrimaryKeyConstraint('commentId')
    )
    op.create_table('ArticleTag',
    sa.Column('articleId', sa.BigInteger(), nullable=False),
    sa.Column('tagId', sa.BigInteger(), nullable=False),
    sa.Column('time', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['articleId'], ['Article.articleId'], ),
    sa.ForeignKeyConstraint(['tagId'], ['Tag.tagId'], ),
    sa.PrimaryKeyConstraint('articleId', 'tagId')
    )
    op.create_table('FavoriteArticle',
    sa.Column('articleId', sa.BigInteger(), nullable=False),
    sa.Column('userId', sa.BigInteger(), nullable=False),
    sa.Column('time', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['articleId'], ['Article.articleId'], ),
    sa.ForeignKeyConstraint(['userId'], ['User.userId'], ),
    sa.PrimaryKeyConstraint('articleId', 'userId')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('FavoriteArticle')
    op.drop_table('ArticleTag')
    op.drop_table('ArticleComment')
    op.drop_table('UserTag')
    op.drop_table('QuestionTag')
    op.drop_table('Follow')
    op.drop_table('FavoriteQuestion')
    op.drop_table('Draft')
    op.drop_table('Article')
    op.drop_table('AnswerComment')
    op.drop_table('Answer')
    op.drop_table('User')
    op.drop_table('Tag')
    op.drop_table('Question')
    op.drop_table('Admin')
    # ### end Alembic commands ###
