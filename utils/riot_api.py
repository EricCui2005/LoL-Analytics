# Imports
import requests
import pandas as pd


class RiotAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.headers = {"X-Riot-Token": api_key}
    
    ### Summoner API Functions ###
    
    def get_puuid_by_name(self, game_name, tag_line):
        try:
            url = f"https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}"
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            data = response.json()
            if "puuid" not in data:
                raise KeyError("PUUID not found in response")
            return data["puuid"]
        except requests.exceptions.RequestException as e:
            print(f"Error making request for {game_name}#{tag_line}: {str(e)}")
            return None
        except (KeyError, ValueError) as e:
            print(f"Error parsing response for {game_name}#{tag_line}: {str(e)}")
            return None


    def get_summoner_name_by_puuid(self, puuid):
        try:
            url = f"https://americas.api.riotgames.com/riot/account/v1/accounts/by-puuid/{puuid}"
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            data = response.json()
            return data["gameName"]
        except requests.exceptions.RequestException as e:
            print(f"Error making request for PUUID {puuid}: {str(e)}")
            return None
        except ValueError as e:
            print(f"Error processing summoner data for PUUID {puuid}: {str(e)}")
            return None
    

    def get_summoner_by_puuid(self, puuid):
        try:
            if not puuid:
                raise ValueError("PUUID cannot be empty")
            url = f"https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/{puuid}"
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            data = response.json()
            if not data:
                raise ValueError("Empty response received")
            return data
        except requests.exceptions.RequestException as e:
            print(f"Error making request for PUUID {puuid}: {str(e)}")
            return None
        except ValueError as e:
            print(f"Error processing summoner data for PUUID {puuid}: {str(e)}")
            return None


    def get_rank_data_by_summoner_id(self, puuid):
        try:
            if not puuid:
                raise ValueError("PUUID cannot be empty")
            url = f"https://na1.api.riotgames.com/lol/league/v4/entries/by-puuid/{puuid}"
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            data = response.json()
            if not isinstance(data, list):
                raise ValueError("Expected list response for rank data")
            return data
        except requests.exceptions.RequestException as e:
            print(f"Error making request for PUUID {puuid}: {str(e)}")
            return None
        except ValueError as e:
            print(f"Error processing rank data for PUUID {puuid}: {str(e)}")
            return None


    def get_champion_mastery_by_puuid(self, puuid, champion_id):
        try:
            url = f"https://na1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-puuid/{puuid}/by-champion/{champion_id}"
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            data = response.json()
            return data
        except requests.exceptions.RequestException as e:
            print(f"Error making request for PUUID {puuid}: {str(e)}")
            return None
        except ValueError as e:
            print(f"Error processing champion mastery data for PUUID {puuid}: {str(e)}")
            return None
        
        
        
    ### Match API Functions ###
    
    def get_matches_by_puuid(self, puuid):
        url = f"https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?count=50"
        response = requests.get(url, headers=self.headers)
        matches = response.json()
        return matches


    def get_match_data_by_match_id(self, match_id):
        url = f"https://americas.api.riotgames.com/lol/match/v5/matches/{match_id}"
        response = requests.get(url, headers=self.headers)
        match_data = response.json()
        return match_data


    def get_match_puuids(self, match_id):
        try:
            match_data = self.get_match_data_by_match_id(match_id)
            if "metadata" not in match_data:
                raise KeyError("Match data does not contain metadata")
            if "participants" not in match_data["metadata"]:
                raise KeyError("Match metadata does not contain participants")
            return match_data["metadata"]["participants"]
        except Exception as e:
            print(f"Error getting match PUUIDs for match {match_id}: {str(e)}")
            return []


    def check_ranked(self, match_id):
        try:
            match_data = self.get_match_data_by_match_id(match_id)
            if "info" not in match_data:
                print(f"Match {match_id} data does not contain info")
                return False
            if "queueId" not in match_data["info"]:
                print(f"Match {match_id} info does not contain queueId")
                return False
            return match_data["info"]["queueId"] == 420
        except Exception as e:
            print(f"Error checking if match {match_id} is ranked: {str(e)}")
            return False


    def get_ranked_matches_by_name(self, game_name, tag_line):
        try:
            # Get PUUID from summoner name and tagline
            puuid = self.get_puuid_by_name(game_name, tag_line)
            if not puuid:
                raise ValueError(f"Could not find PUUID for {game_name}#{tag_line}")
            
            # Get all matches for the PUUID
            matches = self.get_matches_by_puuid(puuid)
            if not matches:
                return []
            
            # Filter for only ranked matches
            ranked_matches = []
            for match_id in matches:
                if self.check_ranked(match_id):
                    ranked_matches.append(match_id)
                    
            return ranked_matches
            
        except Exception as e:
            print(f"Error getting ranked matches for {game_name}#{tag_line}: {str(e)}")
            return []
