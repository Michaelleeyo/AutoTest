Playwright 和Selenium的主要区别
1.playwright支持同步和异步两种使用方法
2.不需要为每个浏览器下载webdriver
3.相比selenium多了一层context抽象
4.支持无头浏览器，且较为推荐（headless默认值为True）
5.可以使用传统定位方式（CSS，XPATH等），也有自定义的新的定位方式（如文字定位）
6.没有使用selenium的先定位元素，再进行操作的方式，而是在操作方法中传入了元素定位，定位和操作同时进行（其实也playwright也提供了单独的定位方法，作为可选）
7.很多方法使用了with的上下文语法
