import time
from rq import get_current_job


def example(seconds):
    job = get_current_job()
    print('staring task')
    for i in range(seconds):
        job.meta['progress'] = 100. * i  / seconds
        job.save_meta()
        print(i)
        time.sleep(1)
    job.meta['progress'] = 100
    job.save_meta()
    print('task completed')






