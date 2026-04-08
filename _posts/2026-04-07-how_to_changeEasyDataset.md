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

当前项目**没有身份验证系统**，所有页面都是公开访问的,所以本博客将介绍如何添加一个简单的登录验证系统，保护敏感页面，并提供用户管理功能。

## 🎯 登录验证实现方案

### 1. 拉取仓库

```bash
git clone https://github.com/ConardLi/easy-dataset.git
cd easy-dataset
## 这个是本地构建的时候的命令行
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
import bcrypt from "bcryptjs";
import jwt from "jsonwebtoken";
import { getUserByEmail } from "@/lib/db/users";

export async function POST(request) {
  try {
    const { email, password } = await request.json();

    // 验证用户
    const user = await getUserByEmail(email);
    if (!user || !bcrypt.compareSync(password, user.password)) {
      return Response.json({ error: "Invalid credentials" }, { status: 401 });
    }

    // 生成JWT token
    const token = jwt.sign(
      { userId: user.id, email: user.email },
      process.env.JWT_SECRET,
      { expiresIn: "7d" },
    );

    return Response.json({
      token,
      user: { id: user.id, email: user.email, name: user.name },
    });
  } catch (error) {
    return Response.json({ error: "Login failed" }, { status: 500 });
  }
}
```

#### 步骤3: 创建登录页面

在`app/login/page.js`：

```javascript
"use client";
import { useState } from "react";
import { useRouter } from "next/navigation";
import { useAuth } from "@/hooks/useAuth";
import {
  Container,
  TextField,
  Button,
  Typography,
  Box,
  Paper,
} from "@mui/material";

export default function LoginPage() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const { login } = useAuth();
  const router = useRouter();

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await login(email, password);
      router.push("/");
    } catch (error) {
      alert("登录失败");
    }
  };

  return (
    <Container maxWidth="sm">
      <Box
        sx={{
          mt: 8,
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
        }}
      >
        <Paper elevation={3} sx={{ p: 4, width: "100%" }}>
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
"use client";
import { createContext, useState, useContext, useEffect } from "react";
import { useRouter } from "next/navigation";

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const router = useRouter();

  useEffect(() => {
    // 检查本地存储的token
    const token = localStorage.getItem("token");
    if (token) {
      // 验证token有效性
      fetchUser(token);
    } else {
      setLoading(false);
    }
  }, []);

  const fetchUser = async (token) => {
    try {
      const response = await fetch("/api/auth/me", {
        headers: { Authorization: `Bearer ${token}` },
      });
      if (response.ok) {
        const userData = await response.json();
        setUser(userData);
      } else {
        localStorage.removeItem("token");
      }
    } catch (error) {
      localStorage.removeItem("token");
    } finally {
      setLoading(false);
    }
  };

  const login = async (email, password) => {
    const response = await fetch("/api/auth/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email, password }),
    });

    if (response.ok) {
      const data = await response.json();
      localStorage.setItem("token", data.token);
      setUser(data.user);
      return data;
    } else {
      throw new Error("Login failed");
    }
  };

  const logout = () => {
    localStorage.removeItem("token");
    setUser(null);
    router.push("/login");
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
    throw new Error("useAuth must be used within AuthProvider");
  }
  return context;
};
```

#### 步骤5: 修改主布局

更新`app/layout.js`：

```javascript
import { AuthProvider } from "@/contexts/AuthContext";

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
import { NextResponse } from "next/server";
import { jwtVerify } from "jose";

export async function middleware(request) {
  const token = request.cookies.get("token")?.value;
  const isAuthPage = request.nextUrl.pathname.startsWith("/login");

  if (!token && !isAuthPage) {
    return NextResponse.redirect(new URL("/login", request.url));
  }

  if (token && isAuthPage) {
    return NextResponse.redirect(new URL("/", request.url));
  }

  return NextResponse.next();
}

export const config = {
  matcher: ["/((?!api|_next/static|_next/image|favicon.ico).*)"],
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

#### 数据库管理

```bash
# 由于本项目添加了一个登陆账号验证的功能，新创建了一张表来做管理员账户
# 1. 把你的数据库结构 → 同步到真实数据库
npm run db:push
# 2. 启动一个网页版数据库可视化管理工具
npm rum db:studio

```

#### 开发模式运行

```bash
npm run dev
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
docker build -t easy-dataset-v1 .
docker build -t easy-dataset-v2 .
```

##### 1. 镜像源.npmrc文件优化

```bash
# 下载慢，镜像源更改，配置.npmrc文件
registry=https://registry.npmjs.org  # 比https://registry.npmmirror.com要好用
strict-ssl=false
fetch-retry-mintimeout=20000
fetch-retry-maxtimeout=120000
fetch-timeout=300000
electron_mirror=https://npmmirror.com/mirrors/electron/
canvas_binary_host_mirror=https://npmmirror.com/mirrors/node-canvas-prebuilt/
prisma_engines_mirror=https://registry.npmmirror.com/-/binary/prisma
```

##### 2. Dockerfile优化

```bash
# 创建包含pnpm的基础镜像
# http://r.cnpmjs.org/
FROM node:20-alpine AS pnpm-base

# 1. 修改 Alpine 软件源为阿里云镜像 (加速 apk add)
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories

# 2. 设置 pnpm 镜像源并安装
RUN npm config set registry https://registry.npmjs.org && \
    npm install -g pnpm@9

# 构建阶段
FROM pnpm-base AS builder
WORKDIR /app

# 添加构建参数，用于识别目标平台
ARG TARGETPLATFORM

# 安装构建依赖 (此时已使用国内 apk 镜像)
RUN apk add --no-cache --virtual .build-deps \
    python3 \
    make \
    g++ \
    cairo-dev \
    pango-dev \
    jpeg-dev \
    giflib-dev \
    librsvg-dev \
    build-base \
    pixman-dev \
    pkgconfig


# 复制依赖文件
COPY package.json pnpm-lock.yaml .npmrc ./

# 核心优化：
# 1. 设置 Electron 镜像 (加速 electron 下载)
# 2. 设置 Canvas 镜像 (加速 canvas 下载，避免本地编译)
# 3. 设置 Prisma 镜像 (加速 prisma 引擎下载)
RUN pnpm config set registry https://registry.npmjs.org && \
    pnpm config set fetch-retries 5 && \
    pnpm config set fetch-retry-maxtimeout 600000 && \
    export ELECTRON_MIRROR="https://npmmirror.com/mirrors/electron/" && \
    export CANVAS_BINARY_HOST_MIRROR="https://npmmirror.com/mirrors/node-canvas-prebuilt/" && \
    export PRISMA_ENGINES_MIRROR="https://registry.npmmirror.com/-/binary/prisma" && \
    pnpm install --no-frozen-lockfile
# 复制源代码
COPY . .

# 根据目标平台设置Prisma二进制目标并构建应用
# 增加 PRISMA_ENGINES_MIRROR 确保 build 过程中的下载也走国内
RUN export PRISMA_ENGINES_MIRROR=https://registry.npmmirror.com/-/binary/prisma && \
    if [ "$TARGETPLATFORM" = "linux/arm64" ]; then \
    echo "Configuring for ARM64 platform"; \
    sed -i 's/binaryTargets = \[.*\]/binaryTargets = \["linux-musl-arm64-openssl-3.0.x"\]/' prisma/schema.prisma; \
    PRISMA_CLI_BINARY_TARGETS="linux-musl-arm64-openssl-3.0.x" pnpm build; \
    else \
    echo "Configuring for AMD64 platform (default)"; \
    sed -i 's/binaryTargets = \[.*\]/binaryTargets = \["linux-musl-openssl-3.0.x"\]/' prisma/schema.prisma; \
    PRISMA_CLI_BINARY_TARGETS="linux-musl-openssl-3.0.x" pnpm build; \
    fi

# 保留Prisma CLI用于数据库管理
# RUN pnpm prune --prod

# 运行阶段
FROM pnpm-base AS runner
WORKDIR /app

# 只安装运行时依赖 (同样受惠于第一步的 apk 加速)
RUN apk add --no-cache \
    cairo \
    pango \
    jpeg \
    giflib \
    librsvg \
    pixman

# 复制文件... (保持不变)
COPY package.json .env ./
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/.next ./.next
COPY --from=builder /app/public ./public
COPY --from=builder /app/electron ./electron
COPY --from=builder /app/prisma /app/prisma-template
COPY docker-entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

ENV NODE_ENV=production
EXPOSE 1717

ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]
CMD ["pnpm", "start"]

```

##### 3. 运行容器

```bash
# 运行容器
docker run -d \
  -p port:port \
  -v ./local-db:/app/local-db \
  -v ./prisma:/app/prisma \
  -e JWT_SECRET=your-secret-key-here \
  --name easy-dataset \
  easy-dataset

#还需要设置关机自启动
docker run -d \
  -p port:port \
  -v ./local-db:/app/local-db \
  -v ./prisma:/app/prisma \
  -e JWT_SECRET=your-secret-key-here \
  --name easy-dataset \
  --restart unless-stopped \
  easy-dataset
```

`--restart`参数的说明

| 参数值             | 说明                                                                                             |
| :----------------- | :----------------------------------------------------------------------------------------------- |
| **no**             | 默认值。容器退出或系统重启后**不会**自动重启。                                                   |
| **always**         | 只要 Docker 服务在运行，容器就会自动重启。即使你手动停止了它，重启电脑后它仍会尝试启动。         |
| **unless-stopped** | **最推荐。** 重启电脑后会自动启动，但前提是你在关机前**没有手动停止**（`docker stop`）这个容器。 |
| **on-failure**     | 只有当容器非正常退出（退出状态码非 0）时才会重启。                                               |

##### 4. 容器报错管理

```bash
# 查看日志
docker logs easy-dataset

# 查看正在运行的容器日志（实时滚动）
docker logs -f easy-dataset

# 查看最近 100 行日志（最常用）
docker logs --tail 100 easy-dataset

# 把日志保存到本地文件里
docker logs easy-dataset > easy-dataset-logs.txt

# 进入容器
docker exec -it easy-dataset sh
```

##### 4. 启动容器内数据库管理功能

由于easydataset内置有一个数据库可视化管理工具，运行以下命令后，在浏览器访问 http://localhost:5555/studio 就可以看到数据库管理界面了，是用来管理用户数据的。

```bash
# 1. 进入容器
easy-dataset $ docker exec -it easy-dataset  sh
/app $  pnpm prisma studio
 ERR_PNPM_RECURSIVE_EXEC_FIRST_FAIL  Command "prisma" not found

# 2. 执行上述命令行发现docker的image里未安装prisma工具
#  由于安装prisma需要先安装openssl，故先配置环境，由于本环境是Alpine 精简系统，缺库，直接装上就好：
apk update  # 可以不执行
apk add --no-cache openssl libc6-compat # 一定要加上--no-cache

# 3. 再次执行命令行，成功启动数据库可视化工具
pnpm dlx prisma@5.20.0 studio --schema /app/prisma/schema.prisma
# http://localhost:5555

# 4. 若需要配置镜像
pnpm config set registry http://r.cnpmjs.org/

```

### 5. 常见登录问题

#### 5.1 公网访问问题

如果是公网访问问题，可以在`.env`文件中进行配置

```bash
ALLOWED_ORIGINS=http://localhost:port,http://your.domain.name:port
```

点击浏览器的`network` 状态,查看输入账号密码后的状态

<img src="https://virginia-pepper.oss-cn-guangzhou.aliyuncs.com/20260408120737081.jpeg" alt="alt text" width="60%" />

如果`\login`状态为 200， 但是无法进行跳转，则有可能是因为 CORS 跨域问题导致。

> 进一步解释： login 请求的状态码已经是 200 OK 了！这说明后端已经验证通过并返回了成功信息。之所以没有跳转，是因为在跨域或穿透环境下，浏览器没有成功处理后端返回的 Set-Cookie（登录凭证），导致前端认为你还是未登录状态，从而卡在原地

> ps: 解释CORS（跨域资源共享）： 安全机制导致的访问失败

<img src="https://virginia-pepper.oss-cn-guangzhou.aliyuncs.com/20260408121001858.png" alt="alt text" width="60%" />

🔍 **核心原因排查**

1. 协议不匹配：你使用的是 `http://domain.cn`（非加密）。现代浏览器对于非`https` 的网站，在处理跨域 `Cookie ``转发时有非常严格的限制。

2. `Cookie` 写入失败：由于你是通过 `frp` 穿透访问，请求头里的 `Host` 是 `domain.cn:port`。如果后端代码中设置 `Cookie` 时指定了 `Domain=localhost` 或者开启了 `Secure` 属性（要求必须 `https`），浏览器会直接丢弃这个 `Cookie`。

🔍 **处理方法**

方案一：修改浏览器的安全策略（最快验证法）

如果只是你自己使用，可以让 Chrome 暂时对你的域名放开 Secure 限制。

1. 在 Chrome 地址栏输入并打开：`chrome://flags/#unsafely-treat-insecure-origin-as-secure`

2. 在输入框中填写你的域名和端口，例如：`http://domain.cn:port`

3. 把右侧的状态从 `Disabled` 改为 `Enabled`。

4. 点击右下角的 `Relaunch` 重启浏览器。

5. 验证：重启后再次登录。此时浏览器会把你的 HTTP 域名当成“安全环境”，即便有 `Secure` 标志，它也会强行存入 Cookie 并允许跳转。

方案二：给自己的域名配置 `ssl` 服务

详细我回再出一篇博客讲解，简单来说就是给自己的域名申请一个免费的 `SSL` 证书（比如通过 Let's Encrypt），然后在你的服务器上配置 `HTTPS` 服务。这样浏览器就会认为你的域名是安全的，自然就不会丢弃` Cookie` 了。

#### 5.2 数据库权限问题

如果是数据库无法读写的问题，需要配置读取权限：`Error code 14: Unable to open the database file` 是 `SQLite`的标准错误，意味着 `Prisma` 找到了路径，但是 没有权限读写文件 或者 该路径指向了一个不存在的目录。

这通常是因为 `Docker 挂载（Volume）后的文件权限变成了 root，而容器内的服务（以其他用户运行）无法操作它。

```bash
# 给数据库目录和文件读写权限
chmod -R 777 $(pwd)/prisma-data
chmod -R 777 $(pwd)/local-db
```

## 🔧 额外建议

1. **用户注册**: 可以添加注册页面和API
2. **密码重置**: 实现忘记密码功能
3. **用户管理**: 管理员可以管理用户
4. **权限控制**: 不同用户访问不同项目
5. **会话管理**: 实现refresh token机制
6. **安全加固**: 添加CSRF保护、输入验证等

这个方案提供了完整的身份验证系统，你可以根据具体需求进行调整和扩展。

```

```
