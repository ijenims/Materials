# coding: utf-8
# Subset Sum Problem // Algorythm & Data Structure

def func(i, w, a):
    ''' i, w ; int
        a : list '''
    print('Call func({}), w = {}, a = {}'.format(i, w, a))
    # base case
    if i == 0:
        if w == 0:
            return True
        else:
            return False
        
    # not choose a[i-1]
    if func(i - 1, w, a):
        # print()
        return True
    
    # choose a[i-1]
    if func(i - 1, w - a[i - 1], a):
        print(a[i - 1])
        return True
    
    # both choice are false
    return False


def main():
    ''' initial '''
    ''''''
    n, w= 4, 14
    a = [3, 2, 6, 5]
    '''
    n, w = 6, 27
    a = [3, 7, 8, 12, 13, 18]
    '''
    
    ''' solve recursive '''
    if func(n, w, a):
        print('Yes')
    else:
        print('No')
        
        
main()
        