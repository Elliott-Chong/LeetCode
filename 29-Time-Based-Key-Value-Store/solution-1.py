class TimeMap:
    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = [[value, timestamp]]
        else:
            self.store[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        values = self.store.get(key, [])
        res = ''
        lp, rp = 0, len(values) - 1
        while lp <= rp:
            mp = (lp+rp) // 2
            curr_value, curr_timestamp = values[mp]
            if timestamp == curr_timestamp:
                return curr_value
            if timestamp > curr_timestamp:
                res = curr_value
                lp = mp + 1
            else:
                rp = mp - 1
        return res

# Your Timemap object will be instantiated and called as such:
# obj = Timemap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)