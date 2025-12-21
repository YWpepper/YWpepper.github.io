---
title: 'How_to_useDocker'
lang: zh-CN
date: 2024-02-07
author: pepper
toc: true
pinned: false
tags:
  - Server
  - Command
---
这篇笔记汇总了在 docker 下常用的快速命令。
<!-- more -->


## 使用本地 Dockerfile 构建

A text file containing instructions to build Docker images automatically 
  -------- 包含自动构建 Docker 镜像指令的文本文件

1. 项目样例： 对于easydataset项目，Dockerfile内容如下：
  
```dockerfile
# 创建包含pnpm的基础镜像
FROM node:20-alpine AS pnpm-base
RUN npm install -g pnpm@9

# 构建阶段
FROM pnpm-base AS builder
WORKDIR /app

# 添加构建参数，用于识别目标平台
ARG TARGETPLATFORM

# 安装构建依赖
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

# 复制依赖文件和npm配置并安装(.npmrc中可配置国内源加速)
COPY package.json pnpm-lock.yaml .npmrc ./
RUN pnpm install

# 复制源代码
COPY . .

# 根据目标平台设置Prisma二进制目标并构建应用
RUN if [ "$TARGETPLATFORM" = "linux/arm64" ]; then \
        echo "Configuring for ARM64 platform"; \
        sed -i 's/binaryTargets = \[.*\]/binaryTargets = \["linux-musl-arm64-openssl-3.0.x"\]/' prisma/schema.prisma; \
        PRISMA_CLI_BINARY_TARGETS="linux-musl-arm64-openssl-3.0.x" pnpm build; \
    else \
        echo "Configuring for AMD64 platform (default)"; \
        sed -i 's/binaryTargets = \[.*\]/binaryTargets = \["linux-musl-openssl-3.0.x"\]/' prisma/schema.prisma; \
        PRISMA_CLI_BINARY_TARGETS="linux-musl-openssl-3.0.x" pnpm build; \
    fi

# 构建完成后移除开发依赖，只保留生产依赖
RUN pnpm prune --prod

# 运行阶段
FROM pnpm-base AS runner
WORKDIR /app

# 只安装运行时依赖
RUN apk add --no-cache \
    cairo \
    pango \
    jpeg \
    giflib \
    librsvg \
    pixman

# 复制package.json和.env文件
COPY package.json .env ./

# 从构建阶段复制精简后的node_modules（只包含生产依赖）
COPY --from=builder /app/node_modules ./node_modules

# 从构建阶段复制构建产物
COPY --from=builder /app/.next ./.next
COPY --from=builder /app/public ./public
COPY --from=builder /app/electron ./electron

# 复制 prisma 到模板目录（用于自动初始化）
COPY --from=builder /app/prisma /app/prisma-template

# 复制并设置 entrypoint 脚本
COPY docker-entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

# 设置生产环境
ENV NODE_ENV=production

EXPOSE 1717

# 使用 entrypoint 脚本
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]
CMD ["pnpm", "start"]

```
由于想自行构建镜像，使用上面项目根目录中的 Dockerfile：
- 克隆仓库：

```bash
git clone https://github.com/ConardLi/easy-dataset.git
cd easy-dataset
```

- 构建 Docker 镜像：
```bash
docker build -t easy-dataset .
```

- 运行容器：
```bash
docker run -d \\
  -p 1717:1717 \\
  -v ./local-db:/app/local-db \\
  -v ./prisma:/app/prisma \\
  --name easy-dataset \\
  easy-dataset
```

> **注意：** 建议直接使用当前代码仓库目录下的 `local-db` 和 `prisma` 文件夹作为挂载路径，这样可以和 NPM 启动时的数据库路径保持一致。

> **注意：** 数据库文件会在首次启动时自动初始化，无需手动执行 `npm run db:push`。

- 打开浏览器，访问 `http://localhost:1717`



## 使用官方 Docker 镜像

- 克隆仓库：

```bash
git clone https://github.com/ConardLi/easy-dataset.git
cd easy-dataset
```

- 更改 `docker-compose.yml` 文件：

```yml
services:
  easy-dataset:
    image: ghcr.io/conardli/easy-dataset
    container_name: easy-dataset
    ports:
      - '1717:1717'
    volumes:
      - ./local-db:/app/local-db
      - ./prisma:/app/prisma
    restart: unless-stopped
```

> **注意：** 建议直接使用当前代码仓库目录下的 `local-db` 和 `prisma` 文件夹作为挂载路径，这样可以和 NPM 启动时的数据库路径保持一致。

> **注意：** 数据库文件会在首次启动时自动初始化，无需手动执行 `npm run db:push`。

- 使用 docker-compose 启动

```bash
docker-compose up -d
```

- 打开浏览器并访问 `http://localhost:1717`

---
