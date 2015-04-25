# __author__ = 'shanshul'

from flask.ext.script import Manager

from bidding import create_app

import sys

manager = Manager(create_app)


@manager.command
def hello():
    print "hello"


if __name__ == "__main__":
    if sys.argv[1] == 'test':
        manager = Manager(create_app(package_name='bidding', config_name='Testing'))

        @manager.command
        def test():
            import nose

            nose.main(argv=['bidding.test', '-s', '-v', '--with-coverage', '--cover-package', 'bidding'])

        manager.run()
    else:
        manager.run()