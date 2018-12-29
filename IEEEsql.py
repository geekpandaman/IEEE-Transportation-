import time
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('mysql://root:680418@localhost/IEEE?charset=utf8mb4')
DBSession = sessionmaker(bind=engine)
SQLsession = DBSession()
Base = declarative_base()

class paper(Base):
    __tablename__ = 'paper'
    id_name = Column(Integer(), primary_key=True)
    title = Column(String(100))
    pub_year = Column(Integer())
    cit_num = Column(Integer())
    kwd = Column(String(100))

# 创建数据表
Base.metadata.create_all(engine)

# 写入商家信息
def paper_db(info_dict):
    temp_id = info_dict['id_name']
    # 判断是否已存在记录
    info = SQLsession.query(paper).filter_by(id_name=temp_id).first()
    if info:
        info.id_name = info_dict.get('id_name', '')
        info.title = info_dict.get('title', '')
        info.pub_year = info_dict.get('pub_year', '')
        info.cit_num = info_dict.get('cit_num', '')
        info.kwd = info_dict.get('kwd', '')
        print('paper exist!')
    else:
        inset_data = paper(
            id_name=info_dict.get('id_name', ''),
            title=info_dict.get('title', ''),
            pub_year=info_dict.get('pub_year', ''),
            cit_num=info_dict.get('cit_num', ''),
            kwd=info_dict.get('kwd', ''),
        )
        SQLsession.add(inset_data)
        print('insert %s successfully!' % info_dict.get('id_name',''))
    SQLsession.commit()
    
