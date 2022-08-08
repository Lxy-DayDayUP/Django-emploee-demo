from django.utils.safestring import mark_safe
import copy
class Pagenation(object):
    """
    用于分页的组件
    初始化需要传入固定参数request,query_set
    query_set是根据搜索条件过滤后的数据库表的集合，[obj,obj,obj,...]
    html函数用于产生html标签   用法：将返回值接收并传入html文件，直接在html文件中                {{ page_li_str }}
    currentpage_data函数   用于返回当前页要显示的数据，需要接收并传入html，然后在html文件中循环并打印
    """
    def __init__(self,request,query_set,page_param='page',page_size=10,page_area = 3):
        self.page_size = page_size  # 每页显示的数据条数，默认10条
        self.query_set = query_set
        self.page_param = page_param
        self.page_area = page_area  #页码前后显示多少页
        self.url = copy.deepcopy(request.GET)  #用于拼接url保留其中原本的search=部分
        self.url._mutable = True
        currentpage = request.GET.get(page_param, '1') # 当前页
        if currentpage.isdecimal():
            self.currentpage = int(currentpage)
        else:
            self.currentpage = 1
        self.start = (self.currentpage - 1) * self.page_size  # 当前页显示的起始数据
        self.end = self.start + self.page_size  # 当前页显示的最后一条数据

    def currentpage_data(self):
        return self.query_set[self.start:self.end]  #当前页要显示的数据
    def html(self):
        page_li = []
        data_count = self.query_set.count()  # 数据库表中总数据条数
        page_count, yushu = divmod(data_count, self.page_size)
        if yushu:
            page_count += 1  # 分页显示的总页数，有余数就加一
        start_page = self.currentpage - self.page_area  # 起始、结束页码
        end_page = self.currentpage + self.page_area
        if end_page >= page_count:
            end_page = page_count
        if self.currentpage <= self.page_area:  # 控制两头页码不超出范围
            start_page = 1
        elif self.currentpage >= page_count - self.page_area:
            end_page = page_count
        self.url.setlist(self.page_param,[1])
        page_li.append('<li><a href="?{}">首页 </a></li>'.format(self.url.urlencode()))
        for i in range(start_page, end_page + 1):  # 构造页码标签
            self.url.setlist(self.page_param, [i])
            if i == self.currentpage:
                li = '<li class="active"><a href="?{}">{} </a></li>'.format(self.url.urlencode(), i)
            else:
                li = '<li><a href="?{}">{} </a></li>'.format(self.url.urlencode(), i)
            page_li.append(li)
        self.url.setlist(self.page_param, [page_count])
        page_li.append('<li><a href="?{}">尾页 </a></li>'.format(self.url.urlencode()))
        page_li.append('<li style="float: right ;width: 300px"><form method="get"><div class="input-group "><input style="width: 200px" type="text" name="page"  class="form-control"placeholder="跳转"><button type="submit" class="btn btn-default">Go</button></div></form>')
        page_li_str = mark_safe(''.join(page_li))
        return page_li_str

