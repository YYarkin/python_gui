def test_del_group(app):
    old_list = app.groups.get_group_list()
    if len(old_list) <= 1:
        app.groups.add_new_group("my group")
        old_list.append("my group")

    del_group = app.groups.del_rand_group(old_list)
    new_list = app.groups.get_group_list()
    old_list.remove(del_group)
    assert sorted(old_list) == sorted(new_list)
