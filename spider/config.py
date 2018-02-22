number='*******'
password='*********'
select='cert_no'
agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
loginUrl='http://opac.jit.edu.cn/reader/redr_verify.php'
targetUrl='http://opac.jit.edu.cn/reader/book_hist.php?page='
headers={
    'Host':'opac.jit.edu.cn',
    'Referer':'http://opac.jit.edu.cn/opac/search.php',
    'User-Agent':agent
}
postData = {
    'number':number,
    'passwd':password,
    'select':select,
    'returnUrl':''
}
