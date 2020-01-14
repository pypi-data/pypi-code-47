from alloy.algo import depth_first_search, breath_first_search

def main():
    # a fake graph
    def child_func(curr_tuple):
        child_list = []
        if curr_tuple[0] + 1 < 10:
            child_list.append((curr_tuple[0]+1,curr_tuple[1]))
        if curr_tuple[1] + 1 < 10:
            child_list.append((curr_tuple[0], curr_tuple[1]+1))
        if curr_tuple[0] + 1 < 10 and curr_tuple[1] + 1 < 10:
            child_list.append((curr_tuple[0]+1, curr_tuple[1]+1))
        return child_list
    
    print(depth_first_search((0,0),(5,3), child_func))
    print(breath_first_search((0,0),(5,3), child_func))


if __name__ == "__main__":
    main()