lo = [0] * (1<<17)
for i in range(1,17):
   for j in range((1<<i)-1, (2<<i)-1):
      lo[j+1] = lo[j] + i
next_num = 1
nums = []
def generate(n, c):
   global next_num
   while n > 0:
      assert(c >= lo[n] and c <= n*(n-1)//2)
      n -= 1
      c -= n
      for i in range((n>>1)+1):
         if lo[i] + lo[n-i] <= c:
            j = len(nums)
            nums.append(0)
            generate(i, lo[i])
            nums[j] = next_num
            next_num += 1
            n -= i
            c -= lo[i]
            break
q = int(input())
for q in range(q):
   n, c = map(int, input().split())
   if c < lo[n] or c > n*(n-1)//2:
      print(-1)
   else:
      nums = []
      next_num = 1
      generate(n, c)
      print(*nums)
















