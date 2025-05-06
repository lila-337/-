
# DeepSeek WebChat on Vercel

## 使用方法

### 1. 本地开发
- 安装依赖：
```
npm install
```
- 启动开发环境（需安装 vercel CLI）：
```
vercel dev
```

### 2. 部署到 Vercel
1. 登录 [https://vercel.com](https://vercel.com) 并导入本项目
2. 在“Project Settings → Environment Variables”中添加：
   - `DEEPSEEK_API_KEY`：你的 DeepSeek API 密钥
3. 部署完成后，即可使用网页进行聊天！

## 注意事项
- `chat.js` 是 API 函数，所有前端请求会被安全转发
- 前端通过 `/chat` 调用，而非直接访问 DeepSeek API
