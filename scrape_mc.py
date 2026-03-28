import requests, json, os

def scrape_minecraft():
    print("📡 Fetching latest Minecraft 1.21 data...")
    # Pulling from a reliable items/blocks database
    items_url = "https://raw.githubusercontent.com/PrismarineJS/minecraft-data/master/data/pc/1.21/items.json"
    blocks_url = "https://raw.githubusercontent.com/PrismarineJS/minecraft-data/master/data/pc/1.21/blocks.json"
    
    items = requests.get(items_url).json()
    blocks = requests.get(blocks_url).json()
    
    knowledge = []
    # Grab first 100 items and blocks to keep the file fast
    for i in items[:100]:
        knowledge.append(f"The item {i['displayName']} has the ID {i['name']}.")
    for b in blocks[:100]:
        knowledge.append(f"The block {b['displayName']} is used in building.")
        
    knowledge.append("Temsin is a Grade 8 student at Samsen and the creator of Temb.")
    
    with open('knowledge.json', 'w') as f:
        json.dump(knowledge, f)
    print("✅ Knowledge saved to knowledge.json")

if __name__ == "__main__":
    scrape_minecraft()
