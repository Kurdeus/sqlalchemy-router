from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import declarative_base

MasterBase = declarative_base()
SlaveBase = declarative_base()


master_engine = create_engine(
    'sqlite:///master.db', echo=True, logging_name='master'
)
slave_engine = create_engine(
    'sqlite:///slave.db', echo=True, logging_name='slave'
)

engines = {
    'master': {"engine": master_engine, "base": MasterBase},
    'slave': {"engine": slave_engine, "base": SlaveBase},
}

class RoutingSession(Session):
    _name = None

    def __init__(self, *args, **kwargs):
        super(RoutingSession, self).__init__(*args, **kwargs)
        self.engines = engines
        self.slave_engines = [e["engine"] for role, e in engines.items()
                              if role != 'master']
        assert self.slave_engines, ValueError('DB slave config is wrong!')

    def get_bind(self, mapper=None, clause=None, **kwargs):
        # Determine which engine to use based on the model's base
        if mapper is not None:
            if hasattr(mapper.class_, '__table__'):
                table = mapper.class_.__table__
                if table.metadata is MasterBase.metadata:
                    return master_engine
                elif table.metadata is SlaveBase.metadata:
                    return slave_engine
        # Fallback to master if unable to determine
        return master_engine
