#coding=utf-8
'''
Created on 2013-12-15

@author: Tom Kliyes
'''
from django.core.paginator import Paginator, InvalidPage


AFTER_RANGE_NUM = 6
BEFORE_RANGE_NUM = 6
DEFAULT_PAGE_SIZE = 1


def set_paging(request, paging_key, data_list, page_size=DEFAULT_PAGE_SIZE):
    request.session[paging_key] = Paging(data_list, page_size)
    return request.session.get(paging_key)


def get_paging(request, paging_key):
    return request.session.get(paging_key)


def validate_page_no(page_no):
    try:
        page = int(page_no)
        return 1 if page < 1 else page
    except ValueError:
        return 1


class Paging(object):
    """
    分页对象
    """
    paginator = None

    def __init__(self, object_list, page_size):
        self.paginator = Paginator(object_list, page_size)

    def current_page_data(self, page_no):
        page_no = validate_page_no(page_no)
        try:
            return self.paginator.page(page_no)
        except InvalidPage:
            return self.paginator.page(self.paginator.num_pages)

    def page_range(self, page_no):
        page_no = validate_page_no(page_no)
        if page_no >= AFTER_RANGE_NUM:
            return self.paginator.page_range[page_no - AFTER_RANGE_NUM:
                                             page_no + BEFORE_RANGE_NUM]
        return self.paginator.page_range[0:page_no + BEFORE_RANGE_NUM]

    def result(self, page_no, page_items_key="page_items", page_range_key="page_range"):
        return {page_items_key: self.current_page_data(page_no),
                page_range_key: self.page_range(page_no)}
