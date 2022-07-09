class Solution:
    def validIPAddress(self, IP: str) -> str:
        ipv4=IP.split(".")
        ipv6=IP.split(":")

        if len(ipv4)==4:
            for piece in ipv4:
                if len(piece)==0:
                    return "Neither"
                if not piece.isdigit():
                    return "Neither"
                if not 0<=int(piece)<=255:
                    return "Neither"
                if int(piece)!=0 and piece[0]=="0":
                    return "Neither"
                if int(piece)==0 and len(piece)>1:
                    return "Neither"

            return "IPv4"

        elif len(ipv6)==8:
            for piece in ipv6:
                if not 0<len(piece)<5:
                    return "Neither"
                try:
                    int(piece,16)
                except:
                    return "Neither"

            return "IPv6"

        else:
            return "Neither"