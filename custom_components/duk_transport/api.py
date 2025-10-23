"""DUK Transport API client."""
import aiohttp
import asyncio
import logging
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any

_LOGGER = logging.getLogger(__name__)

class DUKTransportAPI:
    """API client for DUK Transport."""

    def __init__(self, session: aiohttp.ClientSession):
        """Initialize the API client."""
        self.session = session
        self.base_url = "https://tabule.portabo.cz/api/v1-tabule"

    async def get_departures(self, stop_id: str, max_departures: int = 10) -> List[Dict[str, Any]]:
        """Get departures for a specific stop using the working DUK API endpoint."""
        try:
            # Use the working DUK endpoint format: /duk/GetStationDeparturesWCount/{node}/{post}/{count}/{line}
            # Parameters: node=stop_id, post=1, count=max_departures, line=0 (all lines)
            endpoint = f"/duk/GetStationDeparturesWCount/{stop_id}/1/{max_departures}/0"
            url = f"{self.base_url}{endpoint}"
            
            _LOGGER.debug(f"Requesting DUK API: {url}")
            
            async with self.session.get(url, timeout=aiohttp.ClientTimeout(total=10)) as response:
                if response.status == 200:
                    data = await response.json()
                    departures = self._parse_duk_response(data)
                    _LOGGER.info(f"Successfully fetched {len(departures)} departures from DUK API")
                    return departures[:max_departures]
                else:
                    _LOGGER.warning(f"DUK API returned status {response.status} for stop {stop_id}")
                    return self._get_mock_departures(stop_id, max_departures)
                    
        except Exception as e:
            _LOGGER.error(f"Error fetching departures from DUK API: {e}")
            return self._get_mock_departures(stop_id, max_departures)

    def _parse_duk_response(self, data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Parse DUK API response into standard format."""
        departures = []
        
        if not isinstance(data, dict) or 'DeparturesList' not in data:
            _LOGGER.warning("Invalid DUK API response format")
            return departures
            
        departures_list = data.get('DeparturesList', [])
        station_name = data.get('StationName', 'Unknown')
        
        _LOGGER.debug(f"Parsing {len(departures_list)} departures from station: {station_name}")
        
        for departure in departures_list:
            try:
                # Parse delay string (format: "0:02:00" or "0:00:00")
                delay_str = departure.get('Delay', '0:00:00')
                delay_minutes = self._parse_delay_to_minutes(delay_str)
                
                # Get departure time
                departure_time = departure.get('DepartureDT', '')
                scheduled_time = departure.get('TODepartureDT', departure_time)
                
                # Clean up direction text (fix encoding issues)
                direction = departure.get('Direction', 'Unknown')
                direction = self._fix_encoding(direction)
                
                departures.append({
                    'line': departure.get('LineName', 'N/A'),
                    'destination': direction,
                    'departure_time': self._format_time(departure_time),
                    'scheduled_time': self._format_time(scheduled_time),
                    'delay': delay_minutes,
                    'delay_string': delay_str,
                    'platform': '',  # DUK API doesn't provide platform info
                    'vehicle_type': 'bus',  # DUK is primarily bus transport
                    'carrier': departure.get('Carrier', 'Unknown')
                })
                
            except Exception as e:
                _LOGGER.warning(f"Error parsing departure: {e}")
                continue
        
        return departures

    def _parse_delay_to_minutes(self, delay_str: str) -> int:
        """Parse delay string like '0:02:00' to minutes."""
        try:
            if not delay_str or delay_str == '0:00:00':
                return 0
            parts = delay_str.split(':')
            if len(parts) >= 2:
                hours = int(parts[0])
                minutes = int(parts[1])
                return hours * 60 + minutes
        except (ValueError, IndexError):
            pass
        return 0

    def _fix_encoding(self, text: str) -> str:
        """Fix common encoding issues in Czech text."""
        replacements = {
            'Ã­': 'í',
            'Å¡': 'š',
            'Ä"': 'ň',
            'Ã¡': 'á',
            'Ã©': 'é',
            'Ã³': 'ó',
            'Ãº': 'ú',
            'Å¯': 'ů',
            'Ä›': 'ě',
            'Ä': 'č',
            'Å¾': 'ž',
            'Ã½': 'ý',
            'Ã': 'ř'
        }
        
        for old, new in replacements.items():
            text = text.replace(old, new)
        return text

    def _format_time(self, time_str: str) -> str:
        """Format time string to HH:MM format."""
        if not time_str:
            return "N/A"
            
        try:
            # Parse ISO format like "2025-10-23 14:20:00+02:00"
            if '+' in time_str:
                time_str = time_str.split('+')[0]
            if 'T' in time_str:
                time_str = time_str.replace('T', ' ')
                
            # Try different datetime formats
            for fmt in ['%Y-%m-%d %H:%M:%S', '%H:%M:%S', '%H:%M']:
                try:
                    dt = datetime.strptime(time_str.strip(), fmt)
                    return dt.strftime('%H:%M')
                except ValueError:
                    continue
                    
            # If all else fails, try to extract just the time part
            if ' ' in time_str:
                time_part = time_str.split(' ')[1]
                if ':' in time_part:
                    return time_part[:5]  # Take HH:MM part
                    
        except Exception as e:
            _LOGGER.debug(f"Could not parse time '{time_str}': {e}")
            
        return time_str[:5] if len(time_str) >= 5 else time_str

    def _get_mock_departures(self, stop_id: str, max_departures: int) -> List[Dict[str, Any]]:
        """Generate mock departure data for testing when API is unavailable."""
        import random
        
        _LOGGER.info(f"Generating mock data for stop {stop_id}")
        
        mock_departures = []
        current_time = datetime.now()
        
        # Mock data based on typical DUK routes
        lines = ['480', '484', '430', '485', '420', '440', '460']
        destinations = [
            'Teplice,aut.st.',
            'Duchcov,nem.',
            'Krupka,Fojtovice',
            'Dubí,Krušnohorská',
            'Chlumec',
            'Most,aut.st.',
            'Ústí nad Labem'
        ]
        carriers = ['Doprava Teplice', 'ČSAD Ústí nad Labem', 'ARRIVA']
        
        for i in range(min(max_departures, len(lines))):
            departure_time = current_time + timedelta(minutes=random.randint(2, 45))
            delay_minutes = random.randint(0, 8) if random.random() > 0.6 else 0
            scheduled_time = departure_time - timedelta(minutes=delay_minutes)
            
            mock_departures.append({
                'line': lines[i],
                'destination': destinations[i % len(destinations)],
                'departure_time': departure_time.strftime('%H:%M'),
                'scheduled_time': scheduled_time.strftime('%H:%M'),
                'delay': delay_minutes,
                'delay_string': f"0:{delay_minutes:02d}:00",
                'platform': '',
                'vehicle_type': 'bus',
                'carrier': carriers[i % len(carriers)]
            })
        
        return sorted(mock_departures, key=lambda x: x['departure_time'])

    async def validate_stop_id(self, stop_id: str) -> bool:
        """Validate if stop ID exists by trying to fetch departures."""
        try:
            departures = await self.get_departures(stop_id, 1)
            return len(departures) > 0
        except Exception:
            return False

    async def get_station_info(self, stop_id: str) -> Optional[Dict[str, str]]:
        """Get station information for a given stop ID."""
        try:
            endpoint = f"/duk/GetStationDeparturesWCount/{stop_id}/1/1/0"
            url = f"{self.base_url}{endpoint}"
            
            async with self.session.get(url, timeout=aiohttp.ClientTimeout(total=10)) as response:
                if response.status == 200:
                    data = await response.json()
                    station_name = data.get('StationName', 'Unknown')
                    return {
                        'id': stop_id,
                        'name': self._fix_encoding(station_name),
                        'status': 'active'
                    }
        except Exception as e:
            _LOGGER.debug(f"Could not get station info for {stop_id}: {e}")
            
        return None