class Solution:

    # non - generic approach
    '''def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return 'NA'
        encoded_str = '-'.join(strs)    # separator is hyphen instead of space incase any string is multiword
        return encoded_str

    def decode(self, s: str) -> List[str]:
        if s == 'NA':
            return []
        decoded_strs = s.split('-')
        return decoded_strs'''

    # general solution
    def encode(self, strs: List[str]) -> str:
        encoded_str = ''
        for s in strs:
            str_len = str(len(s))
            encoded_str = encoded_str + str_len + '#' + s
        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0
        while i != len(s):
            str_length = ''
            while s[i] != '#':
                str_length += s[i]
                i += 1
            str_length = int(str_length)
            i += 1
            decoded_strs.append(s[i: i + str_length])
            i = i + str_length
        return decoded_strs
            