import os, re

posts_dir = r'e:\A-workSpace\OneDrive\文档\OneDrive\02-coding\00-gitubPage\YWpepper.github.io\_posts'

changes = {
    '2024-02-07-How_to_useGit.md': ('工具-Git常用命令与笔记润色', '[git, tool]'),
    '2024-02-07-How_to_useUbuntu.md': ('服务器-Ubuntu命令与服务管理', '[ubuntu, server]'),
    '2024-02-07-How_to_useDocker.md': ('服务器-Docker常用命令速查', '[docker, server]'),
    '2022-04-10-dailyResource.md': ('工具-快速查阅手册', '[tool, daily]'),
    '2022-04-10-What_is_Qingdao.md': ('生活-青岛旅行杂记', '[qingdao, travel]'),
    '2022-04-10-what_books_IRead.md': ('生活-读书笔记', '[books, daily]'),
    '2022-04-10-MessyUp.md': ('生活-日常技巧积累', '[daily, tips]'),
    '2000-01-01-what_camera_take.md': ('生活-摄影杂记', '[camera, daily]'),
    '2025-02-07-how_to_make_GitubwithJekyll_in_windows.md': ('工具-GitHub-Pages与Jekyll搭建', '[jekyll, github]'),
    '2025-02-07-What_is_traffic_prediction.md': ('论文-交通预测研究概述', '[traffic, research]'),
    '2025-02-09-how_to_do_ScientificResearchDrawings.md': ('工具-科研绘图与LaTeX模板', '[latex, plot]'),
    '2025-02-11-what_Torchversion_install.md': ('工具-PyTorch版本安装指南', '[pytorch, tool]'),
    '2025-02-28-how_to_ScatterPlotsOnMap.md': ('论文-地图散点图可视化', '[plot, traffic]'),
    '2025-03-03-how_to_learn_graphNetwork.md': ('论文-图神经网络学习资源', '[gnn, research]'),
    '2025-03-11-how_to_use_remoteSSH.md': ('服务器-远程SSH配置与端口转发', '[ssh, server]'),
    '2025-03-11-how_to_change_githubStyle.md': ('工具-GitHub-Pages主题样式修改', '[github, jekyll]'),
    '2025-05-06-SFT_RLHF_RAG.md': ('论文-LLM微调与RAG技术综述', '[llm, sft, rlhf, rag]'),
    '2025-11-02-how_to_install_latex.md': ('工具-VSCode与LaTeX安装配置', '[latex, tool]'),
    '2025-11-02-how-to-install-mySql.md': ('服务器-MySQL安装与配置', '[mysql, server]'),
    '2025-11-09-how_to_make_Xinference.md': ('服务器-Xinference模型推理框架部署', '[xinference, llm, server]'),
    '2025-11-11-how_many_bugs_Nov.md': ('开发-十一月Bug排查记录', '[bug, springboot]'),
    '2025-11-13-What_accidentLLM.md': ('论文-交通场景大模型研究', '[llm, traffic]'),
    '2025-11-14-CoDiEmb_PapperReading copy.md': ('论文-CoDiEmb文本嵌入表示学习', '[nlp, codiemb]'),
    '2025-11-14-FinRpt_PapperReading.md': ('论文-FinRpt股票研报自动生成', '[finreport, nlp]'),
    '2025-11-14-How_to_downloadHF_faster.md': ('工具-HuggingFace模型快速下载', '[hf, tool]'),
    '2025-11-14-What_is_frpServe.md': ('服务器-frp内网穿透部署', '[frp, server]'),
    '2025-11-19-What_issue_I_meet.md': ('开发-SpringBoot配置错误排查', '[springboot, bug]'),
    '2025-11-22-How_to_useJava.md': ('开发-Java代码生成器使用', '[java, maven]'),
    '2025-11-22-What_is_meavn.md': ('开发-Maven项目管理与配置', '[maven, java]'),
    '2025-11-22-latex2word_fastly.md': ('工具-Pandoc将LaTeX转Word', '[pandoc, latex]'),
    '2025-11-22-How to Use Gmail.md': ('工具-Gmail邮箱别名技巧', '[gmail, tool]'),
    '2025-12-07-Training-Free GRPO_PapperReading.md': ('论文-Training-Free-GRPO免训练优化', '[grpo, llm]'),
    '2025-12-08-algorithm_BinarySearch.md': ('算法-二分查找与LeetCode题解', '[binarysearch, algorithm]'),
    '2025-12-08-TrafficIT_PapperReading copy.md': ('论文-Traffic-IT交通场景理解', '[traffic, llm]'),
    '2026-04-02-how-to-use-ollama.md': ('服务器-Ollama常用命令', '[ollama, llm, server]'),
    '2026-04-06-how_to_manageLLM.md': ('服务器-Xinference管理LLM模型', '[xinference, llm, server]'),
    '2026-04-06-how_to_useVLLM.md': ('服务器-vLLM多端口部署LLM', '[vllm, llm, server]'),
    '2026-04-06-interview_recommand.md': ('开发-放贷业务面试应答指南', '[interview, java]'),
    '2026-04-07-how_to_changeEasyDataset.md': ('开发-EasyDataset登录验证开发', '[easydataset, java]'),
    '2026-04-07-how_to_makeSSL.md': ('服务器-SSL证书安装与配置', '[ssl, server]'),
}

success = 0
fail = 0

for fname, (new_title, new_tags) in changes.items():
    fpath = os.path.join(posts_dir, fname)
    if not os.path.exists(fpath):
        print(f'SKIP (not found): {fname}')
        fail += 1
        continue

    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    if not content.startswith('---'):
        fm_start = content.find('---')
        if fm_start < 0:
            print(f'SKIP (no front matter): {fname}')
            fail += 1
            continue
        fm_end = content.find('---', fm_start + 3)
        if fm_end < 0:
            print(f'SKIP (no end front matter): {fname}')
            fail += 1
            continue
        fm = content[fm_start+3:fm_end]
        before = content[:fm_start+3]
        after = content[fm_end:]
    else:
        fm_end = content.find('---', 3)
        if fm_end < 0:
            print(f'SKIP (no end front matter): {fname}')
            fail += 1
            continue
        fm = content[3:fm_end]
        before = '---'
        after = content[fm_end:]

    fm = re.sub(r"title:\s*['\"].*?['\"]\s*$", f"title: '{new_title}'", fm, count=1, flags=re.MULTILINE)
    fm = re.sub(r"title:\s*\S+.*$", f"title: '{new_title}'", fm, count=1, flags=re.MULTILINE)

    fm = re.sub(r'tags:\s*\[.*?\]', f'tags: {new_tags}', fm, count=1)

    lines = fm.split('\n')
    new_lines = []
    skip_tags_list = False
    found_tags = False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith('tags:'):
            if found_tags:
                skip_tags_list = True
                continue
            if 'tags: [' in stripped or 'tags:[' in stripped:
                new_lines.append(f'tags: {new_tags}')
                found_tags = True
                continue
            else:
                new_lines.append(f'tags: {new_tags}')
                found_tags = True
                skip_tags_list = True
                continue
        if skip_tags_list and (stripped.startswith('- ') or stripped.startswith('  - ')):
            continue
        if skip_tags_list and not stripped.startswith('- ') and not stripped.startswith('  - '):
            skip_tags_list = False
        if not skip_tags_list:
            new_lines.append(line)

    fm = '\n'.join(new_lines)

    new_content = before + fm + after

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f'OK: {fname}')
    success += 1

print(f'\nDone: {success} success, {fail} failed')
