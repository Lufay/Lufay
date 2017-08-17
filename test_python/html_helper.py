#!/usr/bin/env python

def renderOptions(options):
    optionArray = []
    for optionName in options:
        optionArray.append('%s="%s"' % (optionName, options[optionName]))
    return ' '.join(optionArray)

def tag(name, content='', **options):
    if not name:
        return content
    return '<%s %s>%s</%s>' % (name, renderOptions(options), content, name)

def table(header, body, caption=''):
    '''
        header is array of col
        body is array of row, while row is array of col
        caption is string
    '''
    headerArray = []
    for hCol in header:
        headerArray.append(tag('th', hCol))
    headerStr = tag('thead', tag('tr', '\n'.join(headerArray)+'\n')+'\n')
    bodyArray = []
    for row in body:
        rowArray = []
        for bCol in row:
            rowArray.append(tag('td', bCol))
        bodyArray.append(tag('tr', '\n'.join(rowArray)+'\n'))
    bodyStr = tag('tbody', '\n'.join(bodyArray)+'\n')
    captionStr = tag('caption', caption) if caption else ''
    return tag('table', '\n%s\n%s\n%s\n' % (captionStr, headerStr, bodyStr), border=1)

if __name__ == '__main__':
    print table(['aaa', 'bbb', 'ccc'], [['r1c1', 'r1c2', 'r1c3'], ['r2c1', 'r2c2', 'r2c3']])
