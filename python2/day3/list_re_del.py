#!/usr/bin/env python3
def list_del_re(list):
    # for i in list[:-2]:
    #     indi=list.index(i)
    #     for j in list[indi+1:]:
    #         indj=list.index(j)
    #         if j==i:
    #             list.pop(indj)
    # return list
    list2=[]
    for i in list:
        if i not in list2:
            list2.append(i)
        else:
            continue
    return list2
if __name__ == '__main__':

    li=list('goooooggle')
    li=list_del_re(li)
    print(li)



