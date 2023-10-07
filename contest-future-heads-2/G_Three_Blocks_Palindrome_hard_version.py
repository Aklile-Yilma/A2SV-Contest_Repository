import sys, threading

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        cnt = [[0] * (n + 1) for _ in range(26)]
        for i in range(n):
            for j in range(26):
                cnt[j][i + 1] = cnt[j][i]
            cnt[a[i] - 1][i + 1] += 1

        ans = 0
        for i in range(26):
            ans = max(ans, cnt[i][n - 1])

        for l in range(n):
            for r in range(l, n):
                cntin = 0
                cntout = 0
                for el in range(26):
                    cntin = max(cntin, cnt[el][r + 1] - cnt[el][l])
                    cntout = max(cntout, min(cnt[el][l], cnt[el][n] - cnt[el][r + 1]) * 2)
                ans = max(ans, cntin + cntout)

        print(ans)


sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)

main_thread = threading.Thread(target = main)
main_thread.start()
main_thread.join()


# t = int(input())
# for _ in range(t):
#     n = int(input())
#     a = list(map(int, input().split()))

#     cnt = [[0] * (n + 1) for _ in range(26)]
#     for i in range(n):
#         for j in range(26):
#             cnt[j][i + 1] = cnt[j][i]
#         cnt[a[i] - 1][i + 1] += 1

#     ans = 0
#     for i in range(26):
#         ans = max(ans, cnt[i][n - 1])

#     for l in range(n):
#         for r in range(l, n):
#             cntin = 0
#             cntout = 0
#             for el in range(26):
#                 cntin = max(cntin, cnt[el][r + 1] - cnt[el][l])
#                 cntout = max(cntout, min(cnt[el][l], cnt[el][n] - cnt[el][r + 1]) * 2)
#             ans = max(ans, cntin + cntout)

#     print(ans)
