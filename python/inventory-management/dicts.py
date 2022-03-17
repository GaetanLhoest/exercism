def create_inventory(items):
    """

    :param items: list - list of items to create an inventory from.
    :return:  dict - the inventory dictionary.
    """
    inventory_dict = {}
    for item in items:
        inventory_dict[item] = inventory_dict.get(item, 0) + 1
    return inventory_dict


def add_items(inventory, items):
    """

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return:  dict - the inventory dictionary update with the new items.
    """

    for item in items:
        inventory[item] = inventory.get(item, 0) + 1
    return inventory


def decrement_items(inventory, items):
    """

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return:  dict - updated inventory dictionary with items decremented.
    """

    for item in items:
        inventory[item] = max(inventory.get(item, 0) - 1, 0)
    return inventory


def remove_item(inventory, item):
    """
    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return:  dict - updated inventory dictionary with item removed.
    """
    try:
        inventory.pop(item)
    except:
        pass
    return inventory


def list_inventory(inventory):
    """

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """
    return [(key, inventory[key]) for key in inventory if inventory[key] > 0]
