FROM duckietown/rpi-gui-tools:master18



ARG CHALLENGE_EVALUATION=/challenge-evaluator
ENV CHALLENGE_EVALUATION ${CHALLENGE_EVALUATION}

COPY requirements.txt ${CHALLENGE_EVALUATION}/requirements.txt

RUN pip install -r ${CHALLENGE_EVALUATION}/requirements.txt

COPY prepare.sh ${CHALLENGE_EVALUATION}/prepare.sh

ENV DUCKIETOWN_DATA=/data

RUN bash -c "source  /home/software/docker/env.sh && source ${CHALLENGE_EVALUATION}/prepare.sh"


COPY eval.py ${CHALLENGE_EVALUATION}/eval.py
RUN chmod +x ${CHALLENGE_EVALUATION}/eval.py




CMD bash -c "source  /home/software/docker/env.sh && python ${CHALLENGE_EVALUATION}/eval.py"

