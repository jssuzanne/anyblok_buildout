from anyblok.config import Configuration


@Configuration.add('message', label="This is the group message")
def add_interpreter(parser, configuration):
    parser.add_argument('--message-before', dest='message_before')
    parser.add_argument('--message-after', dest='message_after')
