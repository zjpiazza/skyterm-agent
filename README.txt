skyterm-agent

A Python daemon that polls ADS-B (Automatic Dependent Surveillance-Broadcast) data from FlightAware and publishes it to Supabase. This agent works in conjunction with skyterm (https://github.com/zjpiazza/skyterm) to provide real-time flight tracking data visualization.

Overview
--------
skyterm-agent serves as the backend data collector for the skyterm project. It continuously fetches aircraft position data and related flight information from FlightAware's API, processes it, and stores it in a Supabase database for consumption by the frontend application.

Prerequisites
------------
- Python 3.8 or higher
- FlightAware API key
- Supabase account and project credentials

Installation
-----------
1. Clone the repository:
   git clone https://github.com/your-username/skyterm-agent.git
   cd skyterm-agent

2. Install dependencies:
   pip install -r requirements.txt

3. Set up environment variables:
   Create a .env file in the project root with the following variables:

   FLIGHTAWARE_API_KEY=your_api_key_here
   SUPABASE_URL=your_supabase_project_url
   SUPABASE_KEY=your_supabase_anon_key

Usage
-----
Start the agent:
python main.py

The agent will run continuously, polling FlightAware's API at regular intervals and updating the Supabase database with the latest aircraft positions and flight data.

Configuration
------------
You can modify the following parameters in config.py:
- Polling interval
- Geographic boundaries for data collection
- Data filtering options

Database Schema
--------------
The agent publishes data to the following tables in Supabase:

flights:
- flight_id (primary key)
- callsign
- aircraft_type
- departure_airport
- arrival_airport
- status
- last_updated

positions:
- position_id (primary key)
- flight_id (foreign key)
- latitude
- longitude
- altitude
- ground_speed
- heading
- timestamp

Contributing
-----------
1. Fork the repository
2. Create your feature branch (git checkout -b feature/amazing-feature)
3. Commit your changes (git commit -m 'Add some amazing feature')
4. Push to the branch (git push origin feature/amazing-feature)
5. Open a Pull Request

Related Projects
--------------
- skyterm (https://github.com/zjpiazza/skyterm) - Frontend application for visualizing flight data

License
-------
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
--------------
- FlightAware for providing the ADS-B data API
- Supabase for the real-time database infrastructure
