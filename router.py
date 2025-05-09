from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import declarative_base


Base = declarative_base()

master_engine = create_engine(
    'sqlite:///master.db', echo=True, logging_name='master'
)
slave_engine= create_engine(
    'sqlite:///slave.db', echo=True, logging_name='slave'
)



engines = {
    'master': master_engine,
    'slave': slave_engine,
}



class RoutingSession(Session):
    _name = None

    def __init__(self, *args, **kwargs):
        super(RoutingSession, self).__init__(*args, **kwargs)
        self.engines = engines
        self.slave_engines = [e for role, e in engines.items()
                              if role != 'master']
        assert self.slave_engines, ValueError('DB slave config is wrong!')

    def get_bind(self, mapper=None, clause=None):
        if self._name:
            return self.engines[self._name]
        else:
            return self.engines['master']



