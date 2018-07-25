import cards_tools
while True:
    # 显示功能菜单
    cards_tools.show_menu()
    acttion_str = input("请选择希望执行的操作：")
    print ("您选择的操作是【%s】" %acttion_str)
    #1,2,3是针对名片的操作
    if acttion_str in ["1","2","3"]:
        #新增名片
        if acttion_str=="1":
            cards_tools.new_card()
        #显示全部
        elif acttion_str=="2":
            cards_tools.show_all()
        #查询名片
        elif acttion_str=="3":
            cards_tools.search_card()

    #0表示退出系统
    elif acttion_str in["0"]:
        print("欢迎再次使用【名片管理系统】")
        break
        #pass
    #其他内容内容输入错误，需要提示用户名
    else:
        print("您输入的不正确，请重新选择")


