import colorama

colorama.init()

def karmaTrend(data):
    max_value = max(count for _, count in data)
    increment = max_value / 25
    longest_label_length = max(len(label) for label, _ in data)
    
    for label, count in data:
        bar_chunks, remainder = divmod(int(count * 7 / increment), 7)
        bar = '█' * bar_chunks
        if remainder > 0:
            bar += chr(ord('█') + (8 - remainder))
        bar = bar or  '▏'
        print(f'{label.rjust(longest_label_length)} ▏ {count:#4d} {bar}')

def daily(data, goal):
    max_value = max(count for _, count in data)
    increment = max_value / 25
    longest_label_length = max(len(label) for label, _ in data)
    
    for label, count in data:
        bar_chunks, remainder = divmod(int(count * 7 / increment), 7)
        bar = '█' * bar_chunks
        if remainder > 0:
            bar += chr(ord('█') + (8 - remainder))
        bar = bar or  ' ▏'
        if count < goal:
            print(f'{label.rjust(longest_label_length)} ▏ {count:#3d} ', end="")
            print(colorama.Fore.RED + f'✔️ {bar}')
            print(colorama.Style.RESET_ALL, end="")
        else:
            print(f'{label.rjust(longest_label_length)} ▏ {count:#3d} ', end="")
            print(colorama.Fore.GREEN + f'✔️ {bar}')
            print(colorama.Style.RESET_ALL, end="")

def weekly(data, goal):
    max_value = max(count for _, count in data)
    increment = max_value / 25
    longest_label_length = max(len(label) for label, _ in data)
    
    for label, count in data:
        bar_chunks, remainder = divmod(int(count * 7 / increment), 7)
        bar = '█' * bar_chunks
        if remainder > 0:
            bar += chr(ord('█') + (8 - remainder))
        bar = bar or  '▏'
        if count < goal:
            print(f'{label.rjust(longest_label_length)} ▏ {count:#3d} ', end="")
            print(colorama.Fore.RED + f'✔️ {bar}')
            print(colorama.Style.RESET_ALL, end="")
        else:
            print(f'{label.rjust(longest_label_length)} ▏ {count:#3d} ', end="")
            print(colorama.Fore.GREEN + f'✔️ {bar}')
            print(colorama.Style.RESET_ALL, end="")
