class is_palindrome:
    num = int(input())
    def palindrome_chk(num_):
        num_str = str(num_)
        new_num = ""
        for i in range(len(num_str)-1,0-1,-1):
            new_num += f"{num_str[i]}"
        if new_num == num_str: 
            print(f"num_str: {num_str}, new_num{new_num}")
    palindrome_chk(num) 
    