def print_list(head):
    arr = []
    cur_head = head
    while cur_head:
        arr.append(cur_head.val)
        cur_head = cur_head.next
    return arr
