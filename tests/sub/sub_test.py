from poetrybase.sub import sub


def test_message():
    assert sub.message("test") == "Hello test!!!"
