"""
T(n) = n^3

"""
class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        # bfs => guarantee minimum distances
        # for each letter in A, try different number combinations and see
        # if we can find B
        
        queue = collections.deque([s1])
        # to record the transformation we have seen
        seen = set()
        
        k = 0
        
        while queue:
            #different layer of the bfs tree
            for _ in range(len(queue)):
                s1 = queue.popleft()
                
                # see if it is the same as s2
                if s1 == s2:
                    return k
                
                # s1 != s2, we need to swap some letters
                # if s1[i] == s2[i], we don't need to do anything
                # if we try all senarios, o(n^k)
                # but since we know B, we can prune the tree towards the
                # direction of B
                # i = the index where s1[i] != s2[i]
                i = 0
                while s1[i] == s2[i]:
                    i += 1
                
                """
                A = aabec
                B = aacbe
                i = 2
                swap a 2, 4 => a= aaceb
                """
                
                for j in range(i, len(s1)):
                    if s2[j] != s1[j] and s2[i] == s1[j]:
                        # swap A[i] and A[j]
                        # since we are gonna swap elements in A
                        # turn it into list
                        s1_list = list(s1)
                        s1_list[i], s1_list[j] = s1_list[j], s1_list[i]
                        # convert it back to string
                        temp_str = "".join(s1_list)
                        
                        # check if we have seen this
                        if temp_str in seen:
                            continue
                        
                        # else add to the queue for next level check
                        queue.append(temp_str)
                        seen.add(temp_str)
            # after each level
            k += 1
        return -1
                        
        
        
        
