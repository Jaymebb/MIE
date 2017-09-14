import abc

DEFAULT_METAMAP_VERSION = '2012'

class MetaMap:
    """ Abstract base class for extracting concepts from text using
        MetaMap. To use this you will need to have downloaded the
        recent MetaMap software from NLM. metamap_filename should point
        to the binary you intend to use.

        Subclasses need to override the extract_concepts method.
    """
    __metaclass__ = abc.ABCMeta
    def __init__(self, metamap_filename, version=None):
        self.metamap_filename = metamap_filename
        if version is None:
            version = DEFAULT_METAMAP_VERSION

    @abc.abstractmethod
    def extract_concepts(self, sentences=None, ids=None,
                         filename=None, composite_phrase=4, 
                         file_format='sldi', word_sense_disambiguation=True):
       """ Extract concepts from a list of sentences using MetaMap. """

    @staticmethod
    def get_instance(metamap_filename, version=None, backend='subprocess',
                     **extra_args):
        extra_args.update(metamap_filename=metamap_filename, version=version)

        if backend == 'subprocess':
            from SubprocessBackend import SubprocessBackend
            return SubprocessBackend(**extra_args)

        raise ValueError("Unknown backend: %r (known backends: "
                         "'subprocess')" % backend)
