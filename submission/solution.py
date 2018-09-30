#!/usr/bin/env python
import rosbag
import os
import duckietown_utils as dtu
from duckietown_challenges import wrap_solution, ChallengeSolution, ChallengeInterfaceSolution


class Solver(ChallengeSolution):
    def run(self, cis):
        assert isinstance(cis, ChallengeInterfaceSolution)

        params = cis.get_challenge_parameters()
        print('parameters: %s' % params)
        to_process = params['to_process']

        for basename in to_process:
            filename = cis.get_challenge_file(basename)
            print('processing %s' % filename)
            bag = rosbag.Bag(filename)
            topic = dtu.get_image_topic(bag)


            fn = os.path.join(cis.get_tmp_dir(), 'tmp.mp4')
            print('creating %s' % fn)
            dtu.d8n_make_video_from_bag(filename, topic, fn)

            cis.set_solution_output_file(basename+'.mp4', fn, 'processed video')

        cis.set_solution_output_dict({'processed': to_process})


if __name__ == '__main__':
    wrap_solution(Solver())
