def solution(id_list, report, k):
    answer=[0 for i in range(len(id_list))]
    cnt = [0 for i in range(len(id_list))]
    tmp = {}

    for i in range(0,len(id_list)):
        tmp[id_list[i]] = [];

    print("tmp: ", tmp)    

    #report 중복 신고 제거
    report = set(report)
    print("report Ready...")





    #for문을 통한 신고 횟수 카운트
    for re in report:
        #report를 space로 split
        result = re.split(' ')

        tmp[result[0]].append(result[1])

        for i in range(0, len(id_list)):
            if result[1] == id_list[i]:
                cnt[i] += 1
        
    print("tmp:", tmp)
    print("======================================")

    #이부분부터 다시 해야함
    for key in tmp.keys():
        for user in tmp[key]:
            if cnt[id_list.index(user)] >= k:
                answer[id_list.index(user)] += 1

    print("id_list : ", id_list)
    #return answer
    #[2,1,1,0]
    return answer





print(solution(	["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2))





