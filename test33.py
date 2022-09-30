if __name__ == '__main__':
    home_count, wifi_count = map(int, input().split(" "))

    home_index = []
    for i in range(home_count):
        index = int(input())
        home_index.append(index)

    home_index.sort()
    
    
    check = False
    average = ((home_index[home_count - 1] - home_index[0]) // wifi_count)
    
    if wifi_count == 2:
        average = home_index[home_count - 1] - home_index[0]
        
    else:
        wifi_count -= 1
        last_position = home_index[0]

        while wifi_count > 0:
            for i in home_index:
                if last_position - i >= average:
                    last_position = i
                    wifi_count-=1

                if wifi_count == 0:
                    break
            average -=1

        print(average)