input output
condition loops-prime, reverse
comments - # and """ ghqh """
variable - type() , multiword - camel,pascal,snake , global
string, list...

Aug-8-2025
string like array, collection crud - list,tuple,set,dict
methods-arbitary arguments, keyword arguments
class method use self, // integer division
cs50 binary search, binary search same- corrected on while s<=e: s=m+1 e=m-1
leetcode run in local : 1. instance of class 2. call method from instance
smallest char - modulo , ceiling

Aug-9-2025
first and last search - tricky, helper func
mountain,rbs -return s or e but while s<e, always m <>m+1 used both {goole docs try}
rbs-pivot 4 cases

Aug-10-2025
RBS-pivot-code, [range 0- n-1 -> n< arr.length]
Bubble n n2 stable-break,
Selection n2 n2 unstable (small) -max,
Insertion- n n2 stable while range to 0,partial-hybrid
Cyclic - o(1), 0-N, actual,for by while, while by if - o(1)

Actual Aug-10-2025
Cyclic code confusing actual from 0 or 1, OG duplicate
missing number- nums[i] <n ignore, duplicate: only copy
Video- duplicate (single pass), all missing duplicates same code
from 0 or 1, actualindex= nums[i], nums[i]-1,
missing positive- hard -> easy, setmismatch- solved in java, python but nums[i] < (n+1\*) ignore,
Pattern : easy, range(0,0) is empty, ternary : col=2\*n-i if i>n else i,diamond spaces
up down with spaces perfect, right left mess-trick python, reverse loop: for i in range(6,0,-1),

Aug-11 Recursion, intro, basics

Aug-13 Reverse-way to use global variable,digits=math.log(n)+1 confused,digits=int(math.log10(n))+1 perfect
steps,zeros easy,Array Search-sorted?,linear rec-single,many-parameter (accumulator) ,global ok, new list confuse-return and combine

August-14-2025 : RBS first rec pivot, confusing, video not clear, gemini- left or right sort, inside or out
pattern- how to reset value again,while return print reverse basic,bubble fine

August-15-2025 : Selection if c<=r:swap(nums,max,c-1), if r==0, if r<0, Merge Sort : light base condition, if s==e: return [nums[s]]

August-16-2025 : best n logn, worst n2,implemented as per video, used if here and check for low high while nums[s]<pivot: s=s+1 while nums[e]>pivot: e=e-1

August-17-2025 : string - consider like array,skip accumulator ok, return and combine none: ans alone,append error, 'str' object has no attribute 'append',concatenate but performance issue,
Skip word- startswith,return not in,substring print easy, ret issue,video ans-two pass ret list of p,
ascii=str(ord(up[0])),permutation range confuse

August-18-2025 : print path error or works and fails, subtract before check,obstacle no reaction,missed return equal,all path board success,path success,phone single case good,return ok, loop confuse,copy 7 and 9 fail,Need to use map,dice,all ans print,processed miss,use extend for list,
N- queens : matrix = [[True for _ in range(3)] for \_ in range(3)]
converted_matrix = [['Q' if val else '.' for val in row] for row in boolean_matrix]
no clear approach, only isSafe try,video loop- infinite,video copy leetcode giveup.

August-19-2025 : OOPS- Linked list in java success, python confuse,Node inside call,too many self add first worked fine,add perfect,delete perfect,doubly insert,display

August-22-2025 : Circular LL skip, insert rec try wrong, debug,recursion return good,duplicates try sample case pass,while,local run,

August-23-2025 : sort 2 ll, 1hour try perfect ans,cycle ok,cycle start unable to run in local due to cycle,
video concept, code modify,happy number solved on own,middle so easy,merge sort ll,local no issue but empty,debug ans correct,(cycle fast slow pointer)

August-24-2025 : ll bubble swap new but skip,reverse try no idea,only that is list,video easy work,
rec copy, loop try debug but different,leetcode rev, part rev - find,rev??,understood question wrong, reverse part in given pos not node,even debug not helps,video not helps,dummyLeft debug half case pass,
self.head removed

August-25-2025 : palindrome,o(1) space, half reverse - mid,reverse try half case pass,1 -> 2 fail,video easy copy, no print ,reorder copy not workout,local computer crash,notes not workout,logic video copy,

August-26-2025 : Stack try,queue ok,video java- flexible but exception and circular skip,LC-two stacks,
parenthesis java confuse,

August-27-2025 : parenthesis,sleeping idea,python remove[0],video copy,gemini suggest,stack[len(stack)-1],inside remove, out peek,pop ans good,elif beats 100 better than kunal,par count without stack half pass,open close try fail,light video code correct but poor perf,video faang last option,double bracket,try not workout,gemini ans,Tree try,debuged and corrected,height added,height fun short,rotate,balanced??video,
balanced checked only height,rotate right left check,rotate left heavy right heavy??,rotate initial try,
kinda working,video clone,height rotate add,

August-28-2025 : left rotate bug-video, comments -height,Segment tree stage set,stage change video,construct tree success,query works only for node interval or 0,no,full,partial overlap gemini,
update try,gemini optimised perf,level order memory exceed,gemini help empty root,

August-30-2025 : average good,zigzag good,level order 2,next confuse,tried debug in local,video correct,
right view,cousins 3 func confuse,siblings video node find- gemini help,

August-31-2025 : symmetric video easy,diameter-height,max wrong,using constructor,using global,invert tree easy,max depth easy,insert sorted-binary insert 2 func,flatten tree logic one take,validate half pass,low high strike video,code confuse,finally video and gemini copy,

September-1-2025 : ancestor video copy,kth small extra list,extra count video use self,tree from inorder preorder,serialize,deserialize skip,path,partial work,video add easy-leaf check,totalsum right half works,pathsum self.ans perfect,video return ans time faster,max path sum-negative node fail,cases cover still fails,finally gemini coded easily,Heap given a try with upheap downheap, need to debug,corrected upheap, down index??,

September-2-2025 : downheap corrected by debug,hashmap theory,gfg hld lld,langgraph-ipynb,neo4j,graph copy gfg,

3,4- bfs,dfs,topo,mst,kruskal-union find,prim-heap

September-5-2025 : graph matrix try,graphlist try empty print,error need to fix,

September-6-2025 : graph list working,module init file no use,bfs stage,halfway in bfs,BFS working fine,
dfs stack try break visited-fix,for else works-dfs stack,corrected dfs approach,dfs using rec,used set instead of index,topo outdegree,indegree,efficient using dict,topo try with dfs cycle??,sorting but can't detect cycle,topo khan - fail,not used queue, topodfs cycle extra rec st set skip.//Kruskal- all edges double,unique edges gemini,w3schools similar,room key fail

September-7-2025 : Union Find- no idea- parent array,tried after video,working inefficient detect cycle,
find return miss,path compression,union by rank robust,gemini video,kruskal-vertex to index gemini copy,uses enumerate, sorted and dict,Eclipse- Prims, Gemini video explain-mst,parent,key,heap delete, using vertex confused,

September-8-2025 : matrix try,gemini like list,

September-9-2025 : bfs try,ans ok but in numbers,perfect bfs,dfs stack and rec success,topo easy but cycle cofuses skip,skipped in list too???,khan list gemini fail,indegree out degree good,gemini easy khan for matrix,import confuse,

September-10-2025 : env var - PYTHON

September-11-2025 : kruskal sort edges,implemented own,prims try-start neighbour heap queue weight,copy from list working,vertex to index,

September-12-2025 : Dijstra try half,matrix implemented heap visited no use,path print last miss,using loop print path, modified dijstra for list,works for negative,Bellman Ford- N^2 and negative,half try,
gemini copy,

September-14-2025 : Leetcode,courses try,copy gem sleepy,

September-15-2025 : prove assignment,provinces debug and fixed,visit all rooms debug,problems skip,judge indegree outdegree,Floyd Warshall,N\*N matrix,algo good,problem modify success,dijstra confuse using 1-n,
bug in adj,corrected to lc,bellman try half fail,i==j remove works still confused,

September-18-2025 : DP,Fibo,2^n -- n,list to dict,tabulation but not rec relation,0/1 Knapsack intro

September-19-2025 : Subset variations,code rec 0/1 Knapsack,added memo,table without loop,loop ans wrong,
