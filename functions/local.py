def update_order():
    chai_type = "Elaichi"
    def kitchen():
        nonlocal chai_type
        chai_type = "Kesar"
    kitchen()

    print("After kitchen update what is the value of chai type :", chai_type)

    update_order()