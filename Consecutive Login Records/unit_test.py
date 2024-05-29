from main import main

def test():
    test_data = ['asdasd', 'asdasd', '2024-04-12 04:23:56', 'asdasd', 'asdasd', '2024-04-07 07:23:56', 'asdasd', 'asdasd', '2024-03-29 21:23:56', '2024-05-03 08:23:56', 'asdasd', 'asdasd', 'asdasd', '2024-04-22 21:23:56', '2024-04-21 23:23:56', '2024-04-09 12:23:56', '2024-04-14 14:23:56', '2024-04-17 15:23:56', '2024-04-30 22:23:56', 'asdasd', '2024-05-05 17:23:56', '2024-03-18 10:23:56', 'asdasd', '2024-05-10 01:23:56', 'asdasd', '2024-05-01 19:23:56', 'asdasd', 'asdasd', 'asdasd', 'asdasd', '2024-03-21 18:23:56', 'asdasd', 'asdasd', 'asdasd', '2024-04-18 13:23:56', '2024-04-13 06:23:56', '2024-04-13 18:23:56', '2024-04-28 18:23:56', 'asdasd', '2024-04-16 06:23:56', 'asdasd', 'asdasd', 'asdasd', 'asdasd', 'asdasd', 'asdasd', 'asdasd', 'asdasd']

    output = main(test_data)

    assert output == [
        ('2024-04-12', '2024-04-14', 4),
        ('2024-04-16', '2024-04-18', 3),
        ('2024-04-21', '2024-04-22', 2),
        ('2024-04-30', '2024-05-01', 2),
        ('2024-03-18', '2024-03-18', 1),
        ('2024-03-21', '2024-03-21', 1),
        ('2024-03-29', '2024-03-29', 1),
        ('2024-04-07', '2024-04-07', 1),
        ('2024-04-09', '2024-04-09', 1),
        ('2024-04-28', '2024-04-28', 1),
        ('2024-05-03', '2024-05-03', 1),
        ('2024-05-05', '2024-05-05', 1),
        ('2024-05-10', '2024-05-10', 1)]
    
    print("OK")
    
if __name__ == "__main__":
    test()