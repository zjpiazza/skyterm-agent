import json
import time
from pathlib import Path
import schedule
from supabase import create_client
from datetime import datetime
from dotenv import load_dotenv
import os
import argparse

# Load environment variables
load_dotenv()

# Supabase configuration from environment variables
SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_KEY')

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("Missing required environment variables. Please check your .env file")

# Initialize Supabase client
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def read_aircraft_json():
    try:
        with open('/var/run/dump1090-fa/aircraft.json', 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error reading aircraft.json: {e}")
        return None

def store_aircraft_data():
    data = read_aircraft_json()
    if not data or 'aircraft' not in data:
        return

    timestamp = int(time.time())

    # Prepare data for upsert
    records = []
    for aircraft in data['aircraft']:
        record = {
            'timestamp': timestamp,
            'hex': aircraft.get('hex', ''),
            'flight': aircraft.get('flight', '').strip() or None,  # Convert empty string to None
            'alt_baro': aircraft.get('alt_baro', 0),
            'lat': aircraft.get('lat', 0.0),
            'lon': aircraft.get('lon', 0.0),
            'speed': aircraft.get('gs', 0.0),
            'track': aircraft.get('track', 0.0),
            'seen': aircraft.get('seen', 0.0),
            'seen_pos': aircraft.get('seen_pos', 0.0)
        }

        # Only add records with valid hex codes
        if record['hex']:
            records.append(record)

    try:
        # Perform upsert operation
        response = (
            supabase.table('aircraft')
            .upsert(records)
            .execute()
        )
        print(f"Stored {len(records)} records at {datetime.fromtimestamp(timestamp)}")
    except Exception as e:
        print(f"Error storing data: {e}")

def cleanup_old_data():
    """Remove data older than 24 hours"""
    try:
        cutoff = int(time.time()) - (24 * 3600)
        _ = (
            supabase.table('aircraft')
            .delete()
            .lt('timestamp', cutoff)
            .execute()
        )
        print(f"Cleaned up old data before {datetime.fromtimestamp(cutoff)}")
    except Exception as e:
        print(f"Error cleaning up old data: {e}")

def main():
    parser = argparse.ArgumentParser(
        description='A simple example script demonstrating argparse usage'
    )
    
    # Add a positional argument
    parser.add_argument(
        'polling_interval',
        default=1,
        help='How often to poll the aircraft data in seconds'
    )

    parser.add_argument(
        'cleanup_interval',
        default=1,
        help='How often to cleanup the old data in hours'
    )


    args = parser.parse_args()


    print("ADSB Logger started. Press Ctrl+C to stop.")
    print(f"Connected to Supabase project: {SUPABASE_URL}")

    # Schedule tasks
    schedule.every(args.polling_interval).seconds.do(store_aircraft_data)
    schedule.every(args.cleanup_interval).hours.do(cleanup_old_data)

    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nShutting down...")

if __name__ == "__main__":
    main()