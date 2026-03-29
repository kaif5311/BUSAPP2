from backend.database import SessionLocal, engine
from backend import models, security
from datetime import time

def force_seed_missing_schedules():
    db = SessionLocal()
    
    # Check current schedules
    schedules = db.query(models.Schedule).all()
    print(f"Currently have {len(schedules)} schedules.")
    
    if len(schedules) < 30:
        print("Clearing old schedules and re-inserting 30 schedules...")
        db.query(models.Schedule).delete()
        db.commit()
        
        new_schedules = [
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
        db.add_all(new_schedules)
        db.commit()
        print("Inserted 30 schedules (6 per route).")
    else:
        print("Database already has 30 or more schedules. Nothing to do.")

if __name__ == "__main__":
    force_seed_missing_schedules()
