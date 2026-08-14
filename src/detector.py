from threading import Thread

class Detector(Thread):


    def run(self):

        while self.running:

            frame=self.queue.get()


            result=self.model(frame)


            self.output.put(result)