#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # Hər bir element üçün yoxla: əgər axtarılan (search) elementdirsə,
    # onu yeni (replace) ilə əvəz et, deyilsə olduğu kimi saxla.
    return [replace if x == search else x for x in my_list]
