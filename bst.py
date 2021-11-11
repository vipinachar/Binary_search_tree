class Node:
    def __init__(self,data):
        self.data = data 
        self.left = None 
        self.right = None 
        
        

def create(val):
    global root 
    print('val',val)
    n = Node(val)
    if root == None:
        root=n 
        return
    else:
        # print(root.data)
        tmp = root
        prev = None
        while tmp!=None:
            print(f'val {val} tmp.data {tmp.data}')
            prev = tmp 
            if int(val) > int(tmp.data):
                print(f'{val}>{tmp.data}')
                print('right')
                tmp = tmp.right 
                if tmp==None:
                    prev.right = n
            else:
                print(f'{val}<{tmp.data}')
                print('left')
                tmp = tmp.left 
                if tmp==None:
                    prev.left = n
        
        
   
def disp(tmp):
    print(tmp.data)
    if tmp.left!=None:
        print(f'left of {tmp.data}',end=' ')
        disp(tmp.left) 
    if tmp.right!=None:
        print(f'right of {tmp.data}',end=' ')
        disp(tmp.right)
    
    
    
def search(val):
    global root 
    if root==None:
        print('no elements')
    else:
        tmp = root
        while tmp!=None:
            if val == int(tmp.data):
                return
            print(tmp.data)
            if int(val) > int(tmp.data):
                tmp = tmp.right 
            else:
                tmp= tmp. left                
    
def inn(root):
    if root==None:
        return
    inn(root.left)
    print(root.data,end=' ')
    inn(root.right)
    return    

if __name__ == '__main__':
    root=None
    while True:
        c=int(input("1)insert 2)search 3)inorder"))
        if c==1:
            create(input('enter elemt: '))
            print('#######disp#########')
            disp(root)
        elif c==2:
            search(input("enter element: "))
        elif c==3:
            inn(root)
            
            