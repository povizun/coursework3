from utils import functions


def test_get_list_of_ops():
    assert functions.get_list_of_ops("tests/test1.json") == [{"test1": 1, "test2": 2}, {"test3": 3}, {"test4": 4}]
    assert functions.get_list_of_ops("tests/test2.json") == [{'date': '2019-08-26T10:50:58.294041',
                                                        'operationAmount': {'amount': '31957.58',
                                                                            'currency': {'name': 'руб.'}}},
                                                       {'date': '2019-07-03T18:35:29.512364'},
                                                       {'date': '2018-06-30T02:08:58.425572'},
                                                       {'date': '2018-03-23T10:45:06.972075'},
                                                       {'date': '2019-04-04T23:20:05.206878'},
                                                       {'date': '2019-03-23T01:09:46.296404'}]
    assert functions.get_list_of_ops("tests/test3.json") == "Файл не найден"


def test_get_list_of_last_ops():

    assert (functions.get_list_of_last_ops([{'date': '2019-08-26T10:50:58.294041',
                                             'operationAmount': {'amount': '31957.58',
                                                                 'currency': {'name': 'руб.'}}},
                                            {'date': '2019-07-03T18:35:29.512364'},
                                            {'date': '2018-06-30T02:08:58.425572'},
                                            {'date': '2018-03-23T10:45:06.972075'},
                                            {'date': '2019-04-04T23:20:05.206878'},
                                            {'date': '2019-03-23T01:09:46.296404'}, {}], 3) ==
                                            [{'date': '2019-08-26T10:50:58.294041',
                                              'operationAmount': {'amount': '31957.58',
                                                                  'currency': {'name': 'руб.'}}},
                                             {'date': '2019-07-03T18:35:29.512364'},
                                             {'date': '2019-04-04T23:20:05.206878'}])
    assert (functions.get_list_of_last_ops([{"date": "2019-07-03T18:35:29.512364"},
                                            {"date": "2018-06-30T02:08:58.425572"}], 3) ==
                                           [{"date": "2019-07-03T18:35:29.512364"},
                                            {"date": "2018-06-30T02:08:58.425572"}])
