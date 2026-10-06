class Solution:

    def encode(self, strs: List[str]) -> str:
        code = ""
        for word in strs:
            code = code + word + "Ω" 
        return code

    def decode(self, s: str) -> List[str]:
        message = []
        word = ""
        for char in s:
            if char == "Ω":
                message.append(word)
                word = ""
            else:
                word = word + char
        return message


                
                



      
