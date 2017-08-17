#!/usr/bin/env python

def log(when):
    def logging(f, *args, **kw_args):
        print '''Call function:
function: %s,
args: %r,
kw_args: %r''' % (f, args, kw_args)

    def pre_logging(f):
        def wraper(*args, **kw_args):
            logging(f, args, kw_args)
            return f(*args, **kw_args)
        return wraper

    def post_logging(f):
        def wraper(*args, **kw_args):
            try:
                return f(*args, **kw_args)
            finally:
                logging(f, args, kw_args)
        return wraper

    try:
        return {
            'pre': pre_logging,
            'post': post_logging
        }[when]
    except KeyError, e:
        raise ValueError(e), 'must be "pre" or "post"'

@log('post')
def hello(name):
    print 'Hello,', name

hello('World!')
