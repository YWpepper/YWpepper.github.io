---
layout: post
title: "how_to_changeEasyDataset"
date: 2026-04-07
author: pepper
tags: [server]
comments: true
toc: true
pinned: false
---

这篇博客介绍了Easy Dataset项目的架构，并指导你如何添加登录验证页面。
<!-- more -->



## 📋 项目架构分析

Easy Dataset是一个基于Next.js的全栈应用，使用：
- **前端**: Next.js 14 + React 18 + Material-UI
- **后端**: Next.js API Routes + Prisma ORM
- **数据库**: SQLite (Prisma)
- **状态管理**: Jotai
- **主题**: next-themes

当前项目**没有身份验证系统**，所有页面都是公开访问的。

## 🎯 登录验证实现方案

### 1. 拉取仓库
```bash
git clone https://github.com/ConardLi/easy-dataset.git
cd easy-dataset
npm install
```

### 2. 需要修改的核心文件

#### 后端部分（API Routes）:
1. **创建认证API**：
   - `app/api/auth/login/route.js` - 登录验证
   - `app/api/auth/logout/route.js` - 登出
   - `app/api/auth/me/route.js` - 获取当前用户信息
   - `app/api/auth/register/route.js` - 用户注册（可选）

2. **数据库模型**：
   - `prisma/schema.prisma` - 添加User模型
   - `lib/db/users.js` - 用户数据库操作

3. **中间件**：
   - `middleware.js` - 路由保护中间件

#### 前端部分：
1. **登录页面**：
   - `app/login/page.js` - 登录页面组件

2. **上下文和状态**：
   - `contexts/AuthContext.js` - 认证状态管理
   - `hooks/useAuth.js` - 认证相关hook

3. **现有组件修改**：
   - `app/layout.js` - 添加认证provider
   - `app/page.js` - 添加登录检查
   - `components/Navbar/index.js` - 添加登录/登出按钮

### 3. 详细实现步骤

#### 步骤1: 修改数据库模型
在`prisma/schema.prisma`中添加用户模型：
```prisma
model User {
  id        String   @id @default(cuid())
  email     String   @unique
  password  String
  name      String?
  createdAt DateTime @default(now())
  updatedAt DateTime @updatedAt
}
```

#### 步骤2: 创建认证API
在`app/api/auth/login/route.js`：
```javascript
import bcrypt from 'bcryptjs';
import jwt from 'jsonwebtoken';
import { getUserByEmail } from '@/lib/db/users';

export async function POST(request) {
  try {
    const { email, password } = await request.json();
    
    // 验证用户
    const user = await getUserByEmail(email);
    if (!user || !bcrypt.compareSync(password, user.password)) {
      return Response.json({ error: 'Invalid credentials' }, { status: 401 });
    }
    
    // 生成JWT token
    const token = jwt.sign(
      { userId: user.id, email: user.email },
      process.env.JWT_SECRET,
      { expiresIn: '7d' }
    );
    
    return Response.json({ token, user: { id: user.id, email: user.email, name: user.name } });
  } catch (error) {
    return Response.json({ error: 'Login failed' }, { status: 500 });
  }
}
```

#### 步骤3: 创建登录页面
在`app/login/page.js`：
```javascript
'use client';
import { useState } from 'react';
import { useRouter } from 'next/navigation';
import { useAuth } from '@/hooks/useAuth';
import { Container, TextField, Button, Typography, Box, Paper } from '@mui/material';

export default function LoginPage() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const { login } = useAuth();
  const router = useRouter();

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await login(email, password);
      router.push('/');
    } catch (error) {
      alert('登录失败');
    }
  };

  return (
    <Container maxWidth="sm">
      <Box sx={{ mt: 8, display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
        <Paper elevation={3} sx={{ p: 4, width: '100%' }}>
          <Typography component="h1" variant="h5" align="center">
            登录
          </Typography>
          <Box component="form" onSubmit={handleSubmit} sx={{ mt: 3 }}>
            <TextField
              margin="normal"
              required
              fullWidth
              id="email"
              label="邮箱"
              name="email"
              autoComplete="email"
              autoFocus
              value={email}
              onChange={(e) => setEmail(e.target.value)}
            />
            <TextField
              margin="normal"
              required
              fullWidth
              name="password"
              label="密码"
              type="password"
              id="password"
              autoComplete="current-password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
            <Button
              type="submit"
              fullWidth
              variant="contained"
              sx={{ mt: 3, mb: 2 }}
            >
              登录
            </Button>
          </Box>
        </Paper>
      </Box>
    </Container>
  );
}
```

#### 步骤4: 创建认证上下文
在`contexts/AuthContext.js`：
```javascript
'use client';
import { createContext, useState, useContext, useEffect } from 'react';
import { useRouter } from 'next/navigation';

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const router = useRouter();

  useEffect(() => {
    // 检查本地存储的token
    const token = localStorage.getItem('token');
    if (token) {
      // 验证token有效性
      fetchUser(token);
    } else {
      setLoading(false);
    }
  }, []);

  const fetchUser = async (token) => {
    try {
      const response = await fetch('/api/auth/me', {
        headers: { 'Authorization': `Bearer ${token}` }
      });
      if (response.ok) {
        const userData = await response.json();
        setUser(userData);
      } else {
        localStorage.removeItem('token');
      }
    } catch (error) {
      localStorage.removeItem('token');
    } finally {
      setLoading(false);
    }
  };

  const login = async (email, password) => {
    const response = await fetch('/api/auth/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email, password })
    });

    if (response.ok) {
      const data = await response.json();
      localStorage.setItem('token', data.token);
      setUser(data.user);
      return data;
    } else {
      throw new Error('Login failed');
    }
  };

  const logout = () => {
    localStorage.removeItem('token');
    setUser(null);
    router.push('/login');
  };

  return (
    <AuthContext.Provider value={{ user, login, logout, loading }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within AuthProvider');
  }
  return context;
};
```

#### 步骤5: 修改主布局
更新`app/layout.js`：
```javascript
import { AuthProvider } from '@/contexts/AuthContext';

export default function RootLayout({ children }) {
  return (
    <html lang="zh" suppressHydrationWarning>
      <body suppressHydrationWarning>
        <AuthProvider>
          <Provider>
            <ThemeRegistry>
              <I18nProvider>
                {children}
                <Toaster richColors position="top-right" duration={1000} />
              </I18nProvider>
            </ThemeRegistry>
          </Provider>
        </AuthProvider>
      </body>
    </html>
  );
}
```

#### 步骤6: 添加路由保护
创建`middleware.js`：
```javascript
import { NextResponse } from 'next/server';
import { jwtVerify } from 'jose';

export async function middleware(request) {
  const token = request.cookies.get('token')?.value;
  const isAuthPage = request.nextUrl.pathname.startsWith('/login');

  if (!token && !isAuthPage) {
    return NextResponse.redirect(new URL('/login', request.url));
  }

  if (token && isAuthPage) {
    return NextResponse.redirect(new URL('/', request.url));
  }

  return NextResponse.next();
}

export const config = {
  matcher: ['/((?!api|_next/static|_next/image|favicon.ico).*)'],
};
```

### 4. 本地构建和部署流程

#### 安装依赖
```bash
npm install bcryptjs jsonwebtoken jose
```

#### 环境变量配置
创建`.env.local`文件：
```
JWT_SECRET=your-secret-key-here
```

#### 数据库迁移
```bash
npm run db:push
```

#### 开发模式运行
```bash
npm run dev
# 访问 http://localhost:1717
```

#### 生产构建
```bash
npm run build
npm run start
# 访问 http://localhost:1717
```

#### Docker部署
```bash
# 构建镜像
docker build -t easy-dataset-with-auth .

# 运行容器
docker run -d \
  -p 1717:1717 \
  -v ./local-db:/app/local-db \
  -v ./prisma:/app/prisma \
  -e JWT_SECRET=your-secret-key-here \
  --name easy-dataset-auth \
  easy-dataset-with-auth
```

## 🔧 额外建议

1. **用户注册**: 可以添加注册页面和API
2. **密码重置**: 实现忘记密码功能
3. **用户管理**: 管理员可以管理用户
4. **权限控制**: 不同用户访问不同项目
5. **会话管理**: 实现refresh token机制
6. **安全加固**: 添加CSRF保护、输入验证等

这个方案提供了完整的身份验证系统，你可以根据具体需求进行调整和扩展。