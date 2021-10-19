#讀取檔案
def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
    return lines

#格式轉換
def convert(lines):
    stan_world_count = 0
    stan_sticker_conut = 0
    stan_image_count = 0
    Jacob_world_count = 0
    Jacob_sticker_conut = 0
    Jacob_image_count = 0
    for line in lines:
        s = line.split(' ')
        time = s[0]
        name = s[1]
        if name == 'Stan':
            if s[2] == '貼圖':
                stan_sticker_conut += 1
            elif s[2] == '圖片':
                stan_image_count += 1
            else:
                for msg in s[2:]:
                    stan_world_count += len(msg) 
        
        elif name == 'Jacob':
            if s[2] == '貼圖':
                Jacob_sticker_conut += 1
            elif s[2] == '圖片':
                Jacob_image_count += 1
            else:
                for msg in s[2:]:
                    Jacob_world_count += len(msg)
    print('Stan說了', stan_world_count, '個文字')
    print('Stan傳了', stan_sticker_conut, '個貼圖')
    print('Stan丟了', stan_image_count, '次圖片')
    print('Jacob說了', Jacob_world_count, '傳了', Jacob_sticker_conut, '個貼圖，丟了',Jacob_image_count, '次圖片')

#    return new


#寫入output檔
def write_file(filename, lines):
     with open(filename, 'w', encoding='utf-8-sig') as f:
        for line in lines:
            f.write(line + '\n')
#程式進入點
def main():
    lines = read_file('line.txt')
    lines = convert(lines)
#    write_file('output.txt', lines)

main()