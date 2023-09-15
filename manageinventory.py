def main():
    T = int(input())

    for _ in range(T):
        N = int(input())
        inventory = {}
        for _ in range(N):
            item, qty = input().split()
            inventory[item] = int(qty)
        M = int(input())
        for _ in range(M):
            operation, item_name, quantity = input().split()
            quantity = int(quantity)
            if operation == "ADD":
                msg = "UPDATED Item" if item_name in inventory else "ADDED Item"
                inventory[item_name] = inventory.get(item_name, 0) + quantity
                print(f"{msg} {item_name}")
            elif operation == "DELETE":
                if item_name not in inventory:
                    print(f"Item {item_name} does not exist")
                elif inventory.get(item_name, 0) < quantity:
                    print(f"Item {item_name} could not be DELETED")
                else:
                    inventory[item_name] -= quantity
                    print(f"DELETED Item {item_name}")
                    if inventory[item_name] <= 0: 
                        del inventory[item_name]
        print(f"Total Items in Inventory: {sum(inventory.values())}")
main()