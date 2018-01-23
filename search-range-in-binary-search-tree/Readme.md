# search-range-in-binary-search-tree 二叉查找树中搜索区间
## 描述
给定两个值 k1 和 k2（k1 < k2）和一个二叉查找树的根节点。找到树中所有值在 k1 到 k2 范围内的节点。即打印所有x (k1 <= x <= k2) 其中 x 是二叉查找树的中的节点值。返回所有升序的节点值。
## 样例 
如果有 k1 = 10 和 k2 = 22, 你的程序应该返回 [12, 20, 22].

    20
   /  \
  8   22
 / \
4   12

题目链接：http://www.lintcode.com/zh-cn/problem/search-range-in-binary-search-tree/