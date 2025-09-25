# Python Roguelike Game

## Introduction
This is a roguelike dungeon-crawling game built with Python for the backend game logic, Supabase as the backend database service, and HTML/CSS for the frontend user interface. The game features procedurally generated dungeons, turn-based movement and combat, and persistent player progress saved in Supabase.

## Features
- Procedurally generated dungeons and levels
- Turn-based player movement and combat system
- Enemy AI with strategic behavior
- Items, traps, and loot scattered throughout the dungeon
- Save and load player progress using Supabase database
- Web-based frontend with dynamic game rendering using HTML and CSS
- REST API endpoints powered by Python backend

## Project Structure
Game/
│
├── src/                    # Core game logic and database interaction
│   ├── logic.py            # Main roguelike game mechanics, movement, combat, AI
│   ├── db.py               # Supabase database interface (save/load game state)
│   └── utils.py            # Helper functions
│
├── frontend/               # Frontend app assets and server
│   ├── app.py              # Frontend server, or static site generator
│   ├── static/             # CSS, JS, images for frontend
│   └── templates/          # HTML templates for rendering UI if using Flask or similar
│
├── api/                    # Backend API
│   └── main.py             # FastAPI or Flask entry point serving game API routes
│
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
├── .env                    # Python variables
└── .gitignore              # Git ignore rules

## Requirements
- Python 3.8 or higher
- Supabase account and project setup
- Python packages listed in `requirements.txt`
- Modern web browser for frontend display


## Installation
## 1. Clone or Download the Project:

## Option 1 : Clone with GIT
git clone <repository_url>

## Option 2 : Download and extract the ZIP file.

## 2. Install Python dependencies:
pip install -r requirements.txt

## 3. Set up Supabase Database:
1. Create a Supabase Project.
2. Create the Tasks Table.

-Go to SQL Editor in your Supabase Dashboard
-Run this SQL Command

CREATE TABLE players (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  username TEXT UNIQUE NOT NULL,
  current_level INT DEFAULT 1,
  position_x INT DEFAULT 0,
  position_y INT DEFAULT 0,
  health INT DEFAULT 100,
  inventory JSONB DEFAULT '{}'::JSONB,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

3. Get your Credentials

## 4. Configure environmental variables
1. Create a `.env` file in the project root.
2. Add your Supabase credentials in the `.env` file:
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key

## 5. Run the Application
### Streamlit Frontend

streamlit run frontend/app.py

The app will open in your browser at ⁠`http://localhost:8080` ⁠

## FastAPI Backend

cd api

python main.py

The API will be available at⁠ `http://localhost:8080` ⁠

## How to Use
1. Setup Supabase Database:
Create a Supabase project.
Add all required tables (players, scores, game_states, items, player_items, enemies).
Configure environment variables in .env for your Supabase URL & API key.

2. Install Dependencies
Run: pip install -r requirements.txt to install Python libraries.

3. Run Backend API
Start the API server: python api/main.py.
API exposes endpoints for game actions like move, attack, and save/load state.

4. Launch Frontend
Run frontend server if applicable: python frontend/app.py.
Or open the HTML/CSS/JS files directly in a browser.
Use the UI to interact with the game which communicates to backend API.

## Technical details

### Technologies Used
•⁠  ⁠*Frontend*: Streamlit (Python web framework)

•⁠  ⁠*Backend*: FastAPI (Python REST API framework)

•⁠  ⁠*Database*: Supabase (PostgreSQL-based backend-as-a-service)

•⁠  ⁠*Language*: Python 3.8+

## Key Components
1. **`api/main.py`** : Backend entry point exposing REST API endpoints,handles requests from frontend and calls game logic and database functions.

2. **`frontend/app.py`** : Frontend server or static site wrapper.Serves HTML, CSS, JS files which create the game UI and handles user interface rendering and input features.

3. **`src/logic.py`** : Core gameplay rules (player movement, enemy AI, combat).Dungeon generation logic and game state updates according to player actions.

4. **`src/db.py`** : Database interface functions to read/write game state to Supabase.CRUD operations for players, scores, items, enemies, etc.

5. **`.env`** : Environment variables and secret keys for Supabase.

6. **`requirements.txt`** : List of Python dependencies for backend and frontend servers.

## Trouble Shooting
If you run into issues, try these solutions:
1. Module Import Errors: Make sure all dependencies are installed (pip install -r requirements.txt) and Python path is correct.
2. Supabase Connection Issues: Verify .env file has correct Supabase URL and API keys, and network access is allowed.
3. Game Logic Bugs: Use print statements or logging to trace errors in movement, combat, or dungeon generation.
4. Frontend Rendering Problems: Clear browser cache, check console for JavaScript errors, and validate API URLs.
5. API Request Failures: Ensure backend is running and endpoints match frontend requests.

## Common Issues
1. Player not moving correctly or stuck at boundaries.
2. Inventory items disappearing or not saving.
3. Game state not persisting across sessions.
4. API calls timing out or returning errors.
5. Visual glitches or misaligned UI components.

## Future Enhancements
1. Add multiplayer support with real-time synchronization via Supabase.
2. Implement advanced procedural dungeon generation with multiple room shapes and traps.
3. Enhance graphics with sprites, animations, and particle effects.
4. Add sound effects and background music.
5. Create an in-game tutorial and help system.
6. Optimize performance for larger maps and more enemies.
7. Implement achievements, quests, and leaderboard features.

# Support

Report issues or request features on the GitHub Issues page.

Contact the maintainer at [keerthi.dandiga17@gmail.com].

