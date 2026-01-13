# hash:sha256:8c8ae41d6eff3b06f0672757628a8bf91394bc95df061f267497dad82c73ad40
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

COPY postInstall /
RUN --mount=type=secret,id=secrets . /run/secrets/secrets \
    && /postInstall
