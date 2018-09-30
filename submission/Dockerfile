FROM duckietown/rpi-gui-tools:master18


ARG CHALLENGE_SOLUTION=/challenge-solution
ENV CHALLENGE_SOLUTION=$CHALLENGE_SOLUTION

RUN echo CHALLENGE_SOLUTION=$CHALLENGE_SOLUTION


COPY requirements.txt $CHALLENGE_SOLUTION/requirements.txt

ARG REFRESHED_REQS=5

RUN pip install -r $CHALLENGE_SOLUTION/requirements.txt

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update
RUN apt-get install -y software-properties-common
RUN add-apt-repository ppa:mc3man/xerus-media
RUN apt-get update
RUN apt-get install -y  mplayer mencoder ffmpeg


COPY solution.py $CHALLENGE_SOLUTION/solution.py
RUN chmod +x $CHALLENGE_SOLUTION/solution.py



CMD bash -c "source  /home/software/docker/env.sh && python ${CHALLENGE_SOLUTION}/solution.py"
