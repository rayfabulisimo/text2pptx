# hash:sha256:5180c9b99e99f80ee1684d4cc3fc5cbda85125c9734558f22fdc66e6f9a3a9a5
ARG REGISTRY_HOST
FROM $REGISTRY_HOST/codeocean/miniconda3:25.3.0-3-python3.12.10-ubuntu22.04

ARG DEBIAN_FRONTEND=noninteractive
ARG GIT_ASKPASS
COPY git-askpass /

ENV CLAUDE_CODE_USE_BEDROCK=1
ENV AWS_REGION=us-east-1
ENV DISABLE_PROMPT_CACHING=1
ENV ANTHROPIC_MODEL=us.anthropic.claude-sonnet-4-5-20250929-v1:0
ENV ANTHROPIC_SMALL_FAST_MODEL=us.anthropic.claude-haiku-4-5-20251001-v1:0
ENV CLAUDE_CODE_MAX_OUTPUT_TOKENS=4096
ENV MAX_THINKING_TOKENS=1024

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        curl=7.81.0-1ubuntu1.21 \
    && rm -rf /var/lib/apt/lists/*

ADD "https://github.com/coder/code-server/releases/download/v4.100.3/code-server-4.100.3-linux-amd64.tar.gz" /.code-server/code-server.tar.gz
	
RUN cd /.code-server \
    && tar -xvf code-server.tar.gz \
    && rm code-server.tar.gz \
    && ln -s /.code-server/code-server-4.100.3-linux-amd64/bin/code-server /usr/bin/code-server \
    && mkdir -p /.vscode/extensions

RUN code-server --extensions-dir="/.vscode/extensions" --install-extension ms-python.python@2025.14.0 \
    && code-server --extensions-dir="/.vscode/extensions" --install-extension ms-toolsai.jupyter@2025.4.1 \
    && code-server --extensions-dir="/.vscode/extensions" --install-extension reditorsupport.r@2.8.6 \
    && code-server --extensions-dir="/.vscode/extensions" --install-extension saoudrizwan.claude-dev@3.35.1

COPY postInstall /
RUN --mount=type=secret,id=secrets . /run/secrets/secrets \
    && /postInstall
