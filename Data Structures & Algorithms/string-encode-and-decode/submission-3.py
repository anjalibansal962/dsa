class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return 'NA'
        encoded_str = '-'.join(strs)    # separator is hyphen instead of space incase any string is multiword
        return encoded_str

    def decode(self, s: str) -> List[str]:
        if s == 'NA':
            return []
        decoded_strs = s.split('-')
        return decoded_strs