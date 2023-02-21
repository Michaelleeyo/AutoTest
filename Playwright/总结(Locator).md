Playwright
主要根据官方文档学习https://playwright.dev/docs/intro

Page.getByRole()定位显示或隐式元素，推荐用于交互性元素，如button,a,input
例：
Await page.frameLocator('#my-frame')getByRole('button',{ name:'Sign in'}).click());
Await expect(page.getByRole('heading',{name: 'Sign up '})).toBeVisible();
Page.getByText() 推荐用于非交互性的元素，如div,span,p
例：
Await expect(page.getByText('Welcom,John',{exact:true})).toBeVisible();
await expect(page.getByText(/welcome, [A-Za-z]+$/i)).toBeVisible();
Page.getByLabel()
例：
Await page.getByLabel('Password').fill('secret');
Page.getByPlaceholder()定位带placeholder的输入框
例:
Await page.getByPlaceholder('name@example.com').fill('playwright@microsoft.com');
Page.getByTitle()
Page.getByAltText() 通常用来根据alternative来定位图片元素
Page.getByTestId()根据元素的 data-tested 属性定位元素


Locate by CSS or Xpath
Css= or xpath= 
Await page.locator('css=button').click();
Await page.locator('//*[@id='tsf']/div[2]/div[1]/input').click():


Locate in Shadow DOM
Await expect(page.locator('x-details')).toContainText('Details');


Filtering Locators
Filter by text
Await page.getByRole('listitem').filter({hasText:'Product 2'}).getByRole('button',{name:'Add to cart'}).click();
Filter by another locator
Await page.getByRole('listitem').filter({has:page.getByRole('heading',{name:'Product 2'})}).getByRoel('button',{name: 'Add to cart'}).click();
Await expect(page.getByRole('listitem').filter({has: age.getByText('Product 2')}).toHaveCount(1));


Chaining Locators
Const product = page.getByRole('listitem'.filter({hasTest :'Product 2'}));
await product.getByRole('button',{name:'Add to cart'}).click();
Await expect(product).toHaveCount(1);


Lists
Count items in a list
Await expect(page.getByRole('listitem')).toHaveCount(3);
Assert all text in a list
Await expect(page.getByRole('listitem').toHaveText(['apple','banana','orange'])); 
Get by nth item
Const banana = await page.getByRole('listitem').nth(1);
