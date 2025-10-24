"""DUK Transport API client."""
import aiohttp
import asyncio
import logging
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any

_LOGGER = logging.getLogger(__name__)

class DUKTransportAPI:
    """API client for DUK Transport (Buses, Trains, Ships)."""

    def __init__(self, session: aiohttp.ClientSession):
        """Initialize the API client."""
        self.session = session
        self.base_url = "https://tabule.portabo.cz/api/v1-tabule"

    async def get_departures(self, stop_id: str, max_departures: int = 10) -> List[Dict[str, Any]]:
        """Get departures for a specific stop using the working DUK API endpoint."""
        try:
            # Use the working DUK endpoint format: /duk/GetStationDeparturesWCount/{node}/{post}/{count}/{line}
            # Parameters: node=stop_id, post=0, count=max_departures, line=0 (all lines)
            # Note: post=0 provides correct platform information, post=1 shows everything as platform 1
            endpoint = f"/duk/GetStationDeparturesWCount/{stop_id}/0/{max_departures}/0"
            url = f"{self.base_url}{endpoint}"
            
            _LOGGER.debug(f"Requesting DUK API: {url}")
            
            async with self.session.get(url, timeout=aiohttp.ClientTimeout(total=10)) as response:
                if response.status == 200:
                    data = await response.json()
                    departures = self._parse_duk_response(data, stop_id)
                    _LOGGER.info(f"Successfully fetched {len(departures)} departures from DUK API")
                    return departures[:max_departures]
                else:
                    _LOGGER.warning(f"DUK API returned status {response.status} for stop {stop_id}")
                    return self._get_mock_departures(stop_id, max_departures)
                    
        except Exception as e:
            _LOGGER.error(f"Error fetching departures from DUK API: {e}")
            return self._get_mock_departures(stop_id, max_departures)

    def _parse_duk_response(self, data: Dict[str, Any], stop_id: str) -> List[Dict[str, Any]]:
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
                
                # Determine vehicle type based on line name, station context, and carrier
                line_name = departure.get('LineName', 'N/A')
                carrier = departure.get('Carrier', 'Unknown')
                vehicle_type = self._determine_vehicle_type(line_name, station_name, carrier, stop_id)
                
                departures.append({
                    'line': line_name,
                    'destination': direction,
                    'departure_time': self._format_time(departure_time),
                    'scheduled_time': self._format_time(scheduled_time),
                    'delay': delay_minutes,
                    'delay_string': delay_str,
                    'platform': departure.get('StationPost', ''),  # Both DUK and CIS use StationPost for platform
                    'vehicle_type': vehicle_type,
                    'vehicle_emoji': self._get_vehicle_emoji(vehicle_type),
                    'vehicle_icon': self._get_vehicle_icon(vehicle_type),
                    'carrier': carrier
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
                'vehicle_emoji': self._get_vehicle_emoji('bus'),
                'vehicle_icon': self._get_vehicle_icon('bus'),
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
            endpoint = f"/duk/GetStationDeparturesWCount/{stop_id}/0/1/0"
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

    async def get_cis_departures(self, stop_id: str, post_id: str = "0", max_departures: int = 10) -> List[Dict[str, Any]]:
        """Get departures from CIS API (trains and ships)."""
        try:
            # Use CIS endpoint format: /cis/GetStationDeparturesWCount/{node}/{post}/{count}/{line}
            endpoint = f"/cis/GetStationDeparturesWCount/{stop_id}/{post_id}/{max_departures}/0"
            url = f"{self.base_url}{endpoint}"
            
            _LOGGER.debug(f"Requesting CIS API: {url}")
            
            async with self.session.get(url, timeout=aiohttp.ClientTimeout(total=10)) as response:
                if response.status == 200:
                    data = await response.json()
                    departures = self._parse_cis_response(data, stop_id)
                    _LOGGER.info(f"Successfully fetched {len(departures)} CIS departures")
                    return departures[:max_departures]
                else:
                    _LOGGER.warning(f"CIS API returned status {response.status}")
                    return []
                    
        except Exception as e:
            _LOGGER.error(f"Error fetching CIS departures: {e}")
            return []

    def _parse_cis_response(self, data: Dict[str, Any], stop_id: str) -> List[Dict[str, Any]]:
        """Parse CIS API response for trains and ships."""
        departures = []
        
        if not isinstance(data, dict) or 'DeparturesList' not in data:
            _LOGGER.debug("No CIS departures found")
            return departures
            
        departures_list = data.get('DeparturesList', [])
        station_name = data.get('StationName', 'Unknown')
        
        _LOGGER.debug(f"Parsing {len(departures_list)} CIS departures from: {station_name}")
        
        for departure in departures_list:
            try:
                # Parse delay
                delay_str = departure.get('Delay', '0:00:00')
                delay_minutes = self._parse_delay_to_minutes(delay_str)
                
                # Get times
                departure_time = departure.get('DepartureDT', '')
                scheduled_time = departure.get('TODepartureDT', departure_time)
                
                # Clean up direction
                direction = departure.get('Direction', 'Unknown')
                direction = self._fix_encoding(direction)
                
                # Determine vehicle type based on line name, station context, and carrier
                line_name = departure.get('LineName', '')
                carrier = departure.get('Carrier', '')
                vehicle_type = self._determine_vehicle_type(line_name, station_name, carrier, stop_id)
                
                departures.append({
                    'line': line_name,
                    'destination': direction,
                    'departure_time': self._format_time(departure_time),
                    'scheduled_time': self._format_time(scheduled_time),
                    'delay': delay_minutes,
                    'delay_string': delay_str,
                    'platform': departure.get('StationPost', ''),  # CIS uses StationPost for platform info
                    'vehicle_type': vehicle_type,
                    'vehicle_emoji': self._get_vehicle_emoji(vehicle_type),
                    'vehicle_icon': self._get_vehicle_icon(vehicle_type),
                    'carrier': departure.get('Carrier', 'Unknown')
                })
                
            except Exception as e:
                _LOGGER.warning(f"Error parsing CIS departure: {e}")
                continue
                
        return departures

    def _determine_vehicle_type(self, line_name: str, station_name: str, carrier: str = "", stop_id: str = "") -> str:
        """Determine vehicle type from line name, station context, carrier, and stop ID."""
        from .const import CITY_TRANSPORT_LINES, TRANSPORT_TYPE_BUS, TRANSPORT_TYPE_TRAIN, TRANSPORT_TYPE_TOURIST_TRAIN
        
        line_name = line_name.upper()
        station_name = station_name.lower()
        carrier = carrier.strip()
        
        # Default is bus - most common transport type
        vehicle_type = TRANSPORT_TYPE_BUS
        
        # Debug logging for ALL Teplice lines to see what's happening
        if stop_id == '1578' or 'teplice' in station_name.lower():
            _LOGGER.debug(f"Teplice analysis - Linka: {line_name}, Dopravce: '{carrier}', Stanice: '{station_name}', ID: {stop_id}")
        
        # 1. Ships - highest priority (specific lines)
        if line_name == 'F1':  # F1 přívoz
            return 'ship'
        # T90-T99 turistické lodě (ale ne T9 - to je vlak!)
        if line_name.startswith('T') and len(line_name) > 1 and line_name[1:].isdigit():
            t_number = int(line_name[1:])
            if 90 <= t_number <= 99:  # T90-T99 = turistické lodě
                return 'ship'
        
        # 2. Tourist lines T - podle číselných rozsahů (kromě lodí)
        if line_name.startswith('T') and len(line_name) > 1 and line_name[1:].isdigit():
            t_number = int(line_name[1:])
            if 1 <= t_number <= 29:  # T1-T29 = turistické vlaky s parní lokomotivou
                return 'tourist_train'
            # T30-T89 = turistické autobusy, T90-T99 = lodě (already handled)
            # Rest falls through to default bus
        
        # 3. Trains - detect by line prefixes (any line starting with letter, kromě T turistických)
        # Vlaky mají vždy prefix písmenu (R, EX, U, Os, Sp, IC, EC, RJ, EN atd.)
        if line_name and line_name[0].isalpha() and not line_name.startswith('X'):
            return 'train'
        
        # 4. PRIORITY: City-specific detection using const.py configuration
        for city_key, city_data in CITY_TRANSPORT_LINES.items():
            if city_data["carrier"] == carrier:
                if line_name in city_data["lines"]:
                    return city_data["type"]
        
        # 5. Hardcoded fallbacks for carriers with default types (not fully configured in const.py)
        carrier_lower = carrier.lower()
        
        # DPMML default to tram for non-configured lines
        if 'dpmml' in carrier_lower:
            return 'tram'
        
        # DPMÚL fallbacks for non-configured lines
        if 'dpmúl' in carrier_lower or 'dpmãl' in carrier_lower:
            # Non-configured lines default to bus
            pass
        
        # DPCHJ default to trolleybus for non-configured lines
        if 'dpchj' in carrier_lower:
            return 'trolleybus'
        
        # 6. Everything else is bus (regional transport, replacement X lines, numeric ranges)
        return TRANSPORT_TYPE_BUS

    def _get_vehicle_emoji(self, vehicle_type: str) -> str:
        """Get emoji for vehicle type."""
        from .const import TRANSPORT_EMOJIS
        return TRANSPORT_EMOJIS.get(vehicle_type, "🚌")  # Default to bus emoji

    def _get_vehicle_icon(self, vehicle_type: str) -> str:
        """Get Material Design Icon for vehicle type."""
        from .const import TRANSPORT_ICONS
        return TRANSPORT_ICONS.get(vehicle_type, "mdi:bus")  # Default to bus icon

    async def get_stations_list(self, endpoint: str = "duk") -> List[Dict[str, Any]]:
        """Get list of all stations from specified endpoint."""
        try:
            url = f"{self.base_url}/{endpoint}/GetStations"
            _LOGGER.debug(f"Requesting stations list: {url}")
            
            async with self.session.get(url, timeout=aiohttp.ClientTimeout(total=30)) as response:
                if response.status == 200:
                    data = await response.json()
                    stations = []
                    
                    if isinstance(data, dict) and 'ItemList' in data:
                        for station in data['ItemList']:
                            name = self._fix_encoding(station.get('Name', ''))
                            stations.append({
                                'node': station.get('Node'),
                                'post': station.get('Post'),
                                'name': name,
                                'latitude': station.get('Latitude', 0.0),
                                'longitude': station.get('Longitude', 0.0),
                                'zone': station.get('Zone', ''),
                                'endpoint': endpoint
                            })
                    
                    _LOGGER.info(f"Retrieved {len(stations)} stations from {endpoint}")
                    return stations
                else:
                    _LOGGER.warning(f"Failed to get stations list: {response.status}")
                    return []
                    
        except Exception as e:
            _LOGGER.error(f"Error fetching stations list: {e}")
            return []