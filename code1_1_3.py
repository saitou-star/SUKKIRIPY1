height = int(input("身長を入力 >>")) / 100
weight = float(input("体重を入力 >>"))

BMI = weight / height / height
print(f"あなたのBMIは{BMI}です。")
print("あなたのBMIは{}です。".format(BMI))