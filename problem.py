import time
class Problem(object):
    def main(self):
        start = time.time()
        print " An: %s" % self.execute()
        print " in: %ss " % (time.time() - start)

    def execute(self):
        raise NotImplementedError("Please Implement this method")
