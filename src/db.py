from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# Players
def create_player(username):
    data = {"username": username}
    return supabase.table("players").insert(data).execute()

def get_player(username):
    return supabase.table("players").select("*").eq("username", username).single().execute()

def update_player(player_id, updates: dict):
    return supabase.table("players").update(updates).eq("id", player_id).execute()

# Game state
def save_game_state(player_id, dungeon_map, entities):
    data = {"player_id": player_id, "dungeon_map": dungeon_map, "entities": entities}
    return supabase.table("game_states").insert(data).execute()

def load_game_state(player_id):
    return supabase.table("game_states").select("*").eq("player_id", player_id).order("created_at", desc=True).limit(1).execute()

# Inventory
def add_item_to_player(player_id, item_id, quantity=1):
    existing = supabase.table("player_items").select("*").eq("player_id", player_id).eq("item_id", item_id).execute()
    if existing.data:
        supabase.table("player_items").update({'quantity': existing.data[0]['quantity'] + quantity}).eq('id', existing.data[0]['id']).execute()
    else:
        supabase.table("player_items").insert({'player_id': player_id, 'item_id': item_id, 'quantity': quantity}).execute()

# Scores
def save_score(player_id, level_reached, enemies_defeated, treasures_collected):
    score = enemies_defeated * 10 + treasures_collected * 5
    supabase.table("scores").insert({
        "player_id": player_id,
        "level_reached": level_reached,
        "enemies_defeated": enemies_defeated,
        "treasures_collected": treasures_collected,
        "score": score
    }).execute()

def get_leaderboard(limit=10):
    return supabase.table("scores").select("score, player_id").order("score", desc=True).limit(limit).execute()
