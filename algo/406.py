class Solution:
    def reconstructQueue(self, people):
        if len(people) <= 1:
            return people
        people.sort(key=lambda r: (r[0], -r[1]), reverse=True)
        for i in range(len(people)):
            self.getAndInsert(people, i)
        return people

    def getAndInsert(self, pepole, select_idx):
        person = pepole[select_idx]
        idx = 0
        if person[1] > 0:
            gt_cnt = 0
            while idx < len(pepole) and gt_cnt < person[1]:
                if person[0] <= pepole[idx][0]:
                    gt_cnt += 1
                idx += 1
        if select_idx != idx:
            #print(idx)
            for i in range(select_idx, idx, -1):
                pepole[i] = pepole[i - 1]
            pepole[idx] = person
            print(idx, pepole)

if __name__ == "__main__":
    input_arr = [[9,0],[7,0],[1,9],[3,0],[2,7],[5,3],[6,0],[3,4],[6,2],[5,2]]
    s = Solution()
    res = s.reconstructQueue(input_arr)
    print(res)