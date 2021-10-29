import datetime

# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------------------
# Class:         Chrono
# Description:   Test for Vamstar interview
# Release:       1.0
# Date:          201.10.30
# Author:        Dr. Eng. Massimo Brozzi - mbrozzi@gmail.com +447438578598
# -----------------------------------------------------------------------------------------------------

class Chrono:
    start_time = None
    stop_time = None

    # -----------------------------------------------------------------------------

    def __init__(
        self,
        autostart=True,
    ):
        self.reset()

        if autostart:
            self.start()

    # -----------------------------------------------------------------------------

    def reset(
        self,
    ):
        self.start_time = None
        self.stop_time = None

    # -----------------------------------------------------------------------------

    def start(
        self,
    ):
        self.reset()
        self.start_time = datetime.datetime.now()

    # -----------------------------------------------------------------------------

    def stop(
        self,
    ):
        if self.start_time:
            self.stop_time = datetime.datetime.now()
        else:
            self.reset()

    # -----------------------------------------------------------------------------

    def elapsed_time_millisecs(
        self,
        autostop=True,
        autorestart=True,
    ):
        result = 0
        if autostop and not self.stop_time:
            self.stop()

        if self.start_time:
            if self.stop_time:
                diff = self.stop_time - self.start_time
            else:
                diff = datetime.datetime.now() - self.start_time
            millis = diff.days * 24 * 60 * 60 * 1000
            millis += diff.seconds * 1000
            millis += diff.microseconds / 1000
            result = int(millis)
        else:
            self.reset()

        if autorestart:
            self.start()

        return result

    # -----------------------------------------------------------------------------

    def elapsed_time_secs(
        self,
        autostop=True,
        autorestart=True,
    ):
        return int(self.elapsed_time_millisecs(autostop, autorestart) / 1000)

    # -----------------------------------------------------------------------------

    def elapsed_time_millisecs_str(
        self,
        autostop=True,
        autorestart=True,
    ):
        t = self.elapsed_time_millisecs(
            autostop=autostop,
            autorestart=autorestart,
        )
        return "[{}] millisecs.".format(t)

    # -----------------------------------------------------------------------------

    def elapsed_time_secs_str(
        self,
        autostop=True,
        autorestart=True,
    ):
        t = self.elapsed_time_secs(
            autostop=autostop,
            autorestart=autorestart,
        )

        return "[{}] secs".format(t)


# -----------------------------------------------------------------------------------------------------
# End of File
# -----------------------------------------------------------------------------------------------------

