class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encode = ""
        for s in strs:
            encode += "".join([str(len(s)),'#',s])
        return encode

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        while s:
            l = r = 0
            while s[r] != '#':
                r +=1
            res.append(s[r+1:r+1+int(s[l:r])])
            s = s[(r+1+int(s[l:r])):]
        return res





# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))