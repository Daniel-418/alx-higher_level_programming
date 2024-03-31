import sqlalchemy.*

Base = declarative.base()

class Network(Base):
    __tablename__ = "network"

    network_id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)

Base.metadata.create_all(engine)
session = Session()
session.add(Network(name='net1'))
session.add(Network(name='net2'))

