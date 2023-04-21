FROM mcr.microsoft.com/devcontainers/anaconda:0.202.20-3

RUN mkdir /memo

# Prevent conda command error
RUN pip install --force-reinstall --user "cryptography==38.0.4" \
    && rm -rf ~/.cache/pip

# Copy environment.yml (if found) to a temp location so we update the environment. Also
# copy "noop.txt" so the COPY instruction does not fail if no environment.yml exists.
COPY .devcontainer/conda_env.txt  /tmp/conda-tmp/
RUN conda install --file /tmp/conda-tmp/conda_env.txt \
    && conda clean -afy \
    && rm /tmp/conda-tmp/conda_env.txt

# [Optional] Uncomment this section to install additional OS packages.
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends git yadm libgl1-mesa-dev

WORKDIR /workspace/
COPY requirements.txt .

RUN pip install --no-cache-dir -r ./requirements.txt
