#
# [182] Duplicate Emails
#
# https://leetcode.com/problems/duplicate-emails/description/
#
# database
# Easy (44.53%)
# Total Accepted:    60.3K
# Total Submissions: 135.5K
# Testcase Example:  '{"headers": {"Person": ["Id", "Email"]}, "rows": {"Person": [[1, "a@b.com"], [2, "c@d.com"], [3, "a@b.com"]]}}'
#
# 
# Write a SQL query to find all duplicate emails in a table named Person.
# 
# 
# +----+---------+
# | Id | Email   |
# +----+---------+
# | 1  | a@b.com |
# | 2  | c@d.com |
# | 3  | a@b.com |
# +----+---------+
# 
# 
# For example, your query should return the following for the above table:
# 
# +---------+
# | Email   |
# +---------+
# | a@b.com |
# +---------+
# 
# 
# Note: All emails are in lowercase.
#
# Write your MySQL query statement below
select distinct p1.Email from Person p1 inner join Person p2 
where p1.Email = p2.Email and p1.id != p2.id

