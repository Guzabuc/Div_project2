from flask import jsonify
from flask_restful import reqparse, abort, Api, Resource

from data import db_session
from data.news import News

def abort_if_news_not_found(news_id):
    session = db_session.create_session()
    news = session.query(News).get(news_id)
    if not news:
        abort(404, message=f'Новость с id={news_id} не найдена')

class NewsResource(Resource):
    def get(self, news_id):
        abort_if_news_not_found(news_id)
        session = db_session.create_session()
        news = session.query(News).get(news_id)
        return jsonify({
            'news': news.to_dict(only=('title', 'content', 'user_id', 'is_private')
                                 )
        }
        )

    def delete(self, news_id):
        abort_if_news_not_found(news_id)
        session = db_session.create_session()
        news = session.query(News).get(news_id)
        session.delete(news)
        session.commit()
        return jsonify({'success': 'OK'})

parser=reqparse.RequestParser()
parser.add_argument('title', required=True)
parser.add_argument('content', required=True)
parser.add_argument('is_private', required=True, type=bool)
parser.add_argument('is_published', required=True, type=bool)
parser.add_argument('user_id', required=True, type=int)

class NewsListReource(Resource):
    def get(self):
        session = db_session.create_session()
        news = session.query(News).all()
        return jsonify({
            'news': [
                item.to_dict(only=('title', 'content', 'user.name'))
                for item in news
            ]
        }
        )

    def post(self):
        agrs = parser.parse_args()
        session = db_session.create_session()
        news = News(
                title=agrs['title'],
                content=agrs['content'],
                user_id=agrs['user_id'],
                is_published=agrs['is_published'],
                is_private=agrs['is_private']
            )
        session.add(news)
        session.commit()
        return jsonify({'success': 'OK'})
