"""Helper script to find DUK stop IDs."""
import requests
import json

def test_stop_ids(stop_name, id_ranges):
    """Test various ID formats for a stop."""
    print(f"🔍 Hledání ID pro zastávku: {stop_name}")
    
    base_urls = [
        "https://tabule.portabo.cz/api/v1-tabule/departures/",
        "https://tabule.portabo.cz/api/v1-tabule/stops/",
        "https://tabule.portabo.cz/api/v1-tabule/timetable/",
    ]
    
    for base_url in base_urls:
        print(f"\n📡 Testování endpointu: {base_url}")
        
        for id_range in id_ranges:
            for stop_id in id_range:
                try:
                    response = requests.get(f"{base_url}{stop_id}", 
                                          headers={"Accept": "application/json"},
                                          timeout=5)
                    
                    if response.status_code == 200:
                        print(f"✅ ID {stop_id} - Status: {response.status_code}")
                        try:
                            data = response.json()
                            if any(stop_name.lower() in str(data).lower() for name in ["krupka", "unčín", "lípy"]):
                                print(f"🎯 MOŽNÁ SHODA! ID: {stop_id}")
                                print(f"Data: {json.dumps(data, indent=2, ensure_ascii=False)[:500]}...")
                        except:
                            print(f"Odpověď není JSON")
                    
                except requests.exceptions.RequestException:
                    pass
                except Exception as e:
                    pass

if __name__ == "__main__":
    # Různé formáty ID k testování
    id_ranges = [
        range(1, 100),      # 1-99
        range(100, 200),    # 100-199  
        range(1000, 1100),  # 1000-1099
        [f"K{i}" for i in range(1, 50)],  # K1-K49
        [f"KR{i}" for i in range(1, 50)], # KR1-KR49
    ]
    
    test_stop_ids("Krupka Unčín U Lípy", id_ranges)