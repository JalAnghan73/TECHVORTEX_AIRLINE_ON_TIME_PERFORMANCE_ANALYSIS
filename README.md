# TECHVORTEX_AIRLINE_ON_TIME_PERFORMANCE_ANALYSIS

# team & parts:
 JAL ANGHAN : DATA IMPLEMENT, FORMATTING & CODING //
 AKSHAY CHAUHAN : CODING & TESTER //
 KRISHA PATEL : DATA COLLECTION & SIMPLIFY //
 SUSHANT DADHEECH : DATA COLLECTION //

# Overwiew & Features:
This code project is an airline performance analysis tool that creates a comprehensive database and analytical system for tracking and visualizing flight performance data. Here's an overview of its key features:

1. Database Creation and Management
- Creates a SQLite database to store detailed flight performance information
- Includes two main tables:
  - `flight_performances`: Stores individual flight details
  - `place_time_delays`: Aggregates delay information by airport and date

2. Data Generation
- Generates synthetic flight performance data with:
  - 10,000 simulated flights
  - 100 unique dates spanning approximately two years
  - Randomized data including:
    - Airlines (Delta, United, American, Southwest, JetBlue)
    - Airports (10 major US airports)
    - Aircraft types
    - Weather conditions
    - Flight distances
    - Departure and arrival delays

3. Data Analysis Features
- Calculates and tracks:
  - Departure delays
  - Arrival delays
  - Flight durations
  - Airport-specific performance metrics

4. Visualization Capabilities
- Two main visualizations:
  - Line plot showing total departure delays over time for different airports
  - Pie chart displaying total delay distribution across airports

5. Main Workflow
- Initialize database
- Generate synthetic performance data
- Aggregate delay information
- Analyze and visualize flight performance metrics

The project is designed as a demonstration of data generation, database management, and performance analysis techniques, specifically tailored to simulate and analyze airline flight data.

Key programming concepts demonstrated:
- Object-oriented programming
- Database management with SQLite
- Data generation and simulation
- Data analysis with pandas
- Data visualization with matplotlib and seaborn

# Requirements:
Python 3.x

# AI used:
claude : for develop code
chatgpt : for convert code

# Required Python libraries:
In this script, the following Python libraries are used:

1. `pandas` (imported as `pd`): For data manipulation and analysis
2. `numpy` (imported as `np`): For numerical computing (though not explicitly used in the code)
3. `sqlite3`: For creating and managing SQLite databases
4. `matplotlib.pyplot` (imported as `plt`): For creating static, animated, and interactive visualizations
5. `seaborn` (imported as `sns`): For statistical data visualization
6. `datetime`: For working with dates and times
7. `random`: For generating random data in the synthetic flight performance dataset

The script primarily uses these libraries to:
- Create and manage a SQLite database of airline performance data
- Generate synthetic flight performance data
- Perform data analysis
- Create visualizations of flight delays using line plots and pie charts

# visualizations:
Here's a concise overview of the visualizations:

1. Line Plot: Total Departure Delays Over Time
- Shows departure delays across different airports
- X-axis: Dates
- Y-axis: Total departure delay minutes
- Color-coded by airport
- Helps track delay trends over time

2. Pie Chart: Total Delay Distribution
- Displays percentage of total delays by airport
- Shows which airports contribute most to overall delays
- Provides quick snapshot of airport performance
- Percentage labels for each airport segment

Both visualizations use matplotlib and seaborn to transform raw flight performance data into intuitive, visually informative graphics that help understand airline and airport performance patterns.



# Output Examples:
Since this is a synthetic data generation script, I'll describe the potential output examples:

1. Place and Time-Based Delay Summary (DataFrame Output):
```
   airport_code  delay_date  total_departure_delay  total_arrival_delay
0           ATL  2023-01-15                 120.5              145.2
1           LAX  2023-01-16                  95.3              110.7
2           ORD  2023-01-17                 135.6              160.4
...
```

2. Line Plot Visualization:
- A graph showing departure delays over time
- Multiple colored lines representing different airports
- X-axis with dates
- Y-axis showing total delay minutes
- Each airport represented by a different color
- Data points marked with small circles

3. Pie Chart Visualization:
- Circular chart divided into segments
- Each segment represents an airport
- Segment size proportional to total delay
- Percentage labels like:
  - ATL: 25.3%
  - LAX: 18.7%
  - ORD: 22.5%
  - DFW: 15.2%
  - Others: Remaining percentages

These visualizations help quickly understand:
- Which airports have most delays
- How delays change over time
- Overall delay distribution across airports

Note: Actual outputs will vary due to random data generation.


