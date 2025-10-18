import random

def number_game():
    start,end = (input("答えの幅を入力してください。(数字で入力してください)例)1,50:")).split(',')
    start = int(start)
    end = int(end)
    if start > end or start == end or start == "" or end == "":
        print("もう一度入力してね")
        number_game()
    answer = random.randint(start,end)
    limit = int(input("チャレンジ回数を入力してね。おすすめ:10回:"))
    count = 0
    while True:
        count += 1
        guess = int(input("数字を入力してください(残り回数" + str(limit) + "):"))
        limit -= 1
        if limit == 0 and answer != guess:
            print("ゲームオーバー！正解は、",answer,"でした")
            break
        elif guess > answer:
            print("もっと小さい！")
        elif guess < answer:
            print("もっと大きい！")
        else:
            print("正解！",count,"回目でクリアしたよ！")
            break

            
while True:
    again =input("チャレンジしますか？yes/no:")
    if again.lower() == "no":
        print("またやってね！")
        break
    elif again.lower() != "yes" and again.lower() != "no":
        print("yesまたはnoで入力してください")
    else:
        number_game()
        

