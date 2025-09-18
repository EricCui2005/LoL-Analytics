# League of Legends Analytics

### [Report](https://drive.google.com/file/d/1zZpbak-gfR3LWQ_Cwj9-owmH6TW9-F54/view?usp=sharing) 🔗

A Python-based analytics project that leverages the Riot Games API to analyze League of Legends match data and generate Markov chain-based predictions for game outcomes.

## Overview

This project provides tools and utilities for:

- Fetching and analyzing League of Legends match data
- Processing match timelines and game states
- Generating Markov chain transition matrices for game state prediction
- Analyzing player statistics and performance metrics

## Features

- **Riot API Integration**: Comprehensive wrapper for the Riot Games API

  - Summoner information retrieval
  - Match history and timeline data
  - Champion mastery statistics
  - Rank information

- **Match Analysis**:

  - Detailed match timeline processing
  - Gold difference tracking
  - Kill difference analysis
  - Structure and objective control tracking
  - Team state comparison

- **Markov Chain Modeling**:
  - Game state transition analysis
  - State space modeling for game progression
  - Transition probability matrix generation
  - Game outcome prediction capabilities

## Prerequisites

- Python 3.12 or higher
- Riot Games API key
- Required Python packages (see `requirements.txt`)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/LoL-Analytics.git
cd LoL-Analytics
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Set up your Riot Games API key:
   - Get an API key from the [Riot Developer Portal](https://developer.riotgames.com/)
   - Add your API key to the configuration or environment variables

## Project Structure

```
LoL-Analytics/
├── notebooks/
│   └── match_data.ipynb    # Jupyter notebook for data analysis
├── utils/
│   ├── riot_api.py        # Riot Games API wrapper
│   └── markov_utils.py    # Markov chain utilities
├── jsons/
│   ├── data/             # Processed data storage
│   ├── frames/           # Match frame data
│   └── timelines/        # Match timeline data
└── README.md
```

## Usage

1. Basic summoner information retrieval:

```python
from utils.riot_api import RiotAPI

api = RiotAPI(api_key)
puuid = api.get_puuid_by_name("summoner_name", "tag_line")
summoner_data = api.get_summoner_by_puuid(puuid)
```

2. Match analysis:

```python
matches = api.get_ranked_matches_by_name("summoner_name", "tag_line")
for match_id in matches:
    timeline = api.get_match_timeline(match_id)
    info_dicts = api.extract_timeline_frame_info(timeline)
```

3. Markov chain analysis:

```python
from utils.markov_utils import MarkovUtils

markov_util = MarkovUtils()
markov_util.convert_raw_info_list_to_markov_data(info_dicts)
transitions = markov_util.get_markov_transitions(info_dicts)
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Riot Games API for providing access to League of Legends data
- The League of Legends community for inspiration and feedback
