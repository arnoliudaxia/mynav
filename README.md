# Hugo-Webstack网址导航网站构建模板

完整的hugo目录结构，可以直接拷贝使用，不需要本地生成。结合自动构建，可在线编辑，自动发布。

详细内容请看主题 [hugo-webstack](https://github.com/oulh/hugo-webstack)

图标使用：[FontAwesome-v6-free ](https://origin.fontawesome.com/search)


## 使用方法

自动构建平台推荐，`Github Pages` 、[vercel](https://vercel.com/)（要用自己的域名）、[netlify](https://www.netlify.com/) 、[zeabur](https://zeabur.com?referralCode=o1289)（国内平台，提供域名） 。

   
   可自定义编辑的内容：
   
   - 网站配置：/hugo.toml

   - 主页面：/data/webstack.yml

   - 子页面：/content/xxx.md

   - “关于”页面：/content/about.md
   
   - 网站logo：/static/images/logo.png
   
   - 导航网址默认logo：/static/images/favicon.png
   
   - 导航网址logo：/static/images/logos/（可自定义路径）
   
   - 导航网址二维码：/static/images/qrcodes/（可自定义路径）

   - 图标等静态文件：/static/images
   
   查看构建状态：Actions - All workflows

   如何希望提交后不触发构建，只需在 commit 信息中包含关键词：`[skip ci]`或`[no ci]`，包括[]符号。

## 配置

留空或去掉"logo" 配置项即自动在线加载logo图标。api提供者：一为API