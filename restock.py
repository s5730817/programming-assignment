def restock_inventory(available_items, inventory_records, current_day):
    '''
***********COMPLETE THIS FUNCTION***********
This function is responsible for updating the stock/restock for a given day.
---------------
Function Input:
---------------
available_items: (integer) Available Tshirts from the previous day.
inventory_records: (List) A list of inventory records until the previous day. Each row contains (day, sales, restocked items, available items)
current_day: (integer) Day number which you want to add as the current day. 

----------------
Function Output:
----------------
available_items:(integer) This function returns this integer which updates the available items at the current day.


The function will also update the inventory_records (For restocking) for a  given current day. It will also return "available_items".
    '''

    if current_day == 0:
        inventory_records.append([0, 0, 2000, available_items])
        return available_items
    
    if current_day % 7 != 0:
        return available_items

    restocked_items = 2000 - available_items
    available_items += restocked_items
    todays_record = [current_day, 0, restocked_items, available_items]
    inventory_records.append(todays_record)

    return available_items