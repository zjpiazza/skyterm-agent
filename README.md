skyterm-agent

A Python daemon that polls ADS-B (Automatic Dependent Surveillance-Broadcast) data from FlightAware and publishes it to Supabase. This agent works in conjunction with [Skyterm](https://github.com/zjpiazza/skyterm) to provide real-time flight tracking data visualization.

Overview
--------
skyterm-agent serves as the backend data collector for the skyterm project. It continuously fetches aircraft position data and related flight information from a FlightAware station, processes it, and stores it in a Supabase database for consumption by the frontend application. This agent was was designed specifically for Piaware, but can be used with any other ADS-B source with some modifications.

Prerequisites
------------
- Python 3.8 or higher
- PiAware/FlightAware
- Supabase account and project credentials

Installation
-----------
1. Clone the repository:
   ```
   git clone https://github.com/your-username/skyterm-agent.git
   cd skyterm-agent
   ```


2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   Create a .env file in the project root with the following variables:

    ```
   SUPABASE_URL=your_supabase_project_url
   SUPABASE_KEY=your_supabase_anon_key
    ```

Usage
-----
Start the agent: 

```python main.py```

The agent will run continuously, polling Piaware's JSON file at regular intervals and updating the Supabase database with the latest aircraft positions and flight data.

Configuration
------------
You can modify the following command line arguments:
- Polling interval
- Cleanup interval

Contributing
-----------
1. Fork the repository
2. Create your feature branch (git checkout -b feature/amazing-feature)
3. Commit your changes (git commit -m 'Add some amazing feature')
4. Push to the branch (git push origin feature/amazing-feature)
5. Open a Pull Request

Related Projects
--------------
- [Skyterm](https://github.com/zjpiazza/skyterm) - Frontend application for visualizing flight data

License
-------
This project is licensed under the MIT License - see the LICENSE file for details.

