#!/usr/bin/env python

from duckietown_challenges import wrap_evaluator, ChallengeEvaluator, ChallengeInterfaceEvaluator

import os

class Evaluator(ChallengeEvaluator):

    def prepare(self, cie):
        assert isinstance(cie, ChallengeInterfaceEvaluator)



        path = os.environ['CHALLENGE_EVALUATION']
        cie.set_challenge_file('log0.bag', os.path.join(path, 'log0.bag'))
        to_process = ['log0.bag']
        cie.set_challenge_parameters({'to_process': to_process})



    def score(self, cie):
        solution_output = cie.get_solution_output_dict()

        cie.set_score('passed', 1.0)


if __name__ == '__main__':
    wrap_evaluator(Evaluator())
