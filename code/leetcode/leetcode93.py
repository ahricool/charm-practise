class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        def get_partition(cur_ip, left_str):
            if not left_str:
                return
            if len(cur_ip) == 3:
                if (left_str[0] != '0' and 0 <= int(left_str) <= 255) or (left_str[0] == "0" and len(left_str) == 1):
                    cur_ip.append(left_str)
                    res.append(".".join(cur_ip))
                    cur_ip.pop()
            else:
                if left_str[0] == "0":
                    cur_ip.append("0")
                    get_partition(cur_ip, left_str[1:])
                    cur_ip.pop()
                else:
                    for i in range(3):
                        if 0 < int(left_str[0:i + 1]) <= 255:
                            cur_ip.append(left_str[0:i + 1])
                            get_partition(cur_ip, left_str[i + 1:], )
                            cur_ip.pop()

        get_partition([], s)
        return res
