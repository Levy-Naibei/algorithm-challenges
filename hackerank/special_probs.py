"""
Lisa just got a new math workbook. A workbook contains exercise problems,
grouped into chapters. Lisa believes a problem to be special if its index (within a chapter) 
is the same as the page number where it's located. The format of Lisa's book is as follows:
There are  chapters in Lisa's workbook, numbered from  to .
The  chapter has  problems, numbered from  to .
Each page can hold up to  problems. Only a chapter's last page of exercises may contain fewer than  problems.
Each new chapter starts on a new page, so a page will never contain problems from more than one chapter.
The page number indexing starts at .
Given the details for Lisa's workbook, can you count its number of special problems?

Example
arr = [4, 2]
k = 3

k is the max number of problems per page
arr[i] is the number of problems per chapter
"""

def workbook(k, arr):
    page_number = 1
    special_problems = 0
    for problems in arr:
        for i in range(1, problems+1):
            if page_number == i:
                special_problems += 1
            if i % k == 0 or i == problems:
                # If i is equal to problems, it means we have reached the end of the chapter.
                # If i is divisible evenly by k, it means we have reached the end of a page
                # because we are allocating k problems per page.
                page_number += 1
    return special_problems

print(workbook(3, [4, 2, 6, 1, 10]))
