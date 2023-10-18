def get_formal_name(fruit):
    """
    Get the scientific name for the supplied `fruit` common name.

    :param fruit: str, common name for a fruit
    :return formal_name: str, the formal name for the supplied fruit
    """
    fruit_dict = {
        'apple': 'Malus domestica',
        'banana': 'Musa acuminata',
        'orange': 'Citrus × sinensis',
        'strawberry': 'Fragaria × ananassa',
        'grape': 'Vitis vinifera',
        'pineapple': 'Ananas comosus',
        'mango': 'Mangifera indica',
        'blueberry': 'Vaccinium corymbosum',
        'peach': 'Prunus persica',
        'watermelon': 'Citrullus lanatus',
        'cherry': 'Prunus avium',
        'pear': 'Pyrus',
        'plum': 'Prunus domestica',
        'raspberry': 'Rubus idaeus',
        'kiwi': 'Actinidia deliciosa',
        'lemon': 'Citrus limon',
        'avocado': 'Persea americana',
        'pomegranate': 'Punica granatum',
        'cranberry': 'Vaccinium macrocarpon',
        'grapefruit': 'Citrus × paradisi'
    }

    try:
        formal_name = fruit_dict[fruit]
    except KeyError:
       print("This Key does not exist in this dict")
    except TypeError:
        print("This doesn't belong to dict")
#    return formal_name