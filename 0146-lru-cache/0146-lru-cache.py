class LRUCache:
    
    # 키가 캐시에 있으면 값을 가져오고 없으면 -1
    # 값이 들어왔을때 이미 키가 캐시에 있으면 값 업데이트
    # 없으면 새로운 캐시에 값 등록
    # 만약 용량이 초과 됐다면 가장 사용하지 않은 캐시를 지운다


    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity


    def get(self, key: int) -> int:
        # 키가 캐시에 있으면
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]

        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        # 이미 키가 존재하면 
        if key in self.cache:
            self.cache.move_to_end(key)
            self.cache[key] = value
        else:
            if len(self.cache) < self.capacity:
                self.cache[key] = value
            else:
                # 가장 사용하지 않은 키 삭제
                self.cache.popitem(last=False)
                self.cache[key] = value
        

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)