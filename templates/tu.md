# 使用教程
#### 先把链接放到这  
!["links.png"]("/static/links.png")  
#### 这是第一个版本，建议先不要搞那么多  
#### 然后放入你要执行的js脚本，必须是原生js脚本，或者你要爬的页面支持jquery也可以用$(....)  
#### 在这放入js脚本  
!["js.jpg"]("./image/js.jpg")  
#### 这是关于时间操作的  
!["js.jpg"]("/static/times.jpg")  
#### 因为我们的代码是  
```
browser.get(url)
time.sleep(start_sleep)  
```
这就意味着，每次重新请求一个url都会在页面加载完成之后等待几秒时间，这也是无奈之举，因为页面大多数数据都是动态绑定的，如页面使用vue，很多逻辑在页面加载完成后有几百毫秒的差值，我们的插件运行速度比几百毫秒快得多，并且结合当前服务器的性能之后，我们认为普通网页加载完成之后等待2秒再执行js比较好  
