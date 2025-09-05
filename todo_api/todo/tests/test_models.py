import pytest

@pytest.mark.django_db
def test_item_toggle_done(list_factory, item_factory):
    todo_list = list_factory()
    item = item_factory(list=todo_list)
    
    # item initially unchecked
    assert item.done is False
    
    # toggle False to True
    item.toggle_done()
    assert item.done is True
    
    # toggle True to False
    item.toggle_done()
    assert item.done is False

