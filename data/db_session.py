import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session
# import sqlalchemy.ext.declarative as dec

SqlAlchemyBase = orm.declarative_base()

created = None   # создана ли сессия

def global_init(db_file):
    global created

    if created:
        return

    if not db_file or not db_file.strip():     # .strip Удаляет начальные и конечные символы в строке
        raise Exception("Забыли подключить файл базы данных!")

    # проверяем не поключились ли мы ранее к базе
    conn_str = f'sqlite:///{db_file.strip()}?check_same_thread=False'

    # для отладки , потом можно отключить
    print('Мы подключились к базе: {conn_str}')

    engine = sa.create_engine(conn_str, echo=False)
    # создаем сессию и привязывам к движку
    created = orm.sessionmaker(bind=engine)


    from . import all_models

    SqlAlchemyBase.metadata.create_all(engine)

# -> Session:- аннотация функции, будет возвращать к функции
def create_session() -> Session:
    global created
    return created
