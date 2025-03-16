class MarkovUtils:
    def __init__(self):
        pass
    
    ### Raw Conversion Functions ###
    
    def convert_gold_diff_to_markov_data(self, gold_diff):
        if gold_diff < -6000:
            return 0
        elif -6000 <= gold_diff < -3000:
            return 1
        elif -3000 <= gold_diff < 0:
            return 2
        elif gold_diff == 0:
            return 3
        elif 0 < gold_diff <= 3000:
            return 4
        elif 3000 < gold_diff <= 6000:
            return 5
        elif 6000 < gold_diff:
            return 6


    def convert_kills_diff_to_markov_data(self, kills_diff):
        if kills_diff < -9:
            return 0
        elif -9 <= kills_diff <= -5:
            return 1
        elif -4 <= kills_diff < 0:
            return 2
        elif kills_diff == 0:
            return 3
        elif 1 <= kills_diff <= 4:
            return 4
        elif 5 <= kills_diff <= 9:
            return 5
        elif kills_diff > 9:
            return 6


    def convert_structure_kills_diff_to_markov_data(self, structure_kills_diff):
        if structure_kills_diff < -5:
            return 0
        elif -5 <= structure_kills_diff <= -3:
            return 1
        elif -2 <= structure_kills_diff < 0:
            return 2
        elif structure_kills_diff == 0:
            return 3
        elif 1 <= structure_kills_diff <= 3:
            return 4
        elif 4 <= structure_kills_diff <= 5:
            return 5
        elif structure_kills_diff > 5:
            return 6
      
        
    def convert_elite_monster_kills_diff_to_markov_data(self, elite_monster_kills_diff):
        if elite_monster_kills_diff < -5:
            return 0
        elif -5 <= elite_monster_kills_diff <= -3:
            return 1
        elif -2 <= elite_monster_kills_diff < 0:
            return 2
        elif elite_monster_kills_diff == 0:
            return 3
        elif 1 <= elite_monster_kills_diff <= 3:
            return 4
        elif 4 <= elite_monster_kills_diff <= 5:
            return 5
        elif elite_monster_kills_diff > 5:
            return 6
       
       
        
    ### Raw Info Dict Conversion Functions ###
    
    def convert_raw_info_dict_to_markov_data(self, info_dict):
        info_dict["gold_diff"] = self.convert_gold_diff_to_markov_data(info_dict["gold_diff"])
        info_dict["kills_diff"] = self.convert_kills_diff_to_markov_data(info_dict["kills_diff"])
        info_dict["structure_kills_diff"] = self.convert_structure_kills_diff_to_markov_data(info_dict["structure_kills_diff"])
        info_dict["elite_monster_kills_diff"] = self.convert_elite_monster_kills_diff_to_markov_data(info_dict["elite_monster_kills_diff"])
        info_dict["markov_coordinate"] = self.convert_markov_data_dict_to_markov_coordinate(info_dict)
    
    
    def convert_raw_info_list_to_markov_data(self, info_list):
        for info_dict in info_list:
            self.convert_raw_info_dict_to_markov_data(info_dict)

    
    
    ### Markov Chain Functions ###
    
    def convert_markov_data_dict_to_markov_coordinate(self, markov_data_dict):
        g = markov_data_dict["gold_diff"]
        k = markov_data_dict["kills_diff"]
        s = markov_data_dict["structure_kills_diff"]
        m = markov_data_dict["elite_monster_kills_diff"]
        w = markov_data_dict["win_state"]
        
        return (1029 * g) + (147 * k) + (21 * s) + (3 * m) + w
    
    
    def get_markov_transitions(self, info_dicts):
        transitions = []
        for i in range(len(info_dicts) - 1):
            current_frame = info_dicts[i]
            next_frame = info_dicts[i + 1]
            transitions.append((current_frame["markov_coordinate"], next_frame["markov_coordinate"]))
        return transitions
        
        
        
        
    
        
        
        