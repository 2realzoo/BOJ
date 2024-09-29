import sys

input = sys.stdin.readline

N = int(input())
paper = []
white_paper = 0
blue_paper = 0

for _ in range(N):
    line = list(map(int, input().rstrip().split()))
    paper.append(line)

def cut_paper(paper): 
    global blue_paper
    global white_paper

    paper1 = [line[0:len(paper)//2] for line in paper[0:len(paper)//2]]
    paper2 = [line[len(paper)//2:] for line in paper[0:len(paper)//2]]
    paper3 = [line[0:len(paper)//2] for line in paper[len(paper)//2:]]
    paper4 = [line[len(paper)//2:] for line in paper[len(paper)//2:]]
    
    color1 = set(sum(paper1, []))
    color2 = set(sum(paper2, []))
    color3 = set(sum(paper3, []))
    color4 = set(sum(paper4, []))
    
    if not len(color1)==1:
        cut_paper(paper1)
    else:
        if 1 in color1:
            blue_paper += 1
        else:
            white_paper += 1
            
    if not len(color2)==1:
        cut_paper(paper2)
    else:
        if 1 in color2:
            blue_paper += 1
        else:
            white_paper += 1
            
    if not len(color3)==1:
        cut_paper(paper3) 
    else:
        if 1 in color3:
            blue_paper += 1
        else:
            white_paper += 1
                      
    if not len(color4)==1:
        cut_paper(paper4)
    else:
        if 1 in color4:
            blue_paper += 1
        else:
            white_paper += 1

if len(set(sum(paper, [])))==1:
        if 1 in set(sum(paper, [])):
            blue_paper += 1
        else:
            white_paper += 1
else:
    cut_paper(paper)     
            
print(f'{white_paper}\n{blue_paper}')

