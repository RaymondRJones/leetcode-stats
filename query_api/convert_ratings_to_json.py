import json

# Assuming the data is structured as in the provided sample, separated by tabs
data = """
Rating	ID	Title	Title ZH	Title Slug	Contest Slug	Problem Index
3111.1274320356	3049	Earliest Second to Mark Indices II	标记所有下标的最早秒数 II	earliest-second-to-mark-indices-ii	weekly-contest-386	Q4
3039.3003256659	3003	Maximize the Number of Partitions After Operations	执行操作后的最大分割数量	maximize-the-number-of-partitions-after-operations	weekly-contest-379	Q4
3018.4940165727	1719	Number Of Ways To Reconstruct A Tree	重构一棵树的方案数	number-of-ways-to-reconstruct-a-tree	biweekly-contest-43	Q4
2978.7961959355	2809	Minimum Time to Make Array Sum At Most x	使数组和小于等于 x 的最少时间	minimum-time-to-make-array-sum-at-most-x	biweekly-contest-110	Q4
2943.2173551759	2945	Find Maximum Non-decreasing Array Length	找到最大非递减数组的长度	find-maximum-non-decreasing-array-length	biweekly-contest-118	Q4
2917.8273567322	3022	Minimize OR of Remaining Elements Using Operations	给定操作次数内使剩余元素的或值最小	minimize-or-of-remaining-elements-using-operations	weekly-contest-382	Q4
2873.9745576413	2699	Modify Graph Edge Weights	修改图中的边权	modify-graph-edge-weights	weekly-contest-346	Q4
2872.0290327119	1982	Find Array Given Subset Sums	从子集的和还原数组	find-array-given-subset-sums	weekly-contest-255	Q4
2863.1378294349	770	Basic Calculator IV	基本计算器 IV	basic-calculator-iv	weekly-contest-68	Q5
2857.6543956169	2851	String Transformation	字符串转换	string-transformation	weekly-contest-362	Q4
2849.4841858619	1728	Cat and Mouse II	猫和老鼠 II	cat-and-mouse-ii	weekly-contest-224	Q4
2824.4551372454	2612	Minimum Reverse Operations	最少翻转操作数	minimum-reverse-operations	weekly-contest-339	Q4
2817.2672126020	1977	Number of Ways to Separate Numbers	划分数字的方案数	number-of-ways-to-separate-numbers	biweekly-contest-59	Q4
2816.0706257586	2916	Subarrays Distinct Element Sum of Squares II	子数组不同元素数目的平方和 II	subarrays-distinct-element-sum-of-squares-ii	biweekly-contest-116	Q4
2803.7652028979	2060	Check if an Original String Exists Given Two Encoded Strings	同源字符串检测	check-if-an-original-string-exists-given-two-encoded-strings	weekly-contest-265	Q4
2779.7855167601	2983	Palindrome Rearrangement Queries	回文串重新排列查询	palindrome-rearrangement-queries	weekly-contest-378	Q4
2768.8154223451	2836	Maximize Value of Function in a Ball Passing Game	在传球游戏中最大化函数值	maximize-value-of-function-in-a-ball-passing-game	weekly-contest-360	Q4
2765.2533837781	803	Bricks Falling When Hit	打砖块	bricks-falling-when-hit	weekly-contest-76	Q4
2758.9704056427	2902	Count of Sub-Multisets With Bounded Sum	和带限制的子多重集合的数目	count-of-sub-multisets-with-bounded-sum	biweekly-contest-115	Q4
2711.8717381409	2603	Collect Coins in a Tree	收集树中金币	collect-coins-in-a-tree	weekly-contest-338	Q4
2709.4067070911	3017	Count the Number of Houses at a Certain Distance II	按距离统计房屋对数目 II	count-the-number-of-houses-at-a-certain-distance-ii	weekly-contest-381	Q4
2695.8096670460	2977	Minimum Cost to Convert String II	转换字符串的最小成本 II	minimum-cost-to-convert-string-ii	weekly-contest-377	Q4
2690.5859406179	1960	Maximum Product of the Length of Two Palindromic Substrings	两个回文子字符串长度的最大乘积	maximum-product-of-the-length-of-two-palindromic-substrings	biweekly-contest-58	Q4
2681.7054310332	2573	Find the String with LCP	找出对应 LCP 矩阵的字符串	find-the-string-with-lcp	weekly-contest-333	Q4
2677.1682592316	2791	Count Paths That Can Form a Palindrome in a Tree	树中可以形成回文的路径数	count-paths-that-can-form-a-palindrome-in-a-tree	weekly-contest-355	Q4
2666.6681508450	1397	Find All Good Strings	找到所有好字符串	find-all-good-strings	weekly-contest-182	Q4
2661.0670044656	1923	Longest Common Subpath	最长公共子路径	longest-common-subpath	weekly-contest-248	Q4
2655.2178711909	1659	Maximize Grid Happiness	最大化网格幸福感	maximize-grid-happiness	weekly-contest-215	Q4
2650.8996457642	2097	Valid Arrangement of Pairs	合法重新排列数对	valid-arrangement-of-pairs	weekly-contest-270	Q4
2648.1748409542	2071	Maximum Number of Tasks You Can Assign	你可以安排的最多任务数目	maximum-number-of-tasks-you-can-assign	biweekly-contest-65	Q4
2647.8258771458	2386	Find the K-Sum of an Array	找出数组的第 K 大和	find-the-k-sum-of-an-array	weekly-contest-307	Q4
2644.8498152558	2954	Count the Number of Infection Sequences	统计感冒序列的数目	count-the-number-of-infection-sequences	weekly-contest-374	Q4
2640.3824813624	1787	Make the XOR of All Segments Equal to Zero	使所有区间的异或结果为零	make-the-xor-of-all-segments-equal-to-zero	weekly-contest-231	Q4
2633.0144045478	2499	Minimum Total Cost to Make Arrays Unequal	让数组不相等的最小总代价	minimum-total-cost-to-make-arrays-unequal	biweekly-contest-93	Q4
2628.7957821141	2213	Longest Substring of One Repeating Character	由单个字符重复的最长子字符串	longest-substring-of-one-repeating-character	weekly-contest-285	Q4
2621.1208072273	2281	Sum of Total Strength of Wizards	巫师的总力量和	sum-of-total-strength-of-wizards	weekly-contest-294	Q4
2620.4181842249	1830	Minimum Number of Operations to Make String Sorted	使字符串有序的最少操作次数	minimum-number-of-operations-to-make-string-sorted	biweekly-contest-50	Q4
2619.7016189999	2790	Maximum Number of Groups With Increasing Length	长度递增组的最大数目	maximum-number-of-groups-with-increasing-length	weekly-contest-355	Q3
2615.1468269481	2338	Count the Number of Ideal Arrays	统计理想数组的数目	count-the-number-of-ideal-arrays	weekly-contest-301	Q4
2610.9906730644	2056	Number of Valid Move Combinations On Chessboard	棋盘上有效移动组合的数目	number-of-valid-move-combinations-on-chessboard	biweekly-contest-64	Q4
2610.0826855063	1687	Delivering Boxes from Storage to Ports	从仓库到码头运输箱子	delivering-boxes-from-storage-to-ports	biweekly-contest-41	Q4
2607.9418744903	2911	Minimum Changes to Make K Semi-palindromes	得到 K 个半回文串的最少修改次数	minimum-changes-to-make-k-semi-palindromes	weekly-contest-368	Q4
2594.1356734520	964	Least Operators to Express Number	表示数字的最少运算符	least-operators-to-express-number	weekly-contest-116	Q4
2588.8752130913	2532	Time to Cross a Bridge	过桥的时间	time-to-cross-a-bridge	weekly-contest-327	Q4
2587.8725248485	1883	Minimum Skips to Arrive at Meeting On Time	准时抵达会议现场的最小跳过休息次数	minimum-skips-to-arrive-at-meeting-on-time	weekly-contest-243	Q4
2583.9006314254	2019	The Score of Students Solving Math Expression	解出数学表达式的学生分数	the-score-of-students-solving-math-expression	weekly-contest-260	Q4
2583.4069119510	936	Stamping The Sequence	戳印序列	stamping-the-sequence	weekly-contest-109	Q4
2582.0814855506	2813	Maximum Elegance of a K-Length Subsequence	子序列最大优雅度	maximum-elegance-of-a-k-length-subsequence	weekly-contest-357	Q4
2581.9961985753	2617	Minimum Number of Visited Cells in a Grid	网格图中最少访问的格子数	minimum-number-of-visited-cells-in-a-grid	weekly-contest-340	Q4
2575.9570281316	1531	String Compression II	压缩字符串 II	string-compression-ii	weekly-contest-199	Q4
2571.5520281210	1489	Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree	找到最小生成树里的关键边和伪关键边	find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree	weekly-contest-194	Q4
2566.5910742837	913	Cat and Mouse	猫和老鼠	cat-and-mouse	weekly-contest-104	Q4
2561.7794931859	2030	Smallest K-Length Subsequence With Occurrences of a Letter	含特定字母的最小子序列	smallest-k-length-subsequence-with-occurrences-of-a-letter	weekly-contest-261	Q4
2561.5081492160	2234	Maximum Total Beauty of the Gardens	花园的最大总美丽值	maximum-total-beauty-of-the-gardens	weekly-contest-288	Q4
2559.4351004238	1815	Maximum Number of Groups Getting Fresh Donuts	得到新鲜甜甜圈的最多组数	maximum-number-of-groups-getting-fresh-donuts	biweekly-contest-49	Q4
2558.3297484354	2014	Longest Subsequence Repeated k Times	重复 K 次的最长子序列	longest-subsequence-repeated-k-times	weekly-contest-259	Q4
2540.4381507360	3013	Divide an Array Into Subarrays With Minimum Cost II	将数组分成最小总代价的子数组 II	divide-an-array-into-subarrays-with-minimum-cost-ii	biweekly-contest-122	Q4
2539.8637263970	1819	Number of Different Subsequences GCDs	序列中不同最大公约数的数目	number-of-different-subsequences-gcds	weekly-contest-235	Q4
2537.7965575726	1595	Minimum Cost to Connect Two Groups of Points	连通两组点的最小成本	minimum-cost-to-connect-two-groups-of-points	weekly-contest-207	Q4
2533.7796160302	1948	Delete Duplicate Folders in System	删除系统中的重复文件夹	delete-duplicate-folders-in-system	weekly-contest-251	Q4
2533.3027905062	1675	Minimize Deviation in Array	数组的最小偏移量	minimize-deviation-in-array	weekly-contest-217	Q4
2533.2830157959	2736	Maximum Sum Queries	最大和查询	maximum-sum-queries	weekly-contest-349	Q4
2531.6452775023	1896	Minimum Cost to Change the Final Value of Expression	反转表达式值的最少操作次数	minimum-cost-to-change-the-final-value-of-expression	biweekly-contest-54	Q4
2530.6905139914	1776	Car Fleet II	车队 II	car-fleet-ii	weekly-contest-230	Q4
2529.5251086936	1632	Rank Transform of a Matrix	矩阵转换后的秩	rank-transform-of-a-matrix	weekly-contest-212	Q4
2517.6829964848	2040	Kth Smallest Product of Two Sorted Arrays	两个有序数组的第 K 小乘积	kth-smallest-product-of-two-sorted-arrays	biweekly-contest-63	Q4
2515.7520586008	2272	Substring With Largest Variance	最大波动的子字符串	substring-with-largest-variance	biweekly-contest-78	Q4
2507.9960044659	2846	Minimum Edge Weight Equilibrium Queries in a Tree	边权重均等查询	minimum-edge-weight-equilibrium-queries-in-a-tree	weekly-contest-361	Q4
2502.5176603922	1938	Maximum Genetic Difference Query	查询最大基因差	maximum-genetic-difference-query	weekly-contest-250	Q4
2499.5640490579	1735	Count Ways to Make Array With Product	生成乘积数组的方案数	count-ways-to-make-array-with-product	biweekly-contest-44	Q4
2499.3282271507	2157	Groups of Strings	字符串分组	groups-of-strings	weekly-contest-278	Q4
2489.6652421066	2035	Partition Array Into Two Arrays to Minimize Sum Difference	将数组分成两个数组并最小化数组和的差	partition-array-into-two-arrays-to-minimize-sum-difference	weekly-contest-262	Q4
2486.2339675701	1916	Count Ways to Build Rooms in an Ant Colony	统计为蚁群构筑房间的不同顺序	count-ways-to-build-rooms-in-an-ant-colony	weekly-contest-247	Q4
2483.9435767299	1932	Merge BSTs to Create Single BST	合并多棵二叉搜索树	merge-bsts-to-create-single-bst	weekly-contest-249	Q4
2481.8722909195	2289	Steps to Make Array Non-decreasing	使数组按非递减顺序排列	steps-to-make-array-non-decreasing	weekly-contest-295	Q3
2481.7175364169	1330	Reverse Subarray To Maximize Array Value	翻转子数组得到最大的数组值	reverse-subarray-to-maximize-array-value	biweekly-contest-18	Q4
2479.3282985529	1803	Count Pairs With XOR in a Range	统计异或值在范围内的数对有多少	count-pairs-with-xor-in-a-range	weekly-contest-233	Q4
2476.7727985927	2117	Abbreviating the Product of a Range	一个区间内所有数乘积的缩写	abbreviating-the-product-of-a-range	biweekly-contest-68	Q4
2476.4517642870	1622	Fancy Sequence	奇妙序列	fancy-sequence	biweekly-contest-37	Q4
2470.2118194809	2286	Booking Concert Tickets in Groups	以组为单位订音乐会的门票	booking-concert-tickets-in-groups	biweekly-contest-79	Q4
2466.8891773908	1703	Minimum Adjacent Swaps for K Consecutive Ones	得到连续 K 个 1 的最少相邻交换次数	minimum-adjacent-swaps-for-k-consecutive-ones	biweekly-contest-42	Q4
2464.5077611012	1994	The Number of Good Subsets	好子集的数目	the-number-of-good-subsets	biweekly-contest-60	Q4
2460.3152437576	2440	Create Components With Same Value	创建价值相同的连通块	create-components-with-same-value	biweekly-contest-89	Q4
2457.1155741860	1782	Count Pairs Of Nodes	统计点对的数目	count-pairs-of-nodes	biweekly-contest-47	Q4
2456.3900212097	1499	Max Value of Equation	满足不等式的最大值	max-value-of-equation	weekly-contest-195	Q4
2455.8244137907	1040	Moving Stones Until Consecutive II	移动石子直到连续 II	moving-stones-until-consecutive-ii	weekly-contest-135	Q4
2454.7653333657	1900	The Earliest and Latest Rounds Where Players Compete	最佳运动员的比拼回合	the-earliest-and-latest-rounds-where-players-compete	weekly-contest-245	Q4
2453.9054896968	2463	Minimum Total Distance Traveled	最小移动总距离	minimum-total-distance-traveled	weekly-contest-318	Q4
2449.3352959316	2953	Count Complete Substrings	统计完全子字符串	count-complete-substrings	weekly-contest-374	Q3
2449.1323757838	2127	Maximum Employees to Be Invited to a Meeting	参加会议的最多员工数	maximum-employees-to-be-invited-to-a-meeting	weekly-contest-274	Q4
2448.4455464535	2926	Maximum Balanced Subsequence Sum	平衡子序列的最大和	maximum-balanced-subsequence-sum	weekly-contest-370	Q4
2444.7192647604	2949	Count Beautiful Substrings II	统计美丽子字符串 II	count-beautiful-substrings-ii	weekly-contest-373	Q4
2444.6660756903	2421	Number of Good Paths	好路径的数目	number-of-good-paths	weekly-contest-312	Q4
2444.2791027022	2968	Apply Operations to Maximize Frequency Score	执行操作使频率分数最大	apply-operations-to-maximize-frequency-score	weekly-contest-376	Q4
2439.7337408636	1872	Stone Game VIII	石子游戏 VIII	stone-game-viii	weekly-contest-242	Q4
2433.3767704629	903	Valid Permutations for DI Sequence	DI 序列的有效排列	valid-permutations-for-di-sequence	weekly-contest-101	Q4
2432.7133991110	2552	Count Increasing Quadruplets	统计上升四元组	count-increasing-quadruplets	weekly-contest-330	Q4
2432.4146343542	2565	Subsequence With the Minimum Score	最少得分子序列	subsequence-with-the-minimum-score	weekly-contest-332	Q4
2429.6705422448	782	Transform to Chessboard	变为棋盘	transform-to-chessboard	weekly-contest-71	Q4
2429.0940568399	1998	GCD Sort of an Array	数组的最大公因数排序	gcd-sort-of-an-array	weekly-contest-257	Q4
2428.7985254341	1044	Longest Duplicate Substring	最长重复子串	longest-duplicate-substring	weekly-contest-136	Q4
2428.3242593838	2867	Count Valid Paths in a Tree	统计树中的合法路径数目	count-valid-paths-in-a-tree	weekly-contest-364	Q4
2424.6761561972	2742	Painting the Walls	给墙壁刷油漆	painting-the-walls	weekly-contest-350	Q4
2422.5309771173	1000	Minimum Cost to Merge Stones	合并石头的最低成本	minimum-cost-to-merge-stones	weekly-contest-126	Q4
2422.3128048015	1987	Number of Unique Good Subsequences	不同的好子序列数目	number-of-unique-good-subsequences	weekly-contest-256	Q4
2419.5791089724	2572	Count the Number of Square-Free Subsets	无平方子集计数	count-the-number-of-square-free-subsets	weekly-contest-333	Q3
2418.5742747632	1203	Sort Items by Groups Respecting Dependencies	项目管理	sort-items-by-groups-respecting-dependencies	weekly-contest-155	Q4
2415.7434855724	2663	Lexicographically Smallest Beautiful String	字典序最小的美丽字符串	lexicographically-smallest-beautiful-string	weekly-contest-343	Q4
2415.2802039252	2493	Divide Nodes Into the Maximum Number of Groups	将节点分成尽可能多的组	divide-nodes-into-the-maximum-number-of-groups	weekly-contest-322	Q4
2415.0089731911	2003	Smallest Missing Genetic Value in Each Subtree	每棵子树内缺失的最小基因值	smallest-missing-genetic-value-in-each-subtree	weekly-contest-258	Q4
2414.6227484407	2518	Number of Great Partitions	好分区的数目	number-of-great-partitions	weekly-contest-325	Q4
2413.3969129689	1928	Minimum Cost to Reach Destination in Time	规定时间内到达终点的最小花费	minimum-cost-to-reach-destination-in-time	biweekly-contest-56	Q4
2409.7580728676	1388	Pizza With 3n Slices	3n 块披萨	pizza-with-3n-slices	biweekly-contest-22	Q4
2405.3375364501	2747	Count Zero Request Servers	统计没有收到请求的服务器数目	count-zero-request-servers	biweekly-contest-107	Q4
2399.5729141925	920	Number of Music Playlists	播放列表的数量	number-of-music-playlists	weekly-contest-105	Q4
2397.9722495587	2538	Difference Between Maximum and Minimum Price Sum	最大价值和与最小价值和的差值	difference-between-maximum-and-minimum-price-sum	weekly-contest-328	Q4
2397.8728428256	2569	Handling Sum Queries After Update	更新数组后处理求和查询	handling-sum-queries-after-update	biweekly-contest-98	Q4
2396.6770372863	2818	Apply Operations to Maximize Score	操作使得分最大	apply-operations-to-maximize-score	weekly-contest-358	Q4
2396.6267778669	808	Soup Servings	分汤	soup-servings	weekly-contest-78	Q3
2395.8765531206	1825	Finding MK Average	求出 MK 平均值	finding-mk-average	weekly-contest-236	Q4
2392.0799451298	2172	Maximum AND Sum of Array	数组的最大与和	maximum-and-sum-of-array	weekly-contest-280	Q4
2391.8086687918	818	Race Car	赛车	race-car	weekly-contest-80	Q4
2391.6572707330	2322	Minimum Score After Removals on a Tree	从树中删除边的最小分数	minimum-score-after-removals-on-a-tree	weekly-contest-299	Q4
2389.9634276167	1681	Minimum Incompatibility	最小不兼容性	minimum-incompatibility	weekly-contest-218	Q4
2387.3525635254	2713	Maximum Strictly Increasing Cells in a Matrix	矩阵中严格递增的单元格数	maximum-strictly-increasing-cells-in-a-matrix	weekly-contest-347	Q4
2385.8072128533	1349	Maximum Students Taking Exam	参加考试的最大学生数	maximum-students-taking-exam	weekly-contest-175	Q4
2383.7724811656	1521	Find a Value of a Mysterious Function Closest to Target	找到最接近目标值的函数值	find-a-value-of-a-mysterious-function-closest-to-target	weekly-contest-198	Q4
2381.6255832890	2577	Minimum Time to Visit a Cell In a Grid	在网格图中访问一个格子的最少时间	minimum-time-to-visit-a-cell-in-a-grid	weekly-contest-334	Q4
2381.6019709166	2468	Split Message Based on Limit	根据限制分割消息	split-message-based-on-limit	biweekly-contest-91	Q4
2381.4790248580	956	Tallest Billboard	最高的广告牌	tallest-billboard	weekly-contest-114	Q4
2381.2160234811	2334	Subarray With Elements Greater Than Varying Threshold	元素值大于变化阈值的子数组	subarray-with-elements-greater-than-varying-threshold	biweekly-contest-82	Q4
2380.5983169295	2589	Minimum Time to Complete All Tasks	完成所有任务的最少时间	minimum-time-to-complete-all-tasks	weekly-contest-336	Q4
2378.6234112504	757	Set Intersection Size At Least Two	设置交集大小至少为2	set-intersection-size-at-least-two	weekly-contest-65	Q4
2377.3895801187	854	K-Similar Strings	相似度为 K 的字符串	k-similar-strings	weekly-contest-89	Q4
2376.8658923518	887	Super Egg Drop	鸡蛋掉落	super-egg-drop	weekly-contest-97	Q4
2374.1850487395	1840	Maximum Building Height	最高建筑高度	maximum-building-height	weekly-contest-238	Q4
2368.6674771307	2556	Disconnect Path in a Binary Matrix by at Most One Flip	二进制矩阵中翻转最多一次使路径不连通	disconnect-path-in-a-binary-matrix-by-at-most-one-flip	biweekly-contest-97	Q4
2367.4705934718	2801	Count Stepping Numbers in Range	统计范围内的步进数字数目	count-stepping-numbers-in-range	weekly-contest-356	Q4
2366.7099607655	1183	Maximum Number of Ones	矩阵中 1 的最大数量	maximum-number-of-ones	biweekly-contest-8	Q4
2364.3930657709	2132	Stamping the Grid	用邮票贴满网格图	stamping-the-grid	biweekly-contest-69	Q4
2364.3455634374	2203	Minimum Weighted Subgraph With the Required Paths	得到要求路径的最小带权子图	minimum-weighted-subgraph-with-the-required-paths	weekly-contest-284	Q4
2363.5096568214	1755	Closest Subsequence Sum	最接近目标值的子序列和	closest-subsequence-sum	weekly-contest-227	Q4
2363.0240184484	2312	Selling Pieces of Wood	卖木头块	selling-pieces-of-wood	weekly-contest-298	Q4
2362.6480880348	1520	Maximum Number of Non-Overlapping Substrings	最多的不重叠子字符串	maximum-number-of-non-overlapping-substrings	weekly-contest-198	Q3
2358.9669560824	1707	Maximum XOR With an Element From Array	与数组中元素的最大异或值	maximum-xor-with-an-element-from-array	weekly-contest-221	Q4
2356.5811122453	1467	Probability of a Two Boxes Having The Same Number of Distinct Balls	两个盒子中球的颜色数相同的概率	probability-of-a-two-boxes-having-the-same-number-of-distinct-balls	weekly-contest-191	Q4
2354.5411153127	2719	Count of Integers	统计整数数目	count-of-integers	weekly-contest-348	Q4
2351.2293628792	2999	Count the Number of Powerful Integers	统计强大整数的数目	count-the-number-of-powerful-integers	biweekly-contest-121	Q4
2350.9694374861	1713	Minimum Operations to Make a Subsequence	得到子序列的最少操作次数	minimum-operations-to-make-a-subsequence	weekly-contest-222	Q4
2350.7421492104	2920	Maximum Points After Collecting Coins From All Nodes	收集所有金币可获得的最大积分	maximum-points-after-collecting-coins-from-all-nodes	weekly-contest-369	Q4
2350.0380300939	837	New 21 Game	新21点	new-21-game	weekly-contest-85	Q3
2348.7273357105	2935	Maximum Strong Pair XOR II	找出强数对的最大异或值 II	maximum-strong-pair-xor-ii	weekly-contest-371	Q4
2348.5159376523	1096	Brace Expansion II	花括号展开 II	brace-expansion-ii	weekly-contest-142	Q4
2346.5717839654	2258	Escape the Spreading Fire	逃离火灾	escape-the-spreading-fire	biweekly-contest-77	Q4
2345.3418191684	1611	Minimum One Bit Operations to Make Integers Zero	使整数变为 0 的最少操作次数	minimum-one-bit-operations-to-make-integers-zero	weekly-contest-209	Q4
2344.3664724791	2478	Number of Beautiful Partitions	完美分割的方案数	number-of-beautiful-partitions	weekly-contest-320	Q4
2341.4506355884	810	Chalkboard XOR Game	黑板异或游戏	chalkboard-xor-game	weekly-contest-78	Q4
2336.5210003185	1505	Minimum Possible Integer After at Most K Adjacent Swaps On Digits	最多 K 次交换相邻数位后得到的最小整数	minimum-possible-integer-after-at-most-k-adjacent-swaps-on-digits	weekly-contest-196	Q4
2333.2401505813	1674	Minimum Moves to Make Array Complementary	使数组互补的最少操作次数	minimum-moves-to-make-array-complementary	weekly-contest-217	Q3
2333.0621537307	1866	Number of Ways to Rearrange Sticks With K Sticks Visible	恰有 K 根木棍可以看到的排列数目	number-of-ways-to-rearrange-sticks-with-k-sticks-visible	weekly-contest-241	Q4
2333.0078041754	1585	Check If String Is Transformable With Substring Sort Operations	检查字符串是否可以通过排序子字符串得到另一个字符串	check-if-string-is-transformable-with-substring-sort-operations	weekly-contest-206	Q4
2328.4294689238	882	Reachable Nodes In Subdivided Graph	细分图中的可到达结点	reachable-nodes-in-subdivided-graph	weekly-contest-96	Q4
2327.5726642605	3045	Count Prefix and Suffix Pairs II	统计前后缀下标对 II	count-prefix-and-suffix-pairs-ii	weekly-contest-385	Q4
2327.4743300299	2940	Find Building Where Alice and Bob Can Meet	找到 Alice 和 Bob 可以相遇的建筑	find-building-where-alice-and-bob-can-meet	weekly-contest-372	Q4
2324.1192580053	2827	Number of Beautiful Integers in the Range	范围中美丽整数的数目	number-of-beautiful-integers-in-the-range	biweekly-contest-111	Q4
2315.6037017989	1187	Make Array Strictly Increasing	使数组严格递增	make-array-strictly-increasing	weekly-contest-153	Q4
2315.0547336936	2188	Minimum Time to Finish the Race	完成比赛的最少时间	minimum-time-to-finish-the-race	weekly-contest-282	Q4
2312.9919953644	1857	Largest Color Value in a Directed Graph	有向图中最大颜色值	largest-color-value-in-a-directed-graph	weekly-contest-240	Q4
2310.3824631335	1959	Minimum Total Space Wasted With K Resizing Operations	K 次调整数组大小浪费的最小总空间	minimum-total-space-wasted-with-k-resizing-operations	biweekly-contest-58	Q3
2308.6545905335	1617	Count Subtrees With Max Distance Between Cities	统计子树中城市之间最大距离	count-subtrees-with-max-distance-between-cities	weekly-contest-210	Q4
2307.0161713185	1655	Distribute Repeating Integers	分配重复整数	distribute-repeating-integers	biweekly-contest-39	Q4
2306.8472649456	862	Shortest Subarray with Sum at Least K	和至少为 K 的最短子数组	shortest-subarray-with-sum-at-least-k	weekly-contest-91	Q4
2305.4498281454	2306	Naming a Company	公司命名	naming-a-company	weekly-contest-297	Q4
2304.3094138939	2242	Maximum Score of a Node Sequence	节点序列的最大得分	maximum-score-of-a-node-sequence	biweekly-contest-76	Q4
2302.4005640818	2513	Minimize the Maximum of Two Arrays	最小化两个数组中的最大值	minimize-the-maximum-of-two-arrays	biweekly-contest-94	Q3
2301.4069974024	2897	Apply Operations on Array to Maximize Sum of Squares	对数组执行操作使平方和最大	apply-operations-on-array-to-maximize-sum-of-squares	weekly-contest-366	Q4
2300.1557840589	1697	Checking Existence of Edge Length Limited Paths	检查边长度限制的路径是否存在	checking-existence-of-edge-length-limited-paths	weekly-contest-220	Q4
2298.6242048519	2458	Height of Binary Tree After Subtree Removal Queries	移除子树后的二叉树高度	height-of-binary-tree-after-subtree-removal-queries	weekly-contest-317	Q4
2297.1053625160	1263	Minimum Moves to Move a Box to Their Target Location	推箱子	minimum-moves-to-move-a-box-to-their-target-location	weekly-contest-163	Q4
2294.8289305714	2858	Minimum Edge Reversals So Every Node Is Reachable	可以到达每一个节点的最少边反转次数	minimum-edge-reversals-so-every-node-is-reachable	biweekly-contest-113	Q4
2294.0981174197	932	Beautiful Array	漂亮数组	beautiful-array	weekly-contest-108	Q4
2292.1434666805	761	Special Binary String	特殊的二进制序列	special-binary-string	weekly-contest-66	Q4
2291.6794536377	2862	Maximum Element-Sum of a Complete Subset of Indices	完全子集的最大元素和	maximum-element-sum-of-a-complete-subset-of-indices	weekly-contest-363	Q4
2290.9040038639	1591	Strange Printer II	奇怪的打印机 II	strange-printer-ii	biweekly-contest-35	Q4
2288.2117442123	1569	Number of Ways to Reorder Array to Get Same BST	将子数组重新排序得到同一个二叉查找树的方案数	number-of-ways-to-reorder-array-to-get-same-bst	weekly-contest-204	Q4
2286.1378742318	1851	Minimum Interval to Include Each Query	包含每个查询的最小区间	minimum-interval-to-include-each-query	weekly-contest-239	Q4
2284.4463940346	1723	Find Minimum Time to Finish All Jobs	完成所有工作的最短时间	find-minimum-time-to-finish-all-jobs	weekly-contest-223	Q4
2281.8816902545	2659	Make Array Empty	将数组清空	make-array-empty	biweekly-contest-103	Q4
2280.3143643878	2407	Longest Increasing Subsequence II	最长递增子序列 II	longest-increasing-subsequence-ii	weekly-contest-310	Q4
2277.9557248587	3031	Minimum Time to Revert Word to Initial State II	将单词恢复初始状态所需的最短时间 II	minimum-time-to-revert-word-to-initial-state-ii	weekly-contest-383	Q4
2277.7923804151	2763	Sum of Imbalance Numbers of All Subarrays	所有子数组中不平衡数字之和	sum-of-imbalance-numbers-of-all-subarrays	weekly-contest-352	Q4
2277.3595662538	2029	Stone Game IX	石子游戏 IX	stone-game-ix	weekly-contest-261	Q3
2277.0238076464	749	Contain Virus	隔离病毒	contain-virus	weekly-contest-63	Q4
2276.9256951751	2973	Find Number of Coins to Place in Tree Nodes	树中每个节点放置的金币数目	find-number-of-coins-to-place-in-tree-nodes	biweekly-contest-120	Q4
2276.4233585631	1498	Number of Subsequences That Satisfy the Given Sum Condition	满足条件的子序列数目	number-of-subsequences-that-satisfy-the-given-sum-condition	weekly-contest-195	Q3
2275.7337818748	1606	Find Servers That Handled Most Number of Requests	找到处理最多请求的服务器	find-servers-that-handled-most-number-of-requests	biweekly-contest-36	Q4
2273.7910625337	753	Cracking the Safe	破解保险箱	cracking-the-safe	weekly-contest-64	Q4
2273.2215764545	1434	Number of Ways to Wear Different Hats to Each Other	每个人戴不同帽子的方案数	number-of-ways-to-wear-different-hats-to-each-other	biweekly-contest-25	Q4
2272.4412003208	2179	Count Good Triplets in an Array	统计数组中好三元组数目	count-good-triplets-in-an-array	biweekly-contest-72	Q4
2272.1122260637	952	Largest Component Size by Common Factor	按公因数计算最大组件大小	largest-component-size-by-common-factor	weekly-contest-113	Q4
2265.2118886972	2141	Maximum Running Time of N Computers	同时运行 N 台电脑的最长时间	maximum-running-time-of-n-computers	weekly-contest-276	Q4
2262.5641910108	3048	Earliest Second to Mark Indices I	标记所有下标的最早秒数 I	earliest-second-to-mark-indices-i	weekly-contest-386	Q3
2260.2799775623	1997	First Day Where You Have Been in All the Rooms	访问完所有房间的第一天	first-day-where-you-have-been-in-all-the-rooms	weekly-contest-257	Q3
2259.6572191969	857	Minimum Cost to Hire K Workers	雇佣 K 名工人的最低成本	minimum-cost-to-hire-k-workers	weekly-contest-90	Q4
2258.6371797452	864	Shortest Path to Get All Keys	获取所有钥匙的最短路径	shortest-path-to-get-all-keys	weekly-contest-92	Q4
2258.0069047781	3007	Maximum Number That Sum of the Prices Is Less Than or Equal to K	价值和小于等于 K 的最大数字	maximum-number-that-sum-of-the-prices-is-less-than-or-equal-to-k	weekly-contest-380	Q3
2250.9318291559	1125	Smallest Sufficient Team	最小的必要团队	smallest-sufficient-team	weekly-contest-145	Q4
2250.2578740769	1199	Minimum Time to Build Blocks	建造街区的最短时间	minimum-time-to-build-blocks	biweekly-contest-9	Q4
2250.0454791316	1307	Verbal Arithmetic Puzzle	口算难题	verbal-arithmetic-puzzle	weekly-contest-169	Q4
2246.8671174565	960	Delete Columns to Make Sorted III	删列造序 III	delete-columns-to-make-sorted-iii	weekly-contest-115	Q4
2246.0452639352	2183	Count Array Pairs Divisible by K	统计可以被 K 整除的下标对数目	count-array-pairs-divisible-by-k	weekly-contest-281	Q4
2241.5199974312	1240	Tiling a Rectangle with the Fewest Squares	铺瓷砖	tiling-a-rectangle-with-the-fewest-squares	weekly-contest-160	Q4
2239.7101856677	2732	Find a Good Subset of the Matrix	找到矩阵中的好子集	find-a-good-subset-of-the-matrix	biweekly-contest-106	Q4
2238.2830745228	2646	Minimize the Total Price of the Trips	最小化旅行的价格总和	minimize-the-total-price-of-the-trips	weekly-contest-341	Q4
2235.9672341699	850	Rectangle Area II	矩形面积 II	rectangle-area-ii	weekly-contest-88	Q4
2235.5784618885	2528	Maximize the Minimum Powered City	最大化城市的最小供电站数目	maximize-the-minimum-powered-city	biweekly-contest-95	Q4
2234.9191877602	1915	Number of Wonderful Substrings	最美子字符串的数目	number-of-wonderful-substrings	weekly-contest-247	Q3
2233.9639034080	1178	Number of Valid Words for Each Puzzle	猜字谜	number-of-valid-words-for-each-puzzle	weekly-contest-152	Q4
2231.8099102949	1766	Tree of Coprimes	互质树	tree-of-coprimes	biweekly-contest-46	Q4
2231.1942136357	3041	Maximize Consecutive Elements in an Array After Modification	修改数组后最大化数组中的连续元素数目	maximize-consecutive-elements-in-an-array-after-modification	biweekly-contest-124	Q4
2230.1673059455	1012	Numbers With Repeated Digits	至少有 1 位重复的数字	numbers-with-repeated-digits	weekly-contest-128	Q4
2228.3454693625	2581	Count Number of Possible Root Nodes	统计可能的树根数目	count-number-of-possible-root-nodes	biweekly-contest-99	Q4
2227.3896051956	2930	Number of Strings Which Can Be Rearranged to Contain Substring	重新排列后包含指定子字符串的字符串数目	number-of-strings-which-can-be-rearranged-to-contain-substring	biweekly-contest-117	Q3
2225.3877535768	2163	Minimum Difference in Sums After Removal of Elements	删除元素后和的最小差值	minimum-difference-in-sums-after-removal-of-elements	biweekly-contest-71	Q4
2223.1762282199	2484	Count Palindromic Subsequences	统计回文子序列数目	count-palindromic-subsequences	biweekly-contest-92	Q4
2222.4805422748	2276	Count Integers in Intervals	统计区间中的整数数目	count-integers-in-intervals	weekly-contest-293	Q4
2221.7931857140	2561	Rearranging Fruits	重排水果	rearranging-fruits	weekly-contest-331	Q4
2221.7336557442	1542	Find Longest Awesome Substring	找出最长的超赞子字符串	find-longest-awesome-substring	biweekly-contest-32	Q4
2221.3538766773	1627	Graph Connectivity With Threshold	带阈值的图连通性	graph-connectivity-with-threshold	weekly-contest-211	Q4
2220.8257124139	2543	Check if Point Is Reachable	判断一个点是否可以到达	check-if-point-is-reachable	biweekly-contest-96	Q4
2220.0903365738	2223	Sum of Scores of Built Strings	构造字符串的总得分和	sum-of-scores-of-built-strings	biweekly-contest-75	Q4
2219.3465296423	2167	Minimum Time to Remove All Cars Containing Illegal Goods	移除所有载有违禁货物车厢所需的最少时间	minimum-time-to-remove-all-cars-containing-illegal-goods	weekly-contest-279	Q4
2217.8090802563	2025	Maximum Number of Ways to Partition an Array	分割数组的最多方案数	maximum-number-of-ways-to-partition-an-array	biweekly-contest-62	Q4
2214.4798747386	1889	Minimum Space Wasted From Packaging	装包裹的最小浪费空间	minimum-space-wasted-from-packaging	weekly-contest-244	Q4
2210.3503183571	992	Subarrays with K Different Integers	K 个不同整数的子数组	subarrays-with-k-different-integers	weekly-contest-123	Q4
2209.8815936961	2081	Sum of k-Mirror Numbers	k 镜像数字的和	sum-of-k-mirror-numbers	weekly-contest-268	Q4
2209.8785430371	2876	Count Visited Nodes in a Directed Graph	有向图访问计数	count-visited-nodes-in-a-directed-graph	weekly-contest-365	Q4
2208.5532172086	1568	Minimum Number of Days to Disconnect Island	使陆地分离的最少天数	minimum-number-of-days-to-disconnect-island	weekly-contest-204	Q3
2207.8565809952	1649	Create Sorted Array through Instructions	通过指令创建有序数组	create-sorted-array-through-instructions	weekly-contest-214	Q4
2207.4917475411	2835	Minimum Operations to Form Subsequence With Target Sum	使子序列的和等于目标的最少操作次数	minimum-operations-to-form-subsequence-with-target-sum	weekly-contest-360	Q3
2205.4304373587	1157	Online Majority Element In Subarray	子数组中占绝大多数的元素	online-majority-element-in-subarray	weekly-contest-149	Q4
2204.3524370174	879	Profitable Schemes	盈利计划	profitable-schemes	weekly-contest-95	Q4
2203.5694828019	2781	Length of the Longest Valid Substring	最长合法子字符串的长度	length-of-the-longest-valid-substring	weekly-contest-354	Q4
2203.1738850937	1246	Palindrome Removal	删除回文子数组	palindrome-removal	biweekly-contest-12	Q4
2201.8209584221	1453	Maximum Number of Darts Inside of a Circular Dartboard	圆形靶内的最大飞镖数量	maximum-number-of-darts-inside-of-a-circular-dartboard	weekly-contest-189	Q4
2201.6219336792	2045	Second Minimum Time to Reach Destination	到达目的地的第二短时间	second-minimum-time-to-reach-destination	weekly-contest-263	Q4
2200.6623666057	847	Shortest Path Visiting All Nodes	访问所有节点的最短路径	shortest-path-visiting-all-nodes	weekly-contest-87	Q4
2198.4642973466	1739	Building Boxes	放置盒子	building-boxes	weekly-contest-225	Q4
2198.3290662783	1621	Number of Sets of K Non-Overlapping Line Segments	大小为 K 的不重叠线段的数目	number-of-sets-of-k-non-overlapping-line-segments	biweekly-contest-37	Q3
2197.0951445919	834	Sum of Distances in Tree	树中距离之和	sum-of-distances-in-tree	weekly-contest-84	Q4
2195.6540241654	2503	Maximum Number of Points From Grid Queries	矩阵查询可获得的最大分数	maximum-number-of-points-from-grid-queries	weekly-contest-323	Q4
2190.1757477854	1478	Allocate Mailboxes	安排邮筒	allocate-mailboxes	biweekly-contest-28	Q4
2189.3802630548	1074	Number of Submatrices That Sum to Target	元素和为目标值的子矩阵数量	number-of-submatrices-that-sum-to-target	weekly-contest-139	Q4
2185.5444704515	943	Find the Shortest Superstring	最短超级串	find-the-shortest-superstring	weekly-contest-111	Q4
2184.5241011615	1081	Smallest Subsequence of Distinct Characters	不同字符的最小子序列	smallest-subsequence-of-distinct-characters	weekly-contest-140	Q4
2182.6180030785	891	Sum of Subsequence Widths	子序列宽度之和	sum-of-subsequence-widths	weekly-contest-98	Q4
2182.0544529810	1771	Maximize Palindrome Length From Subsequences	由子序列构造的最长回文串的长度	maximize-palindrome-length-from-subsequences	weekly-contest-229	Q4
2181.7821188042	1912	Design Movie Rental System	设计电影租借系统	design-movie-rental-system	biweekly-contest-55	Q4
2178.4249114144	2065	Maximum Path Quality of a Graph	最大化一张图中的路径价值	maximum-path-quality-of-a-graph	weekly-contest-266	Q4
2175.7874705227	2768	Number of Black Blocks	黑格子的数目	number-of-black-blocks	biweekly-contest-108	Q4
2175.6850426027	1420	Build Array Where You Can Find The Maximum Exactly K Comparisons	生成数组	build-array-where-you-can-find-the-maximum-exactly-k-comparisons	weekly-contest-185	Q4
2175.1190473433	2454	Next Greater Element IV	下一个更大元素 IV	next-greater-element-iv	biweekly-contest-90	Q4
2172.3890687963	2896	Apply Operations to Make Two Strings Equal	执行操作使两个字符串相等	apply-operations-to-make-two-strings-equal	weekly-contest-366	Q3
2171.9645269732	2709	Greatest Common Divisor Traversal	最大公约数遍历	greatest-common-divisor-traversal	biweekly-contest-105	Q4
2171.7160666640	1691	Maximum Height by Stacking Cuboids 	堆叠长方体的最大高度	maximum-height-by-stacking-cuboids	weekly-contest-219	Q4
2170.1079846744	1862	Sum of Floored Pairs	向下取整数对和	sum-of-floored-pairs	biweekly-contest-52	Q4
2170.0439693714	1931	Painting a Grid With Three Different Colors	用三种不同颜色为网格涂色	painting-a-grid-with-three-different-colors	weekly-contest-249	Q3
2168.7531235448	786	K-th Smallest Prime Fraction	第 K 个最小的素数分数	k-th-smallest-prime-fraction	weekly-contest-72	Q4
2164.8287157213	1036	Escape a Large Maze	逃离大迷宫	escape-a-large-maze	weekly-contest-134	Q4
2159.4844281244	2584	Split the Array to Make Coprime Products	分割数组使乘积互质	split-the-array-to-make-coprime-products	weekly-contest-335	Q3
2158.8988728254	2122	Recover the Original Array	还原原数组	recover-the-original-array	weekly-contest-273	Q4
2158.7683843245	2102	Sequentially Ordinal Rank Tracker	序列顺序查询	sequentially-ordinal-rank-tracker	biweekly-contest-67	Q4
2157.5814371481	2218	Maximum Value of K Coins From Piles	从栈中取出 K 个硬币的最大面值和	maximum-value-of-k-coins-from-piles	weekly-contest-286	Q4
2156.9515428364	1515	Best Position for a Service Centre	服务中心的最佳位置	best-position-for-a-service-centre	weekly-contest-197	Q4
2155.3424932408	2616	Minimize the Maximum Difference of Pairs	最小化数对的最大差值	minimize-the-maximum-difference-of-pairs	weekly-contest-340	Q3
2153.8943791656	2662	Minimum Cost of a Path With Special Roads	前往目标的最小代价	minimum-cost-of-a-path-with-special-roads	weekly-contest-343	Q3
2153.5854429139	2812	Find the Safest Path in a Grid	找出最安全路径	find-the-safest-path-in-a-grid	weekly-contest-357	Q3
2152.8032001597	2972	Count the Number of Incremovable Subarrays II	统计移除递增子数组的数目 II	count-the-number-of-incremovable-subarrays-ii	biweekly-contest-120	Q3
2147.1828941776	1610	Maximum Number of Visible Points	可见点的最大数目	maximum-number-of-visible-points	weekly-contest-209	Q3
2146.6395819980	1906	Minimum Absolute Difference Queries	查询差绝对值的最小值	minimum-absolute-difference-queries	weekly-contest-246	Q4
2145.1839952670	1879	Minimum XOR Sum of Two Arrays	两个数组最小的异或值之和	minimum-xor-sum-of-two-arrays	biweekly-contest-53	Q4
2140.0220703954	906	Super Palindromes	超级回文数	super-palindromes	weekly-contest-102	Q4
2137.5633267453	2290	Minimum Obstacle Removal to Reach Corner	到达角落需要移除障碍物的最小数目	minimum-obstacle-removal-to-reach-corner	weekly-contest-295	Q4
2136.3013259524	2382	Maximum Segment Sum After Removals	删除操作后的最大子段和	maximum-segment-sum-after-removals	biweekly-contest-85	Q4
2135.5738659086	959	Regions Cut By Slashes	由斜杠划分区域	regions-cut-by-slashes	weekly-contest-115	Q3
2134.5448970405	910	Smallest Range II	最小差值 II	smallest-range-ii	weekly-contest-103	Q3
2133.9592509012	1439	Find the Kth Smallest Sum of a Matrix With Sorted Rows	有序矩阵中的第 k 个最小数组和	find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows	weekly-contest-187	Q4
2133.1003195919	898	Bitwise ORs of Subarrays	子数组按位或操作	bitwise-ors-of-subarrays	weekly-contest-100	Q3
2132.1944636902	2910	Minimum Number of Groups to Create a Valid Assignment	合法分组的最少组数	minimum-number-of-groups-to-create-a-valid-assignment	weekly-contest-368	Q3
2132.0623345900	2749	Minimum Operations to Make the Integer Zero	得到整数零需要执行的最少操作数	minimum-operations-to-make-the-integer-zero	weekly-contest-351	Q2
2131.7917160422	1579	Remove Max Number of Edges to Keep Graph Fully Traversable	保证图可完全遍历	remove-max-number-of-edges-to-keep-graph-fully-traversable	weekly-contest-205	Q4
2130.9348604091	2076	Process Restricted Friend Requests	处理含限制条件的好友请求	process-restricted-friend-requests	weekly-contest-267	Q4
2130.1135718486	1039	Minimum Score Triangulation of Polygon	多边形三角剖分的最低得分	minimum-score-triangulation-of-polygon	weekly-contest-135	Q3
2129.7051442916	798	Smallest Rotation with Highest Score	得分最高的最小轮调	smallest-rotation-with-highest-score	weekly-contest-75	Q4
2127.5100545681	2939	Maximum Xor Product	最大异或乘积	maximum-xor-product	weekly-contest-372	Q3
2126.6864346508	1444	Number of Ways of Cutting a Pizza	切披萨的方案数	number-of-ways-of-cutting-a-pizza	weekly-contest-188	Q4
2126.3922279277	2246	Longest Path With Different Adjacent Characters	相邻字符不同的最长路径	longest-path-with-different-adjacent-characters	weekly-contest-289	Q4
2126.1931814161	2746	Decremental String Concatenation	字符串连接删减字母	decremental-string-concatenation	biweekly-contest-107	Q3
2125.3125624762	1955	Count Number of Special Subsequences	统计特殊子序列的数目	count-number-of-special-subsequences	weekly-contest-252	Q4
2124.1329592058	968	Binary Tree Cameras	监控二叉树	binary-tree-cameras	weekly-contest-117	Q4
2124.0317207867	1654	Minimum Jumps to Reach Home	到家的最少跳跃次数	minimum-jumps-to-reach-home	biweekly-contest-39	Q3
2123.5708982185	1970	Last Day Where You Can Still Cross	你能穿过矩阵的最后一天	last-day-where-you-can-still-cross	weekly-contest-254	Q4
2121.3147151648	972	Equal Rational Numbers	相等的有理数	equal-rational-numbers	weekly-contest-118	Q4
2120.4466386371	2376	Count Special Integers	统计特殊整数	count-special-integers	weekly-contest-306	Q4
2118.7923652824	1601	Maximum Number of Achievable Transfer Requests	最多可达成的换楼请求数目	maximum-number-of-achievable-transfer-requests	weekly-contest-208	Q4
2116.4935282950	1547	Minimum Cost to Cut a Stick	切棍子的最小成本	minimum-cost-to-cut-a-stick	weekly-contest-201	Q4
2116.3244842355	2967	Minimum Cost to Make Array Equalindromic	使数组成为等数数组的最小代价	minimum-cost-to-make-array-equalindromic	weekly-contest-376	Q3
2115.0911494487	1483	Kth Ancestor of a Tree Node	树节点的第 K 个祖先	kth-ancestor-of-a-tree-node	weekly-contest-193	Q4
2109.9830154953	1172	Dinner Plate Stacks	餐盘栈	dinner-plate-stacks	weekly-contest-151	Q4
2105.8582288624	2209	Minimum White Tiles After Covering With Carpets	用地毯覆盖后的最少白色砖块	minimum-white-tiles-after-covering-with-carpets	biweekly-contest-74	Q4
2105.7761215397	1937	Maximum Number of Points with Cost	扣分后的最大得分	maximum-number-of-points-with-cost	weekly-contest-250	Q3
2104.9526046945	1944	Number of Visible People in a Queue	队列中可以看到的人数	number-of-visible-people-in-a-queue	biweekly-contest-57	Q4
2104.7441214305	2088	Count Fertile Pyramids in a Land	统计农场中肥沃金字塔的数目	count-fertile-pyramids-in-a-land	biweekly-contest-66	Q4
2101.8673420040	2430	Maximum Deletions on a String	对字母串可执行的最大删除数	maximum-deletions-on-a-string	weekly-contest-313	Q4
2100.3248877105	793	Preimage Size of Factorial Zeroes Function	阶乘函数后 K 个零	preimage-size-of-factorial-zeroes-function	weekly-contest-74	Q4
2096.6201393558	778	Swim in Rising Water	水位上升的泳池中游泳	swim-in-rising-water	weekly-contest-70	Q4
2096.6098086765	899	Orderly Queue	有序队列	orderly-queue	weekly-contest-100	Q4
2094.5924265370	1976	Number of Ways to Arrive at Destination	到达目的地的方案数	number-of-ways-to-arrive-at-destination	biweekly-contest-59	Q3
2092.8943149547	2402	Meeting Rooms III	会议室 III	meeting-rooms-iii	weekly-contest-309	Q4
2092.5366031561	2444	Count Subarrays With Fixed Bounds	统计定界子数组的数目	count-subarrays-with-fixed-bounds	weekly-contest-315	Q4
2092.4861692502	1049	Last Stone Weight II	最后一块石头的重量 II	last-stone-weight-ii	weekly-contest-137	Q4
2092.0222850837	2412	Minimum Money Required Before Transactions	完成所有交易的初始最少钱数	minimum-money-required-before-transactions	biweekly-contest-87	Q4
2091.6580433632	2842	Count K-Subsequences of a String With Maximum Beauty	统计一个字符串的 k 子序列美丽值最大的数目	count-k-subsequences-of-a-string-with-maximum-beauty	biweekly-contest-112	Q4
2091.6474629767	2751	Robot Collisions	机器人碰撞	robot-collisions	weekly-contest-351	Q4
2091.3820373571	1383	Maximum Performance of a Team	最大的团队表现值	maximum-performance-of-a-team	weekly-contest-180	Q4
2090.6800569319	2193	Minimum Number of Moves to Make Palindrome	得到回文串的最少操作次数	minimum-number-of-moves-to-make-palindrome	biweekly-contest-73	Q4
2090.4183788498	2318	Number of Distinct Roll Sequences	不同骰子序列的数目	number-of-distinct-roll-sequences	biweekly-contest-81	Q4
2087.2049275667	1563	Stone Game V	石子游戏 V	stone-game-v	weekly-contest-203	Q4
2084.9697035674	982	Triples with Bitwise AND Equal To Zero	按位与为零的三元组	triples-with-bitwise-and-equal-to-zero	weekly-contest-121	Q4
2084.6866916045	1192	Critical Connections in a Network	查找集群内的「关键连接」	critical-connections-in-a-network	weekly-contest-154	Q4
2084.5752686737	2267	Check if There Is a Valid Parentheses String Path	检查是否有合法括号字符串路径	check-if-there-is-a-valid-parentheses-string-path	weekly-contest-292	Q4
2084.4980206639	2009	Minimum Number of Operations to Make Array Continuous	使数组连续的最少操作数	minimum-number-of-operations-to-make-array-continuous	biweekly-contest-61	Q4
2084.2010769193	774	Minimize Max Distance to Gas Station	最小化去加油站的最大距离	minimize-max-distance-to-gas-station	weekly-contest-69	Q4
2084.1404698713	2050	Parallel Courses III	并行课程 III	parallel-courses-iii	weekly-contest-264	Q4
2081.8087755451	1494	Parallel Courses II	并行课程 II	parallel-courses-ii	biweekly-contest-29	Q4
2081.7518764643	1847	Closest Room	最近的房间	closest-room	biweekly-contest-51	Q4
2081.6985298770	2857	Count Pairs of Points With Distance k	统计距离为 k 的点对	count-pairs-of-points-with-distance-k	biweekly-contest-113	Q3
2081.6909344021	1639	Number of Ways to Form a Target String Given a Dictionary	通过给定词典构造目标字符串的方案数	number-of-ways-to-form-a-target-string-given-a-dictionary	biweekly-contest-38	Q4
2081.1880297942	2560	House Robber IV	打家劫舍 IV	house-robber-iv	weekly-contest-331	Q3
2080.7845644831	2555	Maximize Win From Two Segments	两个线段获得的最多奖品	maximize-win-from-two-segments	biweekly-contest-97	Q3
2080.0425875741	1718	Construct the Lexicographically Largest Valid Sequence	构建字典序最大的可行序列	construct-the-lexicographically-largest-valid-sequence	biweekly-contest-43	Q3
2079.9846866239	1643	Kth Smallest Instructions	第 K 条最小指令	kth-smallest-instructions	weekly-contest-213	Q4
2079.1911227043	975	Odd Even Jump	奇偶跳	odd-even-jump	weekly-contest-119	Q4
2078.6986769435	1712	Ways to Split Array Into Three Subarrays	将数组分成三个子数组的方案数	ways-to-split-array-into-three-subarrays	weekly-contest-222	Q3
2078.5417326415	1786	Number of Restricted Paths From First to Last Node	从第一个节点出发到最后一个节点的受限路径数	number-of-restricted-paths-from-first-to-last-node	weekly-contest-231	Q3
2077.5054883516	843	Guess the Word	猜猜这个单词	guess-the-word	weekly-contest-86	Q4
2077.4738459704	2959	Number of Possible Sets of Closing Branches	关闭分部的可行集合数目	number-of-possible-sets-of-closing-branches	biweekly-contest-119	Q4
2076.8975497986	1088	Confusing Number II	易混淆数 II	confusing-number-ii	biweekly-contest-2	Q4
2076.0155978787	2449	Minimum Number of Operations to Make Arrays Similar	使数组相似的最少操作次数	minimum-number-of-operations-to-make-arrays-similar	weekly-contest-316	Q4
2075.9046975409	2354	Number of Excellent Pairs	优质数对的数目	number-of-excellent-pairs	weekly-contest-303	Q4
2074.8331146269	2906	Construct Product Matrix	构造乘积矩阵	construct-product-matrix	weekly-contest-367	Q4
2074.4120526679	871	Minimum Number of Refueling Stops	最低加油次数	minimum-number-of-refueling-stops	weekly-contest-93	Q4
2073.0480193170	2845	Count of Interesting Subarrays	统计趣味子数组的数目	count-of-interesting-subarrays	weekly-contest-361	Q3
2073.0124645606	1850	Minimum Adjacent Swaps to Reach the Kth Smallest Number	邻位交换的最小次数	minimum-adjacent-swaps-to-reach-the-kth-smallest-number	weekly-contest-239	Q3
2072.7264178313	1799	Maximize Score After N Operations	N 次操作后的最大分数和	maximize-score-after-n-operations	biweekly-contest-48	Q4
2071.6322841217	2866	Beautiful Towers II	美丽塔 II	beautiful-towers-ii	weekly-contest-364	Q3
2071.3208991938	2607	Make K-Subarray Sums Equal	使子数组元素和相等	make-k-subarray-sums-equal	biweekly-contest-101	Q3
2070.2102619334	1808	Maximize Number of Nice Divisors	好因子的最大数目	maximize-number-of-nice-divisors	weekly-contest-234	Q4
2069.7848729824	2514	Count Anagrams	统计同位异构字符串数目	count-anagrams	biweekly-contest-94	Q4
2069.4030284676	1168	Optimize Water Distribution in a Village	水资源分配优化	optimize-water-distribution-in-a-village	biweekly-contest-7	Q4
2068.8066375660	1368	Minimum Cost to Make at Least One Valid Path in a Grid	使网格图至少有一条有效路径的最小代价	minimum-cost-to-make-at-least-one-valid-path-in-a-grid	weekly-contest-178	Q4
2068.0043466118	1770	Maximum Score from Performing Multiplication Operations	执行乘法运算的最大分数	maximum-score-from-performing-multiplication-operations	weekly-contest-229	Q3
2067.0643721733	855	Exam Room	考场就座	exam-room	weekly-contest-89	Q3
2066.0972575597	801	Minimum Swaps To Make Sequences Increasing	使序列递增的最小交换次数	minimum-swaps-to-make-sequences-increasing	weekly-contest-76	Q2
2062.9876807625	2156	Find Substring With Given Hash Value	查找给定哈希值的子串	find-substring-with-given-hash-value	weekly-contest-278	Q3
2062.3601158741	2106	Maximum Fruits Harvested After at Most K Steps	摘水果	maximum-fruits-harvested-after-at-most-k-steps	weekly-contest-271	Q4
2060.3799915170	2366	Minimum Replacements to Sort the Array	将数组排序的最少替换次数	minimum-replacements-to-sort-the-array	biweekly-contest-84	Q4
2060.0818824378	2681	Power of Heroes	英雄的力量	power-of-heroes	biweekly-contest-104	Q4
2060.0720834082	2508	Add Edges to Make Degrees of All Nodes Even	添加边使所有节点度数都为偶数	add-edges-to-make-degrees-of-all-nodes-even	weekly-contest-324	Q3
2059.4040623264	1131	Maximum of Absolute Value Expression	绝对值表达式的最大值	maximum-of-absolute-value-expression	weekly-contest-146	Q4
2057.4788263111	2197	Replace Non-Coprime Numbers in Array	替换数组中的非互质数	replace-non-coprime-numbers-in-array	weekly-contest-283	Q4
2056.3354942160	1473	Paint House III	粉刷房子 III	paint-house-iii	weekly-contest-192	Q4
2056.2598215101	2542	Maximum Subsequence Score	最大子序列的分数	maximum-subsequence-score	biweekly-contest-96	Q3
2055.0970201875	1575	Count All Possible Routes	统计所有可行路径	count-all-possible-routes	biweekly-contest-34	Q4
2053.7468090497	839	Similar String Groups	相似字符串组	similar-string-groups	weekly-contest-85	Q4
2053.3546092920	2467	Most Profitable Path in a Tree	树上最大得分和路径	most-profitable-path-in-a-tree	biweekly-contest-91	Q3
2051.0879431258	1856	Maximum Subarray Min-Product	子数组最小乘积的最大值	maximum-subarray-min-product	weekly-contest-240	Q3
2050.7159774570	1224	Maximum Equal Frequency	最大相等频率	maximum-equal-frequency	weekly-contest-158	Q4
2050.2553211463	1648	Sell Diminishing-Valued Colored Balls	销售价值减少的颜色球	sell-diminishing-valued-colored-balls	weekly-contest-214	Q3
2048.0976546787	1553	Minimum Number of Days to Eat N Oranges	吃掉 N 个橘子的最少天数	minimum-number-of-days-to-eat-n-oranges	weekly-contest-202	Q4
2047.3919190727	2948	Make Lexicographically Smallest Array by Swapping Elements	交换得到字典序最小的数组	make-lexicographically-smallest-array-by-swapping-elements	weekly-contest-373	Q3
2043.1015779104	2735	Collecting Chocolates	收集巧克力	collecting-chocolates	weekly-contest-349	Q3
2042.4005521254	2551	Put Marbles in Bags	将珠子放入背包中	put-marbles-in-bags	weekly-contest-330	Q3
2040.5621123027	1751	Maximum Number of Events That Can Be Attended II	最多可以参加的会议数目 II	maximum-number-of-events-that-can-be-attended-ii	biweekly-contest-45	Q4
2040.5392890370	1371	Find the Longest Substring Containing Vowels in Even Counts	每个元音包含偶数次的最长子字符串	find-the-longest-substring-containing-vowels-in-even-counts	biweekly-contest-21	Q2
2039.1108746890	1201	Ugly Number III	丑数 III	ugly-number-iii	weekly-contest-155	Q2
2038.8592725467	1590	Make Sum Divisible by P	使数组和能被 P 整除	make-sum-divisible-by-p	biweekly-contest-35	Q3
2037.6527962599	2116	Check if a Parentheses String Can Be Valid	判断一个括号字符串是否有效	check-if-a-parentheses-string-can-be-valid	biweekly-contest-68	Q3
2036.7410194704	2245	Maximum Trailing Zeros in a Cornered Path	转角路径的乘积中最多能有几个尾随零	maximum-trailing-zeros-in-a-cornered-path	weekly-contest-289	Q3
2036.7206020719	1348	Tweet Counts Per Frequency	推文计数	tweet-counts-per-frequency	weekly-contest-175	Q3
2034.9740902393	1140	Stone Game II	石子游戏 II	stone-game-ii	weekly-contest-147	Q4
2034.9420578559	1335	Minimum Difficulty of a Job Schedule	工作计划的最低难度	minimum-difficulty-of-a-job-schedule	weekly-contest-173	Q4
2034.6759416871	947	Most Stones Removed with Same Row or Column	移除最多的同行或同列石头	most-stones-removed-with-same-row-or-column	weekly-contest-112	Q3
2034.4067304341	828	Count Unique Characters of All Substrings of a Given String	统计子串中的唯一字符	count-unique-characters-of-all-substrings-of-a-given-string	weekly-contest-83	Q4
2033.4597721985	2136	Earliest Possible Day of Full Bloom	全部开花的最早一天	earliest-possible-day-of-full-bloom	weekly-contest-275	Q4
2033.1699277531	2262	Total Appeal of A String	字符串的总引力	total-appeal-of-a-string	weekly-contest-291	Q4
2032.4773038683	1425	Constrained Subsequence Sum	带限制的子序列和	constrained-subsequence-sum	weekly-contest-186	Q4
2030.9227703010	2919	Minimum Increment Operations to Make Array Beautiful	使数组变美的最小增量运算数	minimum-increment-operations-to-make-array-beautiful	weekly-contest-369	Q3
2030.1021023033	2426	Number of Pairs Satisfying Inequality	满足不等式的数对数目	number-of-pairs-satisfying-inequality	biweekly-contest-88	Q4
2029.4024513478	2772	Apply Operations to Make All Array Elements Equal to Zero	使数组中的所有元素都等于零	apply-operations-to-make-all-array-elements-equal-to-zero	weekly-contest-353	Q4
2029.1301557536	1231	Divide Chocolate	分享巧克力	divide-chocolate	biweekly-contest-11	Q4
2027.8772739639	895	Maximum Frequency Stack	最大频率栈	maximum-frequency-stack	weekly-contest-99	Q4
2027.7304121046	1320	Minimum Distance to Type a Word Using Two Fingers	二指输入的的最小距离	minimum-distance-to-type-a-word-using-two-fingers	weekly-contest-171	Q4
2027.3839266711	1626	Best Team With No Conflicts	无矛盾的最佳球队	best-team-with-no-conflicts	weekly-contest-211	Q3
2026.8957817007	1406	Stone Game III	石子游戏 III	stone-game-iii	weekly-contest-183	Q4
2025.1529365814	1067	Digit Count in Range	范围内的数字计数	digit-count-in-range	biweekly-contest-1	Q4
2025.0377429311	751	IP to CIDR	IP 到 CIDR	ip-to-cidr	weekly-contest-64	Q2
2024.3797833173	1734	Decode XORed Permutation	解码异或后的排列	decode-xored-permutation	biweekly-contest-44	Q3
2023.4303440211	2597	The Number of Beautiful Subsets	美丽子集的数目	the-number-of-beautiful-subsets	weekly-contest-337	Q3
2022.8520613737	1235	Maximum Profit in Job Scheduling	规划兼职工作	maximum-profit-in-job-scheduling	weekly-contest-159	Q4
2022.4752963768	1210	Minimum Moves to Reach Target with Rotations	穿过迷宫的最少移动次数	minimum-moves-to-reach-target-with-rotations	weekly-contest-156	Q4
2022.3137128296	2251	Number of Flowers in Full Bloom	花期内花的数目	number-of-flowers-in-full-bloom	weekly-contest-290	Q4
2021.7790710467	2271	Maximum White Tiles Covered by a Carpet	毯子覆盖的最多白色砖块数	maximum-white-tiles-covered-by-a-carpet	biweekly-contest-78	Q3
2020.7095306378	2741	Special Permutations	特别的排列	special-permutations	weekly-contest-350	Q3
2020.6775180586	2517	Maximum Tastiness of Candy Basket	礼盒的最大甜蜜度	maximum-tastiness-of-candy-basket	weekly-contest-325	Q3
2020.1846215023	3027	Find the Number of Ways to Place People II	人员站位的方案数 II	find-the-number-of-ways-to-place-people-ii	biweekly-contest-123	Q4
2019.9859462755	2547	Minimum Cost to Split an Array	拆分数组的最小代价	minimum-cost-to-split-an-array	weekly-contest-329	Q4
2019.5399647546	909	Snakes and Ladders	蛇梯棋	snakes-and-ladders	weekly-contest-103	Q2
2016.2085876254	3008	Find Beautiful Indices in the Given Array II	找出数组中的美丽下标 II	find-beautiful-indices-in-the-given-array-ii	weekly-contest-380	Q4
2015.7291888336	1353	Maximum Number of Events That Can Be Attended	最多可以参加的会议数目	maximum-number-of-events-that-can-be-attended	weekly-contest-176	Q3
2014.7655493665	1354	Construct Target Array With Multiple Sums	多次求和构造目标数组	construct-target-array-with-multiple-sums	weekly-contest-176	Q4
2014.2979320644	1105	Filling Bookcase Shelves	填充书架	filling-bookcase-shelves	weekly-contest-143	Q3
2013.4354344791	2472	Maximum Number of Non-overlapping Palindrome Substrings	不重叠回文子字符串的最大数目	maximum-number-of-non-overlapping-palindrome-substrings	weekly-contest-319	Q4
2011.9703133514	2477	Minimum Fuel Cost to Report to the Capital	到达首都的最少油耗	minimum-fuel-cost-to-report-to-the-capital	weekly-contest-320	Q3
2011.3542735398	1102	Path With Maximum Minimum Value	得分最高的路径	path-with-maximum-minimum-value	biweekly-contest-3	Q4
2011.0496162515	2333	Minimum Sum of Squared Difference	最小差值平方和	minimum-sum-of-squared-difference	biweekly-contest-82	Q3
2010.5524756946	880	Decoded String at Index	索引处的解码字符串	decoded-string-at-index	weekly-contest-96	Q3
2009.7322365973	1981	Minimize the Difference Between Target and Chosen Elements	最小化目标值与所选元素的差	minimize-the-difference-between-target-and-chosen-elements	weekly-contest-255	Q3
2008.4065079100	1223	Dice Roll Simulation	掷骰子模拟	dice-roll-simulation	weekly-contest-158	Q3
2005.5862669078	1888	Minimum Number of Flips to Make the Binary String Alternating	使二进制字符串字符交替的最少反转次数	minimum-number-of-flips-to-make-the-binary-string-alternating	weekly-contest-244	Q3
2005.3737929084	2448	Minimum Cost to Make Array Equal	使数组相等的最小开销	minimum-cost-to-make-array-equal	weekly-contest-316	Q3
2005.2755755378	1761	Minimum Degree of a Connected Trio in a Graph	一个图中连通三元组的最小度数	minimum-degree-of-a-connected-trio-in-a-graph	weekly-contest-228	Q4
2004.5346526204	1927	Sum Game	求和游戏	sum-game	biweekly-contest-56	Q3
2003.5794613668	2092	Find All People With Secret	找出知晓秘密的所有专家	find-all-people-with-secret	weekly-contest-269	Q4
2001.4515854273	2850	Minimum Moves to Spread Stones Over Grid	将石头分散到网格图的最少移动次数	minimum-moves-to-spread-stones-over-grid	weekly-contest-362	Q3
2001.2074132383	2328	Number of Increasing Paths in a Grid	网格图中递增路径的数目	number-of-increasing-paths-in-a-grid	weekly-contest-300	Q4
2000.8441804448	1686	Stone Game VI	石子游戏 VI	stone-game-vi	biweekly-contest-41	Q3
2000.8021428612	911	Online Election	在线选举	online-election	weekly-contest-103	Q4
1999.1208076854	765	Couples Holding Hands	情侣牵手	couples-holding-hands	weekly-contest-67	Q4
1998.8899147120	2488	Count Subarrays With Median K	统计中位数为 K 的子数组	count-subarrays-with-median-k	weekly-contest-321	Q4
1997.7013718153	2250	Count Number of Rectangles Containing Each Point	统计包含每个点的矩形数目	count-number-of-rectangles-containing-each-point	weekly-contest-290	Q3
1997.1824403719	1274	Number of Ships in a Rectangle	矩形内船只的数目	number-of-ships-in-a-rectangle	biweekly-contest-14	Q4
1995.2937073376	1986	Minimum Number of Work Sessions to Finish the Tasks	完成任务的最少工作时间段	minimum-number-of-work-sessions-to-finish-the-tasks	weekly-contest-256	Q3
1994.3618892548	927	Three Equal Parts	三等分	three-equal-parts	weekly-contest-107	Q3
1992.0032292739	1625	Lexicographically Smallest String After Applying Operations	执行操作后字典序最小的字符串	lexicographically-smallest-string-after-applying-operations	weekly-contest-211	Q2
1990.7738526153	963	Minimum Area Rectangle II	最小面积矩形 II	minimum-area-rectangle-ii	weekly-contest-116	Q3
1990.2800994214	756	Pyramid Transition Matrix	金字塔转换矩阵	pyramid-transition-matrix	weekly-contest-65	Q3
1989.5369509422	902	Numbers At Most N Given Digit Set	最大为 N 的数字组合	numbers-at-most-n-given-digit-set	weekly-contest-101	Q3
1985.2504512337	928	Minimize Malware Spread II	尽量减少恶意软件的传播 II	minimize-malware-spread-ii	weekly-contest-107	Q4
1985.2417520906	940	Distinct Subsequences II	不同的子序列 II	distinct-subsequences-ii	weekly-contest-110	Q4
1984.9685663849	2963	Count the Number of Good Partitions	统计好分割方案的数目	count-the-number-of-good-partitions	weekly-contest-375	Q4
1983.7044070600	1733	Minimum Number of People to Teach	需要教语言的最少人数	minimum-number-of-people-to-teach	biweekly-contest-44	Q2
1983.2319731313	1250	Check If It Is a Good Array	检查「好数组」	check-if-it-is-a-good-array	weekly-contest-161	Q4
1982.5085994817	805	Split Array With Same Average	数组的均值分割	split-array-with-same-average	weekly-contest-77	Q4
1981.3072959787	2861	Maximum Number of Alloys	最大合金数	maximum-number-of-alloys	weekly-contest-363	Q3
1979.9454101467	2151	Maximum Good People Based on Statements	基于陈述统计最多好人数	maximum-good-people-based-on-statements	weekly-contest-277	Q4
1979.1323403633	1278	Palindrome Partitioning III	分割回文串 III	palindrome-partitioning-iii	weekly-contest-165	Q4
1979.1112273597	1882	Process Tasks Using Servers	使用服务器处理任务	process-tasks-using-servers	weekly-contest-243	Q3
1976.7214151234	1092	Shortest Common Supersequence 	最短公共超序列	shortest-common-supersequence	weekly-contest-141	Q4
1975.9693382075	2831	Find the Longest Equal Subarray	找出最长等值子数组	find-the-longest-equal-subarray	weekly-contest-359	Q4
1975.5726300727	907	Sum of Subarray Minimums	子数组的最小值之和	sum-of-subarray-minimums	weekly-contest-102	Q3
1973.7407637067	1488	Avoid Flood in The City	避免洪水泛滥	avoid-flood-in-the-city	weekly-contest-194	Q3
1970.4608098164	1032	Stream of Characters	字符流	stream-of-characters	weekly-contest-133	Q4
1969.9845549158	835	Image Overlap	图像重叠	image-overlap	weekly-contest-84	Q3
1969.2019235672	1943	Describe the Painting	描述绘画结果	describe-the-painting	biweekly-contest-57	Q3
1967.5589835406	2872	Maximum Number of K-Divisible Components	可以被 K 整除连通块的最大数目	maximum-number-of-k-divisible-components	biweekly-contest-114	Q4
1967.3284576938	1293	Shortest Path in a Grid with Obstacles Elimination	网格中的最短路径	shortest-path-in-a-grid-with-obstacles-elimination	weekly-contest-167	Q4
1966.7067914206	1969	Minimum Non-Zero Product of the Array Elements	数组元素的最小非零乘积	minimum-non-zero-product-of-the-array-elements	weekly-contest-254	Q3
1965.1266122355	2439	Minimize Maximum of Array	最小化数组中的最大值	minimize-maximum-of-array	biweekly-contest-89	Q3
1964.3793590858	815	Bus Routes	公交路线	bus-routes	weekly-contest-79	Q4
1962.3314335449	802	Find Eventual Safe States	找到最终的安全状态	find-eventual-safe-states	weekly-contest-76	Q3
1962.2005269503	1642	Furthest Building You Can Reach	可以到达的最远建筑	furthest-building-you-can-reach	weekly-contest-213	Q3
1961.4987013156	1537	Get the Maximum Score	最大得分	get-the-maximum-score	weekly-contest-200	Q4
1960.5763266754	2350	Shortest Impossible Sequence of Rolls	不可能得到的最短骰子序列	shortest-impossible-sequence-of-rolls	biweekly-contest-83	Q4
1960.5517123728	2392	Build a Matrix With Conditions	给定条件下构造矩阵	build-a-matrix-with-conditions	weekly-contest-308	Q4
1959.2696201953	2564	Substring XOR Queries	子字符串异或查询	substring-xor-queries	weekly-contest-332	Q3
1956.7059585934	1463	Cherry Pickup II	摘樱桃 II	cherry-pickup-ii	biweekly-contest-27	Q4
1954.2533254344	1696	Jump Game VI	跳跃游戏 VI	jump-game-vi	weekly-contest-220	Q3
1953.1377267440	2434	Using a Robot to Print the Lexicographically Smallest String	使用机器人打印字典序最小的字符串	using-a-robot-to-print-the-lexicographically-smallest-string	weekly-contest-314	Q3
1952.7073399331	1737	Change Minimum Characters to Satisfy One of Three Conditions	满足三条件之一需改变的最少字符数	change-minimum-characters-to-satisfy-one-of-three-conditions	weekly-contest-225	Q2
1951.5918682146	2435	Paths in Matrix Whose Sum Is Divisible by K	矩阵中和能被 K 整除的路径	paths-in-matrix-whose-sum-is-divisible-by-k	weekly-contest-314	Q4
1951.3509259668	1259	Handshakes That Don't Cross	不相交的握手	handshakes-that-dont-cross	biweekly-contest-13	Q4
1951.2096212775	1690	Stone Game VII	石子游戏 VII	stone-game-vii	weekly-contest-219	Q3
1949.0920823355	1153	String Transforms Into Another String	字符串转化	string-transforms-into-another-string	biweekly-contest-6	Q4
1948.4895007790	2509	Cycle Length Queries in a Tree	查询树中环的长度	cycle-length-queries-in-a-tree	weekly-contest-324	Q4
1947.8832856412	2516	Take K of Each Character From Left and Right	每种字符至少取 K 个	take-k-of-each-character-from-left-and-right	weekly-contest-325	Q2
1947.5013967785	1631	Path With Minimum Effort	最小体力消耗路径	path-with-minimum-effort	weekly-contest-212	Q3
1945.7515607928	1793	Maximum Score of a Good Subarray	好子数组的最大分数	maximum-score-of-a-good-subarray	weekly-contest-232	Q4
1945.5095833982	1482	Minimum Number of Days to Make m Bouquets	制作 m 束花所需的最少天数	minimum-number-of-days-to-make-m-bouquets	weekly-contest-193	Q3
1944.5673996888	2227	Encrypt and Decrypt Strings	加密解密字符串	encrypt-and-decrypt-strings	weekly-contest-287	Q4
1940.6002290953	2111	Minimum Operations to Make the Array K-Increasing	使数组 K 递增的最少操作次数	minimum-operations-to-make-the-array-k-increasing	weekly-contest-272	Q4
1940.2116985812	2762	Continuous Subarrays	不间断子数组	continuous-subarrays	weekly-contest-352	Q3
1939.9323330472	1760	Minimum Limit of Balls in a Bag	袋子里最少数目的球	minimum-limit-of-balls-in-a-bag	weekly-contest-228	Q3
1939.5601655260	2925	Maximum Score After Applying Operations on a Tree	在树上执行操作以后得到的最大分数	maximum-score-after-applying-operations-on-a-tree	weekly-contest-370	Q3
1938.6883365596	777	Swap Adjacent in LR String	在LR字符串中交换相邻字符	swap-adjacent-in-lr-string	weekly-contest-70	Q3
1938.2224916289	866	Prime Palindrome	回文素数	prime-palindrome	weekly-contest-92	Q3
1938.0586460002	2411	Smallest Subarrays With Maximum Bitwise OR	按位或最大的最小子数组长度	smallest-subarrays-with-maximum-bitwise-or	biweekly-contest-87	Q3
1936.6613414859	813	Largest Sum of Averages	最大平均值和的分组	largest-sum-of-averages	weekly-contest-79	Q3
1934.3556201811	1818	Minimum Absolute Sum Difference	绝对差值和	minimum-absolute-sum-difference	weekly-contest-235	Q3
1933.9571917853	827	Making A Large Island	最大人工岛	making-a-large-island	weekly-contest-82	Q4
1933.2169470617	1964	Find the Longest Valid Obstacle Course at Each Position	找出到每个位置为止最长的有效障碍赛跑路线	find-the-longest-valid-obstacle-course-at-each-position	weekly-contest-253	Q4
1932.3730795204	996	Number of Squareful Arrays	正方形数组的数目	number-of-squareful-arrays	weekly-contest-124	Q4
1931.7335479582	1574	Shortest Subarray to be Removed to Make Array Sorted	删除最短的子数组使剩余数组有序	shortest-subarray-to-be-removed-to-make-array-sorted	biweekly-contest-34	Q3
1931.0849921121	1798	Maximum Number of Consecutive Values You Can Make	你能构造出连续值的最大数目	maximum-number-of-consecutive-values-you-can-make	biweekly-contest-48	Q3
1929.9086934334	1705	Maximum Number of Eaten Apples	吃苹果的最大数目	maximum-number-of-eaten-apples	weekly-contest-221	Q2
1929.8973433160	2018	Check if Word Can Be Placed In Crossword	判断单词是否能放入填字游戏内	check-if-word-can-be-placed-in-crossword	weekly-contest-260	Q3
1929.3184180196	1802	Maximum Value at a Given Index in a Bounded Array	有界数组中指定下标处的最大值	maximum-value-at-a-given-index-in-a-bounded-array	weekly-contest-233	Q3
1928.7961204946	2654	Minimum Number of Operations to Make All Array Elements Equal to 1	使数组所有元素变成 1 的最少操作次数	minimum-number-of-operations-to-make-all-array-elements-equal-to-1	weekly-contest-342	Q4
1928.2304187946	1562	Find Latest Group of Size M	查找大小为 M 的最新分组	find-latest-group-of-size-m	weekly-contest-203	Q3
1927.4000816649	1449	Form Largest Integer With Digits That Add up to Target	数位成本和为目标值的最大数字	form-largest-integer-with-digits-that-add-up-to-target	biweekly-contest-26	Q4
1926.7059583253	1727	Largest Submatrix With Rearrangements	重新排列后的最大子矩阵	largest-submatrix-with-rearrangements	weekly-contest-224	Q3
1924.9646394910	1745	Palindrome Partitioning IV	回文串分割 IV	palindrome-partitioning-iv	weekly-contest-226	Q4
1922.9521758079	2731	Movement of Robots	移动机器人	movement-of-robots	biweekly-contest-106	Q3
1919.7433862082	1552	Magnetic Force Between Two Balls	两球之间的磁力	magnetic-force-between-two-balls	weekly-contest-202	Q3
1919.6391896894	1416	Restore The Array	恢复数组	restore-the-array	biweekly-contest-24	Q4
1919.1749818083	1130	Minimum Cost Tree From Leaf Values	叶值的最小代价生成树	minimum-cost-tree-from-leaf-values	weekly-contest-146	Q3
1918.9960035055	2069	Walking Robot Simulation II	模拟行走机器人 II	walking-robot-simulation-ii	biweekly-contest-65	Q2
1917.4314822412	3002	Maximum Size of a Set After Removals	移除后集合的最多元素数	maximum-size-of-a-set-after-removals	weekly-contest-379	Q3
1917.2145829853	2398	Maximum Number of Robots Within Budget	预算内的最多机器人数目	maximum-number-of-robots-within-budget	biweekly-contest-86	Q4
1917.1049672432	2673	Make Costs of Paths Equal in a Binary Tree	使二叉树所有路径值相等的最小代价	make-costs-of-paths-equal-in-a-binary-tree	weekly-contest-344	Q4
1916.0689858272	1043	Partition Array for Maximum Sum	分隔数组以得到最大和	partition-array-for-maximum-sum	weekly-contest-136	Q3
1915.2628132733	2594	Minimum Time to Repair Cars	修车的最少时间	minimum-time-to-repair-cars	biweekly-contest-100	Q4
1914.6717285348	2147	Number of Ways to Divide a Long Corridor	分隔长廊的方案数	number-of-ways-to-divide-a-long-corridor	biweekly-contest-70	Q4
1913.9308694730	2875	Minimum Size Subarray in Infinite Array	无限数组的最短子数组	minimum-size-subarray-in-infinite-array	weekly-contest-365	Q3
1913.6704728453	1373	Maximum Sum BST in Binary Tree	二叉搜索子树的最大键值和	maximum-sum-bst-in-binary-tree	biweekly-contest-21	Q4
1912.8455659711	1671	Minimum Number of Removals to Make Mountain Array	得到山形数组的最少删除次数	minimum-number-of-removals-to-make-mountain-array	biweekly-contest-40	Q4
1912.8440554296	1898	Maximum Number of Removable Characters	可移除字符的最大数目	maximum-number-of-removable-characters	weekly-contest-245	Q2
1912.1926699881	2680	Maximum OR	最大或值	maximum-or	biweekly-contest-104	Q3
1912.0829958001	1147	Longest Chunked Palindrome Decomposition	段式回文	longest-chunked-palindrome-decomposition	weekly-contest-148	Q4
1911.8282317986	2296	Design a Text Editor	设计一个文本编辑器	design-a-text-editor	weekly-contest-296	Q4
1911.7063530593	2049	Count Nodes With the Highest Score	统计最高分的节点数目	count-nodes-with-the-highest-score	weekly-contest-264	Q3
1911.1959516695	873	Length of Longest Fibonacci Subsequence	最长的斐波那契子序列的长度	length-of-longest-fibonacci-subsequence	weekly-contest-94	Q4
1909.5535861652	2585	Number of Ways to Earn Points	获得分数的方法数	number-of-ways-to-earn-points	weekly-contest-335	Q4
1909.4189035523	991	Broken Calculator	坏了的计算器	broken-calculator	weekly-contest-123	Q3
1908.3866125757	1124	Longest Well-Performing Interval	表现良好的最长时间段	longest-well-performing-interval	weekly-contest-145	Q3
1904.2279434479	2608	Shortest Cycle in a Graph	图中的最短环	shortest-cycle-in-a-graph	biweekly-contest-101	Q4
1903.1973989877	2602	Minimum Operations to Make All Array Elements Equal	使数组元素全部相等的最少操作次数	minimum-operations-to-make-all-array-elements-equal	weekly-contest-338	Q3
1900.8434122725	1665	Minimum Initial Energy to Finish Tasks	完成所有任务的最少初始能量	minimum-initial-energy-to-finish-tasks	weekly-contest-216	Q4
1899.6213866649	823	Binary Trees With Factors	带因子的二叉树	binary-trees-with-factors	weekly-contest-81	Q4
1898.8339532179	2901	Longest Unequal Adjacent Groups Subsequence II	最长相邻不相等子序列 II	longest-unequal-adjacent-groups-subsequence-ii	biweekly-contest-115	Q3
1897.5516652727	1878	Get Biggest Three Rhombus Sums in a Grid	矩阵中最大的三个菱形和	get-biggest-three-rhombus-sums-in-a-grid	biweekly-contest-53	Q3
1897.3309169423	780	Reaching Points	到达终点	reaching-points	weekly-contest-71	Q3
1897.1863301576	2360	Longest Cycle in a Graph	图中的最长环	longest-cycle-in-a-graph	weekly-contest-304	Q4
1896.7975214446	878	Nth Magical Number	第 N 个神奇数字	nth-magical-number	weekly-contest-95	Q3
1896.4053993495	3030	Find the Grid of Region Average	找出网格的区域平均强度	find-the-grid-of-region-average	weekly-contest-383	Q3
1896.1411567598	1871	Jump Game VII	跳跃游戏 VII	jump-game-vii	weekly-contest-242	Q3
1894.5496928891	3036	Number of Subarrays That Match a Pattern II	匹配模式数组的子数组数目 II	number-of-subarrays-that-match-a-pattern-ii	weekly-contest-384	Q4
1893.5143805402	2327	Number of People Aware of a Secret	知道秘密的人数	number-of-people-aware-of-a-secret	weekly-contest-300	Q3
1892.1600619469	1722	Minimize Hamming Distance After Swap Operations	执行交换操作后的最小汉明距离	minimize-hamming-distance-after-swap-operations	weekly-contest-223	Q3
1891.8455273506	2537	Count the Number of Good Subarrays	统计好子数组的数目	count-the-number-of-good-subarrays	weekly-contest-328	Q3
1889.4554322242	2817	Minimum Absolute Difference Between Elements With Constraint	限制条件下元素之间的最小绝对差	minimum-absolute-difference-between-elements-with-constraint	weekly-contest-358	Q3
1886.7040111218	2305	Fair Distribution of Cookies	公平分发饼干	fair-distribution-of-cookies	weekly-contest-297	Q3
1885.9015646531	2064	Minimized Maximum of Products Distributed to Any Store	分配给商店的最多商品的最小值	minimized-maximum-of-products-distributed-to-any-store	weekly-contest-266	Q3
1885.1051527272	1066	Campus Bikes II	校园自行车分配 II	campus-bikes-ii	biweekly-contest-1	Q3
1885.0178370385	1326	Minimum Number of Taps to Open to Water a Garden	灌溉花园的最少水龙头数目	minimum-number-of-taps-to-open-to-water-a-garden	weekly-contest-172	Q4
1883.3541964032	2054	Two Best Non-Overlapping Events	两个最好的不重叠活动	two-best-non-overlapping-events	biweekly-contest-64	Q2
1882.0842446557	2976	Minimum Cost to Convert String I	转换字符串的最小成本 I	minimum-cost-to-convert-string-i	weekly-contest-377	Q3
1881.6810367589	1255	Maximum Score Words Formed by Letters	得分最高的单词集合	maximum-score-words-formed-by-letters	weekly-contest-162	Q4
1880.7433591583	858	Mirror Reflection	镜面反射	mirror-reflection	weekly-contest-90	Q3
1880.5909929633	1536	Minimum Swaps to Arrange a Binary Grid	排布二进制网格的最少交换次数	minimum-swaps-to-arrange-a-binary-grid	weekly-contest-200	Q3
1880.4226853663	1106	Parsing A Boolean Expression	解析布尔表达式	parsing-a-boolean-expression	weekly-contest-143	Q4
1880.3261182293	754	Reach a Number	到达终点数字	reach-a-number	weekly-contest-65	Q1
1880.0511044074	2101	Detonate the Maximum Bombs	引爆最多的炸弹	detonate-the-maximum-bombs	biweekly-contest-67	Q3
1877.8983358307	1234	Replace the Substring for Balanced String	替换子串得到平衡字符串	replace-the-substring-for-balanced-string	weekly-contest-159	Q3
1877.5624603804	752	Open the Lock	打开转盘锁	open-the-lock	weekly-contest-64	Q3
1876.3854625677	955	Delete Columns to Make Sorted II	删列造序 II	delete-columns-to-make-sorted-ii	weekly-contest-114	Q3
1876.3611046625	1838	Frequency of the Most Frequent Element	最高频元素的频数	frequency-of-the-most-frequent-element	weekly-contest-238	Q2
1876.1460190080	1392	Longest Happy Prefix	最长快乐前缀	longest-happy-prefix	weekly-contest-181	Q4
1875.4217845362	2808	Minimum Seconds to Equalize a Circular Array	使循环数组所有元素相等的最少秒数	minimum-seconds-to-equalize-a-circular-array	biweekly-contest-110	Q3
1874.6468976233	1015	Smallest Integer Divisible by K	可被 K 整除的最小整数	smallest-integer-divisible-by-k	weekly-contest-129	Q2
1873.0424923433	2975	Maximum Square Area by Removing Fences From a Field	移除栅栏得到的正方形田地的最大面积	maximum-square-area-by-removing-fences-from-a-field	weekly-contest-377	Q2
1873.0367582475	1001	Grid Illumination	网格照明	grid-illumination	weekly-contest-125	Q4
1872.0350138774	1526	Minimum Number of Increments on Subarrays to Form a Target Array	形成目标数组的子数组最少增加次数	minimum-number-of-increments-on-subarrays-to-form-a-target-array	biweekly-contest-31	Q4
1871.8245218615	2008	Maximum Earnings From Taxi	出租车的最大盈利	maximum-earnings-from-taxi	biweekly-contest-61	Q3
1871.3112059413	1589	Maximum Sum Obtained of Any Permutation	所有排列中的最大和	maximum-sum-obtained-of-any-permutation	biweekly-contest-35	Q2
1869.4024391280	2002	Maximum Product of the Length of Two Palindromic Subsequences	两个回文子序列长度的最大乘积	maximum-product-of-the-length-of-two-palindromic-subsequences	weekly-contest-258	Q3
1868.9864493463	2212	Maximum Points in an Archery Competition	射箭比赛中的最大得分	maximum-points-in-an-archery-competition	weekly-contest-285	Q3
1868.9146755896	924	Minimize Malware Spread	尽量减少恶意软件的传播	minimize-malware-spread	weekly-contest-106	Q4
1868.1914861381	1616	Split Two Strings to Make Palindrome	分割两个字符串得到回文串	split-two-strings-to-make-palindrome	weekly-contest-210	Q3
1867.9916069568	1717	Maximum Score From Removing Substrings	删除子字符串的最大得分	maximum-score-from-removing-substrings	biweekly-contest-43	Q2
1867.8619694847	1605	Find Valid Matrix Given Row and Column Sums	给定行和列的和求可行矩阵	find-valid-matrix-given-row-and-column-sums	biweekly-contest-36	Q3
1866.3014601125	1340	Jump Game V	跳跃游戏 V	jump-game-v	weekly-contest-174	Q4
1865.3441063734	2039	The Time When the Network Becomes Idle	网络空闲的时刻	the-time-when-the-network-becomes-idle	biweekly-contest-63	Q3
1864.5644306171	2767	Partition String Into Minimum Beautiful Substrings	将字符串分割为最少的美丽子字符串	partition-string-into-minimum-beautiful-substrings	biweekly-contest-108	Q3
1864.0948676111	1163	Last Substring in Lexicographical Order	按字典序排在最后的子串	last-substring-in-lexicographical-order	weekly-contest-150	Q4
1861.4906863586	1993	Operations on Tree	树上的操作	operations-on-tree	biweekly-contest-60	Q3
1860.7429342910	1996	The Number of Weak Characters in the Game	游戏中弱角色的数量	the-number-of-weak-characters-in-the-game	weekly-contest-257	Q2
1860.5166780235	2301	Match Substring After Replacement	替换字符后匹配	match-substring-after-replacement	biweekly-contest-80	Q3
1858.9581916885	1744	Can You Eat Your Favorite Candy on Your Favorite Day?	你能在你最喜欢的那天吃到你最喜欢的糖果吗？	can-you-eat-your-favorite-candy-on-your-favorite-day	weekly-contest-226	Q3
1857.6431822094	1584	Min Cost to Connect All Points	连接所有点的最小费用	min-cost-to-connect-all-points	weekly-contest-206	Q3
1856.8610192187	2266	Count Number of Texts	统计打字方案数	count-number-of-texts	weekly-contest-292	Q3
1856.6336926997	3035	Maximum Palindromes After Operations	回文字符串的最大数量	maximum-palindromes-after-operations	weekly-contest-384	Q3
1855.5957296285	799	Champagne Tower	香槟塔	champagne-tower	weekly-contest-75	Q3
1855.5611536940	2800	Shortest String That Contains Three Strings	包含三个字符串的最短字符串	shortest-string-that-contains-three-strings	weekly-contest-356	Q3
1855.4479039876	1202	Smallest String With Swaps	交换字符串中的元素	smallest-string-with-swaps	weekly-contest-155	Q3
1855.3770461540	1546	Maximum Number of Non-Overlapping Subarrays With Sum Equals Target	和为目标值的最大数目不重叠非空子数组数目	maximum-number-of-non-overlapping-subarrays-with-sum-equals-target	weekly-contest-201	Q3
1854.9547783559	1334	Find the City With the Smallest Number of Neighbors at a Threshold Distance	阈值距离内邻居最少的城市	find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance	weekly-contest-173	Q3
1854.0126399812	1269	Number of Ways to Stay in the Same Place After Some Steps	停在原地的方案数	number-of-ways-to-stay-in-the-same-place-after-some-steps	weekly-contest-164	Q4
1853.0880092558	1301	Number of Paths with Max Score	最大得分的路径数目	number-of-paths-with-max-score	biweekly-contest-16	Q4
1851.7255023016	2162	Minimum Cost to Set Cooking Time	设置时间的最少代价	minimum-cost-to-set-cooking-time	biweekly-contest-71	Q3
1851.2677996923	2830	Maximize the Profit as the Salesman	销售利润最大化	maximize-the-profit-as-the-salesman	weekly-contest-359	Q3
1850.8490524791	1152	Analyze User Website Visit Pattern	用户网站访问行为分析	analyze-user-website-visit-pattern	biweekly-contest-6	Q3
1850.5506342426	1477	Find Two Non-overlapping Sub-arrays Each With Target Sum	找两个和为目标值且不重叠的子数组	find-two-non-overlapping-sub-arrays-each-with-target-sum	biweekly-contest-28	Q3
1850.4091449367	1775	Equal Sum Arrays With Minimum Number of Operations	通过最少操作次数使数组的和相等	equal-sum-arrays-with-minimum-number-of-operations	weekly-contest-230	Q3
1849.8122180044	2059	Minimum Operations to Convert Number	转化数字的最小运算数	minimum-operations-to-convert-number	weekly-contest-265	Q3
1848.0912848518	1177	Can Make Palindrome from Substring	构建回文串检测	can-make-palindrome-from-substring	weekly-contest-152	Q3
1847.2077654978	1258	Synonymous Sentences	近义词句子	synonymous-sentences	biweekly-contest-13	Q3
1846.4077077642	1514	Path with Maximum Probability	概率最大的路径	path-with-maximum-probability	weekly-contest-197	Q3
1846.3568350016	874	Walking Robot Simulation	模拟行走机器人	walking-robot-simulation	weekly-contest-94	Q2
1845.6611654401	2598	Smallest Missing Non-negative Integer After Operations	执行操作后的最大 MEX	smallest-missing-non-negative-integer-after-operations	weekly-contest-337	Q4
1845.0428731248	1504	Count Submatrices With All Ones	统计全 1 子矩形	count-submatrices-with-all-ones	weekly-contest-196	Q3
1844.6289439644	1411	Number of Ways to Paint N × 3 Grid	给 N x 3 网格图涂色的方案数	number-of-ways-to-paint-n-3-grid	weekly-contest-184	Q4
1843.2383664194	2576	Find the Maximum Number of Marked Indices	求出最多标记下标	find-the-maximum-number-of-marked-indices	weekly-contest-334	Q3
1841.4067816266	2013	Detect Squares	检测正方形	detect-squares	weekly-contest-259	Q3
1840.9122452886	2332	The Latest Time to Catch a Bus	坐上公交的最晚时间	the-latest-time-to-catch-a-bus	biweekly-contest-82	Q2
1839.9203623221	2311	Longest Binary Subsequence Less Than or Equal to K	小于等于 K 的最长二进制子序列	longest-binary-subsequence-less-than-or-equal-to-k	weekly-contest-298	Q3
1837.8252904904	1559	Detect Cycles in 2D Grid	二维网格图中探测环	detect-cycles-in-2d-grid	biweekly-contest-33	Q4
1836.5363480780	1316	Distinct Echo Substrings	不同的循环子字符串	distinct-echo-substrings	biweekly-contest-17	Q4
1836.5345744332	2146	K Highest Ranked Items Within a Price Range	价格范围内最高排名的 K 样物品	k-highest-ranked-items-within-a-price-range	biweekly-contest-70	Q3
1835.4868365659	995	Minimum Number of K Consecutive Bit Flips	K 连续位的最小翻转次数	minimum-number-of-k-consecutive-bit-flips	weekly-contest-124	Q3
1834.8680347090	2370	Longest Ideal Subsequence	最长理想子序列	longest-ideal-subsequence	weekly-contest-305	Q4
1832.7167755024	3012	Minimize Length of Array Using Operations	通过操作使数组长度最小	minimize-length-of-array-using-operations	biweekly-contest-122	Q3
1832.2280384591	755	Pour Water	倒水	pour-water	weekly-contest-65	Q2
1831.9395911303	2034	Stock Price Fluctuation 	股票价格波动	stock-price-fluctuation	weekly-contest-262	Q3
1830.3165569278	980	Unique Paths III	不同路径 III	unique-paths-iii	weekly-contest-120	Q4
1830.1493771696	790	Domino and Tromino Tiling	多米诺和托米诺平铺	domino-and-tromino-tiling	weekly-contest-73	Q4
1828.6438563573	1754	Largest Merge Of Two Strings	构造字典序最大的合并字符串	largest-merge-of-two-strings	weekly-contest-227	Q3
1828.2700238306	2135	Count Words Obtained After Adding a Letter	统计追加字母可以获得的单词数	count-words-obtained-after-adding-a-letter	weekly-contest-275	Q3
1827.0907402220	1095	Find in Mountain Array	山脉数组中查找目标值	find-in-mountain-array	weekly-contest-142	Q3
1825.7704860080	934	Shortest Bridge	最短的桥	shortest-bridge	weekly-contest-109	Q3
1825.4207082682	1702	Maximum Binary String After Change	修改后的最大二进制字符串	maximum-binary-string-after-change	biweekly-contest-42	Q3
1825.0056908946	1835	Find XOR Sum of All Pairs Bitwise AND	所有数对按位与结果的异或和	find-xor-sum-of-all-pairs-bitwise-and	weekly-contest-237	Q4
1824.8294463410	1298	Maximum Candies You Can Get from Boxes	你能从盒子里获得的最大糖果数	maximum-candies-you-can-get-from-boxes	weekly-contest-168	Q4
1823.8779711373	1377	Frog Position After T Seconds	T 秒后青蛙的位置	frog-position-after-t-seconds	weekly-contest-179	Q4
1823.5831437787	1458	Max Dot Product of Two Subsequences	两个子序列的最大点积	max-dot-product-of-two-subsequences	weekly-contest-190	Q4
1822.9768689716	1363	Largest Multiple of Three	形成三的最大倍数	largest-multiple-of-three	weekly-contest-177	Q4
1822.3170524016	2931	Maximum Spending After Buying Items	购买物品的最大开销	maximum-spending-after-buying-items	biweekly-contest-117	Q4
1822.1301265412	2217	Find Palindrome With Fixed Length	找到指定长度的回文数	find-palindrome-with-fixed-length	weekly-contest-286	Q3
1820.5855764400	1405	Longest Happy String	最长快乐字符串	longest-happy-string	weekly-contest-183	Q3
1819.3068421506	2055	Plates Between Candles	蜡烛之间的盘子	plates-between-candles	biweekly-contest-64	Q3
1818.0024504436	861	Score After Flipping Matrix	翻转矩阵后的得分	score-after-flipping-matrix	weekly-contest-91	Q3
1817.9978644712	1792	Maximum Average Pass Ratio	最大平均通过率	maximum-average-pass-ratio	weekly-contest-232	Q3
1817.5282352022	2787	Ways to Express an Integer as Sum of Powers	将一个数字表示成幂的和的方案数	ways-to-express-an-integer-as-sum-of-powers	biweekly-contest-109	Q4
1817.2240262920	1658	Minimum Operations to Reduce X to Zero	将 x 减到 0 的最小操作数	minimum-operations-to-reduce-x-to-zero	weekly-contest-215	Q3
1817.0597073686	795	Number of Subarrays with Bounded Maximum	区间子数组个数	number-of-subarrays-with-bounded-maximum	weekly-contest-74	Q3
1816.5569971270	3026	Maximum Good Subarray Sum	最大好子数组和	maximum-good-subarray-sum	biweekly-contest-123	Q3
1815.1286459024	773	Sliding Puzzle	滑动谜题	sliding-puzzle	weekly-contest-69	Q3
1810.7690062079	1284	Minimum Number of Flips to Convert Binary Matrix to Zero Matrix	转化为全零矩阵的最少反转次数	minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix	weekly-contest-166	Q4
1810.6470004623	2642	Design Graph With Shortest Path Calculator	设计可以求最短路径的图类	design-graph-with-shortest-path-calculator	biweekly-contest-102	Q4
1809.8192888474	1345	Jump Game IV	跳跃游戏 IV	jump-game-iv	biweekly-contest-19	Q4
1809.5579156134	776	Split BST	拆分二叉搜索树	split-bst	weekly-contest-70	Q2
1808.7871088310	1519	Number of Nodes in the Sub-Tree With the Same Label	子树中标签相同的节点数	number-of-nodes-in-the-sub-tree-with-the-same-label	weekly-contest-198	Q2
1808.5754920785	1230	Toss Strange Coins	抛掷硬币	toss-strange-coins	biweekly-contest-11	Q3
1808.3407696613	2302	Count Subarrays With Score Less Than K	统计得分小于 K 的子数组数目	count-subarrays-with-score-less-than-k	biweekly-contest-80	Q4
1807.4618172386	1594	Maximum Non Negative Product in a Matrix	矩阵的最大非负积	maximum-non-negative-product-in-a-matrix	weekly-contest-207	Q3
1806.5891699944	1073	Adding Two Negabinary Numbers	负二进制数相加	adding-two-negabinary-numbers	weekly-contest-139	Q3
1805.5947071171	1035	Uncrossed Lines	不相交的线	uncrossed-lines	weekly-contest-134	Q3
1804.5783242151	1080	Insufficient Nodes in Root to Leaf Paths	根到叶路径上的不足节点	insufficient-nodes-in-root-to-leaf-paths	weekly-contest-140	Q3
1804.5283324227	2096	Step-By-Step Directions From a Binary Tree Node to Another	从二叉树一个节点到另一个节点每一步的方向	step-by-step-directions-from-a-binary-tree-node-to-another	weekly-contest-270	Q3
1803.7518552874	1953	Maximum Number of Weeks for Which You Can Work	你可以工作的最大周数	maximum-number-of-weeks-for-which-you-can-work	weekly-contest-252	Q2
1802.7875657754	2934	Minimum Operations to Maximize Last Elements in Arrays	最大化数组末位元素的最少操作次数	minimum-operations-to-maximize-last-elements-in-arrays	weekly-contest-371	Q3
1802.2256875356	1673	Find the Most Competitive Subsequence	找出最具竞争力的子序列	find-the-most-competitive-subsequence	weekly-contest-217	Q2
1799.4635458535	1186	Maximum Subarray Sum with One Deletion	删除一次得到子数组最大和	maximum-subarray-sum-with-one-deletion	weekly-contest-153	Q3
1797.8728515982	1711	Count Good Meals	大餐计数	count-good-meals	weekly-contest-222	Q2
1797.7466000366	1834	Single-Threaded CPU	单线程 CPU	single-threaded-cpu	weekly-contest-237	Q3
1797.5851607225	1072	Flip Columns For Maximum Number of Equal Rows	按列翻转得到最大值等行数	flip-columns-for-maximum-number-of-equal-rows	weekly-contest-139	Q2
1797.4917663632	1028	Recover a Tree From Preorder Traversal	从先序遍历还原二叉树	recover-a-tree-from-preorder-traversal	weekly-contest-132	Q4
1796.5392133092	3001	Minimum Moves to Capture The Queen	捕获黑皇后需要的最少移动次数	minimum-moves-to-capture-the-queen	weekly-contest-379	Q2
1795.0422250815	966	Vowel Spellchecker	元音拼写检查器	vowel-spellchecker	weekly-contest-117	Q3
1794.6129370985	2998	Minimum Number of Operations to Make X and Y Equal	使 X 和 Y 相等的最少操作次数	minimum-number-of-operations-to-make-x-and-y-equal	biweekly-contest-121	Q3
1794.5827898448	886	Possible Bipartition	可能的二分法	possible-bipartition	weekly-contest-97	Q3
1793.8027487553	1653	Minimum Deletions to Make String Balanced	使字符串平衡的最少删除次数	minimum-deletions-to-make-string-balanced	biweekly-contest-39	Q2
1793.3037316825	2381	Shifting Letters II	字母移位 II	shifting-letters-ii	biweekly-contest-85	Q3
1793.3033536992	2615	Sum of Distances	等值距离和	sum-of-distances	weekly-contest-340	Q2
1792.0767945370	1245	Tree Diameter	树的直径	tree-diameter	biweekly-contest-12	Q3
1791.5102962397	2771	Longest Non-decreasing Subarray From Two Arrays	构造最长非递减子数组	longest-non-decreasing-subarray-from-two-arrays	weekly-contest-353	Q3
1791.0336923305	2712	Minimum Cost to Make All Characters Equal	使所有字符相等的最小成本	minimum-cost-to-make-all-characters-equal	weekly-contest-347	Q3
1790.5747006625	2321	Maximum Score Of Spliced Array	拼接数组的最大分数	maximum-score-of-spliced-array	weekly-contest-299	Q3
1787.8550568757	2192	All Ancestors of a Node in a Directed Acyclic Graph	有向无环图中一个节点的所有祖先	all-ancestors-of-a-node-in-a-directed-acyclic-graph	biweekly-contest-73	Q3
1787.6346864268	768	Max Chunks To Make Sorted II	最多能完成排序的块 II	max-chunks-to-make-sorted-ii	weekly-contest-68	Q4
1787.4514432151	1156	Swap For Longest Repeated Character Substring	单字符重复子串的最大长度	swap-for-longest-repeated-character-substring	weekly-contest-149	Q3
1787.2310751136	1497	Check If Array Pairs Are Divisible by k	检查数组对是否可以被 k 整除	check-if-array-pairs-are-divisible-by-k	weekly-contest-195	Q2
1786.9268132617	1510	Stone Game IV	石子游戏 IV	stone-game-iv	biweekly-contest-30	Q4
1786.6885430540	1312	Minimum Insertion Steps to Make a String Palindrome	让字符串成为回文串的最少插入次数	minimum-insertion-steps-to-make-a-string-palindrome	weekly-contest-170	Q4
1786.5491561897	971	Flip Binary Tree To Match Preorder Traversal	翻转二叉树以匹配先序遍历	flip-binary-tree-to-match-preorder-traversal	weekly-contest-118	Q3
1786.4753467293	787	Cheapest Flights Within K Stops	K 站中转内最便宜的航班	cheapest-flights-within-k-stops	weekly-contest-72	Q3
1786.3121598293	983	Minimum Cost For Tickets	最低票价	minimum-cost-for-tickets	weekly-contest-121	Q3
1785.6872758693	1911	Maximum Alternating Subsequence Sum	最大子序列交替和	maximum-alternating-subsequence-sum	biweekly-contest-55	Q3
1785.6006955353	2653	Sliding Subarray Beauty	滑动子数组的美丽值	sliding-subarray-beauty	weekly-contest-342	Q3
1784.3506628869	2952	Minimum Number of Coins to be Added	需要添加的硬币的最小数量	minimum-number-of-coins-to-be-added	weekly-contest-374	Q2
1784.2539813582	894	All Possible Full Binary Trees	所有可能的满二叉树	all-possible-full-binary-trees	weekly-contest-99	Q3
1783.2337340478	851	Loud and Rich	喧闹和富有	loud-and-rich	weekly-contest-88	Q3
1782.9801784101	1765	Map of Highest Peak	地图中的最高点	map-of-highest-peak	biweekly-contest-46	Q3
1782.3312212058	1171	Remove Zero Sum Consecutive Nodes from Linked List	从链表中删去总和值为零的连续节点	remove-zero-sum-consecutive-nodes-from-linked-list	weekly-contest-151	Q3
1781.8156963676	2353	Design a Food Rating System	设计食物评分系统	design-a-food-rating-system	weekly-contest-303	Q3
1781.3664141686	1895	Largest Magic Square	最大的幻方	largest-magic-square	biweekly-contest-54	Q3
1779.9495819318	842	Split Array into Fibonacci Sequence	将数组拆分成斐波那契序列	split-array-into-fibonacci-sequence	weekly-contest-86	Q3
1779.8364613072	1424	Diagonal Traverse II	对角线遍历 II	diagonal-traverse-ii	weekly-contest-186	Q3
1779.7534349429	1129	Shortest Path with Alternating Colors	颜色交替的最短路径	shortest-path-with-alternating-colors	weekly-contest-146	Q2
1779.7001728541	2369	Check if There is a Valid Partition For The Array	检查数组是否存在有效划分	check-if-there-is-a-valid-partition-for-the-array	weekly-contest-305	Q3
1779.3931248179	1016	Binary String With Substrings Representing 1 To N	子串能表示从 1 到 N 数字的二进制串	binary-string-with-substrings-representing-1-to-n	weekly-contest-129	Q4
1779.0712927572	2601	Prime Subtraction Operation	质数减法运算	prime-subtraction-operation	weekly-contest-338	Q2
1778.4880620629	1824	Minimum Sideway Jumps	最少侧跳次数	minimum-sideway-jumps	weekly-contest-236	Q3
1777.3786570233	918	Maximum Sum Circular Subarray	环形子数组的最大和	maximum-sum-circular-subarray	weekly-contest-105	Q2
1775.8546066480	2531	Make Number of Distinct Characters Equal	使字符串总不同字符的数目相等	make-number-of-distinct-characters-equal	weekly-contest-327	Q3
1774.8764591297	1238	Circular Permutation in Binary Representation	循环码排列	circular-permutation-in-binary-representation	weekly-contest-160	Q2
1772.9528456848	2982	Find Longest Special Substring That Occurs Thrice II	找出出现至少三次的最长特殊子字符串 II	find-longest-special-substring-that-occurs-thrice-ii	weekly-contest-378	Q3
1770.8924569497	1146	Snapshot Array	快照数组	snapshot-array	weekly-contest-148	Q3
1769.4344566771	2685	Count the Number of Complete Components	统计完全连通分量的数量	count-the-number-of-complete-components	weekly-contest-345	Q4
1768.9138093037	2718	Sum of Matrix After Queries	查询后矩阵的和	sum-of-matrix-after-queries	weekly-contest-348	Q3
1768.6238968290	1600	Throne Inheritance	皇位继承顺序	throne-inheritance	weekly-contest-208	Q3
1766.2506177612	1914	Cyclically Rotating a Grid	循环轮转矩阵	cyclically-rotating-a-grid	weekly-contest-247	Q2
1765.5654059263	875	Koko Eating Bananas	爱吃香蕉的珂珂	koko-eating-bananas	weekly-contest-94	Q3
1764.9170564773	1706	Where Will the Ball Fall	球会落何处	where-will-the-ball-fall	weekly-contest-221	Q3
1763.7876799590	2905	Find Indices With Index and Value Difference II	找出满足差值条件的下标 II	find-indices-with-index-and-value-difference-ii	weekly-contest-367	Q3
1763.6404758359	2462	Total Cost to Hire K Workers	雇佣 K 位工人的总代价	total-cost-to-hire-k-workers	weekly-contest-318	Q3
1762.3115124143	948	Bag of Tokens	令牌放置	bag-of-tokens	weekly-contest-112	Q4
1762.0307532652	1262	Greatest Sum Divisible by Three	可被三整除的最大和	greatest-sum-divisible-by-three	weekly-contest-163	Q3
1761.9162628125	2453	Destroy Sequential Targets	摧毁一系列目标	destroy-sequential-targets	biweekly-contest-90	Q3
1760.9131492436	2121	Intervals Between Identical Elements	相同元素的间隔之和	intervals-between-identical-elements	weekly-contest-273	Q3
1759.2287478055	2075	Decode the Slanted Ciphertext	解码斜向换位密码	decode-the-slanted-ciphertext	weekly-contest-267	Q3
1759.0470795449	2498	Frog Jump II	青蛙过河 II	frog-jump-ii	biweekly-contest-93	Q3
1759.0197295594	1541	Minimum Insertions to Balance a Parentheses String	平衡括号字符串的最少插入次数	minimum-insertions-to-balance-a-parentheses-string	biweekly-contest-32	Q3
1758.7525514100	1027	Longest Arithmetic Subsequence	最长等差数列	longest-arithmetic-subsequence	weekly-contest-132	Q3
1758.5135073787	1954	Minimum Garden Perimeter to Collect Enough Apples	收集足够苹果的最小花园周长	minimum-garden-perimeter-to-collect-enough-apples	weekly-contest-252	Q3
1754.1710323358	2568	Minimum Impossible OR	最小无法得到的或值	minimum-impossible-or	biweekly-contest-98	Q3
1753.9062487685	1216	Valid Palindrome III	验证回文字符串 III	valid-palindrome-iii	biweekly-contest-10	Q4
1753.4775753993	764	Largest Plus Sign	最大加号标志	largest-plus-sign	weekly-contest-67	Q3
1752.9555725796	1135	Connecting Cities With Minimum Cost	最低成本联通所有城市	connecting-cities-with-minimum-cost	biweekly-contest-5	Q3
1752.2621077596	939	Minimum Area Rectangle	最小面积矩形	minimum-area-rectangle	weekly-contest-110	Q3
1751.5101577001	2166	Design Bitset	设计位集	design-bitset	weekly-contest-279	Q3
1751.1156254650	2400	Number of Ways to Reach a Position After Exactly k Steps	恰好移动 k 步到达某一位置的方法数目	number-of-ways-to-reach-a-position-after-exactly-k-steps	weekly-contest-309	Q2
1749.9743684275	2856	Minimum Array Length After Pair Removals	删除数对后的最小数组长度	minimum-array-length-after-pair-removals	biweekly-contest-113	Q2
1749.5432375672	2401	Longest Nice Subarray	最长优雅子数组	longest-nice-subarray	weekly-contest-309	Q3
1749.5115037045	2871	Split Array Into Maximum Number of Subarrays	将数组分割成最多数目的子数组	split-array-into-maximum-number-of-subarrays	biweekly-contest-114	Q3
1749.4981778209	1111	Maximum Nesting Depth of Two Valid Parentheses Strings	有效括号的嵌套深度	maximum-nesting-depth-of-two-valid-parentheses-strings	weekly-contest-144	Q4
1748.4522689101	2134	Minimum Swaps to Group All 1's Together II	最少交换次数来组合所有的 1 II	minimum-swaps-to-group-all-1s-together-ii	weekly-contest-275	Q2
1748.1523771585	1297	Maximum Number of Occurrences of a Substring	子串的最大出现次数	maximum-number-of-occurrences-of-a-substring	weekly-contest-168	Q3
1748.1339100823	2171	Removing Minimum Number of Magic Beans	拿出最少数目的魔法豆	removing-minimum-number-of-magic-beans	weekly-contest-280	Q3
1747.6755111029	1191	K-Concatenation Maximum Sum	K 次串联后最大子数组之和	k-concatenation-maximum-sum	weekly-contest-154	Q3
1746.8757919578	1849	Splitting a String Into Descending Consecutive Values	将字符串拆分为递减的连续值	splitting-a-string-into-descending-consecutive-values	weekly-contest-239	Q2
1746.1359179770	1024	Video Stitching	视频拼接	video-stitching	weekly-contest-131	Q4
1745.6580748712	1530	Number of Good Leaf Nodes Pairs	好叶子节点对的数量	number-of-good-leaf-nodes-pairs	weekly-contest-199	Q3
1745.6490739887	1391	Check if There is a Valid Path in a Grid	检查网格中是否存在有效路径	check-if-there-is-a-valid-path-in-a-grid	weekly-contest-181	Q3
1745.5352025872	2502	Design Memory Allocator	设计内存分配器	design-memory-allocator	weekly-contest-323	Q3
1744.7611048301	1638	Count Substrings That Differ by One Character	统计只差一个字符的子串数目	count-substrings-that-differ-by-one-character	biweekly-contest-38	Q3
1744.0388789755	1139	Largest 1-Bordered Square	最大的以 1 为边界的正方形	largest-1-bordered-square	weekly-contest-147	Q3
1743.7319765540	2087	Minimum Cost Homecoming of a Robot in a Grid	网格图中机器人回家的最小代价	minimum-cost-homecoming-of-a-robot-in-a-grid	biweekly-contest-66	Q3
1741.4527995252	1145	Binary Tree Coloring Game	二叉树着色游戏	binary-tree-coloring-game	weekly-contest-148	Q2
1741.3694833067	3020	Find the Maximum Number of Elements in Subset	子集中元素的最大数量	find-the-maximum-number-of-elements-in-subset	weekly-contest-382	Q2
1740.5014205942	1079	Letter Tile Possibilities	活字印刷	letter-tile-possibilities	weekly-contest-140	Q2
1739.5831401172	1593	Split a String Into the Max Number of Unique Substrings	拆分字符串使唯一子字符串的数目最大	split-a-string-into-the-max-number-of-unique-substrings	weekly-contest-207	Q2
1737.8431142688	1814	Count Nice Pairs in an Array	统计一个数组中好对子的数目	count-nice-pairs-in-an-array	biweekly-contest-49	Q3
1737.2065180671	3044	Most Frequent Prime	出现频率最高的质数	most-frequent-prime	weekly-contest-385	Q3
1735.8505509901	2707	Extra Characters in a String	字符串中的额外字符	extra-characters-in-a-string	biweekly-contest-105	Q2
1734.8208369949	1292	Maximum Side Length of a Square with Sum Less than or Equal to Threshold	元素和小于等于阈值的正方形的最大边长	maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold	weekly-contest-167	Q3
1734.0550202798	2048	Next Greater Numerically Balanced Number	下一个更大的数值平衡数	next-greater-numerically-balanced-number	weekly-contest-264	Q2
1732.7813534239	1273	Delete Tree Nodes	删除树节点	delete-tree-nodes	biweekly-contest-14	Q3
1732.5146472785	2786	Visit Array Positions to Maximize Score	访问数组中的位置使分数最大	visit-array-positions-to-maximize-score	biweekly-contest-109	Q3
1731.5555445321	889	Construct Binary Tree from Preorder and Postorder Traversal	根据前序和后序遍历构造二叉树	construct-binary-tree-from-preorder-and-postorder-traversal	weekly-contest-98	Q3
1730.3052054913	1014	Best Sightseeing Pair	最佳观光组合	best-sightseeing-pair	weekly-contest-129	Q3
1729.6074000215	1220	Count Vowels Permutation	统计元音字母序列的数目	count-vowels-permutation	weekly-contest-157	Q4
1725.4481937307	1011	Capacity To Ship Packages Within D Days	在 D 天内送达包裹的能力	capacity-to-ship-packages-within-d-days	weekly-contest-128	Q3
1725.1995150882	2416	Sum of Prefix Scores of Strings	字符串的前缀分数和	sum-of-prefix-scores-of-strings	weekly-contest-311	Q4
1724.3941649340	2261	K Divisible Elements Subarrays	含最多 K 个可整除元素的子数组	k-divisible-elements-subarrays	weekly-contest-291	Q3
1724.1545485476	2070	Most Beautiful Item for Each Query	每一个查询的最大美丽值	most-beautiful-item-for-each-query	biweekly-contest-65	Q3
1722.8129701098	1359	Count All Valid Pickup and Delivery Options	有效的快递序列数目	count-all-valid-pickup-and-delivery-options	biweekly-contest-20	Q4
1722.3088173214	1197	Minimum Knight Moves	进击的骑士	minimum-knight-moves	biweekly-contest-9	Q2
1721.1964988483	2826	Sorting Three Groups	将三个组排序	sorting-three-groups	biweekly-contest-111	Q3
1720.7470612766	2563	Count the Number of Fair Pairs	统计公平数对的数目	count-the-number-of-fair-pairs	weekly-contest-332	Q2
1719.9451998740	1239	Maximum Length of a Concatenated String with Unique Characters	串联字符串的最大长度	maximum-length-of-a-concatenated-string-with-unique-characters	weekly-contest-160	Q3
1718.9772466681	2017	Grid Game	网格游戏	grid-game	weekly-contest-260	Q2
1718.8256321624	2397	Maximum Rows Covered by Columns	被列覆盖的最多行数	maximum-rows-covered-by-columns	biweekly-contest-86	Q3
1716.9721777000	2202	Maximize the Topmost Element After K Moves	K 次操作后最大化顶端元素	maximize-the-topmost-element-after-k-moves	weekly-contest-284	Q3
1714.9927637010	2359	Find Closest Node to Given Two Nodes	找到离给定两个节点最近的节点	find-closest-node-to-given-two-nodes	weekly-contest-304	Q3
1714.6960124182	1781	Sum of Beauty of All Substrings	所有子字符串美丽值之和	sum-of-beauty-of-all-substrings	biweekly-contest-47	Q3
1713.3954468582	2406	Divide Intervals Into Minimum Number of Groups	将区间分为最少组数	divide-intervals-into-minimum-number-of-groups	weekly-contest-310	Q3
1713.2768268466	1372	Longest ZigZag Path in a Binary Tree	二叉树中的最长交错路径	longest-zigzag-path-in-a-binary-tree	biweekly-contest-21	Q3
1712.4010133221	1042	Flower Planting With No Adjacent	不邻接植花	flower-planting-with-no-adjacent	weekly-contest-136	Q2
1711.4873176824	2385	Amount of Time for Binary Tree to Be Infected	感染二叉树需要的总时间	amount-of-time-for-binary-tree-to-be-infected	weekly-contest-307	Q3
1711.1205064321	1801	Number of Orders in the Backlog	积压订单中的订单总数	number-of-orders-in-the-backlog	weekly-contest-233	Q2
1710.9105378431	923	3Sum With Multiplicity	三数之和的多种可能	3sum-with-multiplicity	weekly-contest-106	Q3
1710.3243520032	1567	Maximum Length of Subarray With Positive Product	乘积为正数的最长子数组长度	maximum-length-of-subarray-with-positive-product	weekly-contest-204	Q2
1710.1120861153	759	Employee Free Time	员工空闲时间	employee-free-time	weekly-contest-66	Q3
1710.0787625377	1136	Parallel Courses	平行课程	parallel-courses	biweekly-contest-5	Q4
1709.1461451873	979	Distribute Coins in Binary Tree	在二叉树中分配硬币	distribute-coins-in-binary-tree	weekly-contest-120	Q3
1709.1054732427	2140	Solving Questions With Brainpower	解决智力问题	solving-questions-with-brainpower	weekly-contest-276	Q3
1708.9983361411	1401	Circle and Rectangle Overlapping	圆和矩形是否有重叠	circle-and-rectangle-overlapping	biweekly-contest-23	Q3
1708.9663754668	2944	Minimum Number of Coins for Fruits	购买水果需要的最少金币数	minimum-number-of-coins-for-fruits	biweekly-contest-118	Q3
1708.8735585776	901	Online Stock Span	股票价格跨度	online-stock-span	weekly-contest-101	Q2
1708.8129236790	826	Most Profit Assigning Work	安排工作以达到最大收益	most-profit-assigning-work	weekly-contest-82	Q3
1708.7149486078	3040	Maximum Number of Operations With the Same Score II	相同分数的最大操作数目 II	maximum-number-of-operations-with-the-same-score-ii	biweekly-contest-124	Q3
1708.7056764058	2257	Count Unguarded Cells in the Grid	统计网格图中没有被保卫的格子数	count-unguarded-cells-in-the-grid	biweekly-contest-77	Q3
1707.8992927609	816	Ambiguous Coordinates	模糊坐标	ambiguous-coordinates	weekly-contest-80	Q3
1707.4309979043	3025	Find the Number of Ways to Place People I	人员站位的方案数 I	find-the-number-of-ways-to-place-people-i	biweekly-contest-123	Q2
1705.2545641354	2672	Number of Adjacent Elements With the Same Color	有相同颜色的相邻元素数目	number-of-adjacent-elements-with-the-same-color	weekly-contest-344	Q3
1704.3608916410	1947	Maximum Compatibility Score Sum	最大兼容性评分和	maximum-compatibility-score-sum	weekly-contest-251	Q3
1702.8035923458	958	Check Completeness of a Binary Tree	二叉树的完全性检验	check-completeness-of-a-binary-tree	weekly-contest-115	Q2
1702.4962514406	2100	Find Good Days to Rob the Bank	适合打劫银行的日子	find-good-days-to-rob-the-bank	biweekly-contest-67	Q2
1702.4387527636	2080	Range Frequency Queries	区间内查询数字的频率	range-frequency-queries	weekly-contest-268	Q3
1701.7584658834	1774	Closest Dessert Cost	最接近目标价格的甜点成本	closest-dessert-cost	weekly-contest-230	Q2
1701.5735371897	1054	Distant Barcodes	距离相等的条形码	distant-barcodes	weekly-contest-138	Q4
1701.4341867571	2929	Distribute Candies Among Children II	给小朋友们分糖果 II	distribute-candies-among-children-ii	biweekly-contest-117	Q2
1700.8505554268	2962	Count Subarrays Where Max Element Appears at Least K Times	统计最大元素出现至少 K 次的子数组	count-subarrays-where-max-element-appears-at-least-k-times	weekly-contest-375	Q3
1697.8500495479	1017	Convert to Base -2	负二进制转换	convert-to-base-2	weekly-contest-130	Q2
1697.2356875149	1289	Minimum Falling Path Sum II	下降路径最小和  II	minimum-falling-path-sum-ii	biweekly-contest-15	Q4
1697.0187705319	825	Friends Of Appropriate Ages	适龄的朋友	friends-of-appropriate-ages	weekly-contest-82	Q2
1696.9920075471	1487	Making File Names Unique	保证文件名唯一	making-file-names-unique	weekly-contest-194	Q2
1696.8895579594	2588	Count the Number of Beautiful Subarrays	统计美丽子数组数目	count-the-number-of-beautiful-subarrays	weekly-contest-336	Q3
1695.3076664977	792	Number of Matching Subsequences	匹配子序列的单词数	number-of-matching-subsequences	weekly-contest-74	Q2
1695.2832486322	1942	The Number of the Smallest Unoccupied Chair	最小未被占据椅子的编号	the-number-of-the-smallest-unoccupied-chair	biweekly-contest-57	Q2
1695.0815222626	2420	Find All Good Indices	找到所有好下标	find-all-good-indices	weekly-contest-312	Q3
1694.4339515030	829	Consecutive Numbers Sum	连续整数求和	consecutive-numbers-sum	weekly-contest-83	Q3
1694.4308657594	2466	Count Ways To Build Good Strings	统计构造好字符串的方案数	count-ways-to-build-good-strings	biweekly-contest-91	Q2
1693.4495728383	2337	Move Pieces to Obtain a String	移动片段得到字符串	move-pieces-to-obtain-a-string	weekly-contest-301	Q3
1692.5884631801	1462	Course Schedule IV	课程表 IV	course-schedule-iv	biweekly-contest-27	Q3
1690.9043557462	919	Complete Binary Tree Inserter	完全二叉树插入器	complete-binary-tree-inserter	weekly-contest-105	Q3
1690.1655236843	935	Knight Dialer	骑士拨号器	knight-dialer	weekly-contest-109	Q2
1689.7569144085	1419	Minimum Number of Frogs Croaking	数青蛙	minimum-number-of-frogs-croaking	weekly-contest-185	Q3
1688.9209684568	1963	Minimum Number of Swaps to Make the String Balanced	使字符串平衡的最小交换次数	minimum-number-of-swaps-to-make-the-string-balanced	weekly-contest-253	Q3
1688.6445178061	3043	Find the Length of the Longest Common Prefix	最长公共前缀的长度	find-the-length-of-the-longest-common-prefix	weekly-contest-385	Q2
1686.4493679523	950	Reveal Cards In Increasing Order	按递增顺序显示卡牌	reveal-cards-in-increasing-order	weekly-contest-113	Q3
1685.5389350949	2233	Maximum Product After K Increments	K 次增加后的最大乘积	maximum-product-after-k-increments	weekly-contest-288	Q3
1685.3599641299	2074	Reverse Nodes in Even Length Groups	反转偶数长度组的节点	reverse-nodes-in-even-length-groups	weekly-contest-267	Q2
1682.8882177724	1443	Minimum Time to Collect All Apples in a Tree	收集树上所有苹果的最少时间	minimum-time-to-collect-all-apples-in-a-tree	weekly-contest-188	Q3
1682.1689207800	2497	Maximum Star Sum of a Graph	图中最大星和	maximum-star-sum-of-a-graph	biweekly-contest-93	Q2
1681.3263732456	767	Reorganize String	重构字符串	reorganize-string	weekly-contest-68	Q2
1680.8669178490	2280	Minimum Lines to Represent a Line Chart	表示一个折线图的最少线段数	minimum-lines-to-represent-a-line-chart	weekly-contest-294	Q3
1680.8242599300	1865	Finding Pairs With a Certain Sum	找出和为指定值的下标对	finding-pairs-with-a-certain-sum	weekly-contest-241	Q3
1680.4852623991	1031	Maximum Sum of Two Non-Overlapping Subarrays	两个非重叠子数组的最大和	maximum-sum-of-two-non-overlapping-subarrays	weekly-contest-133	Q3
1680.1353258588	2182	Construct String With Repeat Limit	构造限制重复的字符串	construct-string-with-repeat-limit	weekly-contest-281	Q3
1680.0815931601	2457	Minimum Addition to Make Integer Beautiful	美丽整数的最小增量	minimum-addition-to-make-integer-beautiful	weekly-contest-317	Q3
1679.5737760149	2492	Minimum Score of a Path Between Two Cities	两个城市间路径的最小分数	minimum-score-of-a-path-between-two-cities	weekly-contest-322	Q3
1679.2607152001	1402	Reducing Dishes	做菜顺序	reducing-dishes	biweekly-contest-23	Q4
1678.7231378948	1905	Count Sub Islands	统计子岛屿	count-sub-islands	weekly-contest-246	Q3
1678.6245760413	2698	Find the Punishment Number of an Integer	求一个整数的惩罚数	find-the-punishment-number-of-an-integer	weekly-contest-346	Q3
1678.6241816708	2317	Maximum XOR After Operations 	操作后的最大异或和	maximum-xor-after-operations	biweekly-contest-81	Q3
1678.5871762113	2115	Find All Possible Recipes from Given Supplies	从给定原材料中找到所有可以做出的菜	find-all-possible-recipes-from-given-supplies	biweekly-contest-68	Q2
1678.3947690537	885	Spiral Matrix III	螺旋矩阵 III	spiral-matrix-iii	weekly-contest-97	Q2
1678.1133886034	853	Car Fleet	车队	car-fleet	weekly-contest-89	Q2
1677.4559378473	2943	Maximize Area of Square Hole in Grid	最大化网格图中正方形空洞的面积	maximize-area-of-square-hole-in-grid	biweekly-contest-118	Q2
1676.5007365375	2641	Cousins in Binary Tree II	二叉树的堂兄弟节点 II	cousins-in-binary-tree-ii	biweekly-contest-102	Q3
1675.9894075840	974	Subarray Sums Divisible by K	和可被 K 整除的子数组	subarray-sums-divisible-by-k	weekly-contest-119	Q3
1675.9610355975	987	Vertical Order Traversal of a Binary Tree	二叉树的垂序遍历	vertical-order-traversal-of-a-binary-tree	weekly-contest-122	Q4
1675.7612347410	1870	Minimum Speed to Arrive on Time	准时到达的列车最小时速	minimum-speed-to-arrive-on-time	weekly-contest-242	Q2
1674.9985842835	1339	Maximum Product of Splitted Binary Tree	分裂二叉树的最大乘积	maximum-product-of-splitted-binary-tree	weekly-contest-174	Q3
1674.7986939472	1922	Count Good Numbers	统计好数字的数目	count-good-numbers	weekly-contest-248	Q3
1674.5365205597	1215	Stepping Numbers	步进数	stepping-numbers	biweekly-contest-10	Q3
1672.1678031263	1438	Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit	绝对差不超过限制的最长连续子数组	longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit	weekly-contest-187	Q3
1671.9261598000	2033	Minimum Operations to Make a Uni-Value Grid	获取单值网格的最小操作数	minimum-operations-to-make-a-uni-value-grid	weekly-contest-262	Q2
1671.4657554194	1738	Find Kth Largest XOR Coordinate Value	找出第 K 大的异或坐标值	find-kth-largest-xor-coordinate-value	weekly-contest-225	Q3
1666.3469909790	1162	As Far from Land as Possible	地图分析	as-far-from-land-as-possible	weekly-contest-150	Q3
1665.2490724700	1620	Coordinate With Maximum Network Quality	网络信号最好的坐标	coordinate-with-maximum-network-quality	biweekly-contest-37	Q2
1665.1885910815	2593	Find Score of an Array After Marking All Elements	标记所有元素后数组的分数	find-score-of-an-array-after-marking-all-elements	biweekly-contest-100	Q3
1664.7703749741	1121	Divide Array Into Increasing Sequences	将数组分成几个递增序列	divide-array-into-increasing-sequences	biweekly-contest-4	Q4
1663.4565919330	2611	Mice and Cheese	老鼠和奶酪	mice-and-cheese	weekly-contest-339	Q3
1663.3912882908	2063	Vowels of All Substrings	所有子字符串中的元音	vowels-of-all-substrings	weekly-contest-266	Q2
1663.2612318917	1219	Path with Maximum Gold	黄金矿工	path-with-maximum-gold	weekly-contest-157	Q3
1663.1853149056	863	All Nodes Distance K in Binary Tree	二叉树中所有距离为 K 的结点	all-nodes-distance-k-in-binary-tree	weekly-contest-91	Q2
1662.7075394144	2550	Count Collisions of Monkeys on a Polygon	猴子碰撞的方法数	count-collisions-of-monkeys-on-a-polygon	weekly-contest-330	Q2
1662.6673692545	2170	Minimum Operations to Make the Array Alternating	使数组变成交替数组的最少操作数	minimum-operations-to-make-the-array-alternating	weekly-contest-280	Q2
1659.6231386056	3029	Minimum Time to Revert Word to Initial State I	将单词恢复初始状态所需的最短时间 I	minimum-time-to-revert-word-to-initial-state-i	weekly-contest-383	Q2
1658.9210227330	2195	Append K Integers With Minimal Sum	向数组中追加 K 个整数	append-k-integers-with-minimal-sum	weekly-contest-283	Q2
1658.8190087768	2915	Length of the Longest Subsequence That Sums to Target	和为目标值的最长子序列的长度	length-of-the-longest-subsequence-that-sums-to-target	biweekly-contest-116	Q3
1658.7495899767	1254	Number of Closed Islands	统计封闭岛屿的数目	number-of-closed-islands	weekly-contest-162	Q3
1658.6836278802	1169	Invalid Transactions	查询无效交易	invalid-transactions	weekly-contest-151	Q1
1658.5967147757	1958	Check if Move is Legal	检查操作是否合法	check-if-move-is-legal	biweekly-contest-58	Q2
1658.3530344788	2304	Minimum Path Cost in a Grid	网格中的最小路径代价	minimum-path-cost-in-a-grid	weekly-contest-297	Q2
1658.3474650806	1091	Shortest Path in Binary Matrix	二进制矩阵中的最短路径	shortest-path-in-binary-matrix	weekly-contest-141	Q3
1658.3305547865	1583	Count Unhappy Friends	统计不开心的朋友	count-unhappy-friends	weekly-contest-206	Q2
1657.5344546445	3015	Count the Number of Houses at a Certain Distance I	按距离统计房屋对数目 I	count-the-number-of-houses-at-a-certain-distance-i	weekly-contest-381	Q2
1657.1231739081	1249	Minimum Remove to Make Valid Parentheses	移除无效的括号	minimum-remove-to-make-valid-parentheses	weekly-contest-161	Q3
1656.5588918365	2222	Number of Ways to Select Buildings	选择建筑的方案数	number-of-ways-to-select-buildings	biweekly-contest-75	Q3
1655.6433885989	1004	Max Consecutive Ones III	最大连续1的个数 III	max-consecutive-ones-iii	weekly-contest-126	Q3
1654.0793660142	1257	Smallest Common Region	最小公共区域	smallest-common-region	biweekly-contest-13	Q2
1653.7337081336	1155	Number of Dice Rolls With Target Sum	掷骰子的N种方法	number-of-dice-rolls-with-target-sum	weekly-contest-149	Q2
1653.0356626499	1509	Minimum Difference Between Largest and Smallest Value in Three Moves	三次操作后最大值与最小值的最小差	minimum-difference-between-largest-and-smallest-value-in-three-moves	biweekly-contest-30	Q3
1652.5809810428	1311	Get Watched Videos by Your Friends	获取你好友已观看的视频	get-watched-videos-by-your-friends	weekly-contest-170	Q3
1651.5845871727	750	Number Of Corner Rectangles	角矩形的数量	number-of-corner-rectangles	weekly-contest-63	Q3
1651.5692678340	2343	Query Kth Smallest Trimmed Number	裁剪数字后查询第 K 小的数字	query-kth-smallest-trimmed-number	weekly-contest-302	Q3
1649.9728054796	1367	Linked List in Binary Tree	二叉树中的列表	linked-list-in-binary-tree	weekly-contest-178	Q3
1649.7120733311	2523	Closest Prime Numbers in Range	范围内最接近的两个质数	closest-prime-numbers-in-range	weekly-contest-326	Q4
1649.2000410344	2571	Minimum Operations to Reduce an Integer to 0	将整数减少到零需要的最少操作数	minimum-operations-to-reduce-an-integer-to-0	weekly-contest-333	Q2
1648.3540381514	2423	Remove Letter To Equalize Frequency	删除字符使频率相同	remove-letter-to-equalize-frequency	biweekly-contest-88	Q1
1648.3417578820	870	Advantage Shuffle	优势洗牌	advantage-shuffle	weekly-contest-93	Q3
1648.0880791614	1975	Maximum Matrix Sum	最大方阵和	maximum-matrix-sum	biweekly-contest-59	Q2
1646.1943237127	1358	Number of Substrings Containing All Three Characters	包含所有三种字符的子字符串数目	number-of-substrings-containing-all-three-characters	biweekly-contest-20	Q3
1646.1765343383	2226	Maximum Candies Allocated to K Children	每个小孩最多能分到多少糖果	maximum-candies-allocated-to-k-children	weekly-contest-287	Q3
1643.5283095007	2196	Create Binary Tree From Descriptions	根据描述创建二叉树	create-binary-tree-from-descriptions	weekly-contest-283	Q3
1643.1325351423	2024	Maximize the Confusion of an Exam	考试的最大困扰度	maximize-the-confusion-of-an-exam	biweekly-contest-62	Q3
1642.1446933109	2275	Largest Combination With Bitwise AND Greater Than Zero	按位与结果大于零的最长组合	largest-combination-with-bitwise-and-greater-than-zero	weekly-contest-293	Q3
1641.9424376927	2375	Construct Smallest Number From DI String	根据模式串构造最小数字	construct-smallest-number-from-di-string	weekly-contest-306	Q3
1640.9591585343	2187	Minimum Time to Complete Trips	完成旅途的最少时间	minimum-time-to-complete-trips	weekly-contest-282	Q3
1640.8976042503	2344	Minimum Deletions to Make Array Divisible	使数组可以被整除的最少删除次数	minimum-deletions-to-make-array-divisible	weekly-contest-302	Q4
1638.4147703093	2779	Maximum Beauty of an Array After Applying Operation	数组的最大美丽值	maximum-beauty-of-an-array-after-applying-operation	weekly-contest-354	Q2
1638.3134093066	1926	Nearest Exit from Entrance in Maze	迷宫中离入口最近的出口	nearest-exit-from-entrance-in-maze	biweekly-contest-56	Q2
1638.1281256708	838	Push Dominoes	推多米诺	push-dominoes	weekly-contest-85	Q2
1638.0148920643	990	Satisfiability of Equality Equations	等式方程的可满足性	satisfiability-of-equality-equations	weekly-contest-123	Q2
1637.0082208814	1558	Minimum Numbers of Function Calls to Make Target Array	得到目标数组的最少函数调用次数	minimum-numbers-of-function-calls-to-make-target-array	biweekly-contest-33	Q3
1636.7472106213	2512	Reward Top K Students	奖励最顶尖的 K 名学生	reward-top-k-students	biweekly-contest-94	Q2
1636.6877598712	1386	Cinema Seat Allocation	安排电影院座位	cinema-seat-allocation	biweekly-contest-22	Q2
1636.4732262700	2384	Largest Palindromic Number	最大回文数字	largest-palindromic-number	weekly-contest-307	Q2
1635.6879273926	1899	Merge Triplets to Form Target Triplet	合并若干三元组以形成目标三元组	merge-triplets-to-form-target-triplet	weekly-contest-245	Q3
1635.1520858279	2471	Minimum Number of Operations to Sort a Binary Tree by Level	逐层排序二叉树所需的最少操作数目	minimum-number-of-operations-to-sort-a-binary-tree-by-level	weekly-contest-319	Q3
1633.6202302555	1466	Reorder Routes to Make All Paths Lead to the City Zero	重新规划路线	reorder-routes-to-make-all-paths-lead-to-the-city-zero	weekly-contest-191	Q3
1633.1789521619	1053	Previous Permutation With One Swap	交换一次的先前排列	previous-permutation-with-one-swap	weekly-contest-138	Q3
1633.1372577433	1319	Number of Operations to Make Network Connected	连通网络的操作次数	number-of-operations-to-make-network-connected	weekly-contest-171	Q3
1632.0191837349	820	Short Encoding of Words	单词的压缩编码	short-encoding-of-words	weekly-contest-81	Q3
1631.5850830561	2580	Count Ways to Group Overlapping Ranges	统计将重叠区间合并成组的方案数	count-ways-to-group-overlapping-ranges	biweekly-contest-99	Q3
1631.3381456830	1540	Can Convert String in K Moves	K 次操作转变字符串	can-convert-string-in-k-moves	biweekly-contest-32	Q2
1629.5416832545	1680	Concatenation of Consecutive Binary Numbers	连接连续二进制数字	concatenation-of-consecutive-binary-numbers	weekly-contest-218	Q3
1628.5072578803	1332	Remove Palindromic Subsequences	删除回文子序列	remove-palindromic-subsequences	weekly-contest-173	Q1
1626.6740430119	1182	Shortest Distance to Target Color	与目标颜色间的最短距离	shortest-distance-to-target-color	biweekly-contest-8	Q3
1626.3266982141	1366	Rank Teams by Votes	通过投票对团队排名	rank-teams-by-votes	weekly-contest-178	Q2
1625.9636825798	2684	Maximum Number of Moves in a Grid	矩阵中移动的最大次数	maximum-number-of-moves-in-a-grid	weekly-contest-345	Q3
1625.7172632295	2860	Happy Students	让所有学生保持开心的分组方法数	happy-students	weekly-contest-363	Q2
1624.9775945043	785	Is Graph Bipartite?	判断二分图	is-graph-bipartite	weekly-contest-72	Q2
1624.4737611923	916	Word Subsets	单词子集	word-subsets	weekly-contest-104	Q3
1623.9443250479	1248	Count Number of Nice Subarrays	统计「优美子数组」	count-number-of-nice-subarrays	weekly-contest-161	Q2
1622.8414025136	2086	Minimum Number of Buckets Required to Collect Rainwater from Houses	从房屋收集雨水需要的最少水桶数	minimum-number-of-food-buckets-to-feed-the-hamsters	biweekly-contest-66	Q2
1622.7743864401	2365	Task Scheduler II	任务调度器 II	task-scheduler-ii	biweekly-contest-84	Q3
1622.3970914116	2425	Bitwise XOR of All Pairings	所有数对的异或和	bitwise-xor-of-all-pairings	biweekly-contest-88	Q3
1622.2389577197	2364	Count Number of Bad Pairs	统计坏数对的数目	count-number-of-bad-pairs	biweekly-contest-84	Q2
1619.5054619120	2541	Minimum Operations to Make Array Equal II	使数组中所有元素相等的最小操作数 II	minimum-operations-to-make-array-equal-ii	biweekly-contest-96	Q2
1618.6016480451	1503	Last Moment Before All Ants Fall Out of a Plank	所有蚂蚁掉下来前的最后一刻	last-moment-before-all-ants-fall-out-of-a-plank	weekly-contest-196	Q2
1616.2067360638	2241	Design an ATM Machine	设计一个 ATM 机器	design-an-atm-machine	biweekly-contest-76	Q3
1615.4767730477	1020	Number of Enclaves	飞地的数量	number-of-enclaves	weekly-contest-130	Q4
1614.4877804672	2145	Count the Hidden Sequences	统计隐藏数组数目	count-the-hidden-sequences	biweekly-contest-70	Q2
1613.2485081262	2766	Relocate Marbles	重新放置石块	relocate-marbles	biweekly-contest-108	Q2
1613.0429766636	1277	Count Square Submatrices with All Ones	统计全为 1 的正方形子矩阵	count-square-submatrices-with-all-ones	weekly-contest-165	Q3
1611.8434720083	2232	Minimize Result by Adding Parentheses to Expression	向表达式添加括号后的最小结果	minimize-result-by-adding-parentheses-to-expression	weekly-contest-288	Q2
1611.7621820686	789	Escape The Ghosts	逃脱阻碍者	escape-the-ghosts	weekly-contest-73	Q2
1610.5693981590	1524	Number of Sub-arrays With Odd Sum	和为奇数的子数组数目	number-of-sub-arrays-with-odd-sum	biweekly-contest-31	Q2
1610.1866391145	1670	Design Front Middle Back Queue	设计前中后队列	design-front-middle-back-queue	biweekly-contest-40	Q3
1609.7858209851	2438	Range Product Queries of Powers	二的幂数组中查询范围内的乘积	range-product-queries-of-powers	biweekly-contest-89	Q2
1608.5778758070	2567	Minimum Score by Changing Two Elements	修改两个元素的最小分数	minimum-score-by-changing-two-elements	biweekly-contest-98	Q2
1607.8060859500	962	Maximum Width Ramp	最大宽度坡	maximum-width-ramp	weekly-contest-116	Q2
1607.7036437819	2320	Count Number of Ways to Place Houses	统计放置房子的方式数	count-number-of-ways-to-place-houses	weekly-contest-299	Q2
1607.4192947808	2745	Construct the Longest New String	构造最长的新字符串	construct-the-longest-new-string	biweekly-contest-107	Q2
1607.0005715974	1123	Lowest Common Ancestor of Deepest Leaves	最深叶节点的最近公共祖先	lowest-common-ancestor-of-deepest-leaves	weekly-contest-145	Q2
1606.9895296459	1300	Sum of Mutated Array Closest to Target	转变数组后最接近目标值的数组和	sum-of-mutated-array-closest-to-target	biweekly-contest-16	Q2
1606.2185826486	1604	Alert Using Same Key-Card Three or More Times in a One Hour Period	警告一小时内使用相同员工卡大于等于三次的人	alert-using-same-key-card-three-or-more-times-in-a-one-hour-period	biweekly-contest-36	Q2
1604.9737380545	809	Expressive Words	情感丰富的文字	expressive-words	weekly-contest-78	Q2
1604.6299874552	2546	Apply Bitwise Operations to Make Strings Equal	执行逐位运算使字符串相等	apply-bitwise-operations-to-make-strings-equal	weekly-contest-329	Q3
1604.5128423093	2522	Partition String Into Substrings With Values at Most K	将字符串分割成值不超过 K 的子字符串	partition-string-into-substrings-with-values-at-most-k	weekly-contest-326	Q3
1604.1602280047	2424	Longest Uploaded Prefix	最长上传前缀	longest-uploaded-prefix	biweekly-contest-88	Q2
1604.0695445163	2316	Count Unreachable Pairs of Nodes in an Undirected Graph	统计无向图中无法互相到达点对数	count-unreachable-pairs-of-nodes-in-an-undirected-graph	biweekly-contest-81	Q2
1602.7742849665	2447	Number of Subarrays With GCD Equal to K	最大公因数等于 K 的子数组数目	number-of-subarrays-with-gcd-equal-to-k	weekly-contest-316	Q2
1602.7242171967	2249	Count Lattice Points Inside a Circle	统计圆内格点数目	count-lattice-points-inside-a-circle	weekly-contest-290	Q2
1601.7402292728	3047	Find the Largest Area of Square Inside Two Rectangles	求交集区域内的最大正方形面积	find-the-largest-area-of-square-inside-two-rectangles	weekly-contest-386	Q2
1601.5117605320	926	Flip String to Monotone Increasing	将字符串翻转到单调递增	flip-string-to-monotone-increasing	weekly-contest-107	Q2
1600.5573262373	1864	Minimum Number of Swaps to Make the Binary String Alternating	构成交替字符串需要的最小交换次数	minimum-number-of-swaps-to-make-the-binary-string-alternating	weekly-contest-241	Q2
1599.2720584736	1048	Longest String Chain	最长字符串链	longest-string-chain	weekly-contest-137	Q3
1597.5718383661	2750	Ways to Split Array Into Good Subarrays	将数组划分成若干好子数组的方式	ways-to-split-array-into-good-subarrays	weekly-contest-351	Q3
1597.1931473887	1218	Longest Arithmetic Subsequence of Given Difference	最长定差子序列	longest-arithmetic-subsequence-of-given-difference	weekly-contest-157	Q2
1597.0215918551	1247	Minimum Swaps to Make Strings Equal	交换字符使得字符串相同	minimum-swaps-to-make-strings-equal	weekly-contest-161	Q1
1596.9852244916	2476	Closest Nodes Queries in a Binary Search Tree	二叉搜索树最近节点查询	closest-nodes-queries-in-a-binary-search-tree	weekly-contest-320	Q2
1594.2563236049	822	Card Flipping Game	翻转卡片游戏	card-flipping-game	weekly-contest-81	Q2
1593.8926580448	1577	Number of Ways Where Square of Number Is Equal to Product of Two Numbers	数的平方等于两数乘积的方法数	number-of-ways-where-square-of-number-is-equal-to-product-of-two-numbers	weekly-contest-205	Q2
1591.5492530876	930	Binary Subarrays With Sum	和相同的二元子数组	binary-subarrays-with-sum	weekly-contest-108	Q2
1591.4725328821	1286	Iterator for Combination	字母组合迭代器	iterator-for-combination	biweekly-contest-15	Q3
1590.5791055102	969	Pancake Sorting	煎饼排序	pancake-sorting	weekly-contest-118	Q2
1590.5477136630	1573	Number of Ways to Split a String	分割字符串的方案数	number-of-ways-to-split-a-string	biweekly-contest-34	Q2
1590.2690308330	1664	Ways to Make a Fair Array	生成平衡数组的方案数	ways-to-make-a-fair-array	weekly-contest-216	Q3
1590.0883962313	893	Groups of Special-Equivalent Strings	特殊等价字符串组	groups-of-special-equivalent-strings	weekly-contest-99	Q2
1590.0463215721	877	Stone Game	石子游戏	stone-game	weekly-contest-95	Q2
1588.9690763997	1813	Sentence Similarity III	句子相似性 III	sentence-similarity-iii	biweekly-contest-49	Q2
1588.4826339516	2844	Minimum Operations to Make a Special Number	生成特殊数字的最少操作	minimum-operations-to-make-a-special-number	weekly-contest-361	Q2
1588.3835994255	1764	Form Array by Concatenating Subarrays of Another Array	通过连接另一个数组的子数组得到一个数组	form-array-by-concatenating-subarrays-of-another-array	biweekly-contest-46	Q2
1585.5793143983	1030	Matrix Cells in Distance Order	距离顺序排列矩阵单元格	matrix-cells-in-distance-order	weekly-contest-133	Q2
1583.3117784523	2536	Increment Submatrices by One	子矩阵元素加 1	increment-submatrices-by-one	weekly-contest-328	Q2
1583.2129662240	2874	Maximum Value of an Ordered Triplet II	有序三元组中的最大值 II	maximum-value-of-an-ordered-triplet-ii	weekly-contest-365	Q2
1581.4963716166	2211	Count Collisions on a Road	统计道路上的碰撞次数	count-collisions-on-a-road	weekly-contest-285	Q2
1581.4162718925	3021	Alice and Bob Playing Flower Game	Alice 和 Bob 玩鲜花游戏	alice-and-bob-playing-flower-game	weekly-contest-382	Q3
1580.9748095835	2765	Longest Alternating Subarray	最长交替子序列	longest-alternating-subarray	biweekly-contest-108	Q1
1580.3620959714	1839	Longest Substring Of All Vowels in Order	所有元音按顺序排布的最长子字符串	longest-substring-of-all-vowels-in-order	weekly-contest-238	Q3
1579.2309881035	1743	Restore the Array From Adjacent Pairs	从相邻元素对还原数组	restore-the-array-from-adjacent-pairs	weekly-contest-226	Q2
1578.8503818621	1034	Coloring A Border	边框着色	coloring-a-border	weekly-contest-134	Q2
1577.1141767118	2288	Apply Discount to Prices	价格减免	apply-discount-to-prices	weekly-contest-295	Q2
1575.6324598387	1415	The k-th Lexicographical String of All Happy Strings of Length n	长度为 n 的开心字符串中字典序第 k 小的字符串	the-k-th-lexicographical-string-of-all-happy-strings-of-length-n	biweekly-contest-24	Q3
1574.7542247682	981	Time Based Key-Value Store	基于时间的键值存储	time-based-key-value-store	weekly-contest-121	Q2
1574.0392121288	1578	Minimum Deletion Cost to Avoid Repeating Letters	避免重复字母的最小删除成本	minimum-time-to-make-rope-colorful	weekly-contest-205	Q3
1573.8248079460	1423	Maximum Points You Can Obtain from Cards	可获得的最大点数	maximum-points-you-can-obtain-from-cards	weekly-contest-186	Q2
1573.4042963622	1268	Search Suggestions System	搜索推荐系统	search-suggestions-system	weekly-contest-164	Q3
1573.2701790739	931	Minimum Falling Path Sum	下降路径最小和	minimum-falling-path-sum	weekly-contest-108	Q3
1571.1721048101	779	K-th Symbol in Grammar	第K个语法符号	k-th-symbol-in-grammar	weekly-contest-70	Q1
1570.8347522104	1019	Next Greater Node In Linked List	链表中的下一个更大节点	next-greater-node-in-linked-list	weekly-contest-130	Q3
1569.7528744586	1109	Corporate Flight Bookings	航班预订统计	corporate-flight-bookings	weekly-contest-144	Q2
1569.1579260438	2592	Maximize Greatness of an Array	最大化数组的伟大值	maximize-greatness-of-an-array	biweekly-contest-100	Q2
1567.6884942977	2044	Count Number of Maximum Bitwise-OR Subsets	统计按位或能得到最大值的子集数目	count-number-of-maximum-bitwise-or-subsets	weekly-contest-263	Q3
1566.2526716951	769	Max Chunks To Make Sorted	最多能完成排序的块	max-chunks-to-make-sorted	weekly-contest-68	Q3
1565.2483424929	846	Hand of Straights	一手顺子	hand-of-straights	weekly-contest-87	Q3
1563.9451046163	800	Similar RGB Color	相似 RGB 颜色	similar-rgb-color	weekly-contest-76	Q1
1563.2283814548	2970	Count the Number of Incremovable Subarrays I	统计移除递增子数组的数目 I	count-the-number-of-incremovable-subarrays-i	biweekly-contest-120	Q1
1562.9802666517	1008	Construct Binary Search Tree from Preorder Traversal	前序遍历构造二叉搜索树	construct-binary-search-tree-from-preorder-traversal	weekly-contest-127	Q4
1562.9186033202	1452	People Whose List of Favorite Companies Is Not a Subset of Another List	收藏清单	people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list	weekly-contest-189	Q3
1562.7212466716	856	Score of Parentheses	括号的分数	score-of-parentheses	weekly-contest-90	Q2
1562.0956544608	2409	Count Days Spent Together	统计共同度过的日子数	count-days-spent-together	biweekly-contest-87	Q1
1561.2655635205	1256	Encode Number	加密数字	encode-number	biweekly-contest-13	Q1
1561.0553908973	1376	Time Needed to Inform All Employees	通知所有员工所需的时间	time-needed-to-inform-all-employees	weekly-contest-179	Q3
1559.9709348417	2470	Number of Subarrays With LCM Equal to K	最小公倍数为 K 的子数组数目	number-of-subarrays-with-lcm-equal-to-k	weekly-contest-319	Q2
1558.9522968448	2310	Sum of Numbers With Units Digit K	个位数字为 K 的整数之和	sum-of-numbers-with-units-digit-k	weekly-contest-298	Q2
1558.7188539503	1144	Decrease Elements To Make Array Zigzag	递减元素使数组呈锯齿状	decrease-elements-to-make-array-zigzag	weekly-contest-148	Q1
1558.6880035344	1181	Before and After Puzzle	前后拼接	before-and-after-puzzle	biweekly-contest-8	Q2
1558.4971807039	1101	The Earliest Moment When Everyone Become Friends	彼此熟识的最早时间	the-earliest-moment-when-everyone-become-friends	biweekly-contest-3	Q3
1558.1421869292	1243	Array Transformation	数组变换	array-transformation	biweekly-contest-12	Q2
1557.0170555820	2007	Find Original Array From Doubled Array	从双倍数组中还原原数组	find-original-array-from-doubled-array	biweekly-contest-61	Q2
1556.8824239708	2131	Longest Palindrome by Concatenating Two Letter Words	连接两字母单词得到的最长回文串	longest-palindrome-by-concatenating-two-letter-words	biweekly-contest-69	Q3
1552.8935571247	2461	Maximum Sum of Distinct Subarrays With Length K	长度为 K 子数组中的最大和	maximum-sum-of-distinct-subarrays-with-length-k	weekly-contest-318	Q2
1550.4297615307	2207	Maximize Number of Subsequences in a String	字符串中最多数目的子字符串	maximize-number-of-subsequences-in-a-string	biweekly-contest-74	Q2
1550.0978082682	2208	Minimum Operations to Halve Array Sum	将数组和减半的最少操作次数	minimum-operations-to-halve-array-sum	biweekly-contest-74	Q3
1549.9747683007	2780	Minimum Index of a Valid Split	合法分割的最小下标	minimum-index-of-a-valid-split	weekly-contest-354	Q3
1549.9450401840	2527	Find Xor-Beauty of Array	查询数组 Xor 美丽值	find-xor-beauty-of-array	biweekly-contest-95	Q3
1548.4678056182	1329	Sort the Matrix Diagonally	将矩阵按对角线排序	sort-the-matrix-diagonally	biweekly-contest-18	Q3
1548.1751146981	2456	Most Popular Video Creator	最流行的视频创作者	most-popular-video-creator	weekly-contest-317	Q2
1548.0854419238	1599	Maximum Profit of Operating a Centennial Wheel	经营摩天轮的最大利润	maximum-profit-of-operating-a-centennial-wheel	weekly-contest-208	Q2
1547.5714796512	954	Array of Doubled Pairs	二倍数对数组	array-of-doubled-pairs	weekly-contest-114	Q2
1547.0385279086	758	Bold Words in String	字符串中的加粗单词	bold-words-in-string	weekly-contest-66	Q2
1545.9654593951	2841	Maximum Sum of Almost Unique Subarray	几乎唯一子数组的最大和	maximum-sum-of-almost-unique-subarray	biweekly-contest-112	Q3
1544.8391626032	1104	Path In Zigzag Labelled Binary Tree	二叉树寻路	path-in-zigzag-labelled-binary-tree	weekly-contest-143	Q2
1544.8261365027	1233	Remove Sub-Folders from the Filesystem	删除子文件夹	remove-sub-folders-from-the-filesystem	weekly-contest-159	Q2
1544.6371526659	794	Valid Tic-Tac-Toe State	有效的井字游戏	valid-tic-tac-toe-state	weekly-contest-74	Q1
1543.1204810684	2811	Check if it is Possible to Split Array	判断是否能拆分数组	check-if-it-is-possible-to-split-array	weekly-contest-357	Q2
1542.5630367445	812	Largest Triangle Area	最大三角形面积	largest-triangle-area	weekly-contest-79	Q1
1541.7840320661	1283	Find the Smallest Divisor Given a Threshold	使结果不超过阈值的最小除数	find-the-smallest-divisor-given-a-threshold	weekly-contest-166	Q3
1541.6944600975	986	Interval List Intersections	区间列表的交集	interval-list-intersections	weekly-contest-122	Q3
1541.6176288991	1749	Maximum Absolute Sum of Any Subarray	任意子数组和的绝对值的最大值	maximum-absolute-sum-of-any-subarray	biweekly-contest-45	Q2
1541.5405749918	1209	Remove All Adjacent Duplicates in String II	删除字符串中的所有相邻重复项 II	remove-all-adjacent-duplicates-in-string-ii	weekly-contest-156	Q3
1541.3741526845	2575	Find the Divisibility Array of a String	找出字符串的可整除数组	find-the-divisibility-array-of-a-string	weekly-contest-334	Q2
1541.3484385090	1007	Minimum Domino Rotations For Equal Row	行相等的最少多米诺旋转	minimum-domino-rotations-for-equal-row	weekly-contest-127	Q3
1541.2260256298	1229	Meeting Scheduler	安排会议日程	meeting-scheduler	biweekly-contest-11	Q2
1540.5750839091	1382	Balance a Binary Search Tree	将二叉搜索树变平衡	balance-a-binary-search-tree	weekly-contest-180	Q3
1540.2351411176	2349	Design a Number Container System	设计数字容器系统	design-a-number-container-system	biweekly-contest-83	Q3
1539.2250193318	1992	Find All Groups of Farmland	找到所有的农场组	find-all-groups-of-farmland	biweekly-contest-60	Q2
1538.2331497040	2178	Maximum Split of Positive Even Integers	拆分成最多数目的偶整数之和	maximum-split-of-positive-even-integers	biweekly-contest-72	Q3
1537.1387686755	1023	Camelcase Matching	驼峰式匹配	camelcase-matching	weekly-contest-131	Q3
1536.7018543075	1861	Rotating the Box	旋转盒子	rotating-the-box	biweekly-contest-52	Q3
1536.5893223179	2933	High-Access Employees	高访问员工	high-access-employees	weekly-contest-371	Q2
1535.3680469616	2958	Length of Longest Subarray With at Most K Frequency	最多 K 个重复元素的最长子数组	length-of-longest-subarray-with-at-most-k-frequency	biweekly-contest-119	Q3
1534.3250051510	865	Smallest Subtree with all the Deepest Nodes	具有所有最深节点的最小子树	smallest-subtree-with-all-the-deepest-nodes	weekly-contest-92	Q2
1534.0648719302	1797	Design Authentication Manager	设计一个验证系统	design-authentication-manager	biweekly-contest-48	Q2
1533.9285875234	1362	Closest Divisors	最接近的因数	closest-divisors	weekly-contest-177	Q3
1533.5722750742	3016	Minimum Number of Pushes to Type Word II	输入单词需要的最少按键次数 II	minimum-number-of-pushes-to-type-word-ii	weekly-contest-381	Q3
1533.4738366200	2770	Maximum Number of Jumps to Reach the Last Index	达到末尾下标所需的最大跳跃次数	maximum-number-of-jumps-to-reach-the-last-index	weekly-contest-353	Q2
1533.3376144199	1930	Unique Length-3 Palindromic Subsequences	长度为 3 的不同回文子序列	unique-length-3-palindromic-subsequences	weekly-contest-249	Q2
1532.3349133769	2429	Minimize XOR	最小 XOR	minimize-xor	weekly-contest-313	Q3
1532.2539947529	900	RLE Iterator	RLE 迭代器	rle-iterator	weekly-contest-101	Q1
1530.6451141787	2591	Distribute Money to Maximum Children	将钱分给最多的儿童	distribute-money-to-maximum-children	biweekly-contest-100	Q1
1530.4954397880	1400	Construct K Palindrome Strings	构造 K 个回文字符串	construct-k-palindrome-strings	biweekly-contest-23	Q2
1530.4652027753	1657	Determine if Two Strings Are Close	确定两个字符串是否接近	determine-if-two-strings-are-close	weekly-contest-215	Q2
1530.0343519239	1726	Tuple with Same Product	同积元组	tuple-with-same-product	weekly-contest-224	Q2
1529.7617243868	881	Boats to Save People	救生艇	boats-to-save-people	weekly-contest-96	Q2
1528.7183829005	1695	Maximum Erasure Value	删除子数组的最大得分	maximum-erasure-value	weekly-contest-220	Q2
1527.6868660176	1921	Eliminate Maximum Number of Monsters	消灭怪物的最大数量	eliminate-maximum-number-of-monsters	weekly-contest-248	Q2
1526.2429110307	2918	Minimum Equal Sum of Two Arrays After Replacing Zeros	数组的最小相等和	minimum-equal-sum-of-two-arrays-after-replacing-zeros	weekly-contest-369	Q2
1525.2146106195	2201	Count Artifacts That Can Be Extracted	统计可以提取的工件	count-artifacts-that-can-be-extracted	weekly-contest-284	Q2
1524.8218282113	1272	Remove Interval	删除区间	remove-interval	biweekly-contest-14	Q2
1524.5856276651	2997	Minimum Number of Operations to Make Array XOR Equal to K	使数组异或和等于 K 的最少操作次数	minimum-number-of-operations-to-make-array-xor-equal-to-k	biweekly-contest-121	Q2
1524.5693481538	1442	Count Triplets That Can Form Two Arrays of Equal XOR	形成两个异或相等数组的三元组数目	count-triplets-that-can-form-two-arrays-of-equal-xor	weekly-contest-188	Q2
1524.3227469000	1640	Check Array Formation Through Concatenation	能否连接形成数组	check-array-formation-through-concatenation	weekly-contest-213	Q1
1523.4113866454	1829	Maximum XOR for Each Query	每个查询的最大异或值	maximum-xor-for-each-query	biweekly-contest-50	Q3
1521.9977490324	1615	Maximal Network Rank	最大网络秩	maximal-network-rank	weekly-contest-210	Q2
1521.7133617698	1763	Longest Nice Substring	最长的美好子字符串	longest-nice-substring	biweekly-contest-46	Q1
1521.1768537583	1041	Robot Bounded In Circle	困于环中的机器人	robot-bounded-in-circle	weekly-contest-136	Q1
1521.1616133347	2971	Find Polygon With the Largest Perimeter	找到最大周长的多边形	find-polygon-with-the-largest-perimeter	biweekly-contest-120	Q2
1519.2070276362	2865	Beautiful Towers I	美丽塔 I	beautiful-towers-i	weekly-contest-364	Q2
1519.1715594347	1641	Count Sorted Vowel Strings	统计字典序元音字符串的数目	count-sorted-vowel-strings	weekly-contest-213	Q2
1517.8263048447	2683	Neighboring Bitwise XOR	相邻值的按位异或	neighboring-bitwise-xor	weekly-contest-345	Q2
1516.8229485853	775	Global and Local Inversions	全局倒置与局部倒置	global-and-local-inversions	weekly-contest-69	Q2
1516.4104902196	904	Fruit Into Baskets	水果成篮	fruit-into-baskets	weekly-contest-102	Q2
1515.1162664342	2849	Determine if a Cell Is Reachable at a Given Time	判断能否在给定时间到达单元格	determine-if-a-cell-is-reachable-at-a-given-time	weekly-contest-362	Q2
1514.8181710611	1855	Maximum Distance Between a Pair of Values	下标对中的最大距离	maximum-distance-between-a-pair-of-values	weekly-contest-240	Q2
1512.3323577063	1557	Minimum Number of Vertices to Reach All Nodes	可以到达所有点的最少点数目	minimum-number-of-vertices-to-reach-all-nodes	biweekly-contest-33	Q2
1511.3725353467	1110	Delete Nodes And Return Forest	删点成林	delete-nodes-and-return-forest	weekly-contest-144	Q3
1509.6237874441	2671	Frequency Tracker	频率跟踪器	frequency-tracker	weekly-contest-344	Q2
1509.5562928491	2216	Minimum Deletions to Make Array Beautiful	美化数组的最少删除数	minimum-deletions-to-make-array-beautiful	weekly-contest-286	Q2
1509.5432131875	1647	Minimum Deletions to Make Character Frequencies Unique	字符频次唯一的最小删除次数	minimum-deletions-to-make-character-frequencies-unique	weekly-contest-214	Q2
1508.1169489285	1151	Minimum Swaps to Group All 1's Together	最少交换次数来组合所有的 1	minimum-swaps-to-group-all-1s-together	biweekly-contest-6	Q2
1508.0997658270	1496	Path Crossing	判断路径是否相交	path-crossing	weekly-contest-195	Q1
1507.8701119064	892	Surface Area of 3D Shapes	三维形体的表面积	surface-area-of-3d-shapes	weekly-contest-99	Q1
1507.1617507911	2105	Watering Plants II	给植物浇水 II	watering-plants-ii	weekly-contest-271	Q3
1506.8958220609	1387	Sort Integers by The Power Value	将整数按权重排序	sort-integers-by-the-power-value	biweekly-contest-22	Q3
1505.8669082864	1253	Reconstruct a 2-Row Binary Matrix	重构 2 行二进制矩阵	reconstruct-a-2-row-binary-matrix	weekly-contest-162	Q2
1505.8249995300	1780	Check if Number is a Sum of Powers of Three	判断一个数字是否可以表示成三的幂的和	check-if-number-is-a-sum-of-powers-of-three	biweekly-contest-47	Q2
1505.3120825678	2981	Find Longest Special Substring That Occurs Thrice I	找出出现至少三次的最长特殊子字符串 I	find-longest-special-substring-that-occurs-thrice-i	weekly-contest-378	Q2
1504.9263037499	2761	Prime Pairs With Target Sum	和等于目标值的质数对	prime-pairs-with-target-sum	weekly-contest-352	Q2
1504.8237159326	869	Reordered Power of 2	重新排序得到 2 的幂	reordered-power-of-2	weekly-contest-93	Q2
1504.2133321504	2104	Sum of Subarray Ranges	子数组范围和	sum-of-subarray-ranges	weekly-contest-271	Q2
1504.0178888667	1461	Check If a String Contains All Binary Codes of Size K	检查一个字符串是否包含所有长度为 K 的二进制子串	check-if-a-string-contains-all-binary-codes-of-size-k	biweekly-contest-27	Q2
1502.6623568929	2661	First Completely Painted Row or Column	找出叠涂元素	first-completely-painted-row-or-column	weekly-contest-343	Q2
1502.5363677723	2358	Maximum Number of Groups Entering a Competition	分组的最大数量	maximum-number-of-groups-entering-a-competition	weekly-contest-304	Q2
1502.2633100489	2708	Maximum Strength of a Group	一个小组的最大实力值	maximum-strength-of-a-group	biweekly-contest-105	Q3
1501.9080845668	2730	Find the Longest Semi-Repetitive Substring	找到最长的半重复子字符串	find-the-longest-semi-repetitive-substring	biweekly-contest-106	Q2
1501.6846714598	1750	Minimum Length of String After Deleting Similar Ends	删除字符串两端相同字符后的最短长度	minimum-length-of-string-after-deleting-similar-ends	biweekly-contest-45	Q3
1501.1152614679	1090	Largest Values From Labels	受标签影响的最大值	largest-values-from-labels	weekly-contest-141	Q2
1500.8381829812	915	Partition Array into Disjoint Intervals	分割数组	partition-array-into-disjoint-intervals	weekly-contest-104	Q2
1499.7136257352	1525	Number of Good Ways to Split a String	字符串的好分割数目	number-of-good-ways-to-split-a-string	biweekly-contest-31	Q3
1499.5903720292	2507	Smallest Value After Replacing With Sum of Prime Factors	使用质因数之和替换后可以取到的最小值	smallest-value-after-replacing-with-sum-of-prime-factors	weekly-contest-324	Q2
1499.3290269267	1968	Array With Elements Not Equal to Average of Neighbors	构造元素不等于两相邻元素平均值的数组	array-with-elements-not-equal-to-average-of-neighbors	weekly-contest-254	Q2
1498.1542511841	1904	The Number of Full Rounds You Have Played	你完成的完整对局数	the-number-of-full-rounds-you-have-played	weekly-contest-246	Q2
1497.8880991093	998	Maximum Binary Tree II	最大二叉树 II	maximum-binary-tree-ii	weekly-contest-125	Q3
1496.9128643588	1208	Get Equal Substrings Within Budget	尽可能使字符串相等	get-equal-substrings-within-budget	weekly-contest-156	Q2
1496.6441112156	3011	Find if Array Can Be Sorted	判断一个数组是否可以变为有序	find-if-array-can-be-sorted	biweekly-contest-122	Q2
1496.2502937005	2285	Maximum Total Importance of Roads	道路的最大总重要性	maximum-total-importance-of-roads	biweekly-contest-79	Q3
1496.1462748679	2191	Sort the Jumbled Numbers	将杂乱无章的数字排序	sort-the-jumbled-numbers	biweekly-contest-73	Q2
1495.7157408280	1685	Sum of Absolute Differences in a Sorted Array	有序数组中差绝对值之和	sum-of-absolute-differences-in-a-sorted-array	biweekly-contest-41	Q2
1495.5180147817	2419	Longest Subarray With Maximum Bitwise AND	按位与最大的最长子数组	longest-subarray-with-maximum-bitwise-and	weekly-contest-312	Q2
1495.3186477678	949	Largest Time for Given Digits	给定数字能组成的最大时间	largest-time-for-given-digits	weekly-contest-113	Q1
1494.5007495980	2483	Minimum Penalty for a Shop	商店的最少代价	minimum-penalty-for-a-shop	biweekly-contest-92	Q3
1491.4638194905	1806	Minimum Number of Operations to Reinitialize a Permutation	还原排列的最少操作步数	minimum-number-of-operations-to-reinitialize-a-permutation	weekly-contest-234	Q2
1490.8990184504	1759	Count Number of Homogenous Substrings	统计同构子字符串的数目	count-number-of-homogenous-substrings	weekly-contest-228	Q2
1490.2370387981	1296	Divide Array in Sets of K Consecutive Numbers	划分数组为连续数字的集合	divide-array-in-sets-of-k-consecutive-numbers	weekly-contest-168	Q2
1489.7210915287	2658	Maximum Number of Fish in a Grid	网格图中鱼的最大数目	maximum-number-of-fish-in-a-grid	biweekly-contest-103	Q3
1489.0102202162	1175	Prime Arrangements	质数排列	prime-arrangements	weekly-contest-152	Q1
1487.5826663483	1753	Maximum Score From Removing Stones	移除石子的最大得分	maximum-score-from-removing-stones	weekly-contest-227	Q2
1486.7649334310	1637	Widest Vertical Area Between Two Points Containing No Points	两点之间不包含任何点的最宽垂直面积	widest-vertical-area-between-two-points-containing-no-points	biweekly-contest-38	Q2
1486.4687014051	1566	Detect Pattern of Length M Repeated K or More Times	重复至少 K 次且长度为 M 的模式	detect-pattern-of-length-m-repeated-k-or-more-times	weekly-contest-204	Q1
1486.2147876747	2840	Check if Strings Can be Made Equal With Operations II	判断通过操作能否让字符串相等 II	check-if-strings-can-be-made-equal-with-operations-ii	biweekly-contest-112	Q2
1485.6550472186	1190	Reverse Substrings Between Each Pair of Parentheses	反转每对括号间的子串	reverse-substrings-between-each-pair-of-parentheses	weekly-contest-154	Q2
1485.1354012690	1418	Display Table of Food Orders in a Restaurant	点菜展示表	display-table-of-food-orders-in-a-restaurant	weekly-contest-185	Q2
1484.8385256564	2789	Largest Element in an Array after Merge Operations	合并后数组中的最大元素	largest-element-in-an-array-after-merge-operations	weekly-contest-355	Q2
1483.8137189709	1314	Matrix Block Sum	矩阵区域和	matrix-block-sum	biweekly-contest-17	Q2
1483.3041242255	2904	Shortest and Lexicographically Smallest Beautiful String	最短且字典序最小的美丽子字符串	shortest-and-lexicographically-smallest-beautiful-string	weekly-contest-367	Q2
1481.9608077860	1807	Evaluate the Bracket Pairs of a String	替换字符串中的括号内容	evaluate-the-bracket-pairs-of-a-string	weekly-contest-234	Q3
1481.5701319876	1167	Minimum Cost to Connect Sticks	连接棒材的最低费用	minimum-cost-to-connect-sticks	biweekly-contest-7	Q3
1481.1046340847	2380	Time Needed to Rearrange a Binary String	二进制字符串重新安排顺序需要的时间	time-needed-to-rearrange-a-binary-string	biweekly-contest-85	Q2
1480.1120711991	3006	Find Beautiful Indices in the Given Array I	找出数组中的美丽下标 I	find-beautiful-indices-in-the-given-array-i	weekly-contest-380	Q2
1480.1116248664	1087	Brace Expansion	花括号展开	brace-expansion	biweekly-contest-2	Q3
1479.9828219111	2501	Longest Square Streak in an Array	数组中最长的方波	longest-square-streak-in-an-array	weekly-contest-323	Q2
1479.6908339113	2914	Minimum Number of Changes to Make Binary String Beautiful	使二进制字符串变美丽的最少修改次数	minimum-number-of-changes-to-make-binary-string-beautiful	biweekly-contest-116	Q2
1479.4837595809	1545	Find Kth Bit in Nth Binary String	找出第 N 个二进制字符串中的第 K 位	find-kth-bit-in-nth-binary-string	weekly-contest-201	Q2
1479.0110934646	1166	Design File System	设计文件系统	design-file-system	biweekly-contest-7	Q2
1478.8676835951	2909	Minimum Sum of Mountain Triplets II	元素和最小的山形三元组 II	minimum-sum-of-mountain-triplets-ii	weekly-contest-368	Q2
1478.3848028264	1390	Four Divisors	四因数	four-divisors	weekly-contest-181	Q2
1477.7669322402	2645	Minimum Additions to Make Valid String	构造有效字符串的最少插入数	minimum-additions-to-make-valid-string	weekly-contest-341	Q3
1477.4844514104	951	Flip Equivalent Binary Trees	翻转等价二叉树	flip-equivalent-binary-trees	weekly-contest-113	Q2
1476.9118898539	2368	Reachable Nodes With Restrictions	受限条件下可到达节点的数目	reachable-nodes-with-restrictions	weekly-contest-305	Q2
1476.9062320302	2300	Successful Pairs of Spells and Potions	咒语和药水的成功对数	successful-pairs-of-spells-and-potions	biweekly-contest-80	Q2
1474.0150725665	984	String Without AAA or BBB	不含 AAA 或 BBB 的字符串	string-without-aaa-or-bbb	weekly-contest-121	Q1
1473.8649930450	1328	Break a Palindrome	破坏回文串	break-a-palindrome	biweekly-contest-18	Q2
1473.7057465272	1352	Product of the Last K Numbers	最后 K 个数的乘积	product-of-the-last-k-numbers	weekly-contest-176	Q2
1473.2523136772	897	Increasing Order Search Tree	递增顺序查找树	increasing-order-search-tree	weekly-contest-100	Q2
1472.7864965062	2265	Count Nodes Equal to Average of Subtree	统计值等于子树平均值的节点数	count-nodes-equal-to-average-of-subtree	weekly-contest-292	Q2
1471.8964024887	2047	Number of Valid Words in a Sentence	句子中的有效单词数	number-of-valid-words-in-a-sentence	weekly-contest-264	Q1
1471.6221713607	1093	Statistics from a Large Sample	大样本统计	statistics-from-a-large-sample	weekly-contest-142	Q1
1468.8739273624	2900	Longest Unequal Adjacent Groups Subsequence I	最长相邻不相等子序列 I	longest-unequal-adjacent-groups-subsequence-i	biweekly-contest-115	Q2
1467.9366439696	2012	Sum of Beauty in the Array	数组美丽值求和	sum-of-beauty-in-the-array	weekly-contest-259	Q2
1467.7383709213	2038	Remove Colored Pieces if Both Neighbors are the Same Color	如果相邻两个颜色均相同则删除当前颜色	remove-colored-pieces-if-both-neighbors-are-the-same-color	biweekly-contest-63	Q2
1465.7023558248	1414	Find the Minimum Number of Fibonacci Numbers Whose Sum Is K	和为 K 的最少斐波那契数字数目	find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k	biweekly-contest-24	Q2
1464.6895034875	1361	Validate Binary Tree Nodes	验证二叉树	validate-binary-tree-nodes	weekly-contest-177	Q2
1464.5254961488	1396	Design Underground System	设计地铁系统	design-underground-system	weekly-contest-182	Q3
1462.4423844498	1022	Sum of Root To Leaf Binary Numbers	从根到叶的二进制数之和	sum-of-root-to-leaf-binary-numbers	weekly-contest-131	Q2
1461.9157715206	946	Validate Stack Sequences	验证栈序列	validate-stack-sequences	weekly-contest-112	Q2
1461.2892510067	1909	Remove One Element to Make the Array Strictly Increasing	删除一个元素使数组严格递增	remove-one-element-to-make-the-array-strictly-increasing	biweekly-contest-55	Q1
1460.9610936441	833	Find And Replace in String	字符串中的查找与替换	find-and-replace-in-string	weekly-contest-84	Q2
1460.9105672071	1910	Remove All Occurrences of a Substring	删除一个字符串中所有出现的给定子字符串	remove-all-occurrences-of-a-substring	biweekly-contest-55	Q2
1460.5903088359	1663	Smallest String With A Given Numeric Value	具有给定数值的最小字符串	smallest-string-with-a-given-numeric-value	weekly-contest-216	Q2
1459.8208951847	1310	XOR Queries of a Subarray	子数组异或查询	xor-queries-of-a-subarray	weekly-contest-170	Q2
1459.7513584849	2452	Words Within Two Edits of Dictionary	距离字典两次编辑以内的单词	words-within-two-edits-of-dictionary	biweekly-contest-90	Q2
1458.3564930390	2062	Count Vowel Substrings of a String	统计字符串中的元音子字符串	count-vowel-substrings-of-a-string	weekly-contest-266	Q1
1455.8516200241	2391	Minimum Amount of Time to Collect Garbage	收集垃圾的最少总时间	minimum-amount-of-time-to-collect-garbage	weekly-contest-308	Q3
1454.7459647138	2094	Finding 3-Digit Even Numbers	找出 3 位偶数	finding-3-digit-even-numbers	weekly-contest-270	Q1
1454.5942017003	2487	Remove Nodes From Linked List	从链表中移除节点	remove-nodes-from-linked-list	weekly-contest-321	Q3
1454.3901912166	1846	Maximum Element After Decreasing and Rearranging	减小和重新排列数组后的最大元素	maximum-element-after-decreasing-and-rearranging	biweekly-contest-51	Q3
1453.7818053022	1472	Design Browser History	设计浏览器历史记录	design-browser-history	weekly-contest-192	Q3
1453.1833769825	781	Rabbits in Forest	森林中的兔子	rabbits-in-forest	weekly-contest-71	Q2
1450.8514438667	2947	Count Beautiful Substrings I	统计美丽子字符串 I	count-beautiful-substrings-i	weekly-contest-373	Q2
1450.6986543984	2961	Double Modular Exponentiation	双模幂运算	double-modular-exponentiation	weekly-contest-375	Q2
1450.5787293419	831	Masking Personal Information	隐藏个人信息	masking-personal-information	weekly-contest-83	Q2
1450.0534545623	2511	Maximum Enemy Forts That Can Be Captured	最多可以摧毁的敌人城堡数目	maximum-enemy-forts-that-can-be-captured	biweekly-contest-94	Q1
1448.1865030721	2596	Check Knight Tour Configuration	检查骑士巡视方案	check-knight-tour-configuration	weekly-contest-337	Q2
1448.1207963663	945	Minimum Increment to Make Array Unique	使数组唯一的最小增量	minimum-increment-to-make-array-unique	weekly-contest-112	Q1
1447.0268321102	2099	Find Subsequence of Length K With the Largest Sum	找到和最大的长度为 K 的子序列	find-subsequence-of-length-k-with-the-largest-sum	biweekly-contest-67	Q1
1446.4280778775	1026	Maximum Difference Between Node and Ancestor	节点与其祖先之间的最大差值	maximum-difference-between-node-and-ancestor	weekly-contest-132	Q2
1445.3734269673	1946	Largest Number After Mutating Substring	子字符串突变后可能得到的最大整数	largest-number-after-mutating-substring	weekly-contest-251	Q2
1445.1422945604	2295	Replace Elements in an Array	替换数组中的元素	replace-elements-in-an-array	weekly-contest-296	Q3
1444.6795731919	2028	Find Missing Observations	找出缺失的观测数据	find-missing-observations	weekly-contest-261	Q2
1444.6098846511	1465	Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts	切割后面积最大的蛋糕	maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts	weekly-contest-191	Q2
1444.3218903725	2526	Find Consecutive Integers from a Data Stream	找到数据流中的连续整数	find-consecutive-integers-from-a-data-stream	biweekly-contest-95	Q2
1444.2068009303	942	DI String Match	增减字符串匹配	di-string-match	weekly-contest-111	Q3
1443.2353621969	1560	Most Visited Sector in  a Circular Track	圆形赛道上经过次数最多的扇区	most-visited-sector-in-a-circular-track	weekly-contest-203	Q1
1443.0697629277	763	Partition Labels	划分字母区间	partition-labels	weekly-contest-67	Q2
1442.9468304752	836	Rectangle Overlap	矩形重叠	rectangle-overlap	weekly-contest-85	Q1
1441.4290319373	1094	Car Pooling	拼车	car-pooling	weekly-contest-142	Q2
1439.5656079032	1261	Find Elements in a Contaminated Binary Tree	在受污染的二叉树中查找元素	find-elements-in-a-contaminated-binary-tree	weekly-contest-163	Q2
1438.8988489545	1375	Number of Times Binary String Is Prefix-Aligned	二进制字符串前缀一致的次数	number-of-times-binary-string-is-prefix-aligned	weekly-contest-179	Q2
1438.2231359050	1609	Even Odd Tree	奇偶树	even-odd-tree	weekly-contest-209	Q2
1436.5343999134	845	Longest Mountain in Array	数组中的最长山脉	longest-mountain-in-array	weekly-contest-87	Q2
1436.3892315914	1701	Average Waiting Time	平均等待时间	average-waiting-time	biweekly-contest-42	Q2
1436.1125054038	1433	Check If a String Can Break Another String	检查一个字符串是否可以打破另一个字符串	check-if-a-string-can-break-another-string	biweekly-contest-25	Q3
1435.9559888935	2001	Number of Pairs of Interchangeable Rectangles	可互换矩形的组数	number-of-pairs-of-interchangeable-rectangles	weekly-contest-258	Q2
1435.3564963722	1025	Divisor Game	除数博弈	divisor-game	weekly-contest-132	Q1
1435.0179887342	2559	Count Vowel Strings in Ranges	统计范围内的元音字符串数	count-vowel-strings-in-ranges	weekly-contest-331	Q2
1434.2392062372	2600	K Items With the Maximum Sum	K 件物品的最大和	k-items-with-the-maximum-sum	weekly-contest-338	Q1
1433.0795554833	1535	Find the Winner of an Array Game	找出数组游戏的赢家	find-the-winner-of-an-array-game	weekly-contest-200	Q2
1432.9593207076	967	Numbers With Same Consecutive Differences	连续差相同的数字	numbers-with-same-consecutive-differences	weekly-contest-117	Q2
1432.9051050881	994	Rotting Oranges	腐烂的橘子	rotting-oranges	weekly-contest-124	Q2
1432.0967926378	1785	Minimum Elements to Add to Form a Given Sum	构成特定和需要添加的最少元素	minimum-elements-to-add-to-form-a-given-sum	weekly-contest-231	Q2
1431.6864980883	1170	Compare Strings by Frequency of the Smallest Character	比较字符串最小字母出现频次	compare-strings-by-frequency-of-the-smallest-character	weekly-contest-151	Q2
1431.0523656241	2415	Reverse Odd Levels of Binary Tree	反转二叉树的奇数层	reverse-odd-levels-of-binary-tree	weekly-contest-311	Q3
1430.3429533629	1636	Sort Array by Increasing Frequency	按照频率将数组升序排序	sort-array-by-increasing-frequency	biweekly-contest-38	Q1
1430.3094955812	2924	Find Champion II	找到冠军 II	find-champion-ii	weekly-contest-370	Q2
1429.9599761889	2957	Remove Adjacent Almost-Equal Characters	消除相邻近似相等字符	remove-adjacent-almost-equal-characters	biweekly-contest-119	Q2
1429.6349292399	1357	Apply Discount Every n Orders	每隔 n 个顾客打折	apply-discount-every-n-orders	biweekly-contest-20	Q2
1429.1878389249	988	Smallest String Starting From Leaf	从叶结点开始的最小字符串	smallest-string-starting-from-leaf	weekly-contest-122	Q2
1428.7246677159	2711	Difference of Number of Distinct Values on Diagonals	对角线上不同值的数量差	difference-of-number-of-distinct-values-on-diagonals	weekly-contest-347	Q2
1428.7129059030	817	Linked List Components	链表组件	linked-list-components	weekly-contest-80	Q2
1428.6729861424	1845	Seat Reservation Manager	座位预约管理系统	seat-reservation-manager	biweekly-contest-51	Q2
1428.1443796872	1669	Merge In Between Linked Lists	合并两个链表	merge-in-between-linked-lists	biweekly-contest-40	Q2
1427.7906804882	1887	Reduction Operations to Make the Array Elements Equal	使数组元素相等的减少操作次数	reduction-operations-to-make-the-array-elements-equal	weekly-contest-244	Q2
1426.9800910361	2437	Number of Valid Clock Times	有效时间的数目	number-of-valid-clock-times	biweekly-contest-89	Q1
1426.9483793050	1315	Sum of Nodes with Even-Valued Grandparent	祖父节点值为偶数的节点和	sum-of-nodes-with-even-valued-grandparent	biweekly-contest-17	Q3
1426.7384112327	1432	Max Difference You Can Get From Changing an Integer	改变一个整数能得到的最大差值	max-difference-you-can-get-from-changing-an-integer	biweekly-contest-25	Q2
1426.7144554733	1003	Check If Word Is Valid After Substitutions	检查替换后的词是否有效	check-if-word-is-valid-after-substitutions	weekly-contest-126	Q2
1425.9672522649	840	Magic Squares In Grid	矩阵中的幻方	magic-squares-in-grid	weekly-contest-86	Q1
1425.3981616639	883	Projection Area of 3D Shapes	三维形体投影面积	projection-area-of-3d-shapes	weekly-contest-96	Q1
1423.5501543781	791	Custom Sort String	自定义字符串排序	custom-sort-string	weekly-contest-73	Q3
1423.5195903975	3039	Apply Operations to Make String Empty	进行操作使字符串为空	apply-operations-to-make-string-empty	biweekly-contest-124	Q2
1423.1058649921	1333	Filter Restaurants by Vegan-Friendly, Price and Distance	餐厅过滤器	filter-restaurants-by-vegan-friendly-price-and-distance	weekly-contest-173	Q2
1423.0355763093	1493	Longest Subarray of 1's After Deleting One Element	删掉一个元素以后全为 1 的最长子数组	longest-subarray-of-1s-after-deleting-one-element	biweekly-contest-29	Q3
1422.7125559974	2938	Separate Black and White Balls	区分黑球与白球	separate-black-and-white-balls	weekly-contest-372	Q2
1422.3308967485	2606	Find the Substring With Maximum Cost	找到最大开销的子字符串	find-the-substring-with-maximum-cost	biweekly-contest-101	Q2
1421.9944676861	1630	Arithmetic Subarrays	等差子数组	arithmetic-subarrays	weekly-contest-212	Q2
1421.7251191403	2326	Spiral Matrix IV	螺旋矩阵 IV	spiral-matrix-iv	weekly-contest-300	Q2
1421.6541140049	1360	Number of Days Between Two Dates	日期之间隔几天	number-of-days-between-two-dates	weekly-contest-177	Q1
1421.2624065513	1033	Moving Stones Until Consecutive	移动石子直到连续	moving-stones-until-consecutive	weekly-contest-134	Q1
1420.3698647434	2760	Longest Even Odd Subarray With Threshold	最长奇偶子数组	longest-even-odd-subarray-with-threshold	weekly-contest-352	Q1
1418.9758090724	2374	Node With Highest Edge Score	边积分最高的节点	node-with-highest-edge-score	weekly-contest-306	Q2
1418.8205349928	1656	Design an Ordered Stream	设计有序流	design-an-ordered-stream	weekly-contest-215	Q1
1418.6847740057	1962	Remove Stones to Minimize the Total	移除石子使总数最小	remove-stones-to-minimize-the-total	weekly-contest-253	Q2
1418.1401949854	1052	Grumpy Bookstore Owner	爱生气的书店老板	grumpy-bookstore-owner	weekly-contest-138	Q2
1417.3934930077	2139	Minimum Moves to Reach Target Score	得到目标值的最少行动次数	minimum-moves-to-reach-target-score	weekly-contest-276	Q2
1416.8961009909	1652	Defuse the Bomb	拆炸弹	defuse-the-bomb	biweekly-contest-39	Q1
1416.4124723866	2294	Partition Array Such That Maximum Difference Is K	划分数组使最大差为 K	partition-array-such-that-maximum-difference-is-k	weekly-contest-296	Q2
1414.6100987673	2825	Make String a Subsequence Using Cyclic Increments	循环增长使字符串子序列等于另一个字符串	make-string-a-subsequence-using-cyclic-increments	biweekly-contest-111	Q2
1414.4918812526	890	Find and Replace Pattern	查找和替换模式	find-and-replace-pattern	weekly-contest-98	Q2
1414.4351202231	1985	Find the Kth Largest Integer in the Array	找出数组中的第 K 大整数	find-the-kth-largest-integer-in-the-array	weekly-contest-256	Q2
1413.4238697034	2383	Minimum Hours of Training to Win a Competition	赢得比赛需要的最少训练时长	minimum-hours-of-training-to-win-a-competition	weekly-contest-307	Q1
1413.0376809608	2521	Distinct Prime Factors of Product of Array	数组乘积中的不同质因数数目	distinct-prime-factors-of-product-of-array	weekly-contest-326	Q2
1412.3053230205	1823	Find the Winner of the Circular Game	找出游戏的获胜者	find-the-winner-of-the-circular-game	weekly-contest-236	Q2
1412.2790156634	841	Keys and Rooms	钥匙和房间	keys-and-rooms	weekly-contest-86	Q2
1410.5239927267	1138	Alphabet Board Path	字母板上的路径	alphabet-board-path	weekly-contest-147	Q2
1409.2288385791	2834	Find the Minimum Possible Sum of a Beautiful Array	找出美丽数组的最小和	find-the-minimum-possible-sum-of-a-beautiful-array	weekly-contest-360	Q2
1408.7923640745	1588	Sum of All Odd Length Subarrays	所有奇数长度子数组的和	sum-of-all-odd-length-subarrays	biweekly-contest-35	Q1
1408.4275924170	2110	Number of Smooth Descent Periods of a Stock	股票平滑下跌阶段的数目	number-of-smooth-descent-periods-of-a-stock	weekly-contest-272	Q3
1407.9870845299	1006	Clumsy Factorial	笨阶乘	clumsy-factorial	weekly-contest-127	Q2
1407.5442381391	1217	Minimum Cost to Move Chips to The Same Position	玩筹码	minimum-cost-to-move-chips-to-the-same-position	weekly-contest-157	Q1
1407.1322366299	1325	Delete Leaves With a Given Value	删除给定值的叶子节点	delete-leaves-with-a-given-value	weekly-contest-172	Q3
1407.0629410799	1886	Determine Whether Matrix Can Be Obtained By Rotation	判断矩阵经轮转后是否一致	determine-whether-matrix-can-be-obtained-by-rotation	weekly-contest-244	Q1
1406.1279714442	2451	Odd String Difference	差值数组不同的字符串	odd-string-difference	biweekly-contest-90	Q1
1405.8938478338	2744	Find Maximum Number of String Pairs	最大字符串配对数目	find-maximum-number-of-string-pairs	biweekly-contest-107	Q1
1405.8442434352	2946	Matrix Similarity After Cyclic Shifts	循环移位后的矩阵相似检查	matrix-similarity-after-cyclic-shifts	weekly-contest-373	Q1
1405.7482709086	2996	Smallest Missing Integer Greater Than Sequential Prefix Sum	大于等于顺序前缀和的最小缺失整数	smallest-missing-integer-greater-than-sequential-prefix-sum	biweekly-contest-121	Q1
1405.5786892723	1561	Maximum Number of Coins You Can Get	你可以获得的最大硬币数目	maximum-number-of-coins-you-can-get	weekly-contest-203	Q2
1405.4005354401	1410	HTML Entity Parser	HTML 实体解析器	html-entity-parser	weekly-contest-184	Q3
1405.1231882640	2734	Lexicographically Smallest String After Substring Operation	执行子串操作后的字典序最小字符串	lexicographically-smallest-string-after-substring-operation	weekly-contest-349	Q2
1405.0021415178	1457	Pseudo-Palindromic Paths in a Binary Tree	二叉树中的伪回文路径	pseudo-palindromic-paths-in-a-binary-tree	weekly-contest-190	Q3
1404.7016862187	1237	Find Positive Integer Solution for a Given Equation	找出给定方程的正整数解	find-positive-integer-solution-for-a-given-equation	weekly-contest-160	Q1
1404.1839222000	1700	Number of Students Unable to Eat Lunch	无法吃午餐的学生数量	number-of-students-unable-to-eat-lunch	biweekly-contest-42	Q1
1402.0863615706	1508	Range Sum of Sorted Subarray Sums	子数组和排序后的区间和	range-sum-of-sorted-subarray-sums	biweekly-contest-30	Q2
1401.2246983038	1198	Find Smallest Common Element in All Rows	找出所有行中最小公共元素	find-smallest-common-element-in-all-rows	biweekly-contest-9	Q3
1399.8468905274	2240	Number of Ways to Buy Pens and Pencils	买钢笔和铅笔的方案数	number-of-ways-to-buy-pens-and-pencils	biweekly-contest-76	Q2
1397.9519549403	2799	Count Complete Subarrays in an Array	统计完全子数组的数目	count-complete-subarrays-in-an-array	weekly-contest-356	Q2
1397.8875115008	1071	Greatest Common Divisor of Strings	字符串的最大公因子	greatest-common-divisor-of-strings	weekly-contest-139	Q1
1397.7743198793	1176	Diet Plan Performance	健身计划评估	diet-plan-performance	weekly-contest-152	Q2
1396.8422030812	788	Rotated Digits	旋转数字	rotated-digits	weekly-contest-73	Q1
1396.5990609759	1404	Number of Steps to Reduce a Number in Binary Representation to One	将二进制表示减到 1 的步骤数	number-of-steps-to-reduce-a-number-in-binary-representation-to-one	weekly-contest-183	Q2
1396.5448074496	1306	Jump Game III	跳跃游戏 III	jump-game-iii	weekly-contest-169	Q3
1396.4853538164	944	Delete Columns to Make Sorted	删列造序	delete-columns-to-make-sorted	weekly-contest-111	Q2
1396.1044458638	2566	Maximum Difference by Remapping a Digit	替换一个数字后的最大差值	maximum-difference-by-remapping-a-digit	biweekly-contest-98	Q1
1395.9639246414	2966	Divide Array Into Arrays With Max Difference	划分数组并满足最大差限制	divide-array-into-arrays-with-max-difference	weekly-contest-376	Q2
1395.5132479177	1668	Maximum Repeating Substring	最大重复子字符串	maximum-repeating-substring	biweekly-contest-40	Q1
1394.9149882274	2256	Minimum Average Difference	最小平均差	minimum-average-difference	biweekly-contest-77	Q2
1393.7857353048	2816	Double a Number Represented as a Linked List	翻倍以链表形式表示的数字	double-a-number-represented-as-a-linked-list	weekly-contest-358	Q2
1393.4123491817	978	Longest Turbulent Subarray	最长湍流子数组	longest-turbulent-subarray	weekly-contest-120	Q2
1393.3604603199	2928	Distribute Candies Among Children I	给小朋友们分糖果 I	distribute-candies-among-children-i	biweekly-contest-117	Q1
1392.6601629182	1529	Bulb Switcher IV	灯泡开关 IV	minimum-suffix-flips	weekly-contest-199	Q2
1392.3629194433	2870	Minimum Number of Operations to Make Array Empty	使数组为空的最少操作次数	minimum-number-of-operations-to-make-array-empty	biweekly-contest-114	Q2
1392.0853311911	957	Prison Cells After N Days	N 天后的牢房	prison-cells-after-n-days	weekly-contest-115	Q1
1391.7243180131	1222	Queens That Can Attack the King	可以攻击国王的皇后	queens-that-can-attack-the-king	weekly-contest-158	Q2
1390.5023027273	2155	All Divisions With the Highest Score of a Binary Array	分组得分最高的所有下标	all-divisions-with-the-highest-score-of-a-binary-array	weekly-contest-278	Q2
1389.3311694710	1065	Index Pairs of a String	字符串的索引对	index-pairs-of-a-string	biweekly-contest-1	Q2
1389.0328392117	1214	Two Sum BSTs	查找两棵二叉搜索树之和	two-sum-bsts	biweekly-contest-10	Q2
1388.5363323598	2917	Find the K-or of an Array	找出数组中的 K-or 值	find-the-k-or-of-an-array	weekly-contest-369	Q1
1387.9431104106	1302	Deepest Leaves Sum	层数最深叶子节点的和	deepest-leaves-sum	biweekly-contest-16	Q3
1387.7347071166	2389	Longest Subsequence With Limited Sum	和有限的最长子序列	longest-subsequence-with-limited-sum	weekly-contest-308	Q1
1387.3672639293	937	Reorder Data in Log Files	重新排列日志文件	reorder-data-in-log-files	weekly-contest-110	Q1
1387.2941868867	1860	Incremental Memory Leak	增长的内存泄露	incremental-memory-leak	biweekly-contest-52	Q2
1386.9203620297	1721	Swapping Nodes in a Linked List	交换链表中的节点	swapping-nodes-in-a-linked-list	weekly-contest-223	Q2
1386.3256313989	1276	Number of Burgers with No Waste of Ingredients	不浪费原料的汉堡制作方案	number-of-burgers-with-no-waste-of-ingredients	weekly-contest-165	Q2
1386.1200017827	2530	Maximal Score After Applying K Operations	执行 K 次操作后的最大分数	maximal-score-after-applying-k-operations	weekly-contest-327	Q2
1384.4078082338	1271	Hexspeak	十六进制魔术数字	hexspeak	biweekly-contest-14	Q1
1384.0226911434	2091	Removing Minimum and Maximum From Array	从数组中移除最大值和最小值	removing-minimum-and-maximum-from-array	weekly-contest-269	Q3
1383.7751035280	3034	Number of Subarrays That Match a Pattern I	匹配模式数组的子数组数目 I	number-of-subarrays-that-match-a-pattern-i	weekly-contest-384	Q2
1383.4424411643	762	Prime Number of Set Bits in Binary Representation	二进制表示中质数个计算置位	prime-number-of-set-bits-in-binary-representation	weekly-contest-67	Q1
1382.7606078230	1318	Minimum Flips to Make a OR b Equal to c	或运算的最小翻转次数	minimum-flips-to-make-a-or-b-equal-to-c	weekly-contest-171	Q2
1382.7178688716	849	Maximize Distance to Closest Person	到最近的人的最大距离	maximize-distance-to-closest-person	weekly-contest-88	Q2
1382.6941570342	2682	Find the Losers of the Circular Game	找出转圈游戏输家	find-the-losers-of-the-circular-game	weekly-contest-345	Q1
1382.5129151601	797	All Paths From Source to Target	所有可能的路径	all-paths-from-source-to-target	weekly-contest-75	Q2
1382.4809893713	1185	Day of the Week	一周中的第几天	day-of-the-week	weekly-contest-153	Q2
1381.2168789318	1881	Maximum Value after Insertion	插入后的最大值	maximum-value-after-insertion	weekly-contest-243	Q2
1381.0888968455	2410	Maximum Matching of Players With Trainers	运动员和训练师的最大匹配数	maximum-matching-of-players-with-trainers	biweekly-contest-87	Q2
1380.1541980647	814	Binary Tree Pruning	二叉树剪枝	binary-tree-pruning	weekly-contest-79	Q2
1380.0192844155	1828	Queries on Number of Points Inside a Circle	统计一个圆中点的数目	queries-on-number-of-points-inside-a-circle	biweekly-contest-50	Q2
1379.8787648129	2120	Execution of All Suffix Instructions Staying in a Grid	执行所有后缀指令	execution-of-all-suffix-instructions-staying-in-a-grid	weekly-contest-273	Q2
1379.3426970242	2855	Minimum Right Shifts to Sort the Array	使数组成为递增数组的最少右移次数	minimum-right-shifts-to-sort-the-array	biweekly-contest-113	Q1
1378.7570411077	1013	Partition Array Into Three Parts With Equal Sum	将数组分成和相等的三个部分	partition-array-into-three-parts-with-equal-sum	weekly-contest-129	Q1
1377.6120218199	811	Subdomain Visit Count	子域名访问计数	subdomain-visit-count	weekly-contest-78	Q1
1377.1913915125	1010	Pairs of Songs With Total Durations Divisible by 60	总持续时间可被 60 整除的歌曲	pairs-of-songs-with-total-durations-divisible-by-60	weekly-contest-128	Q2
1376.4549624575	1018	Binary Prefix Divisible By 5	可被 5 整除的二进制前缀	binary-prefix-divisible-by-5	weekly-contest-130	Q1
1376.2600892096	807	Max Increase to Keep City Skyline	保持城市天际线	max-increase-to-keep-city-skyline	weekly-contest-77	Q3
1376.2376633804	2784	Check if Array is Good	检查数组是否是好的	check-if-array-is-good	biweekly-contest-109	Q1
1376.0047008182	2443	Sum of Number and Its Reverse	反转之后的数字和	sum-of-number-and-its-reverse	weekly-contest-315	Q3
1375.4261931199	2614	Prime In Diagonal	对角线上的质数	prime-in-diagonal	weekly-contest-340	Q1
1375.0376362104	2336	Smallest Number in Infinite Set	无限集中的最小数字	smallest-number-in-infinite-set	weekly-contest-301	Q2
1375.0234414965	1288	Remove Covered Intervals	删除被覆盖区间	remove-covered-intervals	biweekly-contest-15	Q2
1374.6755455786	1038	Binary Search Tree to Greater Sum Tree	把二叉搜索树转换为累加树	binary-search-tree-to-greater-sum-tree	weekly-contest-135	Q2
1374.5749003110	1267	Count Servers that Communicate	统计参与通信的服务器	count-servers-that-communicate	weekly-contest-164	Q2
1374.3549007913	1619	Mean of Array After Removing Some Elements	删除某些元素后的数组均值	mean-of-array-after-removing-some-elements	biweekly-contest-37	Q1
1374.3527967199	2583	Kth Largest Sum in a Binary Tree	二叉树中的第 K 大层和	kth-largest-sum-in-a-binary-tree	weekly-contest-335	Q2
1373.8916796083	2610	Convert an Array Into a 2D Array With Conditions	转换二维数组	convert-an-array-into-a-2d-array-with-conditions	weekly-contest-339	Q2
1373.8113453501	1291	Sequential Digits	顺次数	sequential-digits	weekly-contest-167	Q2
1372.7398808669	748	Shortest Completing Word	最短补全词	shortest-completing-word	weekly-contest-63	Q2
1372.5139179378	2482	Difference Between Ones and Zeros in Row and Column	行和列中一和零的差值	difference-between-ones-and-zeros-in-row-and-column	biweekly-contest-92	Q2
1372.4759842416	2899	Last Visited Integers	上一个遍历的整数	last-visited-integers	biweekly-contest-115	Q1
1372.1152262488	1863	Sum of All Subset XOR Totals	找出所有子集的异或总和再求和	sum-of-all-subset-xor-totals	weekly-contest-241	Q1
1371.8092952004	2244	Minimum Rounds to Complete All Tasks	完成所有任务需要的最少轮数	minimum-rounds-to-complete-all-tasks	weekly-contest-289	Q2
1370.6144908238	914	X of a Kind in a Deck of Cards	卡牌分组	x-of-a-kind-in-a-deck-of-cards	weekly-contest-104	Q1
1370.4186698287	1854	Maximum Population Year	人口最多的年份	maximum-population-year	weekly-contest-240	Q1
1369.6144401520	1608	Special Array With X Elements Greater Than or Equal X	特殊数组的特征值	special-array-with-x-elements-greater-than-or-equal-x	weekly-contest-209	Q1
1369.0053354603	1370	Increasing Decreasing String	上升下降字符串	increasing-decreasing-string	biweekly-contest-21	Q1
1368.0043517215	1576	Replace All ?'s to Avoid Consecutive Repeating Characters	替换所有的问号	replace-all-s-to-avoid-consecutive-repeating-characters	weekly-contest-205	Q1
1367.0197235097	2515	Shortest Distance to Target String in a Circular Array	到目标字符串的最短距离	shortest-distance-to-target-string-in-a-circular-array	weekly-contest-325	Q1
1366.6789652398	2433	Find The Original Array of Prefix Xor	找出前缀异或的原始数组	find-the-original-array-of-prefix-xor	weekly-contest-314	Q2
1365.2269076492	2231	Largest Number After Digit Swaps by Parity	按奇偶性交换后的最大数字	largest-number-after-digit-swaps-by-parity	weekly-contest-288	Q1
1364.6787168645	2260	Minimum Consecutive Cards to Pick Up	必须拿起的最小连续卡牌数	minimum-consecutive-cards-to-pick-up	weekly-contest-291	Q2
1364.1548599180	1974	Minimum Time to Type Word Using Special Typewriter	使用特殊打字机键入单词的最少时间	minimum-time-to-type-word-using-special-typewriter	biweekly-contest-59	Q1
1362.7144100401	2486	Append Characters to String to Make Subsequence	追加字符以获得子序列	append-characters-to-string-to-make-subsequence	weekly-contest-321	Q2
1362.6613797387	1592	Rearrange Spaces Between Words	重新排列单词间的空格	rearrange-spaces-between-words	weekly-contest-207	Q1
1361.8801013336	1120	Maximum Average Subtree	子树的最大平均值	maximum-average-subtree	biweekly-contest-4	Q3
1361.6459603518	1980	Find Unique Binary String	找出不同的二进制字符串	find-unique-binary-string	weekly-contest-255	Q2
1361.5824742947	2165	Smallest Value of the Rearranged Number	重排数字的最小值	smallest-value-of-the-rearranged-number	weekly-contest-279	Q2
1360.4212587270	2335	Minimum Amount of Time to Fill Cups	装满杯子需要的最短总时长	minimum-amount-of-time-to-fill-cups	weekly-contest-301	Q1
1360.3005775112	1817	Finding the Users Active Minutes	查找用户活跃分钟数	finding-the-users-active-minutes	weekly-contest-235	Q2
1360.2184128413	1448	Count Good Nodes in Binary Tree	统计二叉树中好节点的数目	count-good-nodes-in-binary-tree	biweekly-contest-26	Q3
1360.0511262593	2379	Minimum Recolors to Get K Consecutive Black Blocks	得到 K 个黑块的最少涂色次数	minimum-recolors-to-get-k-consecutive-black-blocks	biweekly-contest-85	Q1
1358.3561730566	746	Min Cost Climbing Stairs	使用最小花费爬楼梯	min-cost-climbing-stairs	weekly-contest-63	Q1
1358.1526134030	2090	K Radius Subarray Averages	半径为 k 的子数组平均值	k-radius-subarray-averages	weekly-contest-269	Q2
1357.6553050616	1957	Delete Characters to Make Fancy String	删除字符使字符串变好	delete-characters-to-make-fancy-string	biweekly-contest-58	Q1
1356.6925765299	2037	Minimum Number of Moves to Seat Everyone	使每位学生都有座位的最少移动次数	minimum-number-of-moves-to-seat-everyone	biweekly-contest-63	Q1
1356.4450869217	2579	Count Total Number of Colored Cells	统计染色格子数	count-total-number-of-colored-cells	biweekly-contest-99	Q2
1356.1920189231	2043	Simple Bank System	简易银行系统	simple-bank-system	weekly-contest-263	Q2
1355.9817184778	1331	Rank Transform of an Array	数组序号转换	rank-transform-of-an-array	biweekly-contest-18	Q1
1355.5386161215	1894	Find the Student that Will Replace the Chalk	找到需要补充粉笔的学生编号	find-the-student-that-will-replace-the-chalk	biweekly-contest-54	Q2
1355.3956434989	2405	Optimal Partition of String	子字符串的最优划分	optimal-partition-of-string	weekly-contest-310	Q2
1355.3825442341	1689	Partitioning Into Minimum Number Of Deci-Binary Numbers	十-二进制数的最少数目	partitioning-into-minimum-number-of-deci-binary-numbers	weekly-contest-219	Q2
1354.5231125217	2210	Count Hills and Valleys in an Array	统计数组中峰和谷的数量	count-hills-and-valleys-in-an-array	weekly-contest-285	Q1
1354.1247827015	1244	Design A Leaderboard	力扣排行榜	design-a-leaderboard	biweekly-contest-12	Q1
1353.6296778120	1758	Minimum Changes To Make Alternating Binary String	生成交替二进制字符串的最少操作数	minimum-changes-to-make-alternating-binary-string	weekly-contest-228	Q1
1352.7250049956	848	Shifting Letters	字母移位	shifting-letters	weekly-contest-88	Q1
1352.1791099256	1995	Count Special Quadruplets	统计特殊四元组	count-special-quadruplets	weekly-contest-257	Q1
1351.6909336495	2895	Minimum Processing Time	最小处理时间	minimum-processing-time	weekly-contest-366	Q2
1351.4184681108	1513	Number of Substrings With Only 1s	仅含 1 的子串数	number-of-substrings-with-only-1s	weekly-contest-197	Q2
1350.6048768377	2053	Kth Distinct String in an Array	数组中第 K 个独一无二的字符串	kth-distinct-string-in-an-array	biweekly-contest-64	Q1
1350.5883729249	2578	Split With Minimum Sum	最小和分割	split-with-minimum-sum	biweekly-contest-99	Q1
1348.6701914380	1100	Find K-Length Substrings With No Repeated Characters	长度为 K 的无重复字符子串	find-k-length-substrings-with-no-repeated-characters	biweekly-contest-3	Q2
1348.5770106090	2609	Find the Longest Balanced Substring of a Binary String	最长平衡子字符串	find-the-longest-balanced-substring-of-a-binary-string	weekly-contest-339	Q1
1348.0079390256	1029	Two City Scheduling	两地调度	two-city-scheduling	weekly-contest-133	Q1
1347.8521638635	2390	Removing Stars From a String	从字符串中移除星号	removing-stars-from-a-string	weekly-contest-308	Q2
1347.5885281778	2937	Make Three Strings Equal	使三个字符串相等	make-three-strings-equal	weekly-contest-372	Q1
1347.2146542772	2829	Determine the Minimum Sum of a k-avoiding Array	k-avoiding 数组的最小总和	determine-the-minimum-sum-of-a-k-avoiding-array	weekly-contest-359	Q2
1346.9594471871	2284	Sender With Largest Word Count	最多单词数的发件人	sender-with-largest-word-count	biweekly-contest-79	Q2
1346.3556309143	2027	Minimum Moves to Convert String	转换字符串的最少操作次数	minimum-moves-to-convert-string	weekly-contest-261	Q1
1345.7371686090	1679	Max Number of K-Sum Pairs	K 和数对的最大数目	max-number-of-k-sum-pairs	weekly-contest-218	Q2
1344.2261332020	1544	Make The String Great	整理字符串	make-the-string-great	weekly-contest-201	Q1
1343.6289130550	1395	Count Number of Teams	统计作战单位数	count-number-of-teams	weekly-contest-182	Q2
1341.8397242604	1796	Second Largest Digit in a String	字符串中第二大的数字	second-largest-digit-in-a-string	biweekly-contest-48	Q1
1341.5076441361	784	Letter Case Permutation	字母大小写全排列	letter-case-permutation	weekly-contest-72	Q1
1341.3713970313	2023	Number of Pairs of Strings With Concatenation Equal to Target	连接后等于目标字符串的字符串对	number-of-pairs-of-strings-with-concatenation-equal-to-target	biweekly-contest-62	Q2
1341.2659819842	859	Buddy Strings	亲密字符串	buddy-strings	weekly-contest-90	Q1
1341.0476642293	1399	Count Largest Group	统计最大组的数目	count-largest-group	biweekly-contest-23	Q1
1340.5559417151	976	Largest Perimeter Triangle	三角形的最大周长	largest-perimeter-triangle	weekly-contest-119	Q2
1338.8322315568	970	Powerful Integers	强整数	powerful-integers	weekly-contest-118	Q1
1337.8472367494	933	Number of Recent Calls	最近的请求次数	number-of-recent-calls	weekly-contest-109	Q1
1337.6115578703	2161	Partition Array According to Given Pivot	根据给定数字划分数组	partition-array-according-to-given-pivot	biweekly-contest-71	Q2
1337.3722299775	1260	Shift 2D Grid	二维网格迁移	shift-2d-grid	weekly-contest-163	Q1
1336.9494482313	1275	Find Winner on a Tic Tac Toe Game	找出井字棋的获胜者	find-winner-on-a-tic-tac-toe-game	weekly-contest-165	Q1
1336.7830451625	2587	Rearrange Array to Maximize Prefix Score	重排数组以得到最大前缀分数	rearrange-array-to-maximize-prefix-score	weekly-contest-336	Q2
1335.4613368501	2506	Count Pairs Of Similar Strings	统计相似字符串对的数目	count-pairs-of-similar-strings	weekly-contest-324	Q1
1335.0295688697	938	Range Sum of BST	二叉搜索树的范围和	range-sum-of-bst	weekly-contest-110	Q2
1334.5718985411	1409	Queries on a Permutation With Key	查询带键的排列	queries-on-a-permutation-with-key	weekly-contest-184	Q2
1334.5708444649	2126	Destroying Asteroids	摧毁小行星	destroying-asteroids	weekly-contest-274	Q3
1334.0564009231	888	Fair Candy Swap	公平的糖果棒交换	fair-candy-swap	weekly-contest-98	Q1
1334.0516779626	2270	Number of Ways to Split Array	分割数组的方案数	number-of-ways-to-split-array	biweekly-contest-78	Q2
1333.3138174157	1805	Number of Different Integers in a String	字符串中不同整数的数目	number-of-different-integers-in-a-string	weekly-contest-234	Q1
1333.2008827592	2554	Maximum Number of Integers to Choose From a Range I	从一个范围内选择最多整数 I	maximum-number-of-integers-to-choose-from-a-range-i	biweekly-contest-97	Q2
1333.1920503970	2181	Merge Nodes in Between Zeros	合并零之间的节点	merge-nodes-in-between-zeros	weekly-contest-281	Q2
1333.0179956774	2679	Sum in a Matrix	矩阵中的和	sum-in-a-matrix	biweekly-contest-104	Q2
1332.6225967630	1128	Number of Equivalent Domino Pairs	等价多米诺骨牌对的数量	number-of-equivalent-domino-pairs	weekly-contest-146	Q1
1332.6187879411	2274	Maximum Consecutive Floors Without Special Floors	不含特殊楼层的最大连续楼层数	maximum-consecutive-floors-without-special-floors	weekly-contest-293	Q2
1332.4653491345	1471	The k Strongest Values in an Array	数组中的 k 个最强值	the-k-strongest-values-in-an-array	weekly-contest-192	Q2
1331.5287857686	2259	Remove Digit From Number to Maximize Result	移除指定数字得到的最大结果	remove-digit-from-number-to-maximize-result	weekly-contest-291	Q1
1331.3935128035	2373	Largest Local Values in a Matrix	矩阵中的局部最大值	largest-local-values-in-a-matrix	weekly-contest-306	Q1
1330.9185778280	1347	Minimum Number of Steps to Make Two Strings Anagram	制造字母异位词的最小步骤数	minimum-number-of-steps-to-make-two-strings-anagram	weekly-contest-175	Q2
1328.7281033317	1324	Print Words Vertically	竖直打印单词	print-words-vertically	weekly-contest-172	Q2
1328.5499677186	2396	Strictly Palindromic Number	严格回文的数字	strictly-palindromic-number	biweekly-contest-86	Q2
1328.5131477260	1812	Determine Color of a Chessboard Square	判断国际象棋棋盘中一个格子的颜色	determine-color-of-a-chessboard-square	biweekly-contest-49	Q1
1327.0282989915	1086	High Five	前五科的均分	high-five	biweekly-contest-2	Q2
1326.4047670018	1476	Subrectangle Queries	子矩形查询	subrectangle-queries	biweekly-contest-28	Q2
1325.3607218257	2073	Time Needed to Buy Tickets	买票需要的时间	time-needed-to-buy-tickets	weekly-contest-267	Q1
1324.5696223867	1344	Angle Between Hands of a Clock	时钟指针的夹角	angle-between-hands-of-a-clock	biweekly-contest-19	Q3
1324.5320836804	1752	Check if Array Is Sorted and Rotated	检查数组是否经排序和轮转得到	check-if-array-is-sorted-and-rotated	weekly-contest-227	Q1
1324.3520304377	2095	Delete the Middle Node of a Linked List	删除链表的中间节点	delete-the-middle-node-of-a-linked-list	weekly-contest-270	Q2
1324.2140587436	3014	Minimum Number of Pushes to Type Word I	输入单词需要的最少按键次数 I	minimum-number-of-pushes-to-type-word-i	weekly-contest-381	Q1
1324.1757200103	1603	Design Parking System	设计停车系统	design-parking-system	biweekly-contest-36	Q1
1324.1714505166	2660	Determine the Winner of a Bowling Game	保龄球游戏的获胜者	determine-the-winner-of-a-bowling-game	weekly-contest-343	Q1
1323.8236471852	1925	Count Square Sum Triples	统计平方和三元组的数目	count-square-sum-triples	biweekly-contest-56	Q1
1323.1893756783	2491	Divide Players Into Teams of Equal Skill	划分技能点相等的团队	divide-players-into-teams-of-equal-skill	weekly-contest-322	Q2
1322.8302750313	1614	Maximum Nesting Depth of the Parentheses	括号的最大嵌套深度	maximum-nesting-depth-of-the-parentheses	weekly-contest-210	Q1
1322.5926536743	1936	Add Minimum Number of Rungs	新增的最少台阶数	add-minimum-number-of-rungs	weekly-contest-250	Q2
1322.3886921778	2446	Determine if Two Events Have Conflict	判断两个事件是否存在冲突	determine-if-two-events-have-conflict	weekly-contest-316	Q1
1321.9346201204	1694	Reformat Phone Number	重新格式化电话号码	reformat-phone-number	weekly-contest-220	Q1
1321.2748903388	1582	Special Positions in a Binary Matrix	二进制矩阵中的特殊位置	special-positions-in-a-binary-matrix	weekly-contest-206	Q1
1320.6485731562	2079	Watering Plants	给植物浇水	watering-plants	weekly-contest-268	Q2
1317.9521104466	999	Available Captures for Rook	可以被一步捕获的棋子数	available-captures-for-rook	weekly-contest-125	Q2
1317.9207508583	2130	Maximum Twin Sum of a Linked List	链表最大孪生和	maximum-twin-sum-of-a-linked-list	biweekly-contest-69	Q2
1317.4638832497	1313	Decompress Run-Length Encoded List	解压缩编码列表	decompress-run-length-encoded-list	biweekly-contest-17	Q1
1317.2976846981	2221	Find Triangular Sum of an Array	数组的三角和	find-triangular-sum-of-an-array	biweekly-contest-75	Q2
1317.1729927899	1343	Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold	大小为 K 且平均值大于等于阈值的子数组数目	number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold	biweekly-contest-19	Q2
1316.2046992429	2225	Find Players With Zero or One Losses	找出输掉零场或一场比赛的玩家	find-players-with-zero-or-one-losses	weekly-contest-287	Q2
1315.8569286597	2348	Number of Zero-Filled Subarrays	全 0 子数组的数目	number-of-zero-filled-subarrays	biweekly-contest-83	Q2
1315.4085759361	1180	Count Substrings with Only One Distinct Letter	统计只含单一字母的子串	count-substrings-with-only-one-distinct-letter	biweekly-contest-8	Q1
1315.3715333947	1629	Slowest Key	按键持续时间最长的键	slowest-key	weekly-contest-212	Q1
1315.1890809249	2109	Adding Spaces to a String	向字符串添加空格	adding-spaces-to-a-string	weekly-contest-272	Q2
1314.8600143277	1827	Minimum Operations to Make the Array Increasing	最少操作使数组递增	minimum-operations-to-make-the-array-increasing	biweekly-contest-50	Q1
1314.3600610974	2640	Find the Score of All Prefixes of an Array	一个数组所有前缀的分数	find-the-score-of-all-prefixes-of-an-array	biweekly-contest-102	Q2
1314.2912238536	2160	Minimum Sum of Four Digit Number After Splitting Digits	拆分数位后四位数字的最小和	minimum-sum-of-four-digit-number-after-splitting-digits	biweekly-contest-71	Q1
1311.3495317884	1021	Remove Outermost Parentheses	删除最外层的括号	remove-outermost-parentheses	weekly-contest-131	Q1
1310.9129840277	2058	Find the Minimum and Maximum Number of Nodes Between Critical Points	找出临界点之间的最小和最大距离	find-the-minimum-and-maximum-number-of-nodes-between-critical-points	weekly-contest-265	Q2
1309.8100518373	1710	Maximum Units on a Truck	卡车上的最大单元数	maximum-units-on-a-truck	weekly-contest-222	Q1
1309.7266159448	2500	Delete Greatest Value in Each Row	删除每行中的最大值	delete-greatest-value-in-each-row	weekly-contest-323	Q1
1309.3113721825	1451	Rearrange Words in a Sentence	重新排列句子中的单词	rearrange-words-in-a-sentence	weekly-contest-189	Q2
1309.1422268153	1897	Redistribute Characters to Make All Strings Equal	重新分配字符使所有字符串都相等	redistribute-characters-to-make-all-strings-equal	weekly-contest-245	Q1
1308.9617729374	2342	Max Sum of a Pair With Equal Sum of Digits	数位和相等数对的最大和	max-sum-of-a-pair-with-equal-sum-of-digits	weekly-contest-302	Q2
1308.9485479750	2264	Largest 3-Same-Digit Number in String	字符串中最大的 3 位相同数字	largest-3-same-digit-number-in-string	weekly-contest-292	Q1
1307.9800903088	1064	Fixed Point	不动点	fixed-point	biweekly-contest-1	Q1
1307.5663523368	804	Unique Morse Code Words	唯一摩尔斯密码词	unique-morse-code-words	weekly-contest-77	Q2
1307.4608905199	2085	Count Common Words With One Occurrence	统计出现过一次的公共字符串	count-common-words-with-one-occurrence	biweekly-contest-66	Q1
1307.3797385769	1893	Check if All the Integers in a Range Are Covered	检查是否区域内所有整数都被覆盖	check-if-all-the-integers-in-a-range-are-covered	biweekly-contest-54	Q1
1307.3265298181	2022	Convert 1D Array Into 2D Array	将一维数组转变成二维数组	convert-1d-array-into-2d-array	biweekly-contest-62	Q1
1307.2991245272	868	Binary Gap	二进制间距	binary-gap	weekly-contest-93	Q1
1306.2821637677	1984	Minimum Difference Between Highest and Lowest of K Scores	学生分数的最小差值	minimum-difference-between-highest-and-lowest-of-k-scores	weekly-contest-256	Q1
1304.1180812515	2657	Find the Prefix Common Array of Two Arrays	找到两个数组的前缀公共数组	find-the-prefix-common-array-of-two-arrays	biweekly-contest-103	Q2
1303.7347742929	2697	Lexicographically Smallest Palindrome	字典序最小回文串	lexicographically-smallest-palindrome	weekly-contest-346	Q2
1303.5594588137	2331	Evaluate Boolean Binary Tree	计算布尔二叉树的值	evaluate-boolean-binary-tree	biweekly-contest-82	Q1
1303.3201984827	783	Minimum Distance Between BST Nodes	二叉搜索树节点最小距离	minimum-distance-between-bst-nodes	weekly-contest-71	Q1
1303.0225704970	1338	Reduce Array Size to The Half	数组大小减半	reduce-array-size-to-the-half	weekly-contest-174	Q2
1303.0179795942	1051	Height Checker	高度检查器	height-checker	weekly-contest-138	Q1
1302.7005460171	1266	Minimum Time Visiting All Points	访问所有点的最小时间	minimum-time-visiting-all-points	weekly-contest-164	Q1
1302.6469071738	1991	Find the Middle Index in Array	找到数组的中间位置	find-the-middle-index-in-array	biweekly-contest-60	Q1
1301.9432665133	2243	Calculate Digit Sum of a String	计算字符串的数字和	calculate-digit-sum-of-a-string	weekly-contest-289	Q1
1301.9276849391	2740	Find the Value of the Partition	找出分区值	find-the-value-of-the-partition	weekly-contest-350	Q2
1301.4167433184	2525	Categorize Box According to Criteria	根据规则将箱子分类	categorize-box-according-to-criteria	biweekly-contest-95	Q1
1301.4117757184	806	Number of Lines To Write String	写字符串需要的行数	number-of-lines-to-write-string	weekly-contest-77	Q1
1301.4027057843	1646	Get Maximum in Generated Array	获取生成数组中的最大值	get-maximum-in-generated-array	weekly-contest-214	Q1
1301.3817574010	1877	Minimize Maximum Pair Sum in Array	数组中最大数对和的最小值	minimize-maximum-pair-sum-in-array	biweekly-contest-53	Q2
1301.1576743638	2748	Number of Beautiful Pairs	美丽下标对的数目	number-of-beautiful-pairs	weekly-contest-351	Q1
1300.9041426403	1844	Replace All Digits with Characters	将所有数字用字符替换	replace-all-digits-with-characters	biweekly-contest-51	Q1
1300.8009461582	1790	Check if One String Swap Can Make Strings Equal	仅执行一次字符串交换能否使两个字符串相等	check-if-one-string-swap-can-make-strings-equal	weekly-contest-232	Q1
1299.8393735643	2287	Rearrange Characters to Make Target String	重排字符形成目标字符串	rearrange-characters-to-make-target-string	weekly-contest-295	Q1
1299.6035132992	953	Verifying an Alien Dictionary	验证外星语词典	verifying-an-alien-dictionary	weekly-contest-114	Q1
1298.5921473119	908	Smallest Range I	最小差值 I	smallest-range-i	weekly-contest-103	Q1
1297.5338328524	819	Most Common Word	最常见的单词	most-common-word	weekly-contest-80	Q1
1297.4179875409	2913	Subarrays Distinct Element Sum of Squares I	子数组不同元素数目的平方和 I	subarrays-distinct-element-sum-of-squares-i	biweekly-contest-116	Q1
1297.3006230632	1598	Crawler Log Folder	文件夹操作日志搜集器	crawler-log-folder	weekly-contest-208	Q1
1295.8868965907	2224	Minimum Number of Operations to Convert Time	转化时间需要的最少操作数	minimum-number-of-operations-to-convert-time	weekly-contest-287	Q1
1295.7550469800	2717	Semi-Ordered Permutation	半有序排列	semi-ordered-permutation	weekly-contest-348	Q2
1295.4970938463	1539	Kth Missing Positive Number	第 k 个缺失的正整数	kth-missing-positive-number	biweekly-contest-32	Q1
1295.0947625986	2815	Max Pair Sum in an Array	数组中的最大数对和	max-pair-sum-in-an-array	weekly-contest-358	Q1
1294.7724244077	1769	Minimum Number of Operations to Move All Balls to Each Box	移动所有球到每个盒子所需的最小操作数	minimum-number-of-operations-to-move-all-balls-to-each-box	weekly-contest-229	Q2
1294.5800368625	2273	Find Resultant Array After Removing Anagrams	移除字母异位词后的结果数组	find-resultant-array-after-removing-anagrams	weekly-contest-293	Q1
1294.5297034757	1716	Calculate Money in Leetcode Bank	计算力扣银行的钱	calculate-money-in-leetcode-bank	biweekly-contest-43	Q1
1294.2819324126	2833	Furthest Point From Origin	距离原点最远的点	furthest-point-from-origin	weekly-contest-360	Q1
1294.0257382852	2545	Sort the Students by Their Kth Score	根据第 K 场考试的分数排序	sort-the-students-by-their-kth-score	weekly-contest-329	Q2
1293.4904281819	1551	Minimum Operations to Make Array Equal	使数组中所有元素相等的最小操作数	minimum-operations-to-make-array-equal	weekly-contest-202	Q2
1292.8993325204	2496	Maximum Value of a String in an Array	数组中字符串的最大值	maximum-value-of-a-string-in-an-array	biweekly-contest-93	Q1
1291.7449357310	3010	Divide an Array Into Subarrays With Minimum Cost I	将数组分成最小总代价的子数组 I	divide-an-array-into-subarrays-with-minimum-cost-i	biweekly-contest-122	Q1
1290.0361853035	1859	Sorting the Sentence	将句子排序	sorting-the-sentence	biweekly-contest-52	Q1
1289.9451590620	2428	Maximum Sum of an Hourglass	沙漏的最大总和	maximum-sum-of-an-hourglass	weekly-contest-313	Q2
1289.1912178611	2190	Most Frequent Number Following Key In an Array	数组中紧跟 key 之后出现最频繁的数字	most-frequent-number-following-key-in-an-array	biweekly-contest-73	Q1
1288.5621697906	1684	Count the Number of Consistent Strings	统计一致字符串的数目	count-the-number-of-consistent-strings	biweekly-contest-41	Q1
1288.1970048184	1403	Minimum Subsequence in Non-Increasing Order	非递增顺序的最小子序列	minimum-subsequence-in-non-increasing-order	weekly-contest-183	Q1
1287.9002757199	993	Cousins in Binary Tree	二叉树的堂兄弟节点	cousins-in-binary-tree	weekly-contest-124	Q1
1287.8970301681	872	Leaf-Similar Trees	叶子相似的树	leaf-similar-trees	weekly-contest-94	Q1
1287.1053917452	1103	Distribute Candies to People	分糖果 II	distribute-candies-to-people	weekly-contest-143	Q1
1286.7934718934	1791	Find Center of Star Graph	找出星型图的中心节点	find-center-of-star-graph	weekly-contest-232	Q2
1286.3841359213	2352	Equal Row and Column Pairs	相等行列对	equal-row-and-column-pairs	weekly-contest-303	Q2
1286.3167937403	1047	Remove All Adjacent Duplicates In String	删除字符串中的所有相邻重复项	remove-all-adjacent-duplicates-in-string	weekly-contest-137	Q2
1285.9726675488	1381	Design a Stack With Increment Operation	设计一个支持增量操作的栈	design-a-stack-with-increment-operation	weekly-contest-180	Q2
1285.7282180721	860	Lemonade Change	柠檬水找零	lemonade-change	weekly-contest-91	Q1
1285.1547123119	2839	Check if Strings Can be Made Equal With Operations I	判断通过操作能否让字符串相等 I	check-if-strings-can-be-made-equal-with-operations-i	biweekly-contest-112	Q1
1284.4514662456	1720	Decode XORed Array	解码异或后的数组	decode-xored-array	weekly-contest-223	Q1
1284.3625733813	1481	Least Number of Unique Integers after K Removals	不同整数的最少数目	least-number-of-unique-integers-after-k-removals	weekly-contest-193	Q2
1283.6412252736	2303	Calculate Amount Paid in Taxes	计算应缴税款总额	calculate-amount-paid-in-taxes	weekly-contest-297	Q1
1283.5102144800	1507	Reformat Date	转变日期格式	reformat-date	biweekly-contest-30	Q1
1283.4980318021	1252	Cells with Odd Values in a Matrix	奇数值单元格的数目	cells-with-odd-values-in-a-matrix	weekly-contest-162	Q1
1282.5186784876	2639	Find the Width of Columns of a Grid	查询网格图中每一列的宽度	find-the-width-of-columns-of-a-grid	biweekly-contest-102	Q1
1282.4111853142	1837	Sum of Digits in Base K	K 进制表示下的各位数字总和	sum-of-digits-in-base-k	weekly-contest-238	Q1
1282.3870247003	2696	Minimum String Length After Removing Substrings	删除子串后的字符串最小长度	minimum-string-length-after-removing-substrings	weekly-contest-346	Q1
1282.1502428906	2220	Minimum Bit Flips to Convert Number	转换数字的最少位翻转次数	minimum-bit-flips-to-convert-number	biweekly-contest-75	Q1
1281.9771427903	1624	Largest Substring Between Two Equal Characters	两个相同字符之间的最长子字符串	largest-substring-between-two-equal-characters	weekly-contest-211	Q1
1281.0889272532	2570	Merge Two 2D Arrays by Summing Values	合并两个二维数组 - 求和法	merge-two-2d-arrays-by-summing-values	weekly-contest-333	Q1
1280.2941647587	1572	Matrix Diagonal Sum	矩阵对角线元素的和	matrix-diagonal-sum	biweekly-contest-34	Q1
1280.2203734882	2125	Number of Laser Beams in a Bank	银行中的激光束数量	number-of-laser-beams-in-a-bank	weekly-contest-274	Q2
1279.7894769956	2269	Find the K-Beauty of a Number	找到一个数字的 K 美丽值	find-the-k-beauty-of-a-number	biweekly-contest-78	Q1
1279.7669712099	1002	Find Common Characters	查找常用字符	find-common-characters	weekly-contest-126	Q1
1279.3383966145	1534	Count Good Triplets	统计好三元组	count-good-triplets	weekly-contest-200	Q1
1279.0301521682	2807	Insert Greatest Common Divisors in Linked List	在链表中插入最大公约数	insert-greatest-common-divisors-in-linked-list	biweekly-contest-110	Q2
1278.0092842613	2582	Pass the Pillow	递枕头	pass-the-pillow	weekly-contest-335	Q1
1277.9987709491	1742	Maximum Number of Balls in a Box	盒子中小球的最大数量	maximum-number-of-balls-in-a-box	weekly-contest-226	Q1
1277.8260125315	1317	Convert Integer to the Sum of Two No-Zero Integers	将整数转换为两个无零整数的和	convert-integer-to-the-sum-of-two-no-zero-integers	weekly-contest-171	Q1
1276.7817742915	2558	Take Gifts From the Richest Pile	从数量最多的堆取走礼物	take-gifts-from-the-richest-pile	weekly-contest-331	Q1
1275.6108152653	2150	Find All Lonely Numbers in the Array	找出数组中的所有孤独数字	find-all-lonely-numbers-in-the-array	weekly-contest-277	Q3
1274.8817522170	2129	Capitalize the Title	将标题首字母大写	capitalize-the-title	biweekly-contest-69	Q1
1274.7596170193	1078	Occurrences After Bigram	Bigram 分词	occurrences-after-bigram	weekly-contest-140	Q1
1274.6742564805	1005	Maximize Sum Of Array After K Negations	K 次取反后最大化的数组和	maximize-sum-of-array-after-k-negations	weekly-contest-127	Q1
1273.0588534723	2068	Check Whether Two Strings are Almost Equivalent	检查两个字符串是否几乎相等	check-whether-two-strings-are-almost-equivalent	biweekly-contest-65	Q1
1273.0464737970	2138	Divide a String Into Groups of Size k	将字符串拆分为若干长度为 k 的组	divide-a-string-into-groups-of-size-k	weekly-contest-276	Q1
1272.3340330895	2869	Minimum Operations to Collect Elements	收集元素的最少操作次数	minimum-operations-to-collect-elements	biweekly-contest-114	Q1
1271.7726574892	2006	Count Number of Pairs With Absolute Difference K	差的绝对值为 K 的数对数目	count-number-of-pairs-with-absolute-difference-k	biweekly-contest-61	Q1
1271.7055549365	824	Goat Latin	山羊拉丁文	goat-latin	weekly-contest-82	Q1
1271.3776510163	1556	Thousand Separator	千位分隔数	thousand-separator	biweekly-contest-33	Q1
1271.3313760514	925	Long Pressed Name	长按键入	long-pressed-name	weekly-contest-107	Q1
1270.6712381632	2363	Merge Similar Items	合并相似的物品	merge-similar-items	biweekly-contest-84	Q1
1270.0775640451	2873	Maximum Value of an Ordered Triplet I	有序三元组中的最大值 I	maximum-value-of-an-ordered-triplet-i	weekly-contest-365	Q1
1269.8118442786	2843	  Count Symmetric Integers	统计对称整数的数目	count-symmetric-integers	weekly-contest-361	Q1
1269.7567553523	2032	Two Out of Three	至少在两个数组中出现的值	two-out-of-three	weekly-contest-262	Q1
1268.5768566953	1447	Simplified Fractions	最简分数	simplified-fractions	biweekly-contest-26	Q2
1268.0287696194	2325	Decode the Message	解密消息	decode-the-message	weekly-contest-300	Q1
1267.2235913660	1282	Group the People Given the Group Size They Belong To	用户分组	group-the-people-given-the-group-size-they-belong-to	weekly-contest-166	Q2
1266.7001363197	2432	The Employee That Worked on the Longest Task	处理用时最长的那个任务的员工	the-employee-that-worked-on-the-longest-task	weekly-contest-314	Q1
1266.5231114343	2670	Find the Distinct Difference Array	找出不同元素数目差数组	find-the-distinct-difference-array	weekly-contest-344	Q1
1266.5014127879	2785	Sort Vowels in a String	将字符串中的元音字母排序	sort-vowels-in-a-string	biweekly-contest-109	Q2
1266.3414689550	2200	Find All K-Distant Indices in an Array	找出数组中的所有 K 近邻下标	find-all-k-distant-indices-in-an-array	weekly-contest-284	Q1
1266.3368046515	821	Shortest Distance to a Character	字符的最短距离	shortest-distance-to-a-character	weekly-contest-81	Q1
1265.8320564115	2549	Count Distinct Numbers on Board	统计桌面上的不同数字	count-distinct-numbers-on-board	weekly-contest-330	Q1
1264.4836883082	1736	Latest Time by Replacing Hidden Digits	替换隐藏数字得到的最晚时间	latest-time-by-replacing-hidden-digits	weekly-contest-225	Q1
1264.4778916192	2248	Intersection of Multiple Arrays	多个数组求交集	intersection-of-multiple-arrays	weekly-contest-290	Q1
1264.2868345638	2133	Check if Every Row and Column Contains All Numbers	检查是否每一行每一列都包含全部整数	check-if-every-row-and-column-contains-all-numbers	weekly-contest-275	Q1
1263.2728668041	1456	Maximum Number of Vowels in a Substring of Given Length	定长子串中元音的最大数目	maximum-number-of-vowels-in-a-substring-of-given-length	weekly-contest-190	Q2
1262.9387403640	2490	Circular Sentence	回环句	circular-sentence	weekly-contest-322	Q1
1262.5890311992	1089	Duplicate Zeros	复写零	duplicate-zeros	weekly-contest-141	Q1
1262.1006527970	2739	Total Distance Traveled	总行驶距离	total-distance-traveled	weekly-contest-350	Q1
1260.9112824221	2144	Minimum Cost of Buying Candies With Discount	打折购买糖果的最小开销	minimum-cost-of-buying-candies-with-discount	biweekly-contest-70	Q1
1260.8702083080	2255	Count Prefixes of a Given String	统计是给定字符串前缀的字符串数目	count-prefixes-of-a-given-string	biweekly-contest-77	Q1
1260.8697515006	2520	Count the Digits That Divide a Number	统计能整除数字的位数	count-the-digits-that-divide-a-number	weekly-contest-326	Q1
1260.1755576607	1305	All Elements in Two Binary Search Trees	两棵二叉搜索树中的所有元素	all-elements-in-two-binary-search-trees	weekly-contest-169	Q2
1259.9491377450	2562	Find the Array Concatenation Value	找出数组的串联值	find-the-array-concatenation-value	weekly-contest-332	Q1
1259.5707438932	1779	Find Nearest Point That Has the Same X or Y Coordinate	找到最近的有相同 X 或 Y 坐标的点	find-nearest-point-that-has-the-same-x-or-y-coordinate	biweekly-contest-47	Q1
1259.4097261890	884	Uncommon Words from Two Sentences	两句话中的不常见单词	uncommon-words-from-two-sentences	weekly-contest-97	Q1
1259.3406231708	2404	Most Frequent Even Element	出现最频繁的偶数元素	most-frequent-even-element	weekly-contest-310	Q1
1259.1979660519	1213	Intersection of Three Sorted Arrays	三个有序数组的交集	intersection-of-three-sorted-arrays	biweekly-contest-10	Q1
1258.8401788462	867	Transpose Matrix	转置矩阵	transpose-matrix	weekly-contest-92	Q1
1258.6719675401	896	Monotonic Array	单调数列	monotonic-array	weekly-contest-100	Q1
1257.8344655358	2644	Find the Maximum Divisibility Score	找出可整除性得分最大的整数	find-the-maximum-divisibility-score	weekly-contest-341	Q2
1257.7670945029	2103	Rings and Rods	环和杆	rings-and-rods	weekly-contest-271	Q1
1257.7082143289	1356	Sort Integers by The Number of 1 Bits	根据数字二进制下 1 的数目排序	sort-integers-by-the-number-of-1-bits	biweekly-contest-20	Q1
1257.6796331650	1309	Decrypt String from Alphabet to Integer Mapping	解码字母到整数映射	decrypt-string-from-alphabet-to-integer-mapping	weekly-contest-170	Q1
1257.3235146110	2114	Maximum Number of Words Found in Sentences	句子中的最多单词数	maximum-number-of-words-found-in-sentences	biweekly-contest-68	Q1
1257.2649235990	2042	Check if Numbers Are Ascending in a Sentence	检查句子中的数字是否递增	check-if-numbers-are-ascending-in-a-sentence	weekly-contest-263	Q1
1257.1556875655	2177	Find Three Consecutive Integers That Sum to a Given Number	找到和为给定整数的三个连续整数	find-three-consecutive-integers-that-sum-to-a-given-number	biweekly-contest-72	Q2
1257.1166915286	2180	Count Integers With Even Digit Sum	统计各位数字之和为偶数的整数个数	count-integers-with-even-digit-sum	weekly-contest-281	Q1
1256.6807087287	1732	Find the Highest Altitude	找到最高海拔	find-the-highest-altitude	biweekly-contest-44	Q1
1256.4891142083	1085	Sum of Digits in the Minimum Number	最小元素各数位之和	sum-of-digits-in-the-minimum-number	biweekly-contest-2	Q1
1256.0514740971	2239	Find Closest Number to Zero	找到最接近 0 的数字	find-closest-number-to-zero	biweekly-contest-76	Q1
1255.9002796024	1037	Valid Boomerang	有效的回旋镖	valid-boomerang	weekly-contest-135	Q1
1255.5461825223	2475	Number of Unequal Triplets in Array	数组中不等三元组的数目	number-of-unequal-triplets-in-array	weekly-contest-320	Q1
1254.8626139269	1945	Sum of Digits of String After Convert	字符串转化后的各位数字之和	sum-of-digits-of-string-after-convert	weekly-contest-251	Q1
1253.5161450678	2908	Minimum Sum of Mountain Triplets I	元素和最小的山形三元组 I	minimum-sum-of-mountain-triplets-i	weekly-contest-368	Q1
1253.4847783954	2283	Check if Number Has Equal Digit Count and Digit Value	判断一个数的数字计数是否等于数位的值	check-if-number-has-equal-digit-count-and-digit-value	biweekly-contest-79	Q1
1253.1463945043	2194	Cells in a Range on an Excel Sheet	Excel 表中某个范围内的单元格	cells-in-a-range-on-an-excel-sheet	weekly-contest-283	Q1
1253.1107481745	2186	Minimum Number of Steps to Make Two Strings Anagram II	使两字符串互为字母异位词的最少步骤数	minimum-number-of-steps-to-make-two-strings-anagram-ii	weekly-contest-282	Q2
1252.8406166148	2164	Sort Even and Odd Indices Independently	对奇偶下标分别排序	sort-even-and-odd-indices-independently	weekly-contest-279	Q1
1252.7479413966	1833	Maximum Ice Cream Bars	雪糕的最大数量	maximum-ice-cream-bars	weekly-contest-237	Q2
1251.8223786910	830	Positions of Large Groups	较大分组的位置	positions-of-large-groups	weekly-contest-83	Q1
1250.8974254752	2315	Count Asterisks	统计星号	count-asterisks	biweekly-contest-81	Q1
1250.0975318308	2465	Number of Distinct Averages	不同的平均值数目	number-of-distinct-averages	biweekly-contest-91	Q1
1249.9947800752	1150	Check If a Number Is Majority Element in a Sorted Array	检查一个数是否在数组中占绝大多数	check-if-a-number-is-majority-element-in-a-sorted-array	biweekly-contest-6	Q1
1249.9086403595	1161	Maximum Level Sum of a Binary Tree	最大层内元素和	maximum-level-sum-of-a-binary-tree	weekly-contest-150	Q2
1249.8425270142	2395	Find Subarrays With Equal Sum	和相等的子数组	find-subarrays-with-equal-sum	biweekly-contest-86	Q1
1249.7770522505	3000	Maximum Area of Longest Diagonal Rectangle	对角线最长的矩形的面积	maximum-area-of-longest-diagonal-rectangle	weekly-contest-379	Q1
1249.7515196656	2540	Minimum Common Value	最小公共值	minimum-common-value	biweekly-contest-96	Q1
1249.4294341104	766	Toeplitz Matrix	托普利茨矩阵	toeplitz-matrix	weekly-contest-68	Q1
1249.2572200035	2279	Maximum Bags With Full Capacity of Rocks	装满石头的背包的最大数量	maximum-bags-with-full-capacity-of-rocks	weekly-contest-294	Q2
1248.8547072235	1903	Largest Odd Number in String	字符串中的最大奇数	largest-odd-number-in-string	weekly-contest-246	Q1
1248.8026990632	1196	How Many Apples Can You Put into the Basket	最多可以买到的苹果数量	how-many-apples-can-you-put-into-the-basket	biweekly-contest-9	Q1
1248.7224675206	1876	Substrings of Size Three with Distinct Characters	长度为三且各字符不同的子字符串	substrings-of-size-three-with-distinct-characters	biweekly-contest-53	Q1
1247.3198836387	1232	Check If It Is a Straight Line	缀点成线	check-if-it-is-a-straight-line	weekly-contest-159	Q1
1246.3593898992	2932	Maximum Strong Pair XOR I	找出强数对的最大异或值 I	maximum-strong-pair-xor-i	weekly-contest-371	Q1
1246.0341186297	2481	Minimum Cuts to Divide a Circle	分割圆的最少切割次数	minimum-cuts-to-divide-a-circle	biweekly-contest-92	Q1
1246.0141927368	2016	Maximum Difference Between Increasing Elements	增量元素之间的最大差值	maximum-difference-between-increasing-elements	weekly-contest-260	Q1
1245.2999833877	1518	Water Bottles	换酒问题	water-bottles	weekly-contest-198	Q1
1245.2741257148	1099	Two Sum Less Than K	小于 K 的两数之和	two-sum-less-than-k	biweekly-contest-3	Q1
1244.8064626533	2965	Find Missing and Repeated Values	找出缺失和重复的数字	find-missing-and-repeated-values	weekly-contest-376	Q1
1244.3173678830	1228	Missing Number In Arithmetic Progression	等差数列中缺失的数字	missing-number-in-arithmetic-progression	biweekly-contest-11	Q1
1243.6250741657	2399	Check Distances Between Same Letters	检查相同字母间的距离	check-distances-between-same-letters	weekly-contest-309	Q1
1243.1009943284	832	Flipping an Image	翻转图像	flipping-an-image	weekly-contest-84	Q1
1242.9383307344	2716	Minimize String Length	最小化字符串长度	minimize-string-length	weekly-contest-348	Q1
1242.8939284628	2309	Greatest English Letter in Upper and Lower Case	兼具大小写的最好英文字母	greatest-english-letter-in-upper-and-lower-case	weekly-contest-298	Q1
1242.6172898768	1941	Check if All Characters Have Equal Number of Occurrences	检查是否所有字符出现次数相同	check-if-all-characters-have-equal-number-of-occurrences	biweekly-contest-57	Q1
1242.4710735813	921	Minimum Add to Make Parentheses Valid	使括号有效的最少添加	minimum-add-to-make-parentheses-valid	weekly-contest-106	Q2
1241.9262857175	1417	Reformat The String	重新格式化字符串	reformat-the-string	weekly-contest-185	Q1
1241.5775825621	2605	Form Smallest Number From Two Digit Arrays	从两个数字数组里生成最小数字	form-smallest-number-from-two-digit-arrays	biweekly-contest-101	Q1
1241.5645130241	2347	Best Poker Hand	最好的扑克手牌	best-poker-hand	biweekly-contest-83	Q1
1241.5396695569	2299	Strong Password Checker II	强密码检验器 II	strong-password-checker-ii	biweekly-contest-80	Q1
1241.0825147417	2293	Min Max Game	极大极小游戏	min-max-game	weekly-contest-296	Q1
1240.8297581760	2078	Two Furthest Houses With Different Colors	两栋颜色不同且距离最远的房子	two-furthest-houses-with-different-colors	weekly-contest-268	Q1
1239.1621762681	2788	Split Strings by Separator	按分隔符拆分字符串	split-strings-by-separator	weekly-contest-355	Q1
1237.7565585875	1422	Maximum Score After Splitting a String	分割字符串的最大得分	maximum-score-after-splitting-a-string	weekly-contest-186	Q1
1237.6934646090	2864	Maximum Odd Binary Number	最大二进制奇数	maximum-odd-binary-number	weekly-contest-364	Q1
1235.9216009709	2149	Rearrange Array Elements by Sign	按符号重排数组	rearrange-array-elements-by-sign	weekly-contest-277	Q2
1235.8413685224	2154	Keep Multiplying Found Values by Two	将找到的值乘以 2	keep-multiplying-found-values-by-two	weekly-contest-278	Q1
1235.6484230513	2923	Find Champion I	找到冠军 I	find-champion-i	weekly-contest-370	Q1
1235.6114196155	1816	Truncate Sentence	截断句子	truncate-sentence	weekly-contest-235	Q1
1234.8049089605	1385	Find the Distance Value Between Two Arrays	两个数组间的距离值	find-the-distance-value-between-two-arrays	biweekly-contest-22	Q1
1234.7692637513	989	Add to Array-Form of Integer	数组形式的整数加法	add-to-array-form-of-integer	weekly-contest-123	Q1
1234.7084656358	1009	Complement of Base 10 Integer	十进制整数的反码	complement-of-base-10-integer	weekly-contest-128	Q1
1234.4144116814	1184	Distance Between Bus Stops	公交站间的距离	distance-between-bus-stops	weekly-contest-153	Q1
1234.0585375650	1961	Check If String Is a Prefix of Array	检查字符串是否为数组前缀	check-if-string-is-a-prefix-of-array	weekly-contest-253	Q1
1233.5034839998	2980	Check if Bitwise OR Has Trailing Zeros	检查按位或是否存在尾随零	check-if-bitwise-or-has-trailing-zeros	weekly-contest-378	Q1
1232.8314427996	1119	Remove Vowels from a String	删去字符串中的元音	remove-vowels-from-a-string	biweekly-contest-4	Q2
1231.9992413350	1492	The kth Factor of n	n 的第 k 个因子	the-kth-factor-of-n	biweekly-contest-29	Q2
1231.8671440198	1967	Number of Strings That Appear as Substrings in Word	作为子字符串出现在单词中的字符串数目	number-of-strings-that-appear-as-substrings-in-word	weekly-contest-254	Q1
1231.6157956848	876	Middle of the Linked List	链表的中间结点	middle-of-the-linked-list	weekly-contest-95	Q1
1231.4004525633	1134	Armstrong Number	阿姆斯特朗数	armstrong-number	biweekly-contest-5	Q2
1229.7575626899	2848	Points That Intersect With Cars	与车相交的点	points-that-intersect-with-cars	weekly-contest-362	Q1
1229.4850365142	1725	Number Of Rectangles That Can Form The Largest Square	可以形成最大正方形的矩形数目	number-of-rectangles-that-can-form-the-largest-square	weekly-contest-224	Q1
1229.1709574783	1800	Maximum Ascending Subarray Sum	最大升序子数组和	maximum-ascending-subarray-sum	weekly-contest-233	Q1
1228.6309936480	917	Reverse Only Letters	仅仅反转字母	reverse-only-letters	weekly-contest-105	Q1
1228.4824438011	1748	Sum of Unique Elements	唯一元素的和	sum-of-unique-elements	biweekly-contest-45	Q1
1227.9103734800	2729	Check if The Number is Fascinating	判断一个数是否迷人	check-if-the-number-is-fascinating	biweekly-contest-106	Q1
1227.7906887239	844	Backspace String Compare	比较含退格的字符串	backspace-string-compare	weekly-contest-87	Q1
1227.3485530532	1118	Number of Days in a Month	一月有多少天	number-of-days-in-a-month	biweekly-contest-4	Q1
1226.8332278145	1935	Maximum Number of Words You Can Type	可以输入的最大单词数	maximum-number-of-words-you-can-type	weekly-contest-250	Q1
1226.2960135431	1133	Largest Unique Number	最大唯一数	largest-unique-number	biweekly-contest-5	Q1
1225.3923012413	2357	Make Array Zero by Subtracting Equal Amounts	使数组中所有元素都等于零	make-array-zero-by-subtracting-equal-amounts	weekly-contest-304	Q1
1225.3601348675	1346	Check If N and Its Double Exist	检查整数及其两倍数是否存在	check-if-n-and-its-double-exist	weekly-contest-175	Q1
1224.7606792444	1337	The K Weakest Rows in a Matrix	矩阵中战斗力最弱的 K 行	the-k-weakest-rows-in-a-matrix	weekly-contest-174	Q1
1223.9335618833	2460	Apply Operations to an Array	对数组执行操作	apply-operations-to-an-array	weekly-contest-318	Q1
1223.4065703960	2206	Divide Array Into Equal Pairs	将数组划分成相等数对	divide-array-into-equal-pairs	biweekly-contest-74	Q1
1223.3861903833	1408	String Matching in an Array	数组中的字符串匹配	string-matching-in-an-array	weekly-contest-184	Q1
1222.2354919459	2535	Difference Between Element Sum and Digit Sum of an Array	数组元素和与数字和的绝对差	difference-between-element-sum-and-digit-sum-of-an-array	weekly-contest-328	Q1
1221.9872943569	1678	Goal Parser Interpretation	设计 Goal 解析器	goal-parser-interpretation	weekly-contest-218	Q1
1221.8477681772	2414	Length of the Longest Alphabetical Continuous Substring	最长的字母序连续子字符串的长度	length-of-the-longest-alphabetical-continuous-substring	weekly-contest-311	Q2
1221.6801628274	1550	Three Consecutive Odds	存在连续三个奇数的数组	three-consecutive-odds	weekly-contest-202	Q1
1219.5284561367	1221	Split a String in Balanced Strings	分割平衡字符串	split-a-string-in-balanced-strings	weekly-contest-158	Q1
1219.4252907184	1299	Replace Elements with Greatest Element on Right Side	将每个元素替换为右侧最大元素	replace-elements-with-greatest-element-on-right-side	biweekly-contest-16	Q1
1218.9011436003	2442	Count Number of Distinct Integers After Reverse Operations	反转之后不同整数的数目	count-number-of-distinct-integers-after-reverse-operations	weekly-contest-315	Q2
1218.1083231462	2859	Sum of Values at Indices With K Set Bits	计算 K 置位下标对应元素的和	sum-of-values-at-indices-with-k-set-bits	weekly-contest-363	Q1
1217.1184374247	1662	Check If Two String Arrays are Equivalent	检查两个字符串数组是否相等	check-if-two-string-arrays-are-equivalent	weekly-contest-216	Q1
1216.9550221615	3005	Count Elements With Maximum Frequency	最大频率元素计数	count-elements-with-maximum-frequency	weekly-contest-380	Q1
1216.6376846517	1848	Minimum Distance to the Target Element	到目标元素的最小距离	minimum-distance-to-the-target-element	weekly-contest-239	Q1
1216.6129188490	2553	Separate the Digits in an Array	分割数组中数字的数位	separate-the-digits-in-an-array	biweekly-contest-97	Q1
1215.7827321325	2176	Count Equal and Divisible Pairs in an Array	统计数组中相等且可以被整除的数对	count-equal-and-divisible-pairs-in-an-array	biweekly-contest-72	Q1
1215.7443346869	2108	Find First Palindromic String in the Array	找出数组中的第一个回文字符串	find-first-palindromic-string-in-the-array	weekly-contest-272	Q1
1214.7037247760	2806	Account Balance After Rounded Purchase	取整购买后的账户余额	account-balance-after-rounded-purchase	biweekly-contest-110	Q1
1214.5428648910	2956	Find Common Elements Between Two Arrays	找到两个数组中的公共元素	find-common-elements-between-two-arrays	biweekly-contest-119	Q1
1214.2480880984	3042	Count Prefix and Suffix Pairs I	统计前后缀下标对 I	count-prefix-and-suffix-pairs-i	weekly-contest-385	Q1
1213.8073621345	973	K Closest Points to Origin	最接近原点的 K 个点	k-closest-points-to-origin	weekly-contest-119	Q1
1213.4070467355	2656	Maximum Sum With Exactly K Elements 	K 个元素的最大和	maximum-sum-with-exactly-k-elements	biweekly-contest-103	Q1
1212.2606422181	1475	Final Prices With a Special Discount in a Shop	商品折扣后的最终价格	final-prices-with-a-special-discount-in-a-shop	biweekly-contest-28	Q1
1212.2309421538	1413	Minimum Value to Get Positive Step by Step Sum	逐步求和得到正数的最小值	minimum-value-to-get-positive-step-by-step-sum	biweekly-contest-24	Q1
1212.2079075334	3046	Split the Array	分割数组	split-the-array	weekly-contest-386	Q1
1209.6571020247	1822	Sign of the Product of an Array	数组元素积的符号	sign-of-the-product-of-an-array	weekly-contest-236	Q1
1209.3722198224	1523	Count Odd Numbers in an Interval Range	在区间范围内统计奇数数目	count-odd-numbers-in-an-interval-range	biweekly-contest-31	Q1
1208.0417047337	1389	Create Target Array in the Given Order	按既定顺序创建目标数组	create-target-array-in-the-given-order	weekly-contest-181	Q1
1208.0130656905	941	Valid Mountain Array	有效的山脉数组	valid-mountain-array	weekly-contest-111	Q1
1207.7810914125	1380	Lucky Numbers in a Matrix	矩阵中的幸运数	lucky-numbers-in-a-matrix	weekly-contest-180	Q1
1207.7491943483	2706	Buy Two Chocolates	购买两块巧克力	buy-two-chocolates	biweekly-contest-105	Q1
1207.7482390750	2215	Find the Difference of Two Arrays	找出两数组的不同	find-the-difference-of-two-arrays	weekly-contest-286	Q1
1207.7224406285	1704	Determine if String Halves Are Alike	判断字符串的两半是否相似	determine-if-string-halves-are-alike	weekly-contest-221	Q1
1207.3151378208	2485	Find the Pivot Integer	找出中枢整数	find-the-pivot-integer	weekly-contest-321	Q1
1206.5675296817	2595	Number of Even and Odd Bits	奇偶位数	number-of-even-and-odd-bits	weekly-contest-337	Q1
1206.1240971343	1784	Check if Binary String Has at Most One Segment of Ones	检查二进制字符串字段	check-if-binary-string-has-at-most-one-segment-of-ones	weekly-contest-231	Q1
1206.0712568518	2574	Left and Right Sum Differences	左右元素和的差值	left-and-right-sum-differences	weekly-contest-334	Q1
1205.6698455508	1160	Find Words That Can Be Formed by Characters	拼写单词	find-words-that-can-be-formed-by-characters	weekly-contest-150	Q1
1204.9864820183	1869	Longer Contiguous Segments of Ones than Zeros	哪种连续子字符串更长	longer-contiguous-segments-of-ones-than-zeros	weekly-contest-242	Q1
1203.7504950404	1952	Three Divisors	三除数	three-divisors	weekly-contest-252	Q1
1203.1408035909	1688	Count of Matches in Tournament	比赛中的配对次数	count-of-matches-in-tournament	weekly-contest-219	Q1
1203.0737869081	2367	Number of Arithmetic Triplets	算术三元组的数目	number-of-arithmetic-triplets	weekly-contest-305	Q1
1201.8730954169	2148	Count Elements With Strictly Smaller and Greater Elements 	元素计数	count-elements-with-strictly-smaller-and-greater-elements	weekly-contest-277	Q1
1201.7810344050	3038	Maximum Number of Operations With the Same Score I	相同分数的最大操作数目 I	maximum-number-of-operations-with-the-same-score-i	biweekly-contest-124	Q1
1201.7686271329	2124	Check if All A's Appears Before All B's	检查是否所有 A 都在 B 之前	check-if-all-as-appears-before-all-bs	weekly-contest-274	Q1
1201.6117337798	997	Find the Town Judge	找到小镇的法官	find-the-town-judge	weekly-contest-125	Q1
1201.3497763919	1491	Average Salary Excluding the Minimum and Maximum Salary	去掉最低工资和最高工资后的工资平均值	average-salary-excluding-the-minimum-and-maximum-salary	biweekly-contest-29	Q1
1200.9464053417	2319	Check if Matrix Is X-Matrix	判断矩阵是否是一个 X 矩阵	check-if-matrix-is-x-matrix	weekly-contest-299	Q1
1199.8592887103	2169	Count Operations to Obtain Zero	得到 0 的操作数	count-operations-to-obtain-zero	weekly-contest-280	Q1
1199.4477805501	2000	Reverse Prefix of Word	反转单词前缀	reverse-prefix-of-word	weekly-contest-258	Q1
1199.4427635582	1154	Day of the Year	一年中的第几天	day-of-the-year	weekly-contest-149	Q1
1199.2892732505	929	Unique Email Addresses	独特的电子邮件地址	unique-email-addresses	weekly-contest-108	Q1
1199.2392672964	1165	Single-Row Keyboard	单行键盘	single-row-keyboard	biweekly-contest-7	Q1
1198.8420836551	2678	Number of Senior Citizens	老人的数目	number-of-senior-citizens	biweekly-contest-104	Q1
1198.5705825982	1200	Minimum Absolute Difference	最小绝对差	minimum-absolute-difference	weekly-contest-155	Q1
1198.4180401014	985	Sum of Even Numbers After Queries	查询后的偶数和	sum-of-even-numbers-after-queries	weekly-contest-122	Q1
1195.9731842298	2529	Maximum Count of Positive Integer and Negative Integer	正整数和负整数的最大计数	maximum-count-of-positive-integer-and-negative-integer	weekly-contest-327	Q1
1195.7512695571	1207	Unique Number of Occurrences	独一无二的出现次数	unique-number-of-occurrences	weekly-contest-156	Q1
1193.9819783429	1323	Maximum 69 Number	6 和 9 组成的最大数字	maximum-69-number	weekly-contest-172	Q1
1193.2687290573	1437	Check If All 1's Are at Least Length K Places Away	是否所有 1 都至少相隔 k 个元素	check-if-all-1s-are-at-least-length-k-places-away	weekly-contest-187	Q2
1193.1328299324	1528	Shuffle String	重新排列字符串	shuffle-string	weekly-contest-199	Q1
1193.0585534828	2418	Sort the People	按身高排序	sort-the-people	weekly-contest-312	Q1
1192.9770230345	2810	Faulty Keyboard	故障键盘	faulty-keyboard	weekly-contest-357	Q1
1192.3167969426	1436	Destination City	旅行终点站	destination-city	weekly-contest-187	Q1
1191.3681720998	2769	Find the Maximum Achievable Number	找出最大的可达成数字	find-the-maximum-achievable-number	weekly-contest-353	Q1
1189.4358388136	2951	Find the Peaks	找出峰值	find-the-peaks	weekly-contest-374	Q1
1188.6470369782	747	Largest Number At Least Twice of Others	至少是其他数字两倍的最大数	largest-number-at-least-twice-of-others	weekly-contest-64	Q1
1188.6311093158	1122	Relative Sort Array	数组的相对排序	relative-sort-array	weekly-contest-145	Q1
1187.1641565458	1880	Check if Word Equals Summation of Two Words	检查某单词是否等于两单词之和	check-if-word-equals-summation-of-two-words	weekly-contest-243	Q1
1187.1344261572	2119	A Number After a Double Reversal	反转两次的数字	a-number-after-a-double-reversal	weekly-contest-273	Q1
1184.8359383057	2974	Minimum Number Game	最小数字游戏	minimum-number-game	weekly-contest-377	Q1
1184.7957212840	2341	Maximum Number of Pairs in Array	数组能形成多少数对	maximum-number-of-pairs-in-array	weekly-contest-302	Q1
1184.4264833435	1979	Find Greatest Common Divisor of Array	找出数组的最大公约数	find-greatest-common-divisor-of-array	weekly-contest-255	Q1
1184.3385083575	2544	Alternating Digit Sum	交替数字和	alternating-digit-sum	weekly-contest-329	Q1
1182.6489068544	1672	Richest Customer Wealth	最富有客户的资产总量	richest-customer-wealth	weekly-contest-217	Q1
1182.3093772964	2652	Sum Multiples	倍数求和	sum-multiples	weekly-contest-342	Q2
1182.2102562446	2942	Find Words Containing Character	查找包含给定字符的单词	find-words-containing-character	biweekly-contest-118	Q1
1181.9716216714	1189	Maximum Number of Balloons	“气球” 的最大数量	maximum-number-of-balloons	weekly-contest-154	Q1
1181.5839867359	852	Peak Index in a Mountain Array	山脉数组的峰顶索引	peak-index-in-a-mountain-array	weekly-contest-89	Q1
1180.9236239060	1486	XOR Operation in an Array	数组异或操作	xor-operation-in-an-array	weekly-contest-194	Q1
1180.5927490268	3033	Modify the Matrix	修改矩阵	modify-the-matrix	weekly-contest-384	Q1
1180.3543157775	1441	Build an Array With Stack Operations	用栈操作构建数组	build-an-array-with-stack-operations	weekly-contest-188	Q1
1179.1495967491	1287	Element Appearing More Than 25% In Sorted Array	有序数组中出现次数超过25%的元素	element-appearing-more-than-25-in-sorted-array	biweekly-contest-15	Q1
1178.6580069402	2586	Count the Number of Vowel Strings in Range	统计范围内的元音字符串数	count-the-number-of-vowel-strings-in-range	weekly-contest-336	Q1
1178.4942541235	905	Sort Array By Parity	按奇偶排序数组	sort-array-by-parity	weekly-contest-102	Q1
1177.5660617941	965	Univalued Binary Tree	单值二叉树	univalued-binary-tree	weekly-contest-117	Q1
1176.4547272896	1431	Kids With the Greatest Number of Candies	拥有最多糖果的孩子	kids-with-the-greatest-number-of-candies	biweekly-contest-25	Q1
1175.5552151972	3019	Number of Changing Keys	按键变更的次数	number-of-changing-keys	weekly-contest-382	Q1
1174.8589329736	1773	Count Items Matching a Rule	统计匹配检索规则的物品数量	count-items-matching-a-rule	weekly-contest-230	Q1
1174.3019990918	2643	Row With Maximum Ones	一最多的行	row-with-maximum-ones	weekly-contest-341	Q1
1173.5059264820	922	Sort Array By Parity II	按奇偶排序数组 II	sort-array-by-parity-ii	weekly-contest-106	Q1
1172.6819789183	1046	Last Stone Weight	最后一块石头的重量	last-stone-weight	weekly-contest-137	Q1
1172.5106645463	760	Find Anagram Mappings	找出变位映射	find-anagram-mappings	weekly-contest-66	Q1
1172.0548998046	2427	Number of Common Factors	公因子的数目	number-of-common-factors	weekly-contest-313	Q1
1169.4209117977	2960	Count Tested Devices After Test Operations	统计已测试设备	count-tested-devices-after-test-operations	weekly-contest-375	Q1
1168.6157473032	2651	Calculate Delayed Arrival Time	计算列车到站时间	calculate-delayed-arrival-time	weekly-contest-342	Q1
1167.8737144048	2057	Smallest Index With Equal Value	值相等的最小索引	smallest-index-with-equal-value	weekly-contest-265	Q1
1167.6471225010	2441	Largest Positive Integer That Exists With Its Negative	与对应负数同时存在的最大正整数	largest-positive-integer-that-exists-with-its-negative	weekly-contest-315	Q1
1167.1331831913	1304	Find N Unique Integers Sum up to Zero	和为零的N个唯一整数	find-n-unique-integers-sum-up-to-zero	weekly-contest-169	Q1
1167.1241589729	2185	Counting Words With a Given Prefix	统计包含给定前缀的字符串	counting-words-with-a-given-prefix	weekly-contest-282	Q1
1167.0749837258	796	Rotate String	旋转字符串	rotate-string	weekly-contest-75	Q1
1166.7881833200	1832	Check if the Sentence Is Pangram	判断句子是否为全字母句	check-if-the-sentence-is-pangram	weekly-contest-237	Q1
1166.5264284193	1768	Merge Strings Alternately	交替合并字符串	merge-strings-alternately	weekly-contest-229	Q1
1165.8838207286	2824	Count Pairs Whose Sum is Less than Target	统计和小于目标的下标对数目	count-pairs-whose-sum-is-less-than-target	biweekly-contest-111	Q1
1165.4768151611	1446	Consecutive Characters	连续字符	consecutive-characters	biweekly-contest-26	Q1
1165.2135167215	2011	Final Value of Variable After Performing Operations	执行操作后的变量值	final-value-of-variable-after-performing-operations	weekly-contest-259	Q1
1164.8182315157	771	Jewels and Stones	宝石与石头	jewels-and-stones	weekly-contest-69	Q1
1164.5575871589	2710	Remove Trailing Zeros From a String	移除字符串中的尾随零	remove-trailing-zeros-from-a-string	weekly-contest-347	Q1
1164.0227691933	1374	Generate a String With Characters That Have Odd Counts	生成每种字符都是奇数个的字符串	generate-a-string-with-characters-that-have-odd-counts	weekly-contest-179	Q1
1163.6047095526	1342	Number of Steps to Reduce a Number to Zero	将数字变成 0 的操作次数	number-of-steps-to-reduce-a-number-to-zero	biweekly-contest-19	Q1
1161.8236318927	2278	Percentage of Letter in String	字母在字符串中的百分比	percentage-of-letter-in-string	weekly-contest-294	Q1
1161.6227767245	961	N-Repeated Element in Size 2N Array	重复 N 次的元素	n-repeated-element-in-size-2n-array	weekly-contest-116	Q1
1160.8899403409	1512	Number of Good Pairs	好数对的数目	number-of-good-pairs	weekly-contest-197	Q1
1160.4439395369	1920	Build Array from Permutation	基于排列构建数组	build-array-from-permutation	weekly-contest-248	Q1
1157.6407631819	2903	Find Indices With Index and Value Difference I	找出满足差值条件的下标 I	find-indices-with-index-and-value-difference-i	weekly-contest-367	Q1
1155.4545579447	2351	First Letter to Appear Twice	第一个出现两次的字母	first-letter-to-appear-twice	weekly-contest-303	Q1
1154.8280679790	1502	Can Make Arithmetic Progression From Sequence	判断能否形成等差数列	can-make-arithmetic-progression-from-sequence	weekly-contest-196	Q1
1153.4272559620	2469	Convert the Temperature	温度转换	convert-the-temperature	weekly-contest-319	Q1
1152.1494742874	2089	Find Target Indices After Sorting Array	找出数组排序后的目标下标	find-target-indices-after-sorting-array	weekly-contest-269	Q1
1152.1377893605	1365	How Many Numbers Are Smaller Than the Current Number	有多少小于当前数字的数字	how-many-numbers-are-smaller-than-the-current-number	weekly-contest-178	Q1
1151.9713084499	2828	Check if a String Is an Acronym of Words	判别首字母缩略词	check-if-a-string-is-an-acronym-of-words	weekly-contest-359	Q1
1151.9363042898	2778	Sum of Squares of Special Elements 	特殊元素平方和	sum-of-squares-of-special-elements	weekly-contest-354	Q1
1151.5250329621	1460	Make Two Arrays Equal by Reversing Sub-arrays	通过翻转子数组使两个数组相等	make-two-arrays-equal-by-reversing-subarrays	biweekly-contest-27	Q1
1151.3534799042	1290	Convert Binary Number in a Linked List to Integer	二进制链表转整数	convert-binary-number-in-a-linked-list-to-integer	weekly-contest-167	Q1
1151.2537511408	2455	Average Value of Even Numbers That Are Divisible by Three	可被三整除的偶数的平均值	average-value-of-even-numbers-that-are-divisible-by-three	weekly-contest-317	Q1
1147.8274860083	2733	Neither Minimum nor Maximum	既不是最小值也不是最大值	neither-minimum-nor-maximum	weekly-contest-349	Q1
1144.9508874557	2413	Smallest Even Multiple	最小偶倍数	smallest-even-multiple	weekly-contest-311	Q1
1144.6237559885	1913	Maximum Product Difference Between Two Pairs	两个数对之间的最大乘积差	maximum-product-difference-between-two-pairs	weekly-contest-247	Q1
1142.8650731632	1137	N-th Tribonacci Number	第 N 个泰波那契数	n-th-tribonacci-number	weekly-contest-147	Q1
1142.0341823205	2798	Number of Employees Who Met the Target	满足目标工作时长的员工数目	number-of-employees-who-met-the-target	weekly-contest-356	Q1
1141.2363999461	1281	Subtract the Product and Sum of Digits of an Integer	整数的各位积和之差	subtract-the-product-and-sum-of-digits-of-an-integer	weekly-contest-166	Q1
1140.0534541481	2894	Divisible and Non-divisible Sums Difference	分类求和并作差	divisible-and-non-divisible-sums-difference	weekly-contest-366	Q1
1139.6630206282	1295	Find Numbers with Even Number of Digits	统计位数为偶数的数字	find-numbers-with-even-number-of-digits	weekly-contest-168	Q1
1139.4248492279	1351	Count Negative Numbers in a Sorted Matrix	统计有序矩阵中的负数	count-negative-numbers-in-a-sorted-matrix	weekly-contest-176	Q1
1134.7862697576	3024	Type of Triangle	三角形类型	type-of-triangle	biweekly-contest-123	Q1
1132.6812943289	1929	Concatenation of Array	数组串联	concatenation-of-array	weekly-contest-249	Q1
1129.9490902320	977	Squares of a Sorted Array	有序数组的平方	squares-of-a-sorted-array	weekly-contest-120	Q1
1129.3432988996	1450	Number of Students Doing Homework at a Given Time	在既定时间做作业的学生人数	number-of-students-doing-homework-at-a-given-time	weekly-contest-189	Q1
1125.5752382740	1455	Check If a Word Occurs As a Prefix of Any Word in a Sentence	检查单词是否为句中其他单词的前缀	check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence	weekly-contest-190	Q1
1121.0677596555	1464	Maximum Product of Two Elements in an Array	数组中两元素的最大乘积	maximum-product-of-two-elements-in-an-array	weekly-contest-191	Q1
1120.6981836240	1470	Shuffle the Array	重新排列数组	shuffle-the-array	weekly-contest-192	Q1
1118.1080334618	1394	Find Lucky Integer in an Array	找出数组中的幸运数	find-lucky-integer-in-an-array	weekly-contest-182	Q1
1115.8258444602	3028	Ant on the Boundary	边界上的蚂蚁	ant-on-the-boundary	weekly-contest-383	Q1
1104.7359028407	1480	Running Sum of 1d Array	一维数组的动态和	running-sum-of-1d-array	weekly-contest-193	Q1
1084.1319467318	1108	Defanging an IP Address	IP 地址无效化	defanging-an-ip-address	weekly-contest-144	Q1

"""

# Split the data into lines and then into parts
lines = data.strip().split("\n")
headers = lines[0].split("\t")  # Get the headers from the first line
problem_data = []

# Process each line except the first (which are headers)
for line in lines[1:]:
    parts = line.split("\t")
    problem = {headers[i]: parts[i] for i in range(len(parts))}
    problem_data.append(problem)

# Convert to JSON
json_data = json.dumps(problem_data, indent=4)

with open("ratings.json", "w") as file:
    file.write(json_data)
