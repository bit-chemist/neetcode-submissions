class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}

        for letter in s:
            if letter not in s_dict:
                s_dict[letter] = 1
            else:
                s_dict[letter] += 1
        
        for letter in t:
            if letter not in t_dict:
                t_dict[letter] = 1
            else:
                t_dict[letter] += 1

        if len(s_dict) == len(t_dict):
            for key in s_dict:
                if key in t_dict:
                    if s_dict[key] == t_dict[key]:
                        continue
                    else:
                        return False
                else:
                    return False
            return True
        return False
