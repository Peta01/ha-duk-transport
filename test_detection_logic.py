import sys
import os

# Add the custom component path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'custom_components', 'duk_transport'))

# Mock the constants
class MockConst:
    CITY_TRANSPORT_LINES = {}
    TRANSPORT_TYPE_BUS = 'bus'
    TRANSPORT_TYPE_TRAIN = 'train'

sys.modules['custom_components.duk_transport.const'] = MockConst()

# Simple test of the detection logic
def test_vehicle_detection():
    """Test the new vehicle type detection logic"""
    
    # Mock the determine_vehicle_type method logic
    def determine_vehicle_type(line_name, station_name="", carrier="", stop_id=""):
        TRANSPORT_TYPE_BUS = 'bus'
        TRANSPORT_TYPE_TRAIN = 'train'
        
        line_name = line_name.upper()
        station_name = station_name.lower()
        carrier = carrier.strip()
        
        # Ships - detekce podle specifických linek
        if line_name == 'F1':  # F1 přívoz
            return 'ship'
        # T90-T99 turistické lodě
        if line_name.startswith('T') and len(line_name) > 1 and line_name[1:].isdigit():
            t_number = int(line_name[1:])
            if 90 <= t_number <= 99:  # T90-T99 = turistické lodě
                return 'ship'
        
        # Náhradní doprava - linky začínající X jsou náhradní autobusy
        if line_name.startswith('X'):
            return TRANSPORT_TYPE_BUS
        
        # Turistické linky T - podle číselných rozsahů
        if line_name.startswith('T') and len(line_name) > 1 and line_name[1:].isdigit():
            t_number = int(line_name[1:])
            if 1 <= t_number <= 29:  # T1-T29 = turistické vlaky
                return 'train'
            elif 30 <= t_number <= 89:  # T30-T89 = turistické autobusy
                return TRANSPORT_TYPE_BUS
        
        # Trains - detect by line prefixes
        if line_name and line_name[0].isalpha():
            return 'train'
        
        # Fallback patterns for carriers
        carrier_lower = carrier.lower()
        
        # Teplice - MD Teplice
        if 'md teplice' in carrier_lower:
            if line_name in ['101', '102', '103', '104', '105', '106', '107', '108', '109']:
                return 'trolleybus'
            elif line_name in ['110', '119']:
                return TRANSPORT_TYPE_BUS
            return 'trolleybus'
        
        # Most-Litvínov - DPMML
        if 'dpmml' in carrier_lower:
            if line_name in ['1', '2', '3', '4', '40']:
                return 'tram'
            return TRANSPORT_TYPE_BUS
        
        # Ústí nad Labem - DPMÚL
        if 'dpmúl' in carrier_lower or 'dpmãl' in carrier_lower:
            if line_name == '901':
                return 'funicular'
            # Modré linky = trolejbusy (podle mapy)
            elif line_name in ['70', '71', '72', '73', '76', '80', '82', '84', '87', '88']:
                return 'trolleybus'
            # Vše ostatní = autobusy
            else:
                return TRANSPORT_TYPE_BUS
        
        # Chomutov - DPCHJ
        if 'dpchj' in carrier_lower:
            return 'trolleybus'
        
        # Autobusy podle číselných rozsahů
        if line_name.isdigit():
            line_num = int(line_name)
            if 1 <= line_num <= 299:  # Městské linky
                return TRANSPORT_TYPE_BUS
            elif 300 <= line_num <= 799:  # Meziměstské autobusy
                return TRANSPORT_TYPE_BUS
            elif 800 <= line_num <= 899:  # Noční autobusy
                return TRANSPORT_TYPE_BUS
        
        # Default: Regionální autobusy
        return TRANSPORT_TYPE_BUS
    
    print('=== TEST NOVÉ LOGIKY DETEKCE VOZIDEL ===')
    print()
    
    # Test cases
    test_cases = [
        # Line, Carrier, Expected Type, Description
        ('447', 'Doprava Teplice', 'bus', 'Problematická linka 737 - regionální autobus'),
        ('447', 'MD Teplice', 'trolleybus', 'Kdyby byla MD Teplice - trolejbus'),
        ('T5', 'Turistické spoje', 'train', 'Turistický vlak T5'),
        ('T9', 'Turistické spoje', 'train', 'Turistický vlak T9 (ne loď!)'),
        ('T39', 'Turistické spoje', 'bus', 'Turistický autobus T39'),
        ('T91', 'Lodní doprava', 'ship', 'Turistická loď T91'),
        ('T99', 'Lodní doprava', 'ship', 'Turistická loď T99'),
        ('F1', 'Lodní doprava', 'ship', 'Přívoz F1'),
        ('X480', 'Náhradní doprava', 'bus', 'Náhradní autobus X480'),
        ('R14', 'České dráhy', 'train', 'Regionální vlak R14'),
        ('IC123', 'České dráhy', 'train', 'InterCity vlak'),
        ('101', 'MD Teplice', 'trolleybus', 'Teplice trolejbus 101'),
        ('110', 'MD Teplice', 'bus', 'Teplice autobus 110'),
        ('1', 'DPMML', 'tram', 'Most tramvaj 1'),
        ('5', 'DPMML', 'bus', 'Most autobus 5'),
        ('901', 'DPMÚL', 'funicular', 'Ústí lanovka 901'),
        ('70', 'DPMÚL', 'trolleybus', 'Ústí trolejbus 70 (modrá)'),
        ('79', 'DPMÚL', 'bus', 'Ústí autobus 79 (zelená)'),
        ('10', 'DPMÚL', 'bus', 'Ústí turistický autobus 10 (oranžová)'),
        ('350', 'ČSAD', 'bus', 'Meziměstský autobus 350'),
        ('801', 'Noční doprava', 'bus', 'Noční autobus 801'),
    ]
    
    print(f"{'Linka':>6} | {'Typ':>12} | {'Dopravce':>20} | {'Popis'}")
    print("-" * 70)
    
    for line, carrier, expected, description in test_cases:
        result = determine_vehicle_type(line, "", carrier, "")
        status = "✅" if result == expected else "❌"
        print(f"{line:>6} | {result:>12} | {carrier:>20} | {status} {description}")
    
    print()
    print("=== SHRNUTÍ ===")
    print("✅ = Správná detekce")  
    print("❌ = Chybná detekce")

if __name__ == "__main__":
    test_vehicle_detection()