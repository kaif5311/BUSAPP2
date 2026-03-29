from backend.database import SessionLocal, engine
from backend import models, security
from datetime import time, date

def seed_db():
    db = SessionLocal()

    # Create Admin
    admin_user = db.query(models.User).filter(models.User.email == "admin@redbus.com").first()
    if not admin_user:
        hashed_pw = security.get_password_hash("admin123")
        admin = models.User(name="Admin", email="admin@redbus.com", hashed_password=hashed_pw, role="admin")
        db.add(admin)
        db.commit()

    # Create dummy Routes
    if not db.query(models.Route).first():
        routes = [
            models.Route(source="Mumbai", destination="Pune", duration="3.5 hours"),
            models.Route(source="Mumbai", destination="Kolhapur", duration="8 hours"),
            models.Route(source="Pune", destination="Nagpur", duration="12 hours"),
            models.Route(source="Pune", destination="Bangalore", duration="13 hours"),
            models.Route(source="Mumbai", destination="Bangalore", duration="18 hours"),
        ]
        db.add_all(routes)
        db.commit()

    # Create dummy Buses
    if not db.query(models.Bus).first():
        buses = [
            models.Bus(name="SRS Travels", type="Sleeper AC", total_seats=30),
            models.Bus(name="VRL Travels", type="Seater Non-AC", total_seats=40),
            models.Bus(name="Neeta Travels", type="Sleeper Non-AC", total_seats=30),
            models.Bus(name="Orange Travels", type="Seater AC", total_seats=40),
            models.Bus(name="Shivneri (MSRTC)", type="Seater AC", total_seats=40),
            models.Bus(name="Zingbus", type="Sleeper AC", total_seats=30),
            models.Bus(name="IntrCity SmartBus", type="Sleeper AC", total_seats=30),
            models.Bus(name="Garuda Travels", type="Seater Non-AC", total_seats=40),
        ]
        db.add_all(buses)
        db.commit()

    # Create dummy Schedules
    if not db.query(models.Schedule).first():
        schedules = [
            # Route 1: Mumbai to Pune (id=1)
            models.Schedule(bus_id=5, route_id=1, departure_time=time(6, 0), arrival_time=time(9, 30), price=550.0),
            models.Schedule(bus_id=1, route_id=1, departure_time=time(8, 15), arrival_time=time(11, 45), price=750.0),
            models.Schedule(bus_id=6, route_id=1, departure_time=time(10, 30), arrival_time=time(14, 0), price=800.0),
            models.Schedule(bus_id=8, route_id=1, departure_time=time(14, 0), arrival_time=time(17, 30), price=450.0),
            models.Schedule(bus_id=7, route_id=1, departure_time=time(18, 45), arrival_time=time(22, 15), price=850.0),
            models.Schedule(bus_id=2, route_id=1, departure_time=time(22, 30), arrival_time=time(2, 0), price=400.0),
            
            # Route 2: Mumbai to Kolhapur (id=2)
            models.Schedule(bus_id=2, route_id=2, departure_time=time(13, 30), arrival_time=time(21, 30), price=600.0),
            models.Schedule(bus_id=3, route_id=2, departure_time=time(15, 0), arrival_time=time(23, 0), price=650.0),
            models.Schedule(bus_id=4, route_id=2, departure_time=time(17, 15), arrival_time=time(1, 15), price=750.0),
            models.Schedule(bus_id=5, route_id=2, departure_time=time(19, 0), arrival_time=time(3, 0), price=500.0),
            models.Schedule(bus_id=6, route_id=2, departure_time=time(21, 30), arrival_time=time(5, 30), price=850.0),
            models.Schedule(bus_id=8, route_id=2, departure_time=time(23, 45), arrival_time=time(7, 45), price=700.0),

            # Route 3: Pune to Nagpur (id=3)
            models.Schedule(bus_id=3, route_id=3, departure_time=time(20, 0), arrival_time=time(8, 0), price=1200.0),
            models.Schedule(bus_id=1, route_id=3, departure_time=time(16, 0), arrival_time=time(4, 0), price=1500.0),
            models.Schedule(bus_id=4, route_id=3, departure_time=time(18, 30), arrival_time=time(6, 30), price=1100.0),
            models.Schedule(bus_id=5, route_id=3, departure_time=time(21, 15), arrival_time=time(9, 15), price=900.0),
            models.Schedule(bus_id=7, route_id=3, departure_time=time(22, 0), arrival_time=time(10, 0), price=1450.0),
            models.Schedule(bus_id=8, route_id=3, departure_time=time(23, 30), arrival_time=time(11, 30), price=950.0),

            # Route 4: Pune to Bangalore (id=4)
            models.Schedule(bus_id=4, route_id=4, departure_time=time(20, 45), arrival_time=time(9, 45), price=1800.0),
            models.Schedule(bus_id=1, route_id=4, departure_time=time(15, 0), arrival_time=time(4, 0), price=2100.0),
            models.Schedule(bus_id=2, route_id=4, departure_time=time(17, 30), arrival_time=time(6, 30), price=1600.0),
            models.Schedule(bus_id=5, route_id=4, departure_time=time(19, 15), arrival_time=time(8, 15), price=1500.0),
            models.Schedule(bus_id=6, route_id=4, departure_time=time(21, 0), arrival_time=time(10, 0), price=2200.0),
            models.Schedule(bus_id=7, route_id=4, departure_time=time(22, 30), arrival_time=time(11, 30), price=1950.0),

            # Route 5: Mumbai to Bangalore (id=5)
            models.Schedule(bus_id=1, route_id=5, departure_time=time(15, 20), arrival_time=time(9, 20), price=2200.0),
            models.Schedule(bus_id=3, route_id=5, departure_time=time(17, 0), arrival_time=time(11, 0), price=2500.0),
            models.Schedule(bus_id=4, route_id=5, departure_time=time(18, 45), arrival_time=time(12, 45), price=2000.0),
            models.Schedule(bus_id=6, route_id=5, departure_time=time(20, 15), arrival_time=time(14, 15), price=2800.0),
            models.Schedule(bus_id=7, route_id=5, departure_time=time(21, 30), arrival_time=time(15, 30), price=2600.0),
            models.Schedule(bus_id=8, route_id=5, departure_time=time(22, 45), arrival_time=time(16, 45), price=1900.0),
        ]
        db.add_all(schedules)
        db.commit()

    db.close()
    print("Database seeded successfully.")

if __name__ == "__main__":
    seed_db()
