import pandas as pd
import numpy as np
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import random

class AirlinePerformanceDatabase:
    def __init__(self, db_name='airline_performance.db'):
        """
        Initialize SQLite database for storing airline performance data
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_tables()

    def _create_tables(self):
        """
        Create tables for storing flight performance data and delay summaries
        """
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS flight_performances (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            flight_date DATE,
            airline TEXT,
            origin_airport TEXT,
            destination_airport TEXT,
            scheduled_departure DATETIME,
            actual_departure DATETIME,
            scheduled_arrival DATETIME,
            actual_arrival DATETIME,
            departure_delay REAL,
            arrival_delay REAL,
            flight_duration REAL,
            distance REAL,
            aircraft_type TEXT,
            weather_condition TEXT
        )
        ''')
        
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS place_time_delays (
            airport_code TEXT,
            delay_date DATE,
            total_departure_delay REAL,
            total_arrival_delay REAL,
            PRIMARY KEY (airport_code, delay_date)
        )
        ''')
        
        self.conn.commit()

    def insert_flight_performance(self, flight_data):
        """
        Insert flight performance data into the database
        """
        insert_query = '''
        INSERT INTO flight_performances (
            flight_date, airline, origin_airport, destination_airport, 
            scheduled_departure, actual_departure, 
            scheduled_arrival, actual_arrival, 
            departure_delay, arrival_delay, 
            flight_duration, distance, 
            aircraft_type, weather_condition
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        '''
        self.cursor.executemany(insert_query, flight_data)
        self.conn.commit()

    def insert_place_time_delays(self):
        """
        Aggregate and insert place and time-based delay data.
        """
        # Clear existing data in the table to prevent duplicate entries
        self.cursor.execute('DELETE FROM place_time_delays')
        
        # Aggregate and insert new data
        query = '''
        INSERT INTO place_time_delays (airport_code, delay_date, total_departure_delay, total_arrival_delay)
        SELECT 
            origin_airport AS airport_code,
            DATE(flight_date) AS delay_date,
            SUM(departure_delay) AS total_departure_delay,
            SUM(arrival_delay) AS total_arrival_delay
        FROM flight_performances
        GROUP BY origin_airport, DATE(flight_date)
        '''
        self.cursor.execute(query)
        self.conn.commit()

    def generate_performance_data(self, num_flights=10000, num_dates=100):
        """
        Generate synthetic flight performance data with at least 100 unique dates
        """
        airlines = ['Delta', 'United', 'American', 'Southwest', 'JetBlue']
        airports = {
            'ATL': 'Atlanta', 'LAX': 'Los Angeles', 'ORD': 'Chicago',
            'DFW': 'Dallas', 'DEN': 'Denver', 'JFK': 'New York',
            'SFO': 'San Francisco', 'SEA': 'Seattle', 'LAS': 'Las Vegas',
            'MCO': 'Orlando'
        }
        aircraft_types = ['Boeing 737', 'Airbus A320', 'Boeing 787', 'Airbus A330']
        weather_conditions = ['Clear', 'Partly Cloudy', 'Cloudy', 'Rainy', 'Windy']

        # Generate 100 unique dates spanning the last 2 years
        base_start_date = datetime.now() - timedelta(days=730)
        unique_dates = [base_start_date + timedelta(days=i) for i in range(num_dates)]

        flight_data = []
        airport_routes = list([(orig, dest) for orig in airports.keys() for dest in airports.keys() if orig != dest])

        for _ in range(num_flights):
            origin, destination = random.choice(airport_routes)
            airline = random.choice(airlines)
            
            # Select a random unique date from the generated dates
            flight_date = random.choice(unique_dates)
            scheduled_departure = flight_date + timedelta(hours=random.randint(0, 23))
            flight_distance = random.uniform(500, 2500)  # miles
            base_duration = flight_distance / 500  # rough estimate of flight time
            
            # Simulate delays
            departure_delay = max(0, random.normalvariate(15, 30))
            arrival_delay = max(0, random.normalvariate(20, 40))
            
            actual_departure = scheduled_departure + timedelta(minutes=departure_delay)
            scheduled_arrival = scheduled_departure + timedelta(hours=base_duration)
            actual_arrival = scheduled_arrival + timedelta(minutes=arrival_delay)

            flight_data.append((
                flight_date.date(),
                airline,
                origin,
                destination,
                scheduled_departure,
                actual_departure,
                scheduled_arrival,
                actual_arrival,
                departure_delay,
                arrival_delay,
                base_duration,
                flight_distance,
                random.choice(aircraft_types),
                random.choice(weather_conditions)
            ))

        self.insert_flight_performance(flight_data)

    def analyze_place_time_delays(self):
        """
        Analyze total delays by airport and date
        """
        query = '''
        SELECT 
            airport_code, 
            delay_date, 
            total_departure_delay, 
            total_arrival_delay
        FROM place_time_delays
        ORDER BY delay_date ASC, total_departure_delay DESC
        LIMIT 50
        '''
        return pd.read_sql_query(query, self.conn)

    def visualize_place_time_delays(self):
        """
        Visualize place and time-based delays with more dates
        """
        data = self.analyze_place_time_delays()
        plt.figure(figsize=(14, 7))
        sns.lineplot(data=data, x='delay_date', y='total_departure_delay', hue='airport_code', marker="o", legend='full')
        plt.title('Total Departure Delays Over Time by Airport')
        plt.xlabel('Date')
        plt.ylabel('Total Departure Delay (minutes)')
        plt.xticks(rotation=45)
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.tight_layout()
        plt.show()

    def visualize_delay_distribution_pie_chart(self):
        """
        Visualize the distribution of total delays as a pie chart
        """
        query = '''
        SELECT 
            airport_code,
            SUM(total_departure_delay + total_arrival_delay) AS total_delay
        FROM place_time_delays
        GROUP BY airport_code
        '''
        data = pd.read_sql_query(query, self.conn)

        plt.figure(figsize=(10, 7))
        plt.pie(data['total_delay'], labels=data['airport_code'], autopct='%1.1f%%', startangle=140)
        plt.title('Total Delay Distribution by Airport')
        plt.tight_layout()
        plt.show()

def main():
    # Initialize database
    db = AirlinePerformanceDatabase()
    
    # Generate synthetic performance data with at least 100 unique dates
    db.generate_performance_data(num_flights=10000, num_dates=100)
    
    # Aggregate place and time delay data
    db.insert_place_time_delays()
    
    # Print Place-Time Delay Summary
    print("\n--- Place and Time-Based Delay Summary ---")
    place_time_delays = db.analyze_place_time_delays()
    print(place_time_delays)
    
    # Visualize Place-Time Delays
    db.visualize_place_time_delays()
    
    # Visualize Delay Distribution (Pie Chart)
    db.visualize_delay_distribution_pie_chart()

if __name__ == "__main__":
    main()

