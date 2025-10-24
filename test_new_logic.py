import asyncio
import aiohttp
import sys
import os

# Add the custom component path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'custom_components', 'duk_transport'))
from api import DUKTransportAPI

async def test_new_logic():
    async with aiohttp.ClientSession() as session:
        api = DUKTransportAPI(session)
        
        # Test problematic station 737
        print('=== TEST ZASTÁVKY 737 (Teplice problematická) ===')
        departures = await api.get_departures('1737', 5)
        
        for dep in departures:
            print(f"Linka: {dep['line']:>4} | Typ: {dep['vehicle_type']:>12} | Dopravce: {dep['carrier'][:30]:30} | Cíl: {dep['destination'][:30]:30}")
        
        print('\n=== TEST RŮZNÝCH TYPŮ LINEK ===')
        # Test various line types with mock data
        test_lines = [
            ('447', 'Doprava Teplice', 'Regional bus'),
            ('T5', 'Turistické spoje', 'Tourist train'),
            ('T39', 'Turistické spoje', 'Tourist bus'),
            ('T91', 'Lodní doprava', 'Tourist ship'),
            ('F1', 'Lodní doprava', 'Ferry'),
            ('X480', 'Náhradní doprava', 'Replacement bus'),
            ('R14', 'České dráhy', 'Regional train'),
            ('101', 'MD Teplice', 'Teplice trolleybus'),
        ]
        
        for line, carrier, description in test_lines:
            vehicle_type = api._determine_vehicle_type(line, 'test station', carrier, '1234')
            print(f"Linka: {line:>4} | Typ: {vehicle_type:>12} | Test: {description}")

if __name__ == "__main__":
    asyncio.run(test_new_logic())