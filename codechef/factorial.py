# cook your dish here
n = int(input())
for _ in range(n):
    num = int(input())
    i = 1
    cnt = 0
    while num>=5**i:
        cnt += num//5**i
        i += 1
    print(cnt)


# #include <stdio.h>
#
# int main(void) {
#     long long int t;
#     scanf("%lld",&t);
#     while(t--){
#         long long int n;
#         scanf("%lld",&n);
#         int pf = 5,count=0;
#         while(n/pf > 0){
#             count = count+n/pf;
#             pf = pf*5;
#         }
#         printf("%lld\n",count);
#     }
# 	// your code goes here
# 	return 0;
# }

