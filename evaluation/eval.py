#!/usr/bin/env python

from duckietown_challenges import wrap_evaluator, ChallengeEvaluator, ChallengeInterfaceEvaluator

import os

class Evaluator(ChallengeEvaluator):

    def prepare(self, cie):
        assert isinstance(cie, ChallengeInterfaceEvaluator)



        path = os.environ['CHALLENGE_EVALUATION']
        # # Look for some logs
        # logs = db.query("20180108141155_a313")

        # Download the logs
        cie.set_challenge_file('log0.bag', os.path.join(path, 'log0.bag'))
        to_process = ['log0.bag']
        # Give list of files to the submission
        cie.set_challenge_parameters({'to_process': to_process})

        # from easy_logs import get_easy_logs_db2, get_local_bag_file
        # from easy_logs.app_with_logs import download_if_necessary

        # Initialize log DB
        # db = get_easy_logs_db2(do_not_use_cloud=False, do_not_use_local=False, ignore_cache=False)
        # for i, (id_log, log) in enumerate(logs.items()):
        #     # Download the log locally
        #     log = download_if_necessary(log)
        #     filename = get_local_bag_file(log)
        #     # Pass it as a challenge file
        #     basename = 'log%d.bag' % i
        #     cie.set_challenge_file(basename, filename)
        #     to_process.append(basename)


    def score(self, cie):
        solution_output = cie.get_solution_output_dict()

        cie.set_score('passed', 1.0)


if __name__ == '__main__':
    wrap_evaluator(Evaluator())
