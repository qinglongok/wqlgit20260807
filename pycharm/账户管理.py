def make_bank(initial:float):
    bank=initial
    def deposit(amount: float):
        nonlocal bank
        bank+=amount
        return bank
    def withdraw(amount: float):
        nonlocal bank
        if amount > bank:
           return "Insufficient balance"
        else:
           bank-=amount
           return bank

    def operate():
        nonlocal bank
        while True:
            print(f"\n{'='*40}")
            print(f"当前余额：{bank:.2f} 元")
            print(f"{'='*40}\n")
            choice = input("请选择操作 (0-退出/ 1-存款 / 2-取款)：\n")
            if choice == "0":
                print(f"\n{'*' * 40}")
                print(f"{f"\n感谢使用！最终余额：{bank} 元":^40}")
                print(f"{'*' * 40}")
                break
            elif choice=="1":
                print(f"{'*' * 40}")
                print(f'{"欢迎存款！":^40}')
                print(f"{'*' * 40}")
                arg= round(float(input('请输入存款金额：')),2)
                if arg<=0:
                    print("❌ 金额必须大于 0！")
                    continue
                ye= deposit(arg)
                print(f"\n{'=' * 40}")
                print(f'存款成功，当前余额：{ye}')
                print(f"{'=' * 40}\n")
            elif choice=="2":
                print(f"{'*' * 40}")
                print(f'{"欢迎取款！":^40}')
                print(f"{'*' * 40}")
                arg = round(float(input('请输入取款金额：')), 2)
                if arg <= 0:
                    print("❌ 金额必须大于 0！")
                    continue
                ye = withdraw(arg)
                if isinstance(ye,str):
                    print(f"\n❌ 取款失败：{ye}")
                else:
                    print(f"\n{'=' * 40}")
                    print(f'取款成功，当前余额：{ye}')
                    print(f"{'=' * 40}\n")
            else:
                print("❌未知操作，请重新输入！")
    return deposit,withdraw,operate
deposit,withdraw,operate=make_bank(0)   #闭包的概念：内层函数共同引用外层函数的值
operate()