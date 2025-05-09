from models import User_Master, User_Slave
from router import engines, RoutingSession





if __name__ == '__main__':
    for item in engines.values():
        item["base"].metadata.create_all(item["engine"])

    session = RoutingSession()

    print("  --- ADD ---  ")
    session.add_all([
        User_Master(name='paul', email='paul@example.com'),
        User_Slave(name='george', email='george@example.com'),
    ])
    session.commit()


    print("  --- READ ---  ")
    user = session.query(User_Master).first()
    print("🟢 Master User email is", user.email)

    user = session.query(User_Slave).first()
    print("🟢 Slave User email is", user.email)

    print("  --- END ---  ")

    session.close()
