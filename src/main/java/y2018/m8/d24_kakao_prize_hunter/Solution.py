reward_2017 = ({"rank": 1, "reward": 5000000, "limit": 1},
               {"rank": 2, "reward": 3000000, "limit": 2},
               {"rank": 3, "reward": 2000000, "limit": 3},
               {"rank": 4, "reward": 500000, "limit": 4},
               {"rank": 5, "reward": 300000, "limit": 5},
               {"rank": 6, "reward": 100000, "limit": 6})

reward_2018 = ({"rank": 1, "reward": 5120000, "limit": 1},
               {"rank": 2, "reward": 2560000, "limit": 2},
               {"rank": 3, "reward": 1280000, "limit": 4},
               {"rank": 4, "reward": 640000, "limit": 8},
               {"rank": 5, "reward": 320000, "limit": 16})


def get_reward(reward_def, rank):
    cnt = 0
    result = {"reward": 0}
    for i in reward_def:
        if cnt < rank:
            cnt = cnt + i["limit"]
            result = i
    if rank > cnt:
        result = {"reward": 0}

    return result["reward"]


def solution():
    cnt = int(input())
    for i in range(cnt):
        rank_2017, rank_2018 = map(int, input().split(" "))
        reward = get_reward(reward_2017, rank_2017) + get_reward(reward_2018, rank_2018)
        print(reward)


solution()
