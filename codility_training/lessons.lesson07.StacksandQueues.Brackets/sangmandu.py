# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    pass
    st = []
    for i in S:
        if(len(st) == 0):
            if(i == ")" or i == "]" or i == "}"):
                return 0
            st.append(i)
        else:
            if(i == ")"):
                if(st.pop() != "("):
                    return 0
            elif(i == "}"):
                if(st.pop() != "{"):
                    return 0
            elif(i == "]"):
                if(st.pop() != "["):
                    return 0
            else:
                st.append(i)
    return 1 if len(st) == 0 else 0